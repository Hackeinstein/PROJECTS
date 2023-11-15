from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME,"fName")
lastname = driver.find_element(By.NAME,"lName")
email=driver.find_element(By.NAME,"email")
button=driver.find_element(By.CLASS_NAME,"btn")

firstname.send_keys("pablo")
lastname.send_keys("pablet")
email.send_keys("pablo@pabs.com")

button.click()