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
    time.sleep(0.5)
    driver.find_element(By.LINK_TEXT, 'Смотреть все отзывы').click()

    reviews = open('reviews.txt', 'w')
    len_strings =0
    # while len_strings < 200 or :
    #
    #     len_strings += 1
    time.sleep(500)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


