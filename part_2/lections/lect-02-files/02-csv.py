import csv

f = open('./data/exam_balls.csv')

reader = csv.reader(f, delimiter=";")
headers = next(reader)  # читаем строку заголовков
print(*headers)

for row in reader:
    if row[2] == "м":
        print(*row)

f.close()
