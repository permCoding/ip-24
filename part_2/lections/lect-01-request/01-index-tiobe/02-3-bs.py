import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://pcoding.ru/csv/exam02.html"
html = get_from_url(url)
soup = BS(html, 'html.parser')

title = soup.find('title')
print(title)

table = soup.find('table')
print(table)

tbody = table.find('tbody')
print(tbody)

trs = table.find('tbody').find_all('tr')
print(trs)

lst = []
for tr in trs[1:]:
    id = int(tr.find_all('td')[0].text)
    name = tr.find_all('td')[1].text
    rate = float(tr.find_all('td')[2].text)
    lst.append( (id, name, rate) )

lst.sort(key=lambda obj: obj[2], reverse=True)

for obj in lst: print(*obj)
