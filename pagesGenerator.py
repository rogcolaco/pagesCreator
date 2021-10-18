from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm

import accessProcess as access
import const
import createObject
import time

# Ver configurações do create object

# pip install selenium
# pip install tqdm

# ./venv/bin/python pagesGenerator.py

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

    time.sleep(const.time_wait_long)

    access.logoutProcess(driver)

    time.sleep(const.time_wait_short)
    driver.close()

    print('\nBot Finished ...')

main()

