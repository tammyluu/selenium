# selenium
installation de python
installation du JDK
installation de selenium
installation du web driver

C:\Users\59013-30-07>pip install selenium --> 

c:\selenium>python selenium1.py  --> exécuter sur cmd


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="C:/Users/59013-30-07/AppData/Local/Programs/Python/chromedriver.exe")
browser.get('https://trendoceans.com') --> chercher la page
print('Title: %s' % browser.title) --> la fiche
time.sleep(10)
browser.quit()

# Installation XAMPP  
 apatch /config / httpd.conf  --> changer le port en 8080 dans apache (httpd.conf)
demarrer apache

dans le repertoire c:\xamp\htdocs renomer le fichier index.php en indexxx.php

copier vos fichiers html dans ce repertoire htdocs

cherche dans git bash  ipconfig pout connaitre l'adresse  IP
INSTRUCTION INSTALLATION SELENIUM SUR WINDOW

installation du JDK (dernière version)

installation de python
installation de selenium, du driver et du driver manager
    pip install -U selenium
    pip install webdriver-manager


installation de XAMP (pour publier vos pages web)
    configurer le port du serveur web sur 8080 dans fichier httpd.conf de Apache (accessible dans le paneau de configuration de XAMP)
        listen 8080
    redémarrer Apache (stop -> start)

    supprimer le fichier 'index.php' dans le répertoire 'C:/xamp/htdocs'
    copier vos pages web dans ce répertoire 'C:/xamp/htdocs'