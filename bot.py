from selenium import webdriver
import time
from config import personalKeys

web_countries = {
    "USA" : 1,
    "CA" : 2
}

web_provinces = {
    "AB" : 2,
    "BC" : 3,
    "MB" : 4,
    "NB" : 5,
    "NL" : 6,
    "NT" : 7,
    "NS" : 8,
    "NU" : 9,
    "ON" : 10,
    "PE" : 11,
    "QC" : 12,
    "SK" : 13,
    "YT" : 14,
}

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

    driver.find_element_by_xpath('//*[@id="order_billing_country"]/option[web_countries["CA"]]').click() # country dropdown
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[web_provinces["ON"]]').click() # province dropdown
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys["city"])


    driver.find_element_by_xpath('//*[@id="nnaerb"]').send_keys(keys["card_number"])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[9]').click() # credit card expiry month dropdown, change 9 to the whatever number month of the year you need
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[3]').click() # credit card expiry year dropdown, 1 is 2019, 2 is 2020, 3 is 2023 etc.
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["cvv"])


    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins')click() #terms and conditions
    driver.find_element_by_xpath('//*[@id="pay"]/input')click() # process payment button

if __name__ == '__main':
    order(personalKeys)
