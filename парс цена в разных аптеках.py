import requests # Модуль для обработки URL
from bs4 import BeautifulSoup # Модуль для работы с HTML
import time # Модуль для остановки программы
def abc():
    # Основной класс
    # Ссылка на нужную страницу
    DOLLAR_RUB = 'https://apteka35plus.ru/products/8629_Glauprost_kapli_glazn_0.005_25_ml_fl-kappach_kart_x3'
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    # Метод для получения курса валюты

    # Парсим всю страницу
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "product__price-blc"})
    print("Аптека 35 " + convert[0].text)

    
    DOLLAR_RUB = 'https://apteka.ru/product/glauprost-0005-25ml-n3-gl-kapli-flakkap-5e3279c065b5ab0001659bc9/'
    # Заголовки для передачи вместе с URL
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    # Метод для получения курса валюты

    # Парсим всю страницу
    full_page = requests.get(DOLLAR_RUB, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("div", {"class": "ux-money ProductPage__price"})
    print("Аптека ру " + convert[0].text)

abc()

