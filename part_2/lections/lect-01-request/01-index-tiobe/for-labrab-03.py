import csv

headers = ['id', 'firstName', 'lastName', 'rating']
studentsRating = [
    [1, 'Иван', 'Иванов', 4.5],
    [2, 'Петр', 'Петров', 4.6],
    [3, 'Маша', 'Сидорова', 3.8]
]

filename = 'student-rating.csv'

# f = open('')
# f.close()

with open(filename, 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(studentsRating)
