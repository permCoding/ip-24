import requests

def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf8'
    return response.text
