
## Find the name and role of all employees who have not been assigned to a building
``` sql
SELECT * FROM employees WHERE building IS NULL;
```

## Find the names of the buildings that hold no employees
``` sql
SELECT *
FROM buildings
LEFT JOIN employees
    ON buildings.Building_name = employees.Building
WHERE Building is NULL;
```
