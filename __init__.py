from msilib.schema import CreateFolder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

import accessProcess as access
import const
import createFolder
import createPage
import time
import util

#criar ambiente virutal (venv) - apenas no primeiro "clone"
# python3 -m venv venv

# ativar a variável de ambiente
# ./venv/bin/activate ou
# ./venv/Scripts/activate
# pip install selenium
# pip install tqdm
# pip install Unidecode
# colocar uma cópia da engine junto da instalação global do python

# Ver configurações no arquivo const.py
## Em especial 'login' e 'senha'
## Possibilidade de instalação do template junto da página (Ver xpath)

# Atalhos para rodar o bot 
# ./venv/bin/python __init__.py ou
# ./venv/Scripts/python __init__.py

def main():
    print('\nBot Start ....')

    arrayPages = [
        'Subprojetos',
        'Escolas',
        'Livros e Artigos',
    ]

    arrayFolders = [
    ]   

    driver = webdriver.Firefox()


    access.loginProcess(driver)

    if len(arrayPages)>0:
        print('\nStart Pages Generation ..')
        if len(const.location)==0:
            util.setAllPrivate(driver)
        for name in tqdm(arrayPages):
            createPage.createPage(driver, name)

    if len(arrayFolders)>0:
        print('\nStart Folder Generation ..')
        if len(const.location)==0:
            util.setAllPrivate(driver)
        for name in tqdm(arrayFolders):
            createFolder.createFolder(driver, name)
        
    #publicar itens
    util.publish(driver)

    if (len(arrayFolders)>15 or len(arrayPages)>15):
        time.sleep(const.avg_time_wait*2.0)
        access.logoutProcess(driver)
        time.sleep(const.avg_time_wait*2.0)
        driver.close()
    else:
        time.sleep(const.avg_time_wait*0.5)
        access.logoutProcess(driver)
        time.sleep(const.avg_time_wait*0.5)
        driver.close()

    print('\nBot Finished ...')

main()

