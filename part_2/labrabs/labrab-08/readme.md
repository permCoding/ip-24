## LABRAB-08  

```sql
-- SELECT lastName, idGroup
-- FROM users
-- ORDER BY idGroup DESC, lastName 
-- LIMIT 25

-- SELECT g.nameGroup, u.lastName
--   FROM users u, groups g
--  WHERE u.idGroup = g.idGroup
--  ORDER BY nameGroup, lastName 
-- O(n*m)

SELECT g.nameGroup, u.lastName
	FROM users u 
	JOIN groups g ON u.idGroup = g.idGroup
		ORDER BY nameGroup, lastName DESC
-- O(n+m)


-- SELECT 
-- 		row_number() OVER(PARTITION BY g.nameGroup ORDER BY u.lastName) as ind,
-- 		g.nameGroup, 
-- 		u.lastName
-- 	FROM users u 
-- 	JOIN groups g ON u.idGroup = g.idGroup
-- ORDER BY g.nameGroup, ind, u.lastName

SELECT * FROM
(SELECT 
		row_number() OVER(PARTITION BY g.nameGroup ORDER BY u.lastName) as _ind,
		g.nameGroup, 
		u.lastName
	FROM users u 
	JOIN groups g ON u.idGroup = g.idGroup
ORDER BY g.nameGroup, _ind, u.lastName)
WHERE _ind <= 3
```


- сгенерировать csv-файлы со списком групп и со списком учащихся  
- сделать выборку:
  - всех учащихся из определённой группы и отсортировать их по Фамилии  
  - по пять учащихся из каждой группы с сортировкой по Фамилии  
  
---  
  
> далее задачи в продолжение предыдущей лабораторки по SQLite  
> ранее нужно было выполнять задачи за счёт алгоритмов на Python  
> теперь их же нужно реализовать в БД SQLite  
> файлы csv брать из предыдущей лабораторки  

---  

**task_01**  

1. Создать базу данных SQLite, в которую импортировать файлы `directs.csv` и `exam_balls.csv`.  
2. Создать `Foregn Key` для связи таблиц по полю `IdDirect`.  
3. Создать SQL-запросы, которые реализуют все подзадачи из задачи `task_01` (из предыдущей лабы).  
   - 3.1 сортировка по одному критирию  
   - 3.2 сортировка по двум критериям  
   - 3.3 сортировка по трём критериям  

Организовать вывод в задачах так, чтобы вместо цифровых направлений обучения (1, 2, 3) выводились их настоящие названия из таблицы `directs`.  

Проверить будут ли корректно работать сортировки, если направление "Прикладная информатика" в файле `directs` перименовать в "Бизнес аналитика".  

---  

**- task_02 -**  

2.1 Организовать вывод данных, разбитых на категории по направлению поступления и внутри категории отсортированных по убыванию рейтинга (сумма по трём экзаменам).  
2.2 Организовать вывод данных, разбитых на категории по направлению поступления и внутри категория отсортированных по двум критериям - по убыванию рейтинга (сумма по трём экзаменам) и при равенстве по фозрастанию Фамилии - при этом в каждом направлении выбрать только по 5 поступающих.  

---  
