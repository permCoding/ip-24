# Part-02  

## Labrab-02  

1. Написать парсер с паджинацией для маркетплеса "Читай Город"  
   - собрать данные из раздела (например, комиксы, где не менее 5-ти страниц)  
   - отсортированные по популярности (или по цене)  
   - с первых 5-ти страниц сайта  
   - делать случайную паузу в паджинации (от 1 до 3-х секунд)  
   - обязательно в requests.get() добавить User Agent  
   - сохранить массив объектов в json-файл с отступами (по 4 пробела)  

`25.02.2025 делаем только задание №1`  


---  

---  

Всё что ниже - это потом...  

2. спарсить новости с первой страницы сайта универа: `https://pgatu.ru/today/`  
   - собрать данные:  
   - название новости  
   - ссылка на новость  
   - дата  
   - описание новости  
   - сохранить локально в виде json-файла  


### API Parsing  

#### Задания для лабораторной работы:  

---  

**task-01**  

**REST API GitHub**  

https://docs.github.com/ru/rest  

---  

Задание:  

Дан аккаунт: PermCoding  

```txt
- получить список всех публичных репозиториев  
- отфильтровать только те где определён язык программирования  
- выбрать только те где язык программирования Python  
- отсортировать по дате создания от старых к новым  
- упростить объекты, выбрать только поля:  
  - название репозитория  
  - url-адрес репозитория  
  - язык программирования  
  - описание  
  - дата создания  
- сохранить в json-файл (структурированно, с отступами)  
- всем объектам добавить порядковый номер - id  
- id должны начинаться с единицы  
- id добавлять обязательно используя enumerate по коллекции  
```

---  

**task-02**  

Собрать данные с WB  
Задание уточним на Лекции  

---  

---

> в след раз можно сделать постраничный парсинг ЧГ  

--- 
 