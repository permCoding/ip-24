from module import get_html
from bs4 import BeautifulSoup as BS  # pip install bs4



url = 'https://www.tiobe.com/tiobe-index/'
html = get_html(url)

soup = BS(html, "html.parser")  # lxml

h1 = soup.find('h1')

print(h1.text)
