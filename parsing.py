import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def wildberries_parsing(link):

    s = Service(executable_path='webdriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    status = 0
    try:
        driver.maximize_window()
        driver.get(link)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'product-review__count-review').click()
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Смотреть все отзывы').click()
        time.sleep(0.5)

        for _ in range(130):
            driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)

        with open('reviews.csv', 'w+', encoding='utf-8') as file:
            for line in driver.find_elements(By.CLASS_NAME, 'feedback__text'):
                file.write(line.text+'$')

    except Exception as ex:
        print(ex)
        status = 2
    finally:
        driver.quit()
        return status


def sber_parsing(link):

    s = Service(executable_path='webdriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    status = 0

    try:
        f = open('reviews.csv', 'w+', encoding='utf-8')
        driver.maximize_window()
        driver.get(link)
        time.sleep(0.5)
        driver.find_element(By.LINK_TEXT, 'Посмотреть еще отзывы').click()
        time.sleep(0.5)
        for i in range(2, 5):
            try:
                for line in driver.find_elements(By.CLASS_NAME, 'review-item__body-text'):
                    f.write(line.text+'$')
                driver.find_element(By.LINK_TEXT, str(i)).click()
                time.sleep(0.5)
            except:
                pass


    except Exception as ex:
        print(ex)
        status = 3
    finally:
        driver.quit()
        return status


def init(url):
    if url[12:23] == 'wildberries':
        error_code = wildberries_parsing(url)
    elif url[8:12] == 'sber':
        error_code = sber_parsing(url)
    else:
        error_code = 1
    return error_code


