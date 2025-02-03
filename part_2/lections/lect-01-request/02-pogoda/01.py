import requests

def get_html(url):
    resp = requests.get(url)
    resp.encoding = "utf8"
    return resp.text


host = 'https://pogoda7.ru/prognoz/'
city = 'gorod142-Russia-Krasnodarskiy_kray-Krasnodar'
url = host + city
html = get_html(url)

f = open('pogoda.html', 'w', encoding='utf8')
f.write(html)

# <div class="current">