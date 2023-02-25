
## Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.
``` sql
ALTER TABLE Movies
ADD COLUMN Aspect_ratio FLOAT;
```
## Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
``` sql
ALTER TABLE Movies
ADD COLUMN Language TEXT DEFAULT 'English';
```
