from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r'yandexdriver.exe')
options = webdriver.ChromeOptions()

options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

#options.headless = True
driver_file = 'yandexdriver.exe' # path to YandexDriver

driver = webdriver.Chrome(service=service, options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get('https://sokolov.ru/auth/login/')
el = driver.find_element(By.ID, 'loginform-phone')
driver.quit()
