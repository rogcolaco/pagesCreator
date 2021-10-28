from selenium.webdriver.common.keys import Keys

import const
import time

#Pasta onde serão criados os objetos
baseUrl= const.baseUrl+const.location

def scrollDown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scrollUp(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

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

def save(driver):
    scrollDown(driver)
    driver.find_element_by_xpath('//*[@id="form-buttons-save"]').click() 

def publish(driver):
    driver.get(baseUrl)
    driver.find_element_by_xpath('//*[@id="contentview-folderContents"]/a').click() 
    time.sleep(const.avg_time_wait*1.5)
    scrollDown(driver)
    driver.find_element_by_xpath('//*[@id="content-core"]/div/div/aside/ul[2]/li[4]/a').click()
    time.sleep(const.avg_time_wait)
    scrollUp(driver)
    driver.find_element_by_xpath('//*[@id="selectAllInputCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="btn-workflow"]').click()
    scrollDown(driver)
    time.sleep(const.avg_time_wait*0.5)
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/form/fieldset/div[3]/label/input').click()
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').send_keys(Keys.NULL)
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').click()

def createPage(driver, pageName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Document')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(pageName.strip())

    if(const.hasTemplate):
        addTemplate(driver)

    #save
    save(driver)


def createFolder(driver, folderName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Folder')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(folderName.strip())
    #save
    save(driver)

