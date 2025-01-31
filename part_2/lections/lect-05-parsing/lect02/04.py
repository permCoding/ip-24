from module import get_html
from bs4 import BeautifulSoup as BS


def get_smart(tag):
    name = tag.text.strip()
    href = tag.find('a')['href']
    return (name, href)


def to_file(smarts, sep=',', titles=[]):
    with open('./data/smarts.csv', 'w') as f:
        f.write(sep.join(titles) + '\n')
        for smart in smarts:
            f.write(sep.join(smart) + '\n')


url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)

soup = BS(html, "html.parser")

lst = soup \
    .find('div', {'class':'shops shops__info'}) \
    .find_all('li')

smarts = [get_smart(tag) for tag in lst]
to_file(smarts, ';', ['name', 'href'])
