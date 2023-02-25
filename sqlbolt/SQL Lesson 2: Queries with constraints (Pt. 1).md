
## Find the movie with a row id of 6
``` sql
SELECT * FROM movies
  WHERE id IS 6;
```
 
## Find the movies released in the years between 2000 and 2010
``` sql
SELECT * FROM movies
WHERE year BETWEEN 2000 AND 2010;
```

## Find the title and director of each film 
``` sql
SELECT * FROM movies
WHERE year NOT BETWEEN 2000 AND 2010;
```
## Find the title and year of each film
``` sql
SELECT * FROM movies WHERE year LIMIT 5;
```

