from audioop import add
import time
# virtualenv myVirtualPython
#  ou
# python -m venv myVirtualPython
#
# pip install -U selenium
# pip install webdriver-manager
from unittest import result
from selenium import webdriver # import webdriver from selenium package
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # open chrôme

browser.get('http://10.115.57.132:80/additione.html') #navigate to home page "maPage"
#browser.get('http://10.115.57.148:8080/maPage.html') # my adresse IP
#browser.get('./maPage.html')
# fonction for test Input and Output
def testAdditon(testAdd, resultat):


    input = browser.find_element(By.NAME, "saisie")
    input.clear()
    input.send_keys( testAdd )

    bouton = browser.find_element(By.NAME, 'add')
    bouton.click()
    
        
    #bouton = driver.find_element(By.NAME, 'raz')
    #bouton.click()

    div = browser.find_element(By.NAME, 'resultat')
    result = div. get_attribute( 'innerHTML' )
    print(result) 
    if result == resultat:
        print( '-----OK------' )
    else: 
        print( '!!!!! KO !!!!!!!' )

testAdditon("12", "12.00&nbsp;€")
testAdditon("12 + 2.3", "26.30&nbsp;€")







time.sleep(2)
#browser.quit()