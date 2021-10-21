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
    driver.get(baseUrl)
    driver.find_element_by_xpath('//*[@id="contentview-folderContents"]/a').click()
    time.sleep(const.avg_time_wait*1.5)
    driver.find_element_by_xpath('//*[@id="selectAllInputCheckbox"]').click()
    driver.find_element_by_xpath('//*[@id="btn-workflow"]').click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(const.avg_time_wait*0.5)
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/form/fieldset/div[3]/label/input').click()
    driver.find_element_by_xpath('//*[@id="popover-workflow"]/div[3]/button').click()

def createPage(driver, pageName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Document')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(pageName)

    if(const.hasTemplate):
        addTemplate(driver)

    #save
    save(driver)


def createFolder(driver, folderName):
    driver.get(baseUrl)
    driver.get(baseUrl+'/++add++Folder')
    inputName = driver.find_element_by_xpath('//*[@id="form-widgets-IDublinCore-title"]')
    inputName.send_keys(folderName)
    #save
    save(driver)

