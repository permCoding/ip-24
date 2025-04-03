-- SELECT 
--     NameStudent,
--     Gender,
--     BallInf,
--     RANK() OVER (ORDER BY Gender ASC, BallInf DESC) as rank
-- FROM 
--     exam_balls;

-- SELECT 
--     NameStudent,
--     Gender,
--     BallInf,
--     DENSE_RANK() OVER (PARTITION BY Gender ORDER BY Gender ASC, BallInf DESC) as subject_rank
-- FROM 
--     exam_balls;
	
-- SELECT * FROM (
--     SELECT 
-- 		NameStudent,
-- 		IdDirect,
-- 		BallInf,
-- 	ROW_NUMBER() OVER (PARTITION BY IdDirect ORDER BY BallInf DESC, NameStudent) as row_num
-- 	FROM 
-- 		exam_balls
-- 	ORDER BY IdDirect DESC
-- ) 
-- WHERE row_num <= 5;

-- SELECT NameStudent, IdDirect, (BallInf + BallLang + BallMath) as sm FROM exam_balls
-- WHERE IdDirect = 1
-- 
-- UNION ALL
-- 
-- SELECT NameStudent, IdDirect, (BallInf + BallLang + BallMath) as sm  FROM exam_balls
-- WHERE IdDirect = 2
-- 
-- ORDER BY IdDirect, sm DESC

-- 

-- SELECT * FROM (
-- 	SELECT NameStudent, IdDirect, (BallInf + BallLang + BallMath) as sm FROM exam_balls
-- 	WHERE IdDirect = 1
-- 	ORDER BY sm DESC
-- 	LIMIT 3
-- )
-- 
-- UNION ALL
-- 
-- SELECT * FROM (
-- 	SELECT NameStudent, IdDirect, (BallInf + BallLang + BallMath) as sm  FROM exam_balls
-- 	WHERE IdDirect = 2
-- 	ORDER BY sm DESC
-- 	LIMIT 3
-- )

-- 

-- SELECT 
-- 	IdDirect, 
-- 	NameStudent, 
-- 	ROW_NUMBER() OVER (PARTITION BY IdDirect ORDER BY (BallInf + BallLang + BallMath) DESC) as row_num
-- FROM exam_balls
-- WHERE IdDirect IN (1, 2)

-- SELECT 
-- 	IdDirect, 
-- 	NameStudent, 
-- 	(BallInf + BallLang + BallMath) as sm, 
-- 	ROW_NUMBER() OVER (PARTITION BY IdDirect ORDER BY (BallInf + BallLang + BallMath) DESC) as row_num
-- FROM exam_balls

-- 

-- SELECT IdDirect, row_num, NameStudent, sm FROM (
--     SELECT 
--         NameStudent, 
--         IdDirect, 
--         (BallInf + BallLang + BallMath) as sm,
--         ROW_NUMBER() OVER (PARTITION BY IdDirect ORDER BY (BallInf + BallLang + BallMath) DESC) as row_num
--     FROM exam_balls
-- ) 
-- WHERE row_num <= 3
-- ORDER BY IdDirect, sm DESC;

---  

SELECT NameStudent, IdDirect, (BallInf + BallLang + BallMath) as sm
FROM exam_balls
WHERE (BallInf + BallLang + BallMath) > (
    SELECT AVG(BallInf + BallLang + BallMath) FROM exam_balls
)
ORDER BY IdDirect, sm DESC;
