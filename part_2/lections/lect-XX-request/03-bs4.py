import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://www.tiobe.com/tiobe-index/"
html = get_from_url(url)
soup = BS(html, "html.parser")  # lxml

title = soup.find('title')  # весть тег
print(title)
print(soup.find('title').text)  # содержимое тега

table = soup.find('table', id='top20')  # table избыт, тк id уникально
trs = table.find('tbody').find_all('tr')
for tr in trs[:10]:
    print(tr.find_all('td')[4].text)


"""


title = soup.find('title')
print(title)
print(soup.find('title').text)

# soup.find('div')
# soup.find_all('div')

# '<div class="current">'

написать программу
которая сформирует список первых 10-ти языков программирования

=> теперь самостоятельно
- вывести на экран список в формате: язык программирования и его рейтинг
- отсортировать полученный список пар (язык, рейтинг) по алфавиту (не по рейтингу)
- выявить те языки, у которых рейтинг снизился по сравнению с предыдущим годом
"""