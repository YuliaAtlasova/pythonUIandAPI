import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from stepic.resources import stepicSettings
import stepic.steps.loginSteps
from stepic.resources.stepicSettings import STEPIC_WISHLIST_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ApiLoginTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(stepicSettings.STEPIC_HOME_URL)


    def test_check_wishlist(self):
        stepic.steps.loginSteps.login_with_api(self.driver)
        self.driver.get(STEPIC_WISHLIST_URL)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.item-tile__title_with_badge >a')))
        wishlist = self.driver.find_elements(By.CSS_SELECTOR, '.item-tile__title_with_badge >a')
        self.assertEqual(len(wishlist), 2)
        self.assertEqual(wishlist[0].text, 'Algorithms and Data Structures')
        self.assertEqual(wishlist[1].text, 'Data Structures')


    def tearDown(self):
        self.driver.quit()
