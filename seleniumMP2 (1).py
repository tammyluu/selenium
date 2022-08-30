import time
from tokenize import Name
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path="C:/Users/59013-30-07/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('http://10.115.57.148:8080/maPage.html')

# click manuellement
elem = browser.find_element(By.NAME, 'nom')  # Find the search box
elem.send_keys('toto')

# automatiser button test
# finding the button using ID
button = browser.find_element(By.NAME, 'bouton')


# clicking on the button
button.click()

div = browser.find_element(By.NAME, 'resultat')
result = div.get_attribute('innerHTML')


print(result)
if result == 'TOTO':
    print ('----OK-----')
else:
    print ('!!!!!!KO!!!!!')    
    



print('Title: %s' % browser.title)
time.sleep(3)
#browser.quit()