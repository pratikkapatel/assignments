import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://phptravels.net/home")

actions=webdriver.ActionChains(driver)

driver.find_element(By.XPATH,"//a[normalize-space()='flights']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Flying From']").send_keys("los angele")
actions.send_keys(webdriver.Keys.ARROW_DOWN).perform()
actions.send_keys(webdriver.Keys.ENTER).perform()

driver.find_element(By.XPATH,"//input[@id='autocomplete2']").send_keys("dallas")
actions.send_keys(webdriver.Keys.ARROW_DOWN).perform()
actions.send_keys(webdriver.Keys.ENTER).perform()

driver.find_element(By.XPATH,"//input[@class='depart form-control']").send_keys("2022-05-30")
driver.find_element(By.XPATH,"//a[@class='dropdown-toggle dropdown-btn travellers waves-effect']").click()
driver.find_element(By.XPATH,"//i[@class='la la-plus']").click()
driver.find_element(By.XPATH,"//a[@class='dropdown-toggle dropdown-btn travellers waves-effect']").click()
driver.find_element(By.ID,"flights-search").click()
driver.find_element(By.XPATH,"//img[@alt='no results']").is_displayed()

time.sleep(5)
driver.quit()

