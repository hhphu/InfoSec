# Auditing a Playwright POM Test Suite: Mistakes, Fixes, and Best Practices

<img width="1376" height="768" alt="Gemini_Generated_Image_u88ur4u88ur4u88u" src="https://github.com/user-attachments/assets/74cd1373-ed96-4ccd-8778-aff80b76a739" />

When building a Playwright test suite using the Page Object Model (POM) pattern, it's easy to write code that *looks* correct but contains subtle bugs, inconsistencies, and silent failure modes that only surface at the worst possible time. This post walks through a real audit of a POM-based E2E suite for a registration and login flow, documenting every issue found and the reasoning behind each fix.

---

## The Project

The suite tests user registration and login flows on a live e-commerce site. The architecture is straightforward:

- `playwright.config.ts` — global configuration, single Chrome target
- `config/test.config.ts` — shared timeouts
- `tests/pages/` — Page Object Model classes (`BasePage`, `HomePage`, `RegisterPage`, `LogInPage`, `AccountPage`)
- `tests/errors/` — custom error classes
- `tests/data/` — test data and user interfaces
- `tests/*.spec.ts` — spec files

---

## Issue 1: `locator.toString()` Produces Useless Error Messages

### The Problem

In `BasePage`, the `waitForElement` method caught timeout failures and threw a custom `ElementNotFoundError`. The locator's description was passed by calling `.toString()` on it:

```ts
// BasePage.ts — BEFORE
async waitForElement(locator: Locator, timeout?: number) {
    try {
        await locator.waitFor({ timeout: timeout || config.timeouts.default });
    } catch {
        throw new ElementNotFoundError(locator.toString(), timeout || config.timeouts.default);
    }
}
```

When a test fails, the error message looks like:

```
Failed to find element Locator@playwright/lib/locator.js:42 within 10000ms
```

This is the internal string representation of a Playwright `Locator` object — it tells you nothing about *which* field failed.

### The Fix

Add an optional `description` parameter. Callers pass a human-readable label; the error message uses it. If no description is provided, a generic fallback is used instead of the internal object reference.

```ts
// BasePage.ts — AFTER
async waitForElement(locator: Locator, description?: string, timeout?: number) {
    const ms = timeout || config.timeouts.default;
    try {
        await locator.waitFor({ timeout: ms });
    } catch {
        throw new ElementNotFoundError(description ?? 'element', ms);
    }
}
```

Call sites now produce clear failures:

```ts
await this.waitForElement(this.navLocators.joinLink, 'Join link');
// Error: Failed to find element Join link within 10000ms
```

---

## Issue 2: The TOCTOU Race in `fillOutInput`

### The Problem

The original `fillOutInput` used a two-step pattern: wait for the element to be visible, then fill it.

```ts
// BasePage.ts — BEFORE
async fillOutInput(locator: Locator, value: string) {
    await this.waitForElement(locator);  // Step 1: wait
    await locator.fill(value);           // Step 2: fill
}
```

This is a classic **TOCTOU (Time-Of-Check, Time-Of-Use)** race condition. Between the moment `waitForElement` confirms the element is visible and the moment `locator.fill()` runs, the DOM can change — the element can be removed by a re-render, replaced by a loading state, or detached during a framework update. When that happens, `.fill()` throws a raw Playwright error with no helpful context about which field was affected.

### The Fix

Replace the two steps with a single atomic call. Playwright's `locator.fill()` already handles waiting internally — it waits for the element to be attached, visible, and enabled before filling. Passing a `timeout` option directly to `.fill()` makes the whole operation atomic, and the `try/catch` wraps any failure in a meaningful error.

```ts
// BasePage.ts — AFTER
async fillOutInput(locator: Locator, value: string, description?: string) {
    const ms = config.timeouts.default;
    try {
        await locator.fill(value, { timeout: ms });
    } catch {
        throw new ElementNotFoundError(description ?? 'input field', ms);
    }
}
```

Call sites now also get human-readable failure messages:

```ts
await this.fillOutInput(firstName, data.firstName, 'First name');
// Error: Failed to find element First name within 10000ms
```

---

## Issue 3: The Silent URL Bug (`!` in a Template Literal)

### The Problem

This was the most dangerous bug in the suite — a single misplaced character that would cause `verifyRegisterPageLoaded` to *always* fail, with a confusing error message about a URL that doesn't exist.

```ts
// RegisterPage.ts — BEFORE
async verifyRegisterPageLoaded() {
    const registerPageURL = `${process.env.BASE_URL}${this.registerPath}!`;
    //                                                                    ^ !!!
```

The `!` was intended as TypeScript's non-null assertion on `process.env.BASE_URL`. Instead, it was placed inside the template literal, appending it as a literal character to the URL string:

```
https://example.com/account/register!
```

Playwright would then assert the page has URL `https://example.com/account/register!`, which it never would.

### The Fix

Move the URL construction to a getter (lazily evaluated, reusable), and remove the `!`:

```ts
// RegisterPage.ts — AFTER
get registerPageURL() {
    return `${process.env.BASE_URL}${this.registerPath}`;
}

async verifyRegisterPageLoaded() {
    const registerPageTitle = 'Create Account - 1MD';
    await this.verifyPageURL(this.registerPageURL);
    await this.verifyPageTitle(registerPageTitle);
}
```

---

## Issue 4: URL Computed Too Early (Class Field vs. Getter)

### The Problem

`LogInPage` originally computed its URL as a class field:

```ts
// LogInPage.ts — BEFORE
export class LogInPage extends BasePage {
    readonly loginPath = 'account/login';
    readonly loginPageURL = `${process.env.BASE_URL}${this.loginPath}`;
```

Class fields are evaluated at instantiation time, before the constructor body runs. In a typical Playwright setup, `dotenv` is loaded in `playwright.config.ts` — but if a test file imports a page object before the config has fully initialised the environment, `process.env.BASE_URL` is `undefined` at the moment the field is set. The result:

```
"undefinedaccount/login"
```

No error is thrown. The URL is just silently wrong.

### The Fix

Convert the field to a getter. Getters are lazily evaluated — the expression only runs when the property is accessed, by which point the environment is fully loaded.

```ts
// LogInPage.ts — AFTER
get loginPageURL() {
    return `${process.env.BASE_URL}${this.loginPath}`;
}
```

---

## Issue 5: Inconsistency Between Page Object Methods

### The Problem

`BasePage` provides `fillOutInput` and `waitForElement` as helpers with built-in error handling and timeout management. `RegisterPage` used them correctly, but `LogInPage` called Playwright's API directly:

```ts
// LogInPage.ts — BEFORE
async fillForm(data: UserLoggedInData) {
    const { email, password } = this.formLocators;
    await email.fill(data.email);      // raw Playwright call — no error wrapping
    await password.fill(data.password); // no timeout, no description
}

async submitForm() {
    await this.formLocators.submit.click(); // no waitForElement, no error context
}
```

This inconsistency means failures in `LogInPage` produce raw Playwright errors while failures in `RegisterPage` produce helpful custom errors. The suite's error handling becomes unpredictable — whether you get a good error message depends on which page you happen to be testing.

### The Fix

Use the base class helpers everywhere, consistently:

```ts
// LogInPage.ts — AFTER
async fillForm(data: UserLoggedInData) {
    const { email, password } = this.formLocators;
    await this.fillOutInput(email, data.email, 'Email');
    await this.fillOutInput(password, data.password, 'Password');
}

async submitForm() {
    await this.waitForElement(this.formLocators.submit, 'Continue button');
    await this.formLocators.submit.click();
}
```

**Rule of thumb:** If `BasePage` provides a helper for an operation, every subclass should use it. Direct Playwright API calls in page objects bypass the error handling layer you built.

---

## Issue 6: Non-Null Assertions on Environment Variables

### The Problem

Test data was loaded from environment variables using TypeScript's `!` non-null assertion operator:

```ts
// data/users.ts — BEFORE
export const users = {
    registration: {
        firstName: process.env.TEST_USER_FIRST_NAME!,
        lastName:  process.env.TEST_USER_LAST_NAME!,
        email:     process.env.TEST_USER_EMAIL!,
        password:  process.env.TEST_USER_PASSWORD!,
    },
    ...
}
```

The `!` tells TypeScript's type checker to treat the value as `string` rather than `string | undefined`. It does nothing at runtime. If `.env` is missing a variable, the actual value at runtime is `undefined` — TypeScript just stops complaining about it.

The consequence: the form fills with `undefined`, tests run, and the failure appears as a confusing Playwright assertion error deep inside a form interaction, not as "you're missing an env var."

### The Fix

Add a `requireEnv` guard that validates the variable at import time and throws a clear error immediately:

```ts
// data/users.ts — AFTER
function requireEnv(key: string): string {
    const val = process.env[key];
    if (!val) throw new Error(`Environment variable ${key} is required but not set.`);
    return val;
}

export const users = {
    registration: {
        firstName: requireEnv('TEST_USER_FIRST_NAME'),
        lastName:  requireEnv('TEST_USER_LAST_NAME'),
        email:     requireEnv('TEST_USER_EMAIL'),
        password:  requireEnv('TEST_USER_PASSWORD'),
    },
    logInCreds: {
        email:    requireEnv('TEST_USER_EMAIL'),
        password: requireEnv('TEST_USER_PASSWORD'),
    }
}
```

Now if `TEST_USER_EMAIL` is missing, you get this before any test runs:

```
Error: Environment variable TEST_USER_EMAIL is required but not set.
```

**Fail fast, fail clearly** — never let a missing config silently degrade into a confusing test failure.

---

## Issue 7: `dismissModal` Clicks Without Waiting

### The Problem

The homepage loads an SMS sign-up modal in an iframe. `dismissModal` checks if the iframe is visible, then immediately clicks the close button:

```ts
// HomePage.ts — BEFORE
async dismissModal() {
    const { iframe, closeButton } = this.modalLocators;
    if (await iframe.isVisible()) {
        await closeButton.click(); // iframe visible ≠ close button ready
    }
}
```

The iframe loads asynchronously. The outer `<iframe>` element can be visible in the DOM while its internal content (including the close button) is still mounting. Clicking too early results in a flaky failure — sometimes it works, sometimes it doesn't, depending on network speed and rendering timing.

### The Fix

Wait for the close button to be ready before clicking it:

```ts
// HomePage.ts — AFTER
async dismissModal() {
    const { iframe, closeButton } = this.modalLocators;
    if (await iframe.isVisible()) {
        await this.waitForElement(closeButton, 'Modal close button');
        await closeButton.click();
    }
}
```

---

## Issue 8: Mixed URL Construction Strategies

### The Problem

Each page constructed URLs differently, with no consistent pattern:

```ts
// HomePage — absolute URL from env var with ! assertion
async verifyHomePageLoaded() {
    const homePageURL = process.env.BASE_URL!;
    await this.verifyPageURL(homePageURL);
}

// RegisterPage — inline template literal in the method body
async verifyRegisterPageLoaded() {
    const registerPageURL = `${process.env.BASE_URL}${this.registerPath}`;
    await this.verifyPageURL(registerPageURL);
}

// LogInPage — class-level readonly field (evaluated at instantiation)
readonly loginPageURL = `${process.env.BASE_URL}${this.loginPath}`;

// AccountPage — inline template literal in the method body
async verifyAccountPageLoaded() {
    const accountPageURL = `${process.env.BASE_URL}${this.accountPath}`;
    await this.verifyPageURL(accountPageURL);
}
```

Four pages, four different approaches. This makes the codebase harder to reason about and means bugs introduced in one pattern (like the early-evaluation problem) don't get caught by looking at adjacent code.

### The Fix

Standardise on getters across all pages that have a URL:

```ts
// Consistent pattern for all pages
get registerPageURL() {
    return `${process.env.BASE_URL}${this.registerPath}`;
}

get loginPageURL() {
    return `${process.env.BASE_URL}${this.loginPath}`;
}

get accountPageURL() {
    return `${process.env.BASE_URL}${this.accountPath}`;
}
```

Getters are lazy (safe from early evaluation), reusable within the class, and consistent across the codebase.

---

## Summary of Issues and Fixes

| # | File | Issue | Fix |
|---|------|-------|-----|
| 1 | `BasePage.ts` | `locator.toString()` produces useless error messages | Add `description?` param to `waitForElement` and `fillOutInput` |
| 2 | `BasePage.ts` | TOCTOU race between `waitForElement` and `locator.fill()` | Replace two-step with atomic `locator.fill({ timeout })` |
| 3 | `RegisterPage.ts` | `!` inside template literal appended to URL string | Move URL to getter, remove misplaced `!` |
| 4 | `LogInPage.ts` | `loginPageURL` class field evaluated before env is ready | Convert to getter for lazy evaluation |
| 5 | `LogInPage.ts` | `fillForm` and `submitForm` bypass base class helpers | Use `fillOutInput` and `waitForElement` everywhere |
| 6 | `data/users.ts` | `!` assertions allow `undefined` env vars to pass silently | Add `requireEnv` guard that throws on missing variables |
| 7 | `HomePage.ts` | `dismissModal` clicks before iframe content is ready | `waitForElement(closeButton)` before clicking |
| 8 | All pages | Four different URL construction patterns | Standardise on getter pattern across all pages |

---

## Key Takeaways

1. **Fail fast, fail clearly.** Silent failures — undefined env vars, wrong URLs, no error messages — cost far more debugging time than loud ones. Validate at the boundary.

2. **Atomic operations beat two-step operations.** When you check-then-act, the state can change between steps. Use APIs that handle the check and act together (like `locator.fill()` with a timeout).

3. **Consistency is correctness.** When every page follows the same pattern, bugs in one place are visible in others. Mixed patterns hide bugs and create uneven behaviour.

4. **Base class helpers exist for a reason.** If you build an abstraction layer (`waitForElement`, `fillOutInput`) and then bypass it in subclasses, you've undermined the abstraction. Use the helpers everywhere or don't have them at all.

5. **TypeScript's `!` is a promise to the compiler, not a runtime guarantee.** Every non-null assertion on an external value (env vars, API responses, DOM queries) is a place where your tests can silently degrade.
