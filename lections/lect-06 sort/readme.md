# ip-24  

Это для тренировки:  

> сколько простых чисел в диапазоне от 1 до 1000  
> как меняется кол-во простых чисел в диапазонах [1; 1000], [1001; 2000], [2001; 3000], ...  
> можно написать ИГРУ - угадай число  
> написать функцию вычисления синуса  
> написать функцию сортировки по категориям:  
>   например: есть список целых чисел, отсортировать по возрастанию так  
>   чтобы сначала шли чётные, а потом нечётные  
>   было так: lst = [1, 4, 3, 5, 2, 6, 8, 9, 0, 9]  
>   стало так: [0, 2, 4, 6, 8, 1, 3, 5, 9, 9]

"""
       Я         К
###  1234      5834

1    3567 1К
2
3
4
5
6

"""

---  

## lect-06  

### Методы сортировки  

Как сравнивать алгоритмы.  
Ассимптотика сложности алгоритмов.  

Методы сортировки:  
- пузырьком  
- выбором  
- вставкой  
- быстрая  
- слиянием  

---  

Как измерять время?  
Как измерять количество операций?  

---  

Графическое представление результата.  

---  

### решаем ещё вариант задачи №17  

Порешать задачи с сайта [kompege.ru](https://kompege.ru/task)  
Задачи по теме №17: 17873, 17750, 17680.  

---  

>   

### переходим к лабораторке  

#### labrab-03  

0) Потребуется функция генерации случайно последовательности (можно взять с лекции)  

---  

1) Построить таблицы со значениями зависимостей:  

- количества шагов алгоритма от количества элементов в коллекции  
- времени исполнения алгоритма от количества элементов в коллекции  

и **сохранить данные в файле** в соответствии с названием метода сортировки:  
`sort-bubble.txt` +  

Формат сохранения:  

- первая колонка: количество элементов, например, 8000  
- вторая колонка: количество шагов, например, 100000  
- третья колонка: время, потраченное на сортировку коллекции  

Для исследований алгоритмов сортировки (выбором, пузырьком, вставкой) выбрать такие количества элементов коллекции: [1_000, 2_000, 4_000, 8_000, 16_000].  
Проанализировать: если увеличить количество элементов в два раза, то во сколько раз возрастёт время исполнения алгоритма?  
Во сколько раз предполагалось аналитически и во сколько раз получилось на практике?  

---  

2) Сравнить оптимизированный алгоритм сортировки пузырьком с обычным алгоритмом  

**для количества элементов 8_000**  

для трёх случаев:  

- если исходная коллекция полностью случайна  
- если исходная коллекция частично отсортирована  
- если исходная коллекция была почти отсортирова  

---  

```txt
`sort-select.txt`  
`sort-bubble.txt`  
`sort-choice.txt`  
`sort-quick.txt`  
`sort-merge.txt`  

_) построить по данным графики функций (это будем делать в другой раз).  
  
```