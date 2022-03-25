from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import const
import time
import unidecode
import util

baseUrl= const.baseUrl+const.location

def configFolder (driver,folderName):
    delay = 10
    folderName = folderName.lower()
    folderName = unidecode.unidecode(folderName)
    folderName = folderName.replace(' ', '-')
    driver.get(baseUrl + f'/{folderName}/folder_constraintypes_form')
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/main/div[2]/div/div/article/form/div[1]/select').click()
    driver.find_element_by_xpath('//*[@id="form-widgets-constrain_types_mode-2"]').click()
    try:
        isLoad = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-widgets-allowed_types-9"]')))
        isChecked = driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-0"]').is_selected()
        if (isLoad and isChecked):
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-0"]').click()
            #driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-3"]').click()
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-4"]').click()
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-5"]').click()
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-6"]').click()
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-7"]').click()
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-8"]').click()
            driver.find_element_by_xpath('//*[@id="form-widgets-allowed_types-9"]').click()
    except TimeoutException:
        print('Element not found')
    driver.find_element_by_xpath('//*[@id="form-buttons-save"]').send_keys(Keys.NULL)
    time.sleep(const.avg_time_wait)
    driver.find_element_by_xpath('//*[@id="form-buttons-save"]').click()


def createFolder(driver, folderName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Folder')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(folderName.strip())
    #save
    util.save(driver)
    configFolder(driver, folderName)
    util.publish(driver)