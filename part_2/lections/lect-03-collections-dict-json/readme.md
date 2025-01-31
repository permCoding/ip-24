# ЛЕКЦИЯ  

## Python collections  

### list  

### tuple  

### set  

### dict <==  

### array  

---  

**Методы работы со словарём:**  

```py
{}
dict()
{"id": 100, "direct": "asc"}
dict({"id": 100, "direct": "asc"})
dict([("id", 100), ("direct", "asc")])  # список пар
{
	1: {},
	2: {}
}
dct = {"id", 100}
dct["id"]
dct.get("id")

добавить по ключу: dct["direct"] = "desc"
изменить по ключу: dct["direct"] = "asc"
удалить по ключу: dct.pop("direct")
удалить по ключу: del dct["direct"]
очистить словарь: dct.clear()

len()
copy()
цикл по полям словаря: for key, value in dct.items()
только ключи: dct.keys()
собрать словарь: dct.fromkeys(keys) - с пустыми значениями

можно попробовать dict(zip(keys, vals)) - можно и в csv
```

Формат **json** и методы работы с ним:  

```py
import json
json.loads()
json.load()
json.dumps()
json.dump()
```

---  

Используем словарь для работы с данными, полученными из Интернета  

---  

Сортировка списка объектов по двум полям (и по разным направлениям)  

---  

Делаем свой модуль с методом main()  


if __name__ == "__main__":
	main()

---  
