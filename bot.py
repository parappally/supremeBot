from selenium import webdriver
import time
from config import personalKeys

def order(keys):

    driver = webdriver.Chrome('./chromedriver')

    driver.get(keys["product_url"])

    # use chrome developer tools incase headings on site change in the future.. use copy by xpath
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys["name"]) #name in checkout
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys["email"] #email in checkout
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys["telephone"] # telephone number in checkout
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys["address"]) # address in checkout
    # I don't have a unit number, so I skipped this step...
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys["zip"])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys["city"])
    driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(keys["card_number"])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["cvv"])

if __name__ == '__main':
    order(personalKeys)
