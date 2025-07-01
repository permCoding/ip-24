import requests
from bs4 import BeautifulSoup

# URL для Перми (координаты 58.010454, 56.229441)
url = "https://yandex.ru/pogoda/ru/50?lat=58.010454&lon=56.229441"

# Заголовки для имитации браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Отправляем GET-запрос
response = requests.get(url, headers=headers)

# Проверяем, что запрос успешный
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Ищем температуру в HTML. Используем классы, которые часто встречаются на Yandex
    # Обычно текущая температура находится в элементе с классом "temp__value"
    temperature_element = soup.find("div", class_="temp__value")
    
    if temperature_element:
        temperature = temperature_element.get_text()
        print(f"Сегодняшняя температура в Перми: {temperature}")
    else:
        print("Температура не найдена на странице.")
else:
    print(f"Ошибка доступа: {response.status_code}")
