import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://pcoding.ru/darkNet.php"
html = get_from_url(url)
soup = BS(html, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))