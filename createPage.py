from selenium.webdriver.common.keys import Keys

import const
import time
import util

#Pasta onde serão criados os objetos
baseUrl= const.baseUrl+const.location

def addTemplate(driver):
    #ver Xpath do template
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="mceu_20-open"]').send_keys(Keys.NULL)
    driver.find_element_by_xpath('//*[@id="mceu_20-open"]').click()
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="mceu_43"]').click()
      
    if(const.xPathTemplate == '//*[@id="mceu_56"]'):
        time.sleep(const.avg_time_wait*1.5)
        driver.find_element_by_xpath('//*[@id="mceu_52-button"]').click()
    else:
        time.sleep(const.avg_time_wait*1.5)
        driver.find_element_by_xpath('//*[@id="mceu_48-open"]').click()
        time.sleep(const.avg_time_wait*1.5)
        driver.find_element_by_xpath(const.xPathTemplate).click()
        time.sleep(const.avg_time_wait*1.5)
        driver.find_element_by_xpath('//*[@id="mceu_52-button"]').click()
    time.sleep(const.avg_time_wait*0.5)


def createPage(driver, pageName, has_trasnlation):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Document')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(pageName.strip())

    if(const.hasTemplate):
        addTemplate(driver)

    #save
    util.save(driver)
    util.publish(driver, 'is_page', has_trasnlation)

