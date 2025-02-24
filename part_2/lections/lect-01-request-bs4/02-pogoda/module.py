import requests

def get_html(url):
    resp = requests.get(url)
    resp.encoding = "utf8"
    return resp.text
