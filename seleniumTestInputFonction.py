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

#browser.get('http://10.115.57.132:80/maPage.html') #navigate to home page "maPage"
browser.get('http://10.115.57.148:8080/maPage.html')
#browser.get('./maPage.html')
# fonction for test Input and Output
def testInput( idChamp, idBouton, idResultat, entree, sortie ):
    elem = browser.find_element(By.ID, idChamp )  # Find the search box
    elem.clear()
    elem.send_keys( entree )

    bouton = browser.find_element(By.ID, idBouton )#Đặt tên biến là bouton. Sử dụng inspect trên Web để lấy được name của field "bouton"
    bouton.click()

    div = browser.find_element(By.ID, idResultat)
    result = div. get_attribute( 'innerHTML' )

    print( 'test : ' + entree, end =' ' )
    if result == sortie:
        print( 'OK' )
    else: 
        print( 'KO' )



# fonction test for fill in 
def testMaj( testNom ):
    testInput( 'nom', 'bouton', 'resultat', testNom, testNom.upper())


print( "test majuscule ------------------------------")

aTester=[ 'toto', 'rémi', '1234'  ]
for mot in aTester:
    testMaj( mot )

# fonction for calcul
print( "test calcul ------------------------------")
def testCalcul( expression, resultat ):
    testInput( 'saisie', 'go', 'res', expression, resultat )


testCalcul( '2+4', '6')
testCalcul( '2-4', '-2')
testCalcul( '2*4', '8')




#assert result == testNom.upper()

time.sleep(4)
#browser.quit()