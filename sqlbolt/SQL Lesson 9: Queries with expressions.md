
## List all movies and their combined sales in millions of dollars
``` sql
SELECT title,
    (domestic_sales + international_sales) / 1000000 AS sales
FROM movies
JOIN Boxoffice
    ON id = Boxoffice.movie_id;
```

## List all movies and their ratings in percent
``` sql
SELECT DISTINCT Title,
    (Rating * 10) AS rate_percent
FROM movies
JOIN Boxoffice
    ON id = Boxoffice.movie_id;
```

## List all movies that were released on even number years
``` sql
SELECT Title
FROM movies
WHERE Year % 2 = 0;
```
