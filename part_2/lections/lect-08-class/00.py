import csv
import json

 
def get_csv():
    file = open('./data/exam_balls.csv', 'r', encoding='utf8')
    reader = csv.DictReader(file, delimiter=';', skipinitialspace=True)  # заголовки берёт автоматически и убирает лишние пробелы перед данными

    # fieldnames=['id', 'name', 'email']
    # reader = csv.DictReader(file, delimiter=';', fieldnames=fieldnames)  # назначить свои заголовки
    
    records = list(reader)
    return records  # [ { "id": 1, "last_name": "Аня", ... }, ... ]


records = get_csv()
print(json.dumps(records, indent=4, ensure_ascii=False))
