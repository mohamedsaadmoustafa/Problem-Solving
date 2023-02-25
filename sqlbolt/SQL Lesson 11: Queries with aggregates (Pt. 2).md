
## Find the longest time that an employee has been at the studio
``` sql
SELECT COUNT(*) FROM employees
WHERE ROLE = 'Artist';
```

## For each role, find the average number of years employed by employees in that role
``` sql
SELECT Role, COUNT(*) FROM employees
GROUP BY Role;
```

## Find the total number of employee years worked in each building
``` sql
SELECT SUM(Years_employed) FROM employees
WHERE Role = 'Engineer';
```
