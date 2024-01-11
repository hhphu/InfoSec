# Attack Tuning

- Every payload consists of 2 parts: vector and boundaries.
	- vector (`UNION ALL SELECT 1,2,VERSION()`): carry the SQL code to be executed
	- boundaries ('$VECTOR-- -): prefix and suffix formations that are added to the vector

### Prefix/Suffix
- Enclose all vectors with values with static values

```bash
sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"
```

- If we have a vector `UNION ALL SELECT 1,2,VERSION()`, the resulting payload should look like this `%'))UNION ALL SELECT 1,2,VERSION()-- -`

### Level/Risk
- The option --level (1-5, default 1) extends both vectors and boundaries being used, based on their expectancy of success (i.e., the lower the expectancy, the higher the level).

- The option --risk (1-3, default 1) extends the used vector set based on their risk of causing problems at the target side (i.e., risk of database entry loss or denial-of-service).

- To tell the differences between the levels and the risks, use `-v 3`



