import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='webdriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)


try:
    driver.maximize_window()
    driver.get('https://www.wildberries.ru/catalog/93540723/detail.aspx')
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'product-review__count-review').click()
    time.sleep(1)
    driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Смотреть все отзывы').click()
    time.sleep(1)
    reviews = open('reviews.txt', 'w')
    len_strings = 0
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while count <= 200:
    # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-1080);")

    # Wait to load page
        time.sleep(0.5)

    # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    for i in driver.find_elements(By.CLASS_NAME, 'feedback__text'):
        print(i.text)
        count += 1
    print(count)
    # while len_strings < 200:
    #     len_strings += 1
    # print()
    # time.sleep(5)
    # for _ in range(5):
    #     driver.find_element(By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.5)
    # time.sleep(1)
    # for k in driver.find_elements(By.CLASS_NAME, 'feedback__text'):
    #     print(k.text)
    time.sleep(500)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


