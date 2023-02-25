
## The director for A Bug's Life is incorrect, it was actually directed by John Lasseter 
``` sql
UPDATE Movies
SET Director = 'John Lasseter'
WHERE Id = 2;
```

## The year that Toy Story 2 was released is incorrect, it was actually released in 1999
``` sql
UPDATE Movies
SET Year = 1999
WHERE Id = 3;
```

## Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
``` sql
UPDATE Movies
SET Title = 'Toy Story 3',
     director = 'Lee Unkrich'
WHERE id = 11;
```
