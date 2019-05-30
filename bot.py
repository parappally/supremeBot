from selenium import webdriver
import time
from config import personalKeys

def order(keys):

    driver = webdriver.Chrome('./chromedriver')

    driver.get(keys["product_url"])

    driver.find_element_by_xpath('')
    # going to need to be able to find at least 10 elements on the page
    # use chrome developer tools incase headings on site change in the future
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')
    driver.find_element_by_xpath('')

if __name__ == '__main':
    order(personalKeys)
