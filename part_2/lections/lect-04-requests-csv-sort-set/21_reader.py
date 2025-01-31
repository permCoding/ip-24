import csv


filename = "./csv/exam_balls.csv"
# filename = "http://files-pcoding.1gb.ru/csv?filename=exam_balls.csv"

with open(filename, 'r', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=";")

    # for row in reader: print(row)

    lst = list(reader)[1:]  # убираем строку заголовков
    # t = sorted(lst, key=lambda x: x[1])
    # print(t)
    
    # lst = [item for item in lst if len(item) > 0]
    iterator = filter(lambda item: len(item)>0, lst)
    
    for item in sorted(iterator, key=lambda x: x[1])[:5]:
        print(item)
