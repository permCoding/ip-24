from module import get_html
from bs4 import BeautifulSoup as BS

url = 'https://pogoda7.ru/prognoz/gorod702-Russia-Permskiy_kray-Berezniki'
html = get_html(url)

soup = BS(html, "html.parser")  # lxml

title = soup.find('title')
print(title)
print(soup.find('title').text)

# soup.find('div')
# soup.find_all('div')

# '<div class="current">'