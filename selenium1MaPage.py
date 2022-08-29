import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="C:/Users/59013-30-07/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('http://10.115.57.132/maPage.html')
print('Title: %s' % browser.title)
time.sleep(40)
browser.quit()