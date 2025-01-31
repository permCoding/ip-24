from module import get_html
from bs4 import BeautifulSoup as BS



url = 'https://pcoding.ru/parsing/01/page.html'
html = get_html(url)

soup = BS(html, "html.parser")  # lxml

print(soup.find('title').text)
print(soup.find('h1').text)

lst = soup \
    .find('div', {'class':'shops shops__info'}) \
    .find_all('li')

smarts = [elm.text.strip() for elm in lst]

print(smarts)
