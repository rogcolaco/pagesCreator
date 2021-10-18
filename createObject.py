import const
import time

#Pasta onde serão criados os objetos
baseUrl= const.baseUrl+const.location

def addTemplate(driver):
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="mceu_20-open"]').click()
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="mceu_43"]').click()
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="mceu_48-open"]').click()
    time.sleep(const.avg_time_wait*1.5)

    #ver Xpath do template
    driver.find_element_by_xpath(const.xPathTemplate).click()
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="mceu_52-button"]').click()
    time.sleep(const.avg_time_wait*1.5)

def save(driver):
   driver.find_element_by_xpath('//*[@id="form-buttons-save"]').click() 

def publish(driver):
    driver.find_element_by_xpath('//*[@id="plone-contentmenu-workflow"]/a/span[2]/span[3]').click()
    time.sleep(const.avg_time_wait/2)
    driver.find_element_by_xpath('//*[@id="workflow-transition-publish"]').click()

def createPage(driver, pageName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Document')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(pageName)

    if(const.hasTemplate):
        addTemplate(driver)

    #save
    save(driver)
    time.sleep(const.avg_time_wait*1.5)

    #publicar página
    publish(driver)


def createFolder(driver, folderName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Folder')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(folderName)
    #save
    save(driver)
    time.sleep(const.avg_time_wait*1.5)

    #publicar página
    publish(driver)

