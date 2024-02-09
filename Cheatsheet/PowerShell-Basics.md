### Common PowerShell commands

| CMDlet          | Function                                         | Equivalent command     |
| --------------- | ------------------------------------------------ | ---------------------- |
| `Set-Location`  | Changes to specified directory                   | `cd`                   |
| `Get-ChildItem` | Returns current directories contents             | `ls`, `dir`            |
| `New-Item`      | Makes a new directory                            | `mkdir`                |
| `Remove-Item`   | Deletes a file or directory                      | `rm`, `rmdir`          |
| `Get-Location`  | Retrieves path to current directory              | `pwd`                  |
| `Get-Content`   | Returns file contents                            | `cat`, `type`          |
| `Copy-Item`     | Copies a file from one given location to another | `cp`                   |
| `Move-Item`     | Moves a file from one given location to another  | `mv`                   |
| `Write-Output`  | Prints output                                    | `echo`                 |
| `Get-Alias`     | Shows aliases for the current session.           | `alias`                |
| `Get-Help`      | Retrieves information about PowerShell commands  | `man`                  |
| `Get-Process`   | Gets processes running on local machine          | `ps`                   |
| `Stop-Process`  | Stops one or more defined process(es)            | `kill`                 |
| `Get-Service`   | Gets a list of services                          | `service --status-all` |

### How to use documentation and find commands

How to find documentation on a cmdlet:

> `Get-Help {cmdlet}`

To find documentation on `Set-Location`:

> `Get-Help Set-Location`

Finding specific examples:

> `Get-Help {cmdlet} -examples`

How to find cmdlets by noun:

> `Get-Command -Type Cmdlet | Sort-Object -Property Noun | Format-Table -GroupBy Noun`

How to find cmdlets by verb:

> `Get-Command -Type Cmdlet | Sort-Object -Property Verb | Format-Table -GroupBy Verb`

#### Wildcards

How to find by noun:

> `Get-Command -Noun {noun}`

How to find by verb:

> `Get-Command -Verb {verb}`

### An Example Remote Transfer Script

A Sample script that will create files and transfer them to a remote server.

- Note: You will need to run the script a directory above the files that you are transferring over.

> ##### Example Script

```PowerShell
mkdir ".\Files\" -Force

New-Item ".\Files\file1.txt" -Force
New-Item ".\Files\file2.txt" -Force
New-Item ".\Files\file3.txt" -Force

$Session = New-PSSession -ComputerName 192.168.1.5 -Credential "ExampleUser"

$files_list = ls ".\Files\*"

foreach ($file in $files_list) {
    Copy-Item $log -Destination "C:\Files\" -ToSession $Session
    echo "Copied $file to remote machine C:\Files directory!"
}
```

When this script is run it will do the following:

- Create a new directory `Files`. If the directory exists, the rest of the script will not error because the `-Force` parameter.

- Create three empty files in the `Files` directory. If the files exist, the rest of the script will not error because the `-Force` parameter.

- Establish a remote PowerShell session as a variable.

- Retrieve the contents of the `Files` directory and assign it to `$files_list`.

- A `foreach` loop that, for every file item that exists in the directory, will:

  - Transfer the file from the `Files` folder to the remote machine's `C:\Files\` directory.

  - Print to console, the name of the file item that was transferred.
