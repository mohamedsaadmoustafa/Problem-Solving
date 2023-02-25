
## Find all the Toy Story movies
``` sql
SELECT * FROM movies
WHERE Title LIKE "Toy Story%";
```
 
## Find all the movies directed by John Lasseter
``` sql
SELECT * FROM movies
WHERE Director = "John Lasseter";
```

## Find all the movies (and director) not directed by John Lasseter
``` sql
SELECT * FROM movies
WHERE Director != "John Lasseter";
```
## Find all the WALL-* movies
``` sql
SELECT * FROM movies
WHERE Title LIKE "WALL%";
```

