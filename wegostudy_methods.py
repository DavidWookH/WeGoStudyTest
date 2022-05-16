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

def log_in(useremail, password):
    print(f'*---[Process Positive Log In]---------------------------------------------------------')
    print(useremail == locators.login_email)
    print(password == locators.login_password)
    if (useremail == locators.login_email and password == locators.login_password):
        driver.find_element(By.XPATH, '/html/body/header/div[1]/a[2]/b').click()
        #driver.find_element(By.NAME, 'LOGIN').click()
        sleep(2)
        print(f'*--[LOG IN PAGES]--------------------------------------------------------------*')
        print(f'## Login page is displayed! please Continue.')
        sleep(1)
        driver.find_element(By.ID, 'user_email').send_keys(useremail)
        sleep(0.5)
        driver.find_element(By.ID, 'user_password').send_keys(password)
        sleep(0.5)
        #driver.find_element(By.ID, 'sign_in_btnundefined').click() #method 1 using ID
        driver.find_element(By.XPATH,'//*[@id="new_user"]/div[3]/input').click() # method 3 using XPATH
        sleep(1.5)
        print(f'{locators.app}  Login is successful. {datetime.datetime.now()} ')
        print("")
    else:
        print(f' There is something wrong with login. please check again ')

def log_out():
    print(f'*---[Sign Out]----------------------------------------------------------------*')
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="navbar-nav"]/ul[2]/li[2]/a/div/img').click()
    sleep(1.5)
    driver.find_element(By.LINK_TEXT, 'Log out').click()
    # sleep(1.5)
    #Select(driver.find_element(By.CLASS_NAME, 'dropdown-item')).select_by_visible_text('Log out')
    sleep(0.25)
    #driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle>label[translate="Sign_out"]').click()
    sleep(2)
    if driver.current_url == locators.adshopcart_url:
       print(f'# Sign Out successful! {datetime.datetime.now()}')
       print(f'*----------------------------------------------------------------------------*'
        
        
def tearDown():
    if driver is not None:
        print(f'-------------------------***--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


