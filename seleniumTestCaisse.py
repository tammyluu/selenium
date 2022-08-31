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
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://10.115.57.132/additione.html')



def testErreur( ):
    div = browser.find_element(By.ID, 'erreur' )
    if div.get_attribute( 'innerHTML' ) == 'ERREUR !!!' :
        return True
    return False

def lireResultat( ):
    div = browser.find_element(By.ID, 'resultat' )
    return div.get_attribute( 'innerHTML' )

def saisirSomme( somme ):
    elem = browser.find_element(By.ID, 'saisie' )
    elem.clear()
    elem.send_keys( somme )

def clickADD( ):
    bouton = browser.find_element(By.ID, 'add' )
    bouton.click()

def clickRAZ( ):
    bouton = browser.find_element(By.ID, 'raz' )
    bouton.click()


#scénario
def scenarAdd2chiffre():
    print( 'test de 2 addition'  )
    saisirSomme( 12 )
    clickADD()
    saisirSomme( 13 )
    clickADD()
    result = lireResultat()
    #print( result )
    if result == '25,00&nbsp;€':
        print( 'OK' )
    else:
        print( 'KO' )

def scenarTestErreur():
    print( "test de l'erreur"  )
    saisirSomme( 'toto' )
    clickADD()
    result = lireResultat()
    if testErreur() :
        print( 'OK' )
    else:
        print( 'KO' )



scenarAdd2chiffre()
scenarTestErreur()


browser.quit()