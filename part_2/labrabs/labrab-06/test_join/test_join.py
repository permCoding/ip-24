people = [line.strip().split(';') for line in open('./people.csv').readlines()[1:]]
cities = [line.strip().split(';') for line in open('./cities.csv').readlines()[1:]]

for person in people:
    for city in cities:
        if person[2] == city[0]:
            print( person[1], city[1] )

"""
SELECT people.lastName, cities.nameCity
FROM people
JOIN cities 
ON people.idCity = cities.idCity
ORDER BY cities.nameCity
"""

# добавить САМОСТОЯТЕЛЬНО сортировку по городу
