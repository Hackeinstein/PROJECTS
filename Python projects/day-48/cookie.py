from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_object = driver.find_element(By.ID, "cookie")
timeout = time.time() + 5
five_min = time.time() + (60 * 5)

while True:
    cookie_object.click()
    if time.time() > timeout:
        # check price compare and buy
        price_list = []
        store_object = driver.find_elements(By.CSS_SELECTOR, "#store div")
        object_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        cookie = int(driver.find_element(By.ID, "money").text)
        # get prices into list and make them integer for comparison
        for price in object_price:
            try:
                price_ = price.text.split(" - ")
                price_list.append(int(price_[1].replace(",", "")))
            except IndexError:
                pass
        # compare and get item to click
        buy: int

        for price in price_list:
            if cookie > price:
                buy = price_list.index(price)

        store_object[buy].click()

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break
