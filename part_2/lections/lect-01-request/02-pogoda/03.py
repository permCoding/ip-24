from module import get_html
import re


def ex_01(html):
    pos = 0
    # pos = html.find('<div class="current">')
    # print(html[pos:pos+1000])

    pos = html.find('<div class="temperature"', pos)
    # print(html[pos:pos+200])

    pos = html.find('>', pos)
    content = html[pos+1:pos+5]
    print(f"T = {content}")


def ex_02(html):
    pos = 0
    posA = html.find('<div class="temperature"', pos)
    posB = html.find('</div>', posA)
    tag = html[posA:posB+6]
    # print(tag)
    pattern = r'<div[^>]*>(.*?)</div>'
    match = re.search(pattern, tag, re.IGNORECASE | re.DOTALL)

    if match:
        content = match.group(1).strip()
        print(f"T = {content}")
    else:
        print("Содержимое не найдено")



url = 'https://pogoda7.ru/prognoz/gorod702-Russia-Permskiy_kray-Berezniki'
# url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm'

html = get_html(url)

ex_01(html)
ex_02(html)

"""
<div class="temperature tooltip" title="Текущая температура в Перми: -1.8°C .. -1.3°C">
    -1°C
</div>
"""