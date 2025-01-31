from module import get_html
from bs4 import BeautifulSoup as BS
import json


def get_smart(tag):
    name = tag.text.strip()
    href = tag.find('a')['href']
    return (name, href)


def get_all(html):
    soup = BS(html, "html.parser")
    lst = soup \
        .find('div', {'class':'shops shops__info'}) \
        .find_all('li')
    return [get_smart(tag) for tag in lst]


def to_json(smarts, sep=',', titles=[]):
    arr = []
    for smart in smarts:
        arr.append({'name': smart[0],'href': smart[1]})
    # with open('./data/smarts.csv', 'w') as f:
    print(json.dumps(arr, indent=2))


html = get_html('https://pcoding.ru/parsing/01/page.html')
smarts = get_all(html)
to_json(smarts)
