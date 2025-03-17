import sqlite3
import csv

 
def get_csv():
    file = open('./data/data_01.csv', 'r', encoding='utf8')
    reader = csv.DictReader(file)
    # for item in reader: print(item)
    records = list(reader)
    return records


def db_create():
    query = "create table people ( \
        id integer primary key, \
        last_name text, \
        rating integer \
    )"
    cursor.execute(query)


def db_insert(records):
    query = "insert into people (last_name, rating) \
        values (?, ?)"
    for record in records:
        values = (record['last_name'], record['rating'])
        cursor.execute(query, values)


def db_insert_(records):
    query = "insert into people (last_name, rating) \
        values (:last_name, :rating)"
    for record in records:
        # print(record)
        cursor.execute(query, record)
    

def db_insert_one(record):
    query = "insert into people (last_name, rating) \
        values (?, ?)"
    cursor.execute(query, record)


def db_insert_many():
    lst = [
        "INSERT INTO 'people' VALUES (1,'Миша',207);",
        "INSERT INTO 'people' VALUES (2,'Аня',192);",
        "INSERT INTO 'people' VALUES (3,'Маша',205);",
        "INSERT INTO 'people' VALUES (4,'Аня',222);",
        "INSERT INTO 'people' VALUES (5,'Вика',211);",
        "INSERT INTO 'people' VALUES (6,'Коля',189);"
    ]
    for query in lst:
        cursor.execute(query)


def db_insert_many_ex():
    records = [
        (1,'Миша',207),
        (2,'Аня',192),
        (3,'Маша',205),
        (4,'Аня',222),
        (5,'Вика',211),
        (6,'Коля',189)
    ]
    query = "INSERT INTO people VALUES(?, ?, ?)"
    cursor.executemany(query, records)


def db_insert_records():
    records = [
        (1,'Миша',207),
        (2,'Аня',192),
        (3,'Маша',205),
        (4,'Аня',222),
        (5,'Вика',211),
        (6,'Коля',189)
    ]
    for _id, _last_name, _rating in records:
        # print(_id, _last_name, _rating)
        query = f"INSERT INTO people VALUES ({_id}, '{_last_name}', {_rating})"
        cursor.execute(query)


def db_delete(value):
    query = "delete from people where last_name = ?"
    cursor.execute(query, (value, ))


def db_delete_all(name_table):
    query = f"delete from {name_table}"
    cursor.execute(query)


def db_select():
    query = """select last_name, rating from people 
        where rating >= 180 
        order by rating desc"""
    results = cursor.execute(query).fetchall()
    for item in results:
        print(*item)


def db_select_many(count):
    query = "select * from people order by rating"
    results = cursor.execute(query).fetchmany(count)
    for item in results: print(*item)


def db_select_one(last_name):
    query = "select * from people where last_name=:last_name"
    result = cursor \
        .execute(query, {'last_name':last_name}) \
        .fetchone()
    print(result)


def db_select_like():
    query = "select id, last_name, rating \
        from people where last_name like 'М%'"
    results = cursor.execute(query).fetchall()
    for item in results:
        print(*item)


def db_update():
    query = "update people set rating=? where last_name=?"
    cursor.execute(query, (205, "Маша"))


def db_drop():
    query = "DROP TABLE IF EXISTS people"
    # query = "DROP TABLE people"
    cursor.execute(query)


conn = sqlite3.connect("./data/datafile.db")

cursor = conn.cursor()

# db_create()
# db_drop()
# db_delete_all('people')

# records = get_csv()
# db_insert(records)
# db_insert_(records)
# db_insert_one( ('Коля', 189) )
# db_insert_many()
# db_insert_many_ex()
db_insert_records()
# db_delete('Коля')
# db_select()
# db_select_many(3)
# db_select_one('Вика')
# db_select_like()
# db_update()

conn.commit()
