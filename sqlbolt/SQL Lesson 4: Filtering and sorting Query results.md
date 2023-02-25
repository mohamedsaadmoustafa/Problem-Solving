
## List all directors of Pixar movies (alphabetically), without duplicates
``` sql
SELECT DISTINCT director FROM movies
ORDER BY director;
```
 
## List the last four Pixar movies released (ordered from most recent to least)
``` sql
SELECT Title FROM movies
ORDER BY Year DESC
LIMIT 4;
```

## List the first five Pixar movies sorted alphabetically
``` sql
SELECT Title FROM movies
ORDER BY Title 
LIMIT 5;
```
## List the next five Pixar movies sorted alphabetically
``` sql
SELECT Title FROM movies
ORDER BY Title 
LIMIT 5 
OFFSET 5;
```

