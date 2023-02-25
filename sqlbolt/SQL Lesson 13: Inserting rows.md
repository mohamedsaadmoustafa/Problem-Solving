
## Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
``` sql
INSERT INTO Movies
(id, Title, Director, Year,	Length_minutes)
VALUES (15, 'Toy Story 4', 'John Lasseter', 2017, 123);
```

## Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
``` sql
INSERT INTO BoxOffice
(Movie_id, Rating, Domestic_sales, International_sales)
VALUES (15, 8.7, 340, 270);
```
