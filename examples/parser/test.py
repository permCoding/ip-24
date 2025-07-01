import requests
from bs4 import BeautifulSoup


url = "https://yandex.ru/pogoda/ru/50?lat=58.010454&lon=56.229441"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверяем, что запрос успешен
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # temp_element = soup.find('span', {'class': 'temp__value temp__value_with-unit'})
    temp_element = soup.find('span', {'class': 'AppFactTemperature_value__2qhsG'})
    
    if temp_element:
        temperature = temp_element.text
        print(f"Текущая температура в Перми: {temperature}°C")
    else:
        print("Не удалось найти температуру на странице.")
        
except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к Яндекс.Погоде: {e}")
    
# <span class="AppFactTemperature_value__2qhsG">21</span>
