import requests  # pip install requests


def get_lines_from_url(url):
    """получить список строк из файла по адресу"""
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text


url = "https://pcoding.ru/csv/exam02.html"
# url = "https://www.tiobe.com/tiobe-index/"

txt = get_lines_from_url(url)
with open('./02.html', mode='w', encoding='utf8') as f:
    f.write(txt)
