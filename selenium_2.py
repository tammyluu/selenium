import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



browser = webdriver.Chrome(executable_path="C:/Users/luuta/AppData/Local/Programs/Python/chromedriver.exe")

browser.get('http://www.yahoo.com')
time.sleep(5)

#assert 'Yahoo' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box

elem.send_keys('afpa' + Keys.RETURN)


time.sleep(30)
browser.quit()
