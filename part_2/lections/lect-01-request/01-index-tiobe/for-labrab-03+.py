def write_to_csv(filename, headers, lstRecords, sep=','):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(','.join(headers) + '\n')
        for record in lstRecords:
            # ','.join([str(field) for field in record])
            f.write(','.join(map(str, record)) + '\n')


headers = ['id', 'firstName', 'lastName', 'rating']
studentsRating = [
    [1, 'Иван', 'Иванов', 4.5],
    [2, 'Петр', 'Петров', 4.6],
    [3, 'Оля', 'Сидорова', 3.8]
]
filename = 'student-rating.csv'
write_to_csv(filename, headers, studentsRating)
