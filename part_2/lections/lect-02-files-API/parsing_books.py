import requests

def get_next_page(numPage):
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    url = f'https://www.chitai-gorod.ru/catalog/books/detskaya-hudozhestvennaya-literatura-110091?page={numPage}'
    repsonse = requests.get(url, headers=headers)
    repsonse.encoding = "utf8"
    return repsonse.text


numPage = 2
html = get_next_page(numPage)
print(html[:300])
