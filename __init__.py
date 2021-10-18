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
        'Análise e monitoramento de bioprocessos',
        'Análise Microbiológica de Solo, Produtos e Processos Agrícolas e Industriais',
        'Análises Tecnológicas de Produtos do Setor Sucroalcooleiro',
        'Aproveitamento de resíduos agroindustriais para obtenção de biomoléculas',
        'Bioenergy Hub',
        'Boletim Informativo GEAgro',
        'Cálculo da Cesta Básica do Município de Araras-SP',
        'Continuando a Compartilhar Saberes: Desdobramentos e Perspectivas',
        'Conversão de Unidades e Variáveis de Processos Industriais',
        'Curso - Aguardente Bidestilada',
        'Curso - Melado, Rapadura e Açúcar Mascavo',
        'Empresa Jr Sustec Jr',
        'Estudo técnico – agroindústria',
        'Estudo técnico - setor de bebidas',
        'Fronteira HUB',
        'Grupo de Estudos em Probabilidade e Estatística (GEPE)',
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

    time.sleep(const.avg_time_wait*2)

    access.logoutProcess(driver)

    time.sleep(const.avg_time_wait/2)
    driver.close()

    print('\nBot Finished ...')

main()

