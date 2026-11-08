import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)

driver.get("https://www.google.com")

print(driver,title)
print(driver,current_url)

driver.refresh()

time.sleep(5)

driver.quit()