import sqlite3


def db_select():
    query = """SELECT * FROM users WHERE 
        users.idUser = (SELECT MAX(idUser) FROM users)"""
    cursor.execute(query)
    for row in cursor.fetchall(): print(row)


def db_insert(values):
    query = """insert into users 
        (lastName, firstName, gender, idGroup) 
        values (?, ?, ?, 
            (SELECT idGroup FROM groups WHERE nameGroup = ?)
        )"""
    
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Данные успешно вставлены.")
    except sqlite3.Error as e:
        print(f"Ошибка при вставке данных: {e}")


conn = sqlite3.connect("./users.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

person = ("Петров", "Саша", 1, "ПИб-3")

# db_insert(person)
db_select()

conn.close()
