import requests  # pip install requests


def get_from_url(url):
    """получить список строк из файла по адресу"""
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://www.tiobe.com/tiobe-index/"
html = get_from_url(url)
pos = html.find('<table id="top20"')
posStart = html.find('<tbody>', pos) + 8
posFinish = html.find('</tbody>', pos)
tbody = html[posStart: posFinish]

print(tbody)
"""
написать программу
которая сформирует csv-файл с данными
разместив их в три колонки:
место_за_2024_год;название_языка_программирования;рейтинг

Пример:
1;Python;22.85%
2;C++;10.64%
...
"""