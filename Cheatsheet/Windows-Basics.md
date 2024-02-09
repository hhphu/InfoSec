### Windows Directory Paths

> **NOTE** Windows directories use the backslash, `\`, to delimit paths as opposed to Unix's forward slash, `/`!!

- `C:\` (or whichever root drive Windows is installed on) is a root drive.

- `C:\Program Files\` is where 64-bit applications are installed.

- `C:\Program Files (x86)\` is where 32-bit applications are installed.

- `C:\ProgramData\` [hidden] is a hidden directory where application-specific settings reside.

- `C:\Users\` is the directory for all users, including the `Default` user. Similar to Linux's `/home` directory.

- `C:\Users\[username]\` is each specific user's home folder. Their settings and files are saved here and in subdirectories.

  - `C:\Users\[username]\Documents\` is the `Documents` folder for the current user.

  - `C:\Users\[username]\Desktop\` is the `Desktop` folder for the current user.

- `C:\Windows\` is where Windows-specific programs and libraries are located.

  - `C\Windows\System32\` is where (counterintuitively) 64-bit main component Windows system applications configuration settings are located.

### Windows Directory Command-Line Interaction and Navigation

- `cd` or `chdir` is to change directories, just like with Linux's `cd`.

- `dir` lists the contents of a directory, similarly to Linux's `ls`

- `md` or `mkdir` creates directories.

- `copy` copies a file. This is the equivalent to Linux's `cp`.

- `move` works like cutting and pasting files, equivalent to Linux's `mv`.

- `del` or `erase` deletes files and directories. Directories will prompt a user to confirm.

  - Note that files deleted with this command do not go to the `Recycle Bin`, unlike when they are deleted with the GUI.

- `rd` or `rmdir` removes a directory if it's empty. Non-empty directories must be removed with `rmdir /S` or `rd /S`.

- `find` will search a file for whatever is defined. For example, `find "hello" greeting.txt` will search the `greeting.txt` file for the string `hello`.

- `exit` will close `cmd`.

- `type` followed by a file name will show the contents of a file. Similar to `cat` in Linux.

- `| more` or "pipe more" shows contents of the command-line in a per-screen format.

- `>` will _output_ to a file. It will make a new file or rewrite it if it exists.

  > Example: `echo hello > greeting.txt` will create a new `greeting.txt` file every time it is run.

- `>>` will _append_ to a file. It will either start a new file or add lines to the existing one.

  > Example: `echo world >> greeting.txt` will keep adding the word `world` to a new line of this file.

### Common Environment Variables

| Environment Variable | Default Value          |
| -------------------- | ---------------------- |
| %CD%                 | Current directory      |
| %DATE%               | The current date       |
| %OS%                 | Windows                |
| %ProgramFiles%       | C:\Program FIles       |
| %ProgramFiles(x86)%  | C:\Program Files (x86) |
| %TIME                | The current time       |
| %USERPROFILE%        | C:\Users\{username}    |
| %SYSTEMDRIVE%        | C:\                    |
| %SYSTEMROOT%         | C:\Windows             |

> Example: `echo %CD%` will print the `current directory` path. Note: this variable is different from the **terminal command**, `cd`.

### `WMIC` Windows Management Instrumentation Command

`wmic` has the following query structure:

- `wmic [GLOBAL SWITCHES] [ALIAS] [VERBS] [PROPERTIES]`

> Example: `wmic os get /value` will return all properties of `wmic os` for you to choose properties from:

    ```console
    BootDevice=\Device\HarddiskVolume6
    BuildNumber=18362
    BuildType=Multiprocessor Free
    Caption=Microsoft Windows 10 Pro
    ... [results truncated]
    ```

> Example 2: `wmic /APPEND:report.txt os get caption` will retrieve the operating system's common name and _append_ that to a file `report.txt`. In this example, `/APPEND:report.txt` is a global switch, `os` is an alias, `get` is our verb and `caption` is our property we're retrieving.

You can modify `wmic` queries with the `where` clause.

> Example 3: `wmic service where (startmode="auto") get caption` finds services where the `startup` property equals `auto`.

### `net` CMD

The `net user` and `net localgroup` and `net accounts` command-line utilities allow you to manage and interact with different local user and group-related settings.

