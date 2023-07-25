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

        with open('reviews_wb.csv', 'w', encoding='utf-8') as file:
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


def sber_parsing(link):

    s = Service(executable_path='webdriver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    try:
        f = open('reviews.csv', 'w', encoding='utf-8')
        driver.maximize_window()
        driver.get(link)
        time.sleep(0.5)
        # driver.find_element(By.CLASS_NAME, 'reviews-rating__reviews-count').click()
        driver.find_element(By.LINK_TEXT, 'Посмотреть еще отзывы').click()
        time.sleep(0.5)
        for i in range(2, 10):
            # for line in driver.find_elements(By.CLASS_NAME, 'review-item__body-text'):
            #     print(line.text+'$')
            try:
                for line in driver.find_elements(By.CLASS_NAME, 'review-item__body-text'):
                    f.write(line.text+'$')
                driver.find_element(By.LINK_TEXT, str(i)).click()
                time.sleep(0.5)
            except:
                pass

        time.sleep(1)

    except Exception as ex:
        print(ex)
        print('Введите полную ссылку на товар с Sbermegamarket')
    finally:
        # driver.close()
        driver.quit()
    return 0


def init():
    url = input()
    if url[12:23] == 'wildberries':
        wildberries_parsing(url)
    elif url[8:12] == 'sber':
        sber_parsing(url)
    else:
        print('Введите ссылку именно на товар с Wildberries')
    return 0

init()
