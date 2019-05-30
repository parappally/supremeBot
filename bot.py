from selenium import webdriver
import time
from config import personalKeys

def order(keys):

    driver = webdriver.Chrome('./chromedriver')

    driver.get(keys["product_url"])

    driver.find_element_by_xpath('')

if __name__ == '__main':
    order(personalKeys)
