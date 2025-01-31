import csv


def get_date(filename):
    with open(filename, "r", encoding="utf8") as f:
        reader = csv.reader(f, delimiter=";")
        rows = list(reader)
        titles = rows[0]  # заголовки
        data = rows[1:]  # данные
    return [titles, data]


def get_data_filtered(lst):
    return [(elm[1],elm[3],elm[4],elm[5]) for elm in lst if elm[-1] == '1' and elm[2] == "ж"]


def create_csv(lst, titles, sep=","):
    titles = [titles[1], titles[3], titles[4], titles[5]]
    with open("./csv/result.csv", "w", encoding="utf8", newline="") as f:
        writer = csv.writer(f, delimiter=sep)
        writer.writerow(titles)  # записать строку заголовков
        writer.writerows(lst)  # записать все строки с данными


filename = "./csv/exam_balls.csv"
titles, data = get_date(filename)
lst = get_data_filtered(data)
create_csv(lst, titles)

"""
в Windows нужен параметр newline="" чтобы не было лишних переносов
"""