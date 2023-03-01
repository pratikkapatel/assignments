import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")

driver.find_element(By.CSS_SELECTOR,"#sign-in-icon-down").click()
driver.find_element(By.ID,"signInLink").click()

# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='modalframe']"))
# driver.find_element(By.XPATH,"//input[@value='Confirm Create New Patient']").click()
# driver.switch_to.default_content()

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='modalIframe']"))
driver.find_element(By.ID,"mobileNoInp").send_keys("7898")
print(driver.find_element(By.XPATH,"//span[@class='error-message-fixed error-message-full top-fix']").text)

driver.switch_to.default_content()
time.sleep(5)
driver.quit()