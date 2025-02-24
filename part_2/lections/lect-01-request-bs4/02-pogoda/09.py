from module import get_html
from bs4 import BeautifulSoup as BS

def get_temp(html):
    soup = BS(html, "html.parser")
    return soup \
        .find('div', {"class":"current"}) \
        .find('div', {"class":"temperature"}) \
        .text


for city in cities:
    url = host + city
    html = get_html(url)
    temp = get_temp(html)
    print(temp)

# доработать