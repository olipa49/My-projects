from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random, time
#phone = '9637328400'
phone = '9005469722'
def ran():
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = ''
    for i in range(11):
        b += random.choice(a)
    return b
def ran_ru():
    a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    b = ''
    for i in range(11):
        b += random.choice(a)
    return b
#service = Service(executable_path=r'chromedriver.exe')
options = webdriver.ChromeOptions()

options.add_argument("start-maximized")

# options.add_argument("--headless")

options.headless = True

driver = webdriver.Chrome(options=options)

#driver.set_window_size(300, 300)
driver.get('https://mavlivefaberlic.ru/710389187?utm_source=yandexanvsestrani&utm_medium=cpc&utm_campaign=104301049&utm_content=15738500911&utm_term=Череповец&yclid=16151467680312852479')
el = driver.find_element(By.ID, 'regform-surname')
el.send_keys("Иван")
el = driver.find_element(By.ID, 'regform-name')
el.send_keys("Смирнов")
el = driver.find_element(By.ID, 'regform-birthday')
el.send_keys('01012000')
el = driver.find_element(By.ID, 'regform-email')
el.send_keys(ran() + '@gmail.com')
el = driver.find_element(By.ID, 'regform-phone')
el.send_keys(phone)
el = driver.find_element(By.XPATH, '//*[@id="step1"]/div[9]/button')
el.click()
time.sleep(1)


driver.get('https://armyansk.roliksushi.ru/')
el = driver.find_element(By.XPATH, '//*[@id="root"]/header/div/div[1]/div[2]/span/button')
el.click()
el = driver.find_element(By.XPATH, '//*[@id="auth_modal"]/div[4]/div[1]/input')
el.send_keys(phone)

##select = Select(driver.find_element(By.XPATH, '//*[@id="auth_modal"]/div[4]/div[2]/div[2]/select'))
##select.select_by_value("sms")

el = driver.find_element(By.XPATH, '//*[@id="auth_modal"]/div[4]/div[2]/div[1]/label[3]')
el.click()
el = driver.find_element(By.XPATH, '//*[@id="auth_modal"]/div[4]/div[3]/button')
el.click()
time.sleep(1)

if phone == "9005469722":
    driver.get('https://alizaim.ru/')
    driver.find_element(By.XPATH, '/html/body/app-root/div/div[1]/div/app-header/div[1]/header/div/div[3]/span[2]').click()
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[3]/div/div[1]/span').click()
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[2]/form/div/div[2]/div[1]/input').send_keys(phone)
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[2]/form/div/div[2]/div[2]/input').send_keys("Смирнов")
    driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div/div[2]/form/p/button').click()
time.sleep(1)
