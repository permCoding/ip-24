import requests  # pip install requests


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


def get_next_tag(_str, posB, _tag, _class=None):
    cl =  f' class="{_class}"' if _class else ''
    posA = _str.find(f'<{_tag}{cl}>', posB)
    posB = _str.find(f'</{_tag}>', posA)
    tagTr = _str[posA:posB+3+len(_tag)]
    return tagTr, posB

    
url = "https://pcoding.ru/csv/exam02.html"

html = get_from_url(url)

posTr = 0
while True:
    tagTr, posTr = get_next_tag(html, posTr, 'tr', 'person')
    if posTr < 0: break
    # print(tagTr, posTr)
    
    tdList = []
    posTd = 0
    while True:
        tagTd, posTd = get_next_tag(tagTr, posTd, 'td')
        if posTd < 0: break
        tdList.append(tagTd)
    print(*tdList)


"""

<tr class="person"><td>8</td><td>Третий</td><td>10.0</td></tr>


дописать программу:

1) написать функцию выбора содержимого из td
2) написать функцию выбора содержимого из tr
3) получить все данные таблицы построчно и сформировать список объектов
4) отсортировать объекты по рейтингу по убыванию и сохранить в файл

"""