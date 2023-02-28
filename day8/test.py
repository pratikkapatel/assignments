from selenium import webdriver
from selenium.webdriver.common.by import By
import time

d1=webdriver.Chrome()
d1.maximize_window()
d1.implicitly_wait(10)
d1.get("https://nasscom.in/")

action = webdriver.ActionChains(d1)
action.move_to_element(d1.find_element(By.XPATH,"//a[text()='Membership']")).perform()
action.move_to_element(d1.find_element(By.XPATH,"//a[text()='Become a Member']")).perform()
d1.find_element(By.XPATH,"//a[text()='Membership Benefits']").click()

d1.quit()