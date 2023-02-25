
## Find the list of all buildings that have employees
``` sql
SELECT DISTINCT building FROM Employees;
```
 
## Find the list of all buildings and their capacity
``` sql
SELECT * FROM Buildings;;
```

## List all buildings and the distinct employee roles in each building (including empty buildings)
``` sql
SELECT DISTINCT Building_name, Role FROM Buildings
LEFT JOIN Employees 
    ON Employees.Building = Buildings.Building_name;
```
