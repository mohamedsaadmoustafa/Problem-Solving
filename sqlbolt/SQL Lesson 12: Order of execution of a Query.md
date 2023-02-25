
## Find the number of movies each director has directed
``` sql
SELECT Director, COUNT(Title) FROM movies
GROUP BY Director;
```

## Find the total domestic and international sales that can be attributed to each director
``` sql
SELECT Director, SUM(Domestic_sales + International_sales)
FROM movies
JOIN Boxoffice
    ON id = Boxoffice.Movie_id
GROUP BY Director;
```
