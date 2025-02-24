from module import get_html
from bs4 import BeautifulSoup as BS

url = 'https://pogoda7.ru/prognoz/gorod702-Russia-Permskiy_kray-Berezniki'
html = get_html(url)

soup = BS(html, "html.parser")  # lxml

div = soup.find('div', {"class":"current"})
print(div)

# '<div class="current">'