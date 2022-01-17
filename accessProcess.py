import const
import venv

def loginProcess(driver):
    driver.get(const.baseUrl+'/login')

    login = driver.find_element_by_xpath('//*[@id="__ac_name"]')
    password = driver.find_element_by_xpath('//*[@id="__ac_password"]')

    login.clear()
    password.clear()
    login.send_keys(venv.login)
    password.send_keys(venv.password)

    driver.find_element_by_xpath('//*[@id="buttons-login"]').click()

def logoutProcess(driver):
   driver.get(const.baseUrl+'/logout') 

