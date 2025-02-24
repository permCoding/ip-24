from module import get_html
from bs4 import BeautifulSoup as BS

def get_temp(html):
    soup = BS(html, "html.parser")
    return soup \
        .find('div', {"class":"current"}) \
        .find('div', {"class":"temperature"}) \
        .text


host = 'https://pogoda7.ru/prognoz/'
cities = [
    'gorod701-Russia-Permskiy_kray-Perm',
    'gorod142-Russia-Krasnodarskiy_kray-Krasnodar',
    'gorod702-Russia-Permskiy_kray-Berezniki'
]

for city in cities:
    url = host + city
    html = get_html(url)
    temp = get_temp(html)
    print(temp)
