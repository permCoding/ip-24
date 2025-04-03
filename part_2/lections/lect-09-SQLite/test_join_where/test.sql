
-- EXPLAIN QUERY PLAN 
SELECT hobby.idDirect, hobby.nameHobby
FROM hobby, directs
WHERE hobby.idDirect = directs.idDirect AND hobby.nameHobby LIKE 'на%'
-- ORDER BY directs.idDirect, hobby.nameHobby
-- Result: 2491 строк возвращено за 60 мс

-- EXPLAIN QUERY PLAN 
-- SELECT hobby.idDirect, hobby.nameHobby
-- FROM hobby JOIN directs
-- ON hobby.idDirect = directs.idDirect AND hobby.nameHobby LIKE 'на%'
-- ORDER BY directs.idDirect, hobby.nameHobby
-- Result: 200000 строк возвращено за 849мс

-- DELETE FROM hobby;
-- DELETE FROM directs;




-- SELECT hobby.idDirect, hobby.nameHobby
-- FROM hobby, directs
-- WHERE hobby.idDirect = directs.idDirect
-- ORDER BY directs.idDirect, hobby.nameHobby
-- 90 msec

-- SELECT hobby.idDirect, hobby.nameHobby
-- FROM hobby JOIN directs
-- ON hobby.idDirect = directs.idDirect
-- ORDER BY directs.idDirect, hobby.nameHobby
-- 36 msec

-- SELECT users.nameUser, users.gender, hobby.nameHobby
-- FROM users
-- JOIN refUserHobby ON users.idUser = refUserHobby.idUser
-- JOIN hobby ON hobby.idHobby = refUserHobby.idHobby
-- ORDER BY users.gender, users.nameUser

-- SELECT users.nameUser, users.gender, hobby.nameHobby
-- FROM users, refUserHobby, hobby
-- WHERE users.idUser = refUserHobby.idUser AND hobby.idHobby = refUserHobby.idHobby
-- ORDER BY users.gender, users.nameUser


-- SELECT DISTINCT hobby.nameHobby
-- FROM users
-- JOIN refUserHobby ON users.idUser = refUserHobby.idUser
-- JOIN hobby ON hobby.idHobby = refUserHobby.idHobby
-- ORDER BY hobby.nameHobby

-- SELECT DISTINCT hobby.nameHobby
-- FROM hobby
-- JOIN refUserHobby ON hobby.idHobby = refUserHobby.idHobby
-- ORDER BY hobby.nameHobby

-- SELECT DISTINCT hobby.nameHobby
-- FROM hobby, refUserHobby
-- WHERE hobby.idHobby = refUserHobby.idHobby
-- ORDER BY hobby.nameHobby