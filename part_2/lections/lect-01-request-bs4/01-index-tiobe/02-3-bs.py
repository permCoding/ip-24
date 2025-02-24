import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://pcoding.ru/csv/exam02.html"
# url = "https://pgatu.ru/today/"
html = get_from_url(url)
soup = BS(html, 'html.parser')

# title = soup.find('title').text
# print(title)

table = soup.find('table')
# print(table)

# tbody = table.find('tbody')
# print(tbody)

trs = table.find('tbody').find_all('tr')
# for tr in trs[1:]: print(tr)
# print(trs)

lst = []
for tr in trs[1:]:
    tds = tr.find_all('td')
    id = int(tds[0].text)
    lastName = tds[1].text
    rate = float(tds[2].text)
    lst.append( (id, lastName, rate) )

lst.sort(key=lambda obj: obj[2], reverse=True)

for obj in lst: print(*obj)
