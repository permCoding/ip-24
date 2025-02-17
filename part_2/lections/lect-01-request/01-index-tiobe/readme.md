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

**поиск тегов с использованием библиотеки BeautifulSoup**  

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

Извлечь все url-адреса из тегов a:  

```py
for link in soup.find_all('a'):
    print(link.get('href'))
```

---  

Найти ПЕРВЫЙ тег любого вида с классом "person":  

```py
tag = soup.find(class_="person")
```

Найти ВСЕ теги с классом "person":  

```py
tags = soup.find_all(class_="person")
if tags:
    for tag in tags:
        print(tag)
else:
    print("Теги с классом 'person' не найдены")
```

---  

Найти ПЕРВЫЙ тег <div> по классу "person":  

```py
# '<div class="person">'  
div = soup.find('div', {"class": "person"})
```

Найти ПЕРВЫЙ тег <div> по классу "person":  
`tag = soup.find('div', class_="person")`  

Найти все теги определённого вида с классом "person", например <div>:  
`tags = soup.find_all('div', class_="person")`  

Есть другой синтаксис для реализации поиска тегов:  

`tag = soup.select_one('.person')`  

`tags = soup.select('.person')`  

---  

Найти все теги с комбинацией классов:  
`tags = soup.find_all(class_=["person", "active"])`  

Найти все теги с комбинацией классов (вариант с селекторами):  
tags = soup.select('.person.active')

---  

Можно использовать **регулярки** для поиска похожих по названию.  

Найти теги, в классе которых содержится person:  

```py
import re

tags = soup.find_all(class_=re.compile(r'person'))
```

---  
