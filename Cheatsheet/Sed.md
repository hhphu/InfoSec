## sed command
- Replace string in a file
```bash
sed 's/<string>/<replaced_string>/' <filename>
```

- Replace the nth occurence of a pattern 
```bash
sed 's/<string>/<replaced_string>/n' <filename>
```

- Replace all occurences of the pattern
```bash
sed 's/<string>/<replaced_string>/g' <filename>
```

- Replace from nth occurence to all occurences:
```bash
sed 's/<string>/<replaced_string>/4g' <filename>
```

- Delete a particular line from a file (assuming line 3)
```bash
sed '3d' <filename>
```

- Delete the last line of the file
```bash
sed '$d' <filename>
```

- Delete a number of lines (assuming from line 5 to 10)
```bash
sed '5,10d' <filename>
```

