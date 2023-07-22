import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def correct_url(link):
    s = Service(executable_path='webdriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    try:
        driver.get(link)
        return 'correct'
    except:
        return 0

def wildberries_parsing(link):

    s = Service(executable_path='webdriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    try:
        driver.maximize_window()
        driver.get(link)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'product-review__count-review').click()
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'Смотреть все отзывы').click()
        time.sleep(1)

        for _ in range(100):
            driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)

        with open('reviews.csv', 'w', encoding='utf-8') as file:
            for line in driver.find_elements(By.CLASS_NAME, 'feedback__text'):
                # print(line.text+'$$')
                file.write(line.text+'$')

        time.sleep(1)

    except Exception as ex:
        print(ex)
        print('Введите полную ссылку на товар с Wildberries')
    finally:
        # driver.close()
        driver.quit()
    return 0

def init():
    url = input()
    if url[12:23] == 'wildberries':
        wildberries_parsing(url)
    else:
        print('Введите ссылку именно на товар с Wildberries')
    return 0

init()
