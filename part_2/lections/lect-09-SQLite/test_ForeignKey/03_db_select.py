import sqlite3


def db_select():
    # query = "SELECT * FROM users"
    query = "SELECT lastName, firstName, gender FROM users WHERE gender = false ORDER BY lastName, firstName"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все записи в виде списка кортежей
    for row in rows:
        print(row)  # Вывод каждой строки




conn = sqlite3.connect("./users.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем поддержку внешних ключей

db_select()

conn.close()
