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


#mon adresse IP
#browser.get('http://10.115.57.148:8080/maPage.html')
#browser.get('./maPage.html')
def testInput( browser, idSaisie, idBouton, idResultat, entree, sortie ):
    elem = browser.find_element(By.ID, idSaisie)  # Find the search box
    elem.clear()
    elem.send_keys( entree )

    bouton = browser.find_element(By.ID, idBouton)
    bouton.click()
        
    div = browser.find_element(By.ID, idResultat )
    result = div. get_attribute( 'innerHTML' )

    print ('test : ' + entree, end= ' ')
    
    if result == sortie:
        print( ' ---> OK' )
    else: 
        print( '!!!!! KO!!!' )
    
def testInput1( testNom, browser ) :
    #testNom = 'toto'

    elem = browser.find_element(By.NAME, 'nom')  # Find the search box
    elem.clear()
    elem.send_keys( testNom )

    bouton = browser.find_element(By.NAME, 'bouton')
    bouton.click()
        
    div = browser.find_element(By.NAME, 'resultat')
    result = div. get_attribute( 'innerHTML' )

    print ('test : ' + testNom, end= ' ')
    
    if result == testNom.upper():
        print( ' ---> OK' )
    else: 
        print( '!!!!! KO!!!' )
    
    
        
def testInput2( testCalcule, res, browser) :
    #testNom = 'toto'

    elem = browser.find_element(By.NAME, 'saisie')  # Find the search box
    elem.clear()
    elem.send_keys( testCalcule )

    bouton = browser.find_element(By.NAME, 'go')
    bouton.click()
    
        
    div = browser.find_element(By.NAME, 'res')
    result = div. get_attribute( 'innerHTML' )

    print ('test de calcule: ' + testCalcule, end= ' ')
    
    
    if result == res:
        print( ' ---> OK' )
    else: 
        print( '!!!!! KO!!!' )



if __name__ == "__main__":

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('http://10.115.57.132:80/maPage.html')


    testInput2 ('2*5', '10', browser)
    testInput2 ('2-8', '-6', browser)
    testInput2 ('3%2', '1', browser)
    testInput2 ('3/2', '1.5', browser)

    testInput ('toto', browser)
    testInput ('tété', browser)
    testInput ('1234', browser)


    time.sleep(1)
    browser.quit()
    