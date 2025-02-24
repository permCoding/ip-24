import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4
import re


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


cities = [
  "gorod142-Russia-Krasnodarskiy_kray-Krasnodar",
  "gorod701-Russia-Permskiy_kray-Perm"
]

for city in cities:
    url = "https://pogoda7.ru/prognoz/"
    url += city
    html = get_from_url(url)
    soup = BS(html, 'html.parser')

    tmp = soup \
        .find('div', class_=['temperature','tooltip']) \
        .text
    print(tmp.strip()[:-2], city)

# match = re.search(r"([-+]?\d+)", tmp)
# if match:
#   number = match.group(1)
#   print(number)

'''
символ - или + ноль или один раз (?)
потом цифра (\d) один или больше раз
потом выбрать группу - это скобки ( )
'''

# match = re.search(r"([-+]{0,1}\d{1,})", tmp)
# if match:
#   number = match.group(1)
#   print(number)
