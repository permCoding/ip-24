-- SELECT u.idUser, u.nameUser, sum(o.pay) sm
--   FROM users u
--   JOIN orders o
--     ON u.idUser = o.idUser
--  GROUP BY u.idUser
--  ORDER BY sm DESC, u.idUser

-- WITH t as (
-- 	SELECT u.idUser, u.nameUser, sum(o.pay) sm
-- 	  FROM users u
-- 	  JOIN orders o
-- 		ON u.idUser = o.idUser
-- 	 GROUP BY u.idUser
-- 	 ORDER BY sm DESC, u.idUser
-- ) 
--     SELECT *
-- 	  FROM t
-- 	 WHERE t.sm = 5000

-- WITH t as (
-- 	SELECT u.idUser, u.nameUser, sum(o.pay) sm
-- 	  FROM users u
-- 	  JOIN orders o
-- 		ON u.idUser = o.idUser
-- 	 GROUP BY u.idUser
-- 	 ORDER BY sm DESC, u.idUser
-- ) 
--     SELECT *
-- 	  FROM t
-- 	 WHERE t.sm = (SELECT max(t.sm) FROM t)

-- SELECT u.idUser, u.nameUser, sum(o.pay) sm
--   FROM users u
--   JOIN orders o
--     ON u.idUser = o.idUser
--  WHERE o.dateOrder BETWEEN '2025-04-01' AND '2025-06-31'
--  GROUP BY u.idUser
--  ORDER BY sm DESC, u.nameUser

WITH t as (
	SELECT u.idUser, u.nameUser, sum(o.pay) sm
	  FROM users u
	  JOIN orders o
		ON u.idUser = o.idUser
	 WHERE o.dateOrder BETWEEN '2025-04-01' AND '2025-06-31'
	 GROUP BY u.idUser
)
    SELECT * FROM t
	WHERE t.sm = (SELECT max(t.sm) FROM t)
	ORDER BY t.nameUser
