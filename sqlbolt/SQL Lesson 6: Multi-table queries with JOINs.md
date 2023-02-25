
## Find the domestic and international sales for each movie
``` sql
SELECT Title, Domestic_sales, International_sales FROM movies
INNER JOIN Boxoffice 
    ON movies.Id = Boxoffice.Movie_id;
```
 
## Show the sales numbers for each movie that did better internationally rather than domestically
``` sql
SELECT Title, Domestic_sales, International_sales FROM movies
INNER JOIN Boxoffice 
    ON movies.Id = Boxoffice.Movie_id
WHERE Domestic_sales < International_sales;
```

## List all the movies by their ratings in descending order
``` sql
SELECT Title, Rating FROM movies
INNER JOIN Boxoffice 
    ON movies.Id = Boxoffice.Movie_id
ORDER BY Rating DESC;
```
