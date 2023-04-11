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

    @parameterized.expand(load_csv_test_cases('../resources/validEmails.csv'))
    def test_valid_email(self, name, valid_email):
        debug_print('test name = ', name)
        self.email_field.clear()
        self.email_field.send_keys(valid_email)
        wait = WebDriverWait(self.driver, 5)
        continue_btn = self.driver.find_element(By.CSS_SELECTOR, '[data-optimizely-event = "click.signup_continue.email"]')
        wait.until(ec.element_to_be_clickable(continue_btn))
        assert continue_btn.is_enabled()
