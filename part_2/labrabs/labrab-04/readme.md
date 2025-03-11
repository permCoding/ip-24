# Part-02  

## Labrab-04  

> 11.03.2025  

Собрать данные с сайта `https://www.wildberries.ru/`  
НЕ парсить html-страницу, а сделать запрос к API и получить массив продуктов в виде json  
Для работы использовать библиотеки **requests** и **json**  

```py
import json

json.dump()  # для сохранения json-файла на диск

json.load()  # для загрузки json-фалй с диска
```

---  

**task-01**  

Выбрать на сайте WB такой продукт, у которого будет не менее 3-х страниц (это примерно более 300 продуктов)  
Найти в браузере с помощью Инструмента разработчика на вкладке Net (Сеть) на самом сайте WB ссылку на запрос про выбранные продукты  

Например, для адресной строки такой: `https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=popular&search=onyx+book`  
Запрос от сайта WB на получение списка продуктов для первой страницы будет выглядеть так:  
`https://search.wb.ru/exactmatch/ru/male/v9/search?ab_testing=false&appType=1&curr=rub&dest=12358373&lang=ru&page=1&query=onyx%20book&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false&uclusters=1&uiv=0&uv=AQEAAQIACD5sOCFIPTfWO1xEpcH_tMw78CxSvNNAnbMawum_qkJGurOqTcQsRP8-_j2KxDzBmD3AxNDA-8AQu4U4rzggPh6lWrwhvz3DuLq6vKnAwKx0P7ZBdTskP8bFQrygQbI0-MQzvsNEYsZLRQBAAUCXudC4ar_gNhU6vD2XuaA0LTn1Nm_DXzqcwRA5nbpVQ0e8wzf7Pr84rEBPw00-qjmQvr5A8rp8Pqa9_0MTwMUvzzybPMU4mT7JOjavTcIZPHbEDThzxD26zrvHQ4s-1sDntLu5vDymQ3w_NLF3QY-89DDCuhhCPbcjseC9TTocN7u9qcQKvJg1iC_MPt86N0DxQJs`  
Для остальных страниц требуется только поменять параметр в запросе: `page=1`  

Используя библиотеку requests с помощью метода get по этой ссылке на продукты получить массив продуктов с трёх первых страниц и сохранить их локально на диске все в виде одного большого файла json - `all_products.json`  

---  

**task-02**  

Загрузите в программу массив объектов из файла `all_products.json`  
Выбрать только требуемые данные для каждого из объектов и сохранить в виде нового json-массива в таком формате:  

```txt
[
    {
        "brand": "Pocketbook",
        "name": "Электронная книга 970",
        "reviewRating": 4.8,
        "feedbacks": 203,
        "price": 3629800,
        "totalQuantity": 32,
        "id": 182763343,
        "link": "https://www.wildberries.ru/catalog/182763343/detail.aspx"
    },
    ...
]

---  
