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
from selenium.webdriver.support.ui import Select

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
def discount( ):
    div = browser.find_element(By.ID, 'remise' )
    return div.get_attribute( 'innerHTML' )


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
    if testErreur() :
        print( 'OK' )
    else:
        print( 'KO' )



def scenarTestSelect():
    elem = browser.find_element(By.ID, 'select-paiement' )
    #listOption = elem.first_selected_option
    listOption = Select( elem )    
    #print selected_option.text
    #for opt in listOption.options:
    #    print( opt.text )
    print ('=======test moyen payment ============') 
    if listOption.options[0].text == 'Espèce':
        print( 'OK' )
    else:
        print( 'KO' )

    if listOption.options[1].text == 'Carte bancaire':
        print( 'OK' )
    else:
        print( 'KO' )

    if listOption.options[2].text == 'Cheque':
        print( 'OK' )
    else:
        print( 'KO' )
def testRemise ( somme, result ):
    print ( '=====test de remise ============')
    
    saisirSomme( somme)
    clickADD()
    result = lireResultat()
    print ( result)
    if  clickADD ():
        print( '----- OK -------' )
    else:
        print( '!!!!!! KO  !!!!!!' )
testRemise( "99", "99.00&nbsp;€") 
testRemise("100", "5.00&nbsp;€")  
testRemise("101", "5.05&nbsp;€")
testRemise("299", "14.95&nbsp;€")  
testRemise("300", "21.00&nbsp;€")
testRemise("301", "21.07&nbsp;€")  
testRemise("499", "34.93&nbsp;€") 
testRemise("500", "50.0&nbsp;€") 
testRemise("501", "5.01&nbsp;€") 
    

    
    
    
   

    

#scenarAdd2chiffre()
#scenarTestErreur()
#scenarTestSelect()




time.sleep(5)
browser.quit()