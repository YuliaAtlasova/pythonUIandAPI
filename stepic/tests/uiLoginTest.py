import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from stepic.resources import stepicSettings
import stepic.steps.loginSteps


class UiLoginTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(stepicSettings.STEPIC_HOME_URL)


    def test_check_favorites(self):
        stepic.steps.loginSteps.login_with_ui(self.driver)
        self.driver.get('https://stepik.org/learn/courses/favorites')
        time.sleep(5)
        favourites = self.driver.find_elements(By.CSS_SELECTOR, '.item-tile__title_with_badge >a')
        self.assertEqual(len(favourites), 2)
        self.assertEqual(favourites[0].text, 'Common English Verbs')
        self.assertEqual(favourites[1].text, 'TOEFL vocabulary')


    def tearDown(self):
        self.driver.quit()
