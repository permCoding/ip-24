import csv

headers = ['id', 'firstName', 'lastName', 'rating']
studentsRating = [
    [1, 'Иван', 'Иванов', 4.5],
    [2, 'Петр', 'Петров', 4.6],
    [3, 'Мария', 'Сидорова', 3.8]
]

filename = 'student-rating.csv'

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(studentsRating)
