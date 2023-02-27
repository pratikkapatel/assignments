import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.oracle.com/in/database/")
driver.find_element(By.XPATH,"//span[@id='acctBtnLabel']").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//a[@class='u30darkcta']").click()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME,'ssousername').send_keys('John')
driver.find_element(By.NAME, 'password').send_keys('12344')
driver.find_element(By.ID,'signin_button').click()

driver.implicitly_wait(5)
actual_error=driver.find_element(By.XPATH,"//div[contains(text(),'Invalid')]").text
print(actual_error)
time.sleep(20)
driver.quit()