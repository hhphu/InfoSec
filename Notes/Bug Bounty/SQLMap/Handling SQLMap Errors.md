# Handling SQLMap Errors

- Display Errors: Use the `--parse-errors` flag. This will give us clarity on what the issue we may encounter.

```bash
...SNIP...
[16:09:20] [INFO] testing if GET parameter 'id' is dynamic
[16:09:20] [INFO] GET parameter 'id' appears to be dynamic
[16:09:20] [WARNING] parsed DBMS error message: 'SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '))"',),)((' at line 1'"
[16:09:20] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')
[16:09:20] [WARNING] parsed DBMS error message: 'SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''YzDZJELylInm' at line 1'
...SNIP...
```

- Store the traffic: use the `-t` option
```bash
sqlmap ...SNIP... --batch -t /tmp/traffic.txt
```

- Verbose Output: use `-v` option
```bash
sqlmap ...SNIP... -v 6 --batch
```

