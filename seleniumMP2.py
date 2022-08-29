import time
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(executable_path="C:/Users/59013-30-07/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('http://10.115.57.132:80/maPage.html')

testNom = 'toto'

elem = browser.find_element(By.NAME, 'nom')  # Find the search box
elem.send_keys( testNom )

bouton = browser.find_element(By.NAME, 'bouton')
bouton.click()

div = browser.find_element(By.NAME, 'resultat')
#result = div.getText()
result = div. get_attribute( 'innerHTML' )

if result == testNom.upper():
    print( 'OK' )
else: 
    print( 'KO' )

assert result == testNom.upper()

time.sleep(1)
#browser.quit()