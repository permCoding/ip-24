import requests  # pip install requests


def get_lines_from_url(url):
    """получить список строк из файла по адресу"""
    req = requests.get(url)
    req.encoding = "utf8"
    return req.text.split('\n')


url = "https://pcoding.ru/csv/exam03.txt"
url = "https://pcoding.ru/csv/exam_balls.csv"
url = "https://pcoding.ru/csv/14.txt"
url = "https://www.tiobe.com/tiobe-index/"
lines = get_lines_from_url(url)
print(lines)
