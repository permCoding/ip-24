import sqlite3  # pip install sqlite3
import csv
import json

 
def get_csv(fn):
    file = open(fn, 'r', encoding='utf8')
    reader = csv.DictReader(file, delimiter=';')  # { "id": 1, "last_name": "Аня" }
    return list(reader)  # [ {}, {}, {}, ..]


def db_create():
    
    query = 'CREATE TABLE IF NOT EXISTS "groups" ( \
        "idGroup" integer, \
        "nameGroup"	text, \
        PRIMARY KEY("idGroup" AUTOINCREMENT) \
    )'
    cursor.execute(query)

    query = 'CREATE TABLE IF NOT EXISTS "users" ( \
        "idUser" INTEGER, \
        "lastName" TEXT, \
        "firstName" TEXT, \
        "gender" INTEGER, \
        "idGroup" INTEGER, \
        FOREIGN KEY("idGroup") REFERENCES "groups"("idGroup") \
    )'
    cursor.execute(query)


def db_insert_groups(records):
    query = "insert into groups (idGroup, nameGroup) values (?, ?)"
    for record in records:
        values = (record['idGroup'], record['nameGroup'])
        cursor.execute(query, values)


def db_insert_users(records):
    query = "insert into users \
        (idUser, lastName, firstName, gender, idGroup) \
        values (?, ?, ?, ?, ?)"
    for record in records:
        values = (
            record['idUser'], 
            record['lastName'], 
            record['firstName'], 
            record['gender'], 
            record['idGroup']
        )
        cursor.execute(query, values)


conn = sqlite3.connect("./users.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")  # Включаем поддержку внешних ключей

# db_create()

records = get_csv('./groups.csv')
# print(json.dumps(records, indent=4, ensure_ascii=False))
db_insert_groups(records)

records = get_csv('./users.csv')
# print(json.dumps(records, indent=4, ensure_ascii=False))
db_insert_users(records)

conn.commit()
conn.close()

# commit() после изменения данных INSERT/UPDATE/DELETE
