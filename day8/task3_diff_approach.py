import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.online.citibank.co.in/")

# //a[@class='fancybox-item fancybox-close']
d.find_element(By.CLASS_NAME,"fancybox-close").click()
d.find_element(By.XPATH,"//span[normalize-space()='Login']").click()

d.switch_to.window(d.window_handles[1])

d.find_element(By.XPATH,"//div[contains(text(),'Forgot User')]").click()

d.find_element(By.LINK_TEXT,"select your product type").click()
d.find_element(By.LINK_TEXT,"Credit Card").click()

d.find_element(By.CSS_SELECTOR,"#citiCard1").send_keys("7897")
d.find_element(By.CSS_SELECTOR,"input[name='citiCard2']").send_keys("7897")
d.find_element(By.CSS_SELECTOR,"[name='citiCard3']").send_keys("7897")
d.find_element(By.ID,"citiCard4").send_keys("7897")

d.find_element(By.ID,"cvvnumber").send_keys("889")

#approach 1 - not working
# d.find_element(By.ID,"bill-date-long").send_keys("14/04/2022")

#approach 2
# d.find_element(By.ID,"bill-date-long").click()
#
# select_year=Select(d.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
# select_year.select_by_visible_text("2000")
#
# select_month=Select(d.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
# select_month.select_by_visible_text("Apr")
#
# d.find_element(By.LINK_TEXT,"14").click()

#approach 3 - javascript
ele1=d.find_element(By.XPATH,"//input[@name='DOB']")
d.execute_script("arguments[0].value='11/09/2000'",ele1)

d.find_element(By.XPATH,"//input[@value='PROCEED']").click()


actual_error1=d.find_element(By.XPATH,"//li[contains(text(),'Term')]").text

actual_error2=d.find_element(By.XPATH,"//div[@role='dialog']").text

print(actual_error1)
print(actual_error2)

time.sleep(5)
d.quit()