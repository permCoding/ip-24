import requests
# import csv
from csv import reader


filename = "https://pcoding.ru/csv/abiturs.csv"
# filename = "http://files-pcoding.1gb.ru/csv?filename=abiturs.csv"

response = requests.get(filename)
response.encoding = "utf8"
lines = response.text.split("\n")
# print(lines)
# for line in lines: print(line)

# reader = csv.reader(lines, delimiter=",")
reader = reader(lines)  # delimiter=","

headers = next(reader)  # читаем строку заголовков
print(headers)
print(f'headers = {", ".join(headers)}')

for row in reader: print(row)
