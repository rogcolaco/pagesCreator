from turtle import delay
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import const
import time

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
    scrollDown(driver)
    driver.find_element_by_xpath('//*[@id="form-buttons-save"]').click() 

def publish(driver):
    driver.get(baseUrl)
    driver.find_element_by_xpath('//*[@id="contentview-folderContents"]/a').click() 
    scrollDown(driver)
    time.sleep(const.avg_time_wait*1.5)
    if (isDisable(driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[4]/a'))):
        driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[3]').click()
    else:
        driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[4]').click()  
    time.sleep(const.avg_time_wait)
    scrollUp(driver)
    time.sleep(const.avg_time_wait)
    driver.find_element_by_xpath('//*[@id="selectAllInputCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="btn-workflow"]').click()
    #scrollDown(driver)
    #time.sleep(const.avg_time_wait*0.5)
    resp = waitLoad(driver, '//*[@id="popover-workflow"]/div[3]/form/fieldset/div[3]/label/input')
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/form/fieldset/div[3]/label/input').click() if resp else print('Element not found')
    #driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/form/fieldset/div[3]/label/input').click()
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').send_keys(Keys.NULL)
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').click()
    resp = waitLoad(driver, '//*[@id="popover-workflow"]/div[3]/button')
    driver.get(baseUrl) if resp else print('Element not found')

def setAllPrivate(driver):
    driver.get(baseUrl)
    driver.find_element_by_xpath('//*[@id="contentview-folderContents"]/a').click() 
    scrollDown(driver)
    time.sleep(const.avg_time_wait*1.5)
    if (isDisable(driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[4]/a'))):
        driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[3]').click()
    else:
        driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[4]').click()    
    time.sleep(const.avg_time_wait)
    scrollUp(driver)
    time.sleep(const.avg_time_wait)
    driver.find_element_by_xpath('//*[@id="selectAllInputCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="btn-workflow"]').click()
    scrollDown(driver)
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/form/fieldset/div[3]/label/input').click()
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').send_keys(Keys.NULL)
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').click()
    time.sleep(const.avg_time_wait*2)

