from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options= Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com") 
driver.maximize_window()
email=driver.find_element(By.NAME, 'email')
email.send_keys("[EMAIL_ADDRESS]")
password= driver.find_element(By.NAME, 'pass')
password.send_keys("Your password")
loginbutton= driver.find_element(By.XPATH, "//span[text()='Log in']")
loginbutton.click()
time.sleep(5)
perpostbtn=driver.find_element(By.CSS_SELECTOR, '[aria-label="Facebook menu"]')
perpostbtn.click()
time.sleep(2)
post= driver.find_element(By.XPATH, "//div[./svg]")
post.click()
time.sleep(5)
