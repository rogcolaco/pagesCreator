from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import const

baseUrl= const.baseUrl+const.location

def isDisable(element):
    if 'disabled' in element.get_attribute('class').split():
        return True
    else:
        return False

def scrollDown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scrollUp(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

def waitLoad(driver, xpath):
    try:
        isLoad = WebDriverWait(driver, const.delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
        if (isLoad):
            return True
    except TimeoutException:
        return False

def save(driver):
    driver.find_element_by_xpath('//*[@id="form-buttons-save"]').send_keys(Keys.NULL) 
    driver.find_element_by_xpath('//*[@id="form-buttons-save"]').click() 

def publish(driver, what_is, has_translation):
    if has_translation:
        if what_is=='is_page':
            driver.find_element_by_xpath('/html/body/div[1]/div/nav/ul[1]/li[5]/a').click() 
    
        if what_is =='is_folder':
            driver.find_element_by_xpath('/html/body/div[1]/div/nav/ul[1]/li[6]/a').click() 

    else:
        if what_is=='is_page':
            driver.find_element_by_xpath('/html/body/div[1]/div/nav/ul[1]/li[4]/a').click() 

        
        if what_is =='is_folder':
            driver.find_element_by_xpath('/html/body/div[1]/div/nav/ul[1]/li[5]/a').click() 

    
    driver.find_element_by_xpath('//*[@id="workflow-transition-publish"]').click() 


