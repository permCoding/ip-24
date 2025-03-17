-- SELECT * 
-- FROM people
-- WHERE rating > 195
-- ORDER BY rating DESC

-- INSERT INTO people (last_name, rating)
-- VALUES ("Клава", 199)

-- UPDATE people 
-- SET rating = 188
-- WHERE last_name = "Ася"

-- DELETE FROM people
-- WHERE last_name = "Клава"
 
-- SELECT count(*) 
-- FROM exam_balls
-- WHERE Gender = "м"

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