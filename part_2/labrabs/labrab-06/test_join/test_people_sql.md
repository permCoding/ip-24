```sql
SELECT people.lastName, cities.nameCity
FROM people
JOIN cities ON people.idCity = cities.idCity
```