from http.client import OK
import time
# virtualenv myVirtualPython
#  ou
# python -m venv myVirtualPython
#
# pip install -U selenium
# pip install webdriver-manager
from unittest import result
from webbrowser import Konqueror
from selenium import webdriver # import webdriver from selenium package
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # open chrôme

browser.get('http://10.115.57.132:80/maPage.html') #navigate to home page "maPage"
#browser.get('http://10.115.57.148:8080/maPage.html') # my adresse IP
#browser.get('./maPage.html')
# fonction for test Input and Output
def testInput( idChamp, idBouton , idResultat, entree, sortie ):
    elem = browser.find_element(By.ID, idChamp )  # Find the search box
    elem.clear()
    elem.send_keys( entree )
    elem.send_keys(Keys.ENTER)
    
    if idBouton != '':
        bouton = browser.find_element(By.ID, idBouton )#Đặt tên biến là bouton. Sử dụng inspect trên Web để lấy được name của field "bouton"
        bouton.click()
    else :
        elem.send_keys(Keys.RETURN)
    
    div = browser.find_element(By.ID, idResultat)
    result = div. get_attribute( 'innerHTML' )

    print( 'test : ' + entree,' =>', result,  end =' ' )
    if result == sortie:
        print( '< OK >' )
    else: 
        print( '!!! KO !!!' )
        
def saisieSomme (somme):
    elem = browser.find_element(By.ID, 'saisie' )  # Find the search box
    elem.clear()
    clickAdd()
    
def clickAdd() :
    bouton = browser.find_element(By.ID, 'add' )#Đặt tên biến là bouton. Sử dụng inspect trên Web để lấy được name của field "bouton"
    bouton.click()
def clickRaz():
    bouton = browser.find_element(By.ID, 'raz' )#Đặt tên biến là bouton. Sử dụng inspect trên Web để lấy được name của field "bouton"
    bouton.click()
def lireResultat():
    div = browser.find_element(By.ID, 'resultat' )  # Find the search box
    return div.get_attribute ('innerHTML')


def add2Chiffre ():
    print ('-----test de 2 addition------ ')
    saisieSomme(12)
    clickAdd()
    saisieSomme(13)
    clickAdd()
    result = lireResultat ()
    if result == '25,00&nbsp;€':
        print ( 'OK')
    else :
        print ( 'KO')   
def testError ():
    print ('-----test Error----- ')
    saisieSomme('toto')
    clickAdd()

    result = lireResultat ()
    if result == 'ERREUR !!!':
        print ( 'OK')
    else :
        print ( 'KO')   
        
add2Chiffre()
testError()
def testMagic( entree, sortie ):
    testInput( 'motMagique', '' , 'resultatMagique', entree, sortie)


print( "test Nombre Magic------------------------------")

testMagic( 'xavier', '13')
testMagic( 'Xavier', '13')
testMagic( '', '')
testMagic( '     ', '')
testMagic( '123', '')



time.sleep(2)
browser.quit()