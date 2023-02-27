import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.automationworld.com/")
driver.implicitly_wait(5)
driver.find_element(By.CLASS_NAME,'close-olytics-image-bottom-middarkblue').click()
driver.find_element(By.XPATH,"//a[@target='_blank']").click()
driver.find_element(By.XPATH,"//input[@type='radio']").click()

time.sleep(20)
driver.quit()
