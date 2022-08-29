import time
from tokenize import Name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path="C:/Users/59013-30-07/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('http://10.115.57.132/maPage.html')

elem = browser.find_element(By.NAME, 'nom')  # Find the search box
elem.send_keys('Afpa' )
# automatiser button test
# finding the button using ID
button = browser.find_element(By.NAME, 'bouton')

# clicking on the button
button.click()


print('Title: %s' % browser.title)
time.sleep(3)
#browser.quit()