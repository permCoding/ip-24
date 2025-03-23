import sqlite3


def sel_cities(table_name):  # добавим город в таблицу cities
    query = f"SELECT * FROM {table_name}"
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(*row)
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")


def add_city(cityName):  # добавим город в таблицу cities
    try:
        cursor.execute("INSERT INTO cities (cityName) VALUES (?)", (cityName, ))
        conn.commit()
        print("Город успешно добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка при вставке города: {e}")


def add_person(lastName, cityName):
    query = """INSERT INTO people (lastName, idCity) 
        VALUES (
            ?, 
            (SELECT id FROM cities WHERE cityName = ?)
        )"""
    try:
        cursor.execute(query, (lastName, cityName))
        conn.commit()
        print("Человек успешно добавлен!")
    except sqlite3.Error as e:
        print(f"Ошибка при вставке человека: {e}")


db_path = './people.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем поддержку внешних ключей


# sel_cities('people')
# add_city('Барда')
add_person('Ниязов', 'Барда')

conn.close()
