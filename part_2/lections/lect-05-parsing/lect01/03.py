from module import get_html


url = 'https://pogoda7.ru/prognoz/gorod702-Russia-Permskiy_kray-Berezniki'
html = get_html(url)

pos = html.find('<div class="current">')
print(html[pos:pos+1000])