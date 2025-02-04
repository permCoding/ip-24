import requests  # pip install requests


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text

def get_from_file():
    pass
    pass


url = "https://pcoding.ru/csv/exam02.html"

txt = get_from_url(url)

posA = txt.find('<tr class="person">')
posB = txt.find('</tr>', posA)
tagTr = txt[posA:posB+5]
print(tagTr)


"""
дописать программу:

1) написать функцию выбора содержимого из td
2) написать функцию выбора содержимого из tr
3) получить все данные таблицы построчно и сформировать список объектов
4) отсортировать объекты по рейтингу по убыванию и сохранить в файл

"""