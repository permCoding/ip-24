import sqlite3
import csv

 
def get_csv():
    file = open('./data/data_01.csv', 'r', encoding='utf8')
    reader = csv.DictReader(file)
    records = list(reader)
    return records


def db_create():
    # query = "create table people ( \
    #     id integer primary key, \
    #     last_name text, \
    #     rating integer \
    # )"

    query = 'CREATE TABLE "people" ( \
        "id"	integer, \
        "last_name"	text, \
        "rating"	integer, \
        PRIMARY KEY("id" AUTOINCREMENT) \
    )'
    cursor.execute(query)


def db_insert(records):
    query = "insert into people (last_name, rating) \
        values (?, ?)"
    for record in records:
        values = (record['last_name'], record['rating'])
        cursor.execute(query, values)


conn = sqlite3.connect("./data/datafile_test.db")

cursor = conn.cursor()

# db_create()

records = get_csv()
# print(records)
db_insert(records)

conn.commit()
