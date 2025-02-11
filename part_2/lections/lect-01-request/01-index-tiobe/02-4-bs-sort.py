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

table = soup.find('table')

trs = table.find('tbody').find_all('tr')

lst = []
for tr in trs[1:]:
    tds = tr.find_all('td')
    id = int(tds[0].text)
    lastName = tds[1].text
    rate = float(tds[2].text)
    lst.append( (id, lastName, rate) )

# lst.sort(key=lambda obj: (obj[2], -obj[0]))  # Арсений
# for obj in lst: print(*obj)

# lst_sorted = sorted(lst, key=lambda obj: obj[1], reverse=True)  # Полина
# lst_sorted = sorted(lst_sorted, key=lambda obj: -obj[2])  # Полина
# for obj in lst_sorted: print(*obj)

lst_sorted = sorted(
    sorted(lst, key=lambda obj: obj[1]), 
    key=lambda obj: -obj[2]
)
for obj in lst_sorted: print(*obj)
