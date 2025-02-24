from module import get_html


host = 'https://pogoda7.ru/prognoz/'
cities = [
    'gorod701-Russia-Permskiy_kray-Perm',
    'gorod142-Russia-Krasnodarskiy_kray-Krasnodar',
    'gorod702-Russia-Permskiy_kray-Berezniki'
]

for city in cities:
    url = host + city
    html = get_html(url)
    # найти температуру
    # напечатать

# доработать - адреса городов скинуть в json-файл
