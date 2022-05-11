import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select


s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'-------------------------***--------------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.wegostudy_url)
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f'Yey! {locators.app} website launched successfully')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        
#------ [LOG_IN Script ] WH-------------------------------------------------------
def log_in(useremail, password):
    print(f'*---[Process Positive Log In]---------------------------------------------------------')
    print(useremail == locators.login_email)
    print(password == locators.login_password)
    if (useremail == locators.login_email and password == locators.login_password):
        driver.find_element(By.XPATH, '//button[contains(text(),"LOGIN")]').click()
        #driver.find_element(By.NAME, 'LOGIN').click()
        sleep(2)
        print(f'*--[LOG IN PAGES]--------------------------------------------------------------*')
        print(f'## Login page is displayed! please Continue.')
        sleep(1)
        driver.find_element(By.ID, 'user_email').send_keys(useremail)
        sleep(0.5)
        driver.find_element(By.ID, 'user_password').send_keys(password)
        sleep(0.5)
        driver.find_element(By.XPATH,'//button[contains(text(),"SIGN IN")]').click()
        sleep(0.5)
        print(f'{locators.app}  Login is successful. {datetime.datetime.now()} ')
        print("")
    else:
        print(f' There is something wrong with login. please check again ')
#-----------------------------------------------------------------------------------------------------

def tearDown():
    if driver is not None:
        print(f'-------------------------***--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


