# SQLite  

1) Создание внешнего ключа при создании таблицы people:  

Если таблица people еще не создана, можно сразу добавить определение внешнего ключа в SQL-код для создания таблицы:  

```sql
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    lastName TEXT,
    idCity INTEGER,
    FOREIGN KEY (idCity) REFERENCES cities(idCity)
);
```

---  

2) Добавление внешнего ключа к существующей таблице people:  

Если таблица people уже существует, можно добавить внешний ключ с помощью команды ALTER TABLE.  
SQLite ранее имел ограниченную поддержку ALTER TABLE, но современные версии (3.35.0 и новее) поддерживают добавление внешних ключей напрямую.  

```sql
ALTER TABLE people
ADD FOREIGN KEY (idCity) REFERENCES cities(idCity);
```

---  

Включение поддержки внешних ключей  

По умолчанию, поддержка внешних ключей в SQLite отключена. В большинстве случаев нужно включить её для каждого соединения с базой данных. Это делается следующим образом:  

```sql
PRAGMA foreign_keys = ON;
```

Вы должны выполнить этот запрос после каждого открытия соединения с базой данных. Некоторые инструменты (например, ORM) могут делать это автоматически. Если вы этого не сделаете, внешние ключи не будут работать (ограничения не будут применяться).  

**Существующие данные:** Прежде чем добавить внешний ключ к существующей таблице, убедитесь, что все значения в столбце idCity таблицы people соответствуют существующим значениям в столбце idCity таблицы cities. Если есть значения, которые не соответствуют, добавление внешнего ключа завершится ошибкой. Вам нужно будет исправить данные перед добавлением внешнего ключа.  

**Типы данных:** Убедитесь, что столбцы idCity в обеих таблицах имеют совместимые типы данных (обычно INTEGER).  

**Первичный ключ/UNIQUE ограничение:** Столбец, на который ссылается внешний ключ (в данном случае cities.idCity), должен быть первичным ключом или иметь ограничение UNIQUE в таблице cities.  

---  

С помощью оператора CONSTRAINT можно задать имя для ограничения внешнего ключа:

```sql
CREATE TABLE users
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    company_id INTEGER,
    CONSTRAINT users_companies_fk 
    FOREIGN KEY (company_id)  REFERENCES companies (id)
);
```

Вставка записи в таблицу с внешним ключём:  

```sql
SELECT lastName, cityName 
FROM people
JOIN cities
WHERE people.idCity = cities.id
```

```sql
INSERT INTO people (lastName, idCity) 
VALUES 
(
    'Максимов', 
    (SELECT id FROM cities WHERE cityName = "Кунгур")
);
```
