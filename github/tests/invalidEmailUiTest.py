import time
import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from github.resources.githubSettings import START_URL
from utils.debug import debug_print
from utils.file_loader import load_csv_test_cases


class ValidEmailUiTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(START_URL)
        sign_up_btn = cls.driver.find_element(By.CSS_SELECTOR, '.HeaderMenu-link--sign-up')
        sign_up_btn.click()
        time.sleep(5)
        cls.email_field = cls.driver.find_element(By.CSS_SELECTOR, '#email')
        debug_print('driver connection open', '')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        debug_print('driver connection closed', '')

    @parameterized.expand(load_csv_test_cases('../resources/invalidEmails.csv'))
    def test_invalid_email(self, test_name, invalid_email):
        debug_print('test name = ', test_name)
        self.email_field.clear()
        self.email_field.send_keys(invalid_email)
        wait = WebDriverWait(self.driver, 5)
        continue_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-optimizely-event = "click.signup_continue.email"]')
        assert not continue_btn.is_enabled()
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#email-err')))


