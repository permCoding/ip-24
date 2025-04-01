import csv
import json


class Person:
    def __init__(self, record):
        self.id = int(record["IdStudent"])
        self.name = record["NameStudent"]
        self.Math = int(record["BallMath"])
        self.Lang = int(record["BallLang"])
        self.Inf = int(record["BallInf"])
        self.idDir = int(record["IdDirect"])

    def sum_balls(self):
        return self.Math + self.Lang + self.Inf


def get_csv():
    file = open('./data/exam_balls.csv', 'r', encoding='utf8')
    reader = csv.DictReader(file, delimiter=';')
    return list(reader)


records = get_csv()
# print(json.dumps(records, indent=4, ensure_ascii=False))

persons = []
for rec in records:
    person = Person(rec)
    persons.append(person)

for pers in sorted(persons, key=lambda x: -x.sum_balls())[:5]:
    print(pers.name, pers.sum_balls())
