```bash
$ man grep
```

#### grep (search) for the word "http" in the file index.html

```bash
$ grep http index.html
```

#### grep (search) for the word "http" in the files file1.html file2.html file3.html

```bash
$ grep http file1.html file2.html file3.html
```

#### grep (search) recursively for the word "http" in all files in a directory tree

```bash
$ grep -r http 
```


#### grep (search) for the word 'inet' from the output of the "ip addr show" command

```bash
$ ip addr show | grep inet

```

#### grep (search) for the word 'Master' ignoring case

```bash
$ grep -i Master
```
