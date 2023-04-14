import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.debug import debug_print
from stepic.resources.stepicSettings import STEPIC_EMAIL
from stepic.resources.stepicSettings import STEPIC_PASSWORD
from stepic.api import loginApi

def login_with_ui(driver: webdriver):
    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    login_link = wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'navbar__auth_login')))
    login_link.click()
    login_field = wait.until(ec.visibility_of_element_located((By.ID, 'id_login_email')))
    login_field.send_keys(STEPIC_EMAIL)
    pwd_field = wait.until(ec.visibility_of_element_located((By.ID, 'id_login_password')))
    pwd_field.send_keys(STEPIC_PASSWORD)
    login_btn = driver.find_element(By.CSS_SELECTOR, '.sign-form__btn')
    login_btn.click()
    time.sleep(5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.navbar__profile-img')))


def login_with_api(driver: webdriver):
    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'navbar__auth_login')))
    all_cookies = driver.get_cookies()
    new_cookies = loginApi.get_auth_cookies(all_cookies)
    session_cookie = {
        'name': 'sessionid',
        'value': new_cookies.get('sessionid'),
        'domain': 'stepik.org',
        'path': '/',
        'secure': True
    }
    csrftoken_cookie = {
        'name': 'csrftoken',
        'value': new_cookies.get('csrftoken'),
        'domain': 'stepik.org',
        'path': '/',
        'secure': True
    }
    driver.add_cookie(session_cookie)
    driver.add_cookie(csrftoken_cookie)
