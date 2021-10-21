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
        'Apresentação'
    ]

    arrayFolders = [
        'Educação, Música e Formação Humana',
        'Ações e Reflexões em Educação e Educação Musical',
        'Música Popular: História, Performance e Ensino',
        'Educação Musical e Organizações Sociais de Cultura: Parceria entre a UFSCar e o Projeto Guri',
        'Orquestra',
        'Iniciação Musical ao Longo da Vida',
        'Prática de Samba e Choro: Formação do Corpo Coletivo e o Aprendizado Musical na Roda',
        'Projeto Big Band na UFSCar',
        'Outras atividades',

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

