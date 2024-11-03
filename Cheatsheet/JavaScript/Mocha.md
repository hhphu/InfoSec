# Mocha

## Installation
- Installing dependencies
```bash
npm init
npm install mocha -D

-D signifies that this package is a development dependency.
```

- Add a script to `package.json`. In the "scripts" object in `package.json`, set the value of "test" to "mocha". It should look like this:

```bash
"scripts": {
  "test": "mocha"
}
```
## `Describe` and `it` functions
- We group tests using `Describe` and defining tests using `it` functions.

```javascript
describe('Math', () => {
  describe('.min', () => {
    it('returns the argument with the lowest value', () => {
      //test
    });
    it('returns -Infinity when no arguments are provided', () => {
      //test
    })
  })
})
```

## Writing tests
- Import `assert`

```javascript
const assert = require('assert');
```

- Write a test

```javascript
describe('+', () => {
  it('returns the sum of its arguments', () => {
    // Write assertion here
    assert.ok( 3+4 === 7 )

  });
});
```

