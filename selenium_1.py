import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="C:/Users/luuta/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('https://trendoceans.com')
print('Title: %s' % browser.title) # print title of web
time.sleep(10)
browser.quit() # close chrôme