import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import stepic.steps.loginSteps
from stepic.resources.stepicSettings import STEPIC_FAVOURITES_URL
from stepic.resources.stepicSettings import STEPIC_HOME_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class UiLoginTest(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(STEPIC_HOME_URL)


    def test_check_favorites(self):
        stepic.steps.loginSteps.login_with_ui(self.driver)
        self.driver.get(STEPIC_FAVOURITES_URL)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.item-tile__title_with_badge >a')))
        favourites = self.driver.find_elements(By.CSS_SELECTOR, '.item-tile__title_with_badge >a')
        self.assertEqual(len(favourites), 2)
        self.assertEqual(favourites[0].text, 'Common English Verbs')
        self.assertEqual(favourites[1].text, 'TOEFL vocabulary')


    def tearDown(self):
        self.driver.quit()
