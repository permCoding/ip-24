# bs4

---  

Загрузить html-страницу и сделать объект BeautifulSoup для парсинга данных:  

```py
import requests  # pip install requests
from bs4 import BeautifulSoup as BS  # pip install bs4


def get_from_url(url):
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://pgatu.ru/today/"
html = get_from_url(url)
soup = BS(html, 'html.parser')

title = soup.find('title').text
print(title)
```

---  

поиск тегов с использованием библиотеки BeautifulSoup:  

Найти все теги <a> на странице и вывести их содержимое:  

```py
links = soup.find_all('a')  
for link in links:  
    print(link.text)
```

Найти элемент с определённым идентификатором и вывести его содержимое:  

```py
element = soup.find(id='my-element')  
print(element.text)
```

Найти элементы по атрибутам и их значениям:  

```py
elements = soup.find_all(attrs={'data-name': 'my-data'})  
for element in elements:  
    print(element.text)
```

Найти тег по классу:  

```py
# '<div class="current">'  

div = soup.find('div', {"class": "current"})
print(div)
```

Извлечь все url-адреса из тегов a:  

```py
for link in soup.find_all('a'):
    print(link.get('href'))
```

---  

