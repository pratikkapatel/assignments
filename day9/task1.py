import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://demo.openemr.io/b/openemr/")

#//input[contains(@id,'UserFirst')]
driver.find_element(By.XPATH,"//input[contains(@id,'authUser')]").send_keys("admin")
driver.find_element(By.XPATH,"//input[contains(@id,'clearPass')]").send_keys("pass")

#//select[@title='Month']
select_lang = Select(driver.find_element(By.XPATH,"//select[@name='languageChoice']"))
select_lang.select_by_visible_text("English (Indian)")

#//button[contains(text(),'start my free')]
driver.find_element(By.XPATH,"//button[contains(text(),'Login')]").click()

actions = webdriver.ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH,"//div[text()='Patient']")).perform()
actions.move_to_element(driver.find_element(By.XPATH,"//div[contains(text(),'New/Search')]")).click()

time.sleep(10)
driver.find_element(By.XPATH,"//input[contains(@id,'form_fname')]").send_keys("pratik")
#driver.find_element(By.XPATH,"//input[contains(@id,'form_lname')]").send_keys("patel")
#driver.find_element(By.XPATH,"//input[@id='form_DOB']']").send_keys("2023-03-01")

#select_gender = Select(driver.find_element(By.XPATH,"//select[@title='Sex']"))
#select_gender.select_by_visible_text("Male")

#driver.find_element(By.XPATH,"//button[@id='create']")

