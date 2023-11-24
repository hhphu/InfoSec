```bash
$ man find
```

#### Find all the files and directories in the current tree  

```bash
$ find
```

#### Find files in a specific directory

```bash
$ find ./demo
```

#### Find a file by name (case sensitive) in the current directory

```bash
$ find  . -name index.html
```

#### Find a file by name (not case sensitive)

```bash
$ find  . -iname index.html
```

#### Find all files in a directory

```bash
$ find  -type f
```

#### Find all directories

```bash
$ find  -type d 
```

#### Find all the .txt files

```bash
$ find -type f -name '*.txt'
```

#### Find directories that begin with Demo

```bash
$ find -type d -name 'Demo*'
```

#### Find files that are over 5MB in size

```bash
$ find ~/joe -size +5M
```

#### Find files before or after a creation time

```bash
$ find . -cmin +2
```

#### Find all html files and copy them to the directory /joe

```bash
$ find . -name '*.html' -exec cp '{}' ~/joe/ \;
```
