from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

import accessProcess as access
import const
import createObject
import time

#criar ambiente virutal (venv) - apenas no primeiro "clone"
# python3 -m venv venv

# ativar a variável de ambiente
# ./venv/bin/activate ou
# ./venv/Scripts/activate
# pip install selenium
# pip install tqdm
# colocar uma cópia da engine junto da instalação global do python

# Ver configurações no arquivo const.py
## Em especial 'login' e 'senha'
## Possibilidade de instalação do template junto da página (Ver xpath)

# ./venv/bin/python __init__.py ou
# ./venv/Sripts/python __init__.py

def main():
    print('\nBot Start ....')
    arrayPages = [
	    'Prof. Dr. Adelcio Camilo Machado',
        'Prof. Dr. Antônio Carlos Leme Junior',
        'Prof. Dr. Daniel Marcondes Gohn',
        'Profa. Dra. Daniela Dotto Machado',
        'Prof. Dr. Eduardo Conegundes de Souza',
        'Prof. Dr. Eduardo Nespoli',
        'Prof. Dr. Fernando Stanzione Galizia',
        'Prof. Dr. Fred Siqueira Cavalcante',
        'Prof. Dr. Glauber Lúcio Alves Santiago',
        'Profa. Dra. Isamara Alves Carvalho',
        'Prof. Me. José Alessandro G. Silva',
        'Profa. Dra. Juliana Marília Coli',
        'Profa. Dra. Maria Carolina Leme Joly',
        'Profa. Me. Natália Búrigo Severino',
        'Profa. Dra. Renata Franco Severo Fantini',
        'Profa. Dra. Thais dos Guimarães Alvim Nunes',
        'Profa. Dra. Suzana Reck Miranda',
    ]

    arrayFolders = [
    ]   

    driver = webdriver.Firefox()

    access.loginProcess(driver)

    if len(arrayPages)>0:
        print('\nStart Pages Generation ..')
        for name in tqdm(arrayPages):
            createObject.createPage(driver, name)

    if len(arrayFolders)>0:
        print('\nStart Folder Generation ..')
        for name in tqdm(arrayFolders):
            createObject.createFolder(driver, name)
        
    #publicar itens
    createObject.publish(driver)

    time.sleep(const.avg_time_wait*0.5)

    access.logoutProcess(driver)

    time.sleep(const.avg_time_wait*0.5)
    driver.close()

    print('\nBot Finished ...')

main()

