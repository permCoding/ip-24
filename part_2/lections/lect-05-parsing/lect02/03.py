from module import get_html
from bs4 import BeautifulSoup as BS


def get_smart(tag):
    name = tag.text.strip()
    href = tag.find('a')['href']
    return (name, href)


url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)

soup = BS(html, "html.parser")

lst = soup \
    .find('div', {'class':'shops shops__info'}) \
    .find_all('li')

smarts = [get_smart(tag) for tag in lst]

for smart in smarts:
    print(*smart)
