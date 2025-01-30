import re

def palindrome(my_string):
    # приводим к нижнему регистру и удаляем все символы кроме букв и цифр
    removed = re.sub(r'[^a-z0-9а-яё]', '', my_string.lower())
    reversed_string = removed[::-1]  # разворачиваем
    return removed == reversed_string


lst = ["топот", "капот", "А роза упала на лапу Азора"]
for line in lst:
    print(palindrome(line))
