import sqlite3


def db_select():
    # query = "SELECT * FROM users"

    # query = """SELECT lastName, firstName, gender 
    #                 FROM users 
    #                 WHERE gender = false 
    #                 ORDER BY lastName, firstName
    #                 LIMIT 10"""

    # query = """
    #     SELECT nameGroup, lastName, firstName
    #         FROM users u, groups g 
    #         WHERE u.idGroup = g.idGroup
    #         ORDER BY g.nameGroup, u.lastName"""

    # query = """
    #     SELECT nameGroup, lastName, firstName
    #         FROM users u 
    #         JOIN groups g 
    #         ON u.idGroup = g.idGroup
    #         ORDER BY g.nameGroup, u.lastName"""

    # query = """
    #     SELECT 
    #         ROW_NUMBER() OVER (
    #             PARTITION BY nameGroup ORDER BY lastName, firstName
    #         ) as row_number, 
    #         nameGroup, 
    #         lastName, 
    #         firstName
    #     FROM users u JOIN groups g ON u.idGroup = g.idGroup
    #     ORDER BY nameGroup, lastName"""

    # query = """
    #     SELECT * FROM (
    #         SELECT 
    #             ROW_NUMBER() OVER (
    #                 PARTITION BY nameGroup ORDER BY lastName, firstName
    #             ) as row_number, 
    #             nameGroup, 
    #             lastName, 
    #             firstName
    #         FROM users u JOIN groups g ON u.idGroup = g.idGroup
    #         ORDER BY nameGroup, lastName
    #     ) WHERE row_number <= 5"""
    
    query = """
        SELECT 
            NTILE(4) OVER (ORDER BY lastName, firstName) as num_band, 
            nameGroup, 
            lastName, 
            firstName
        FROM users u JOIN groups g ON u.idGroup = g.idGroup
        ORDER BY num_band, nameGroup, lastName"""
    
    cursor.execute(query)
    for row in cursor.fetchall(): print(row)


conn = sqlite3.connect("./users.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем поддержку внешних ключей

db_select()

conn.close()

"""
Оконные функции не изменяют данные, а только 
добавляют вычисленные значения к результирующему набору.

Оконные функции выполняются после WHERE, GROUP BY и HAVING, но до ORDER BY.

Не все базы данных поддерживают одинаковый набор оконных функций. 
SQLite поддерживает большинство основных оконных функций.

Синтаксис OVER():

Ключевым компонентом оконных функций является клауза OVER(), внутри OVER() можно указать:
  
  PARTITION BY column1, column2, ...: 
  Разбивает данные на разделы на основе значений указанных столбцов. 
  Оконная функция будет применяться отдельно к каждой секции. 
  Если PARTITION BY не указан, оконная функция применяется ко всей таблице.
  
  ORDER BY column1, column2, ...: 
  Определяет порядок строк внутри каждого раздела. 
  Это важно для функций ранжирования и функций значений.

  ROWS BETWEEN start AND end: 
  Определяет рамки окна (какие строки включаются в вычисление функции). 

Функции ранжирования - присваивают ранг каждой строке в окне на основе заданного порядка.

  RANK(): 
  Присваивает ранг каждой строке на основе порядка значений. 
  Строки с одинаковыми значениями получают одинаковый ранг, и следующий ранг пропускается. 
  Например: 1, 2, 2, 4, 5, …

  DENSE_RANK(): 
  Аналогично RANK(), но не пропускает ранги. 
  Строки с одинаковыми значениями получают одинаковый ранг, и следующий ранг идет по порядку. 
  Например: 1, 2, 2, 3, 4, …

  NTILE(n): 
  Разбивает строки в окне на n групп (плиток) и присваивает каждой строке номер плитки. 
  Полезно для разделения данных на квартили, децили и т.д.

  PERCENT_RANK(): 
  Вычисляет относительный ранг строки в окне в процентах (от 0 до 1). 
  Выражает ранг строки как процент от общего числа строк в окне.

  CUME_DIST(): 
  Вычисляет кумулятивное распределение строки в окне. 
  Выражает долю строк в окне, которые меньше или равны текущей строке.

  ROW_NUMBER():
  Вычисляет порядковый номер строки в окне.
"""