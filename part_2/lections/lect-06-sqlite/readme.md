# SQLite  

https://docs.python.org/3/library/sqlite3.html  

```txt
01.py  
чтение из csv  
соединение с БД  
insert insert_many delete drop select update  
```

---  

```SQLite
SELECT * 
FROM people
WHERE rating > 195
ORDER BY rating DESC

-- INSERT INTO people (last_name, rating)
-- VALUES ("Клава", 199)

-- UPDATE people 
-- SET rating = 188
-- WHERE last_name = "Ася"

-- DELETE FROM people
-- WHERE last_name = "Клава"

SELECT count(*) 
FROM exam_balls
WHERE Gender = "м"

SELECT *
FROM (
  SELECT
    NameStudent,
    BallInf,
    BallLang,
    BallMath,
    (BallInf + BallLang + BallMath) AS total_sum
  FROM
    exam_balls
) AS subquery
WHERE total_sum > 222
ORDER BY total_sum DESC;

SELECT
  last_name,
  rating,
  ntile(3) OVER (ORDER BY rating DESC) as group_rating
FROM
  people;
```

- отсортировать по убыванию суммарного балла за три экзамена
- вычислить средний балл для "м"
- вычислить средний балл для "ж"



---  
