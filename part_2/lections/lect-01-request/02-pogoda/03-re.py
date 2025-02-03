import re

html = '<div class="temperature tooltip" title="Текущая температура в Перми: -1.8°C .. -1.3°C">-1°C</div>'

pattern = r'<div[^>]*>(.*?)</div>'
match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)

if match:
    content = match.group(1).strip()
    print(content)  # Вывод: -1°C
else:
    print("Содержимое не найдено")


"""
Регулярное выражение r'<div[^>]*>(.*?)</div>':
  - <div[^>]*> — ищет открывающий тег <div 
  - потом любые символы кроме > 
  - до закрывающей >
  - потом группа (.*?) — захватывает её до первого </div>
  - знак ? делает квантификатор ленивым, чтобы остановиться на первом </div>

Флаги:
  - re.IGNORECASE — игнорирует регистр тега (на случай, если в HTML есть <DIV>).
  - re.DOTALL — позволяет символу . включать переносы строк (если содержимое многострочное).

"""