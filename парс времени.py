import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
def abc():
    # Основной класс
    # Ссылка на нужную страницу
    DOLLAR_RUB = 'https://www.google.com/search?q=время&sourceid=chrome&ie=UTF-8'
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    # Метод для получения курса валюты

    # Парсим всю страницу
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "gsrt", "class": "vk_bk"})
    print(convert[0].text)
##    time.sleep(1)
    abc()
abc()

