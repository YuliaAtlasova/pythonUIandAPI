import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.debug import debug_print
from utils import stepicSettings
import stepic.steps.loginSteps
from utils.stepicSettings import STEPIC_WISHLIST_URL

class UiLoginTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(stepicSettings.STEPIC_HOME_URL)


    def test_check_wishlist(self):
        debug_print('', 'test_check_wishlist')
        stepic.steps.loginSteps.login_with_api(self.driver)
        self.driver.get(STEPIC_WISHLIST_URL)
        time.sleep(3)
        wishlist = self.driver.find_elements(By.CSS_SELECTOR, '.item-tile__title_with_badge >a')
        self.assertEqual(len(wishlist), 2)
        self.assertEqual(wishlist[0].text, 'Algorithms and Data Structures')
        self.assertEqual(wishlist[1].text, 'Data Structures')


    def tearDown(self):
        self.driver.quit()
