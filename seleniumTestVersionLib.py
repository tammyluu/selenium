import time
# virtualenv myVirtualPython
#  ou
# python -m venv myVirtualPython
#
# pip install -U selenium
# pip install webdriver-manager
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from seleniumTestInput import testInput

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://10.115.57.132:80/maPage.html')
#mon adresse IP
#browser.get('http://10.115.57.148:8080/maPage.html')
#browser.get('./maPage.html')


def testUpper (testNom) :
    testInput( browser, 'nom', 'bouton', 'resultat', testNom, testNom.upper() )

def testCalc (IN, OUT) :
    testInput( browser, 'saisie', 'go', 'res', IN, OUT )
    
print ("===== Test capitalizer =======")
toDo =[' toto', ' tété' , '1234']
for mot in toDo:
    testUpper( mot )

print ("===== Test Calcul =======")

testCalc( '2+3', '5')


time.sleep(2)
#browser.quit()