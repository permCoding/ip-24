import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://www.tiobe.com/tiobe-index/"
html = get_from_url(url)
soup = BS(html, 'html.parser')

trs = soup \
    .find('table') \
    .find('tbody') \
    .find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    print(tds[4].text)
