from selenium.webdriver.common.keys import Keys

import const
import time

baseUrl= const.baseUrl+const.location

def scrollDown(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scrollUp(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

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