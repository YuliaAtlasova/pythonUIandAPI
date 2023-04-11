import requests
import unittest
from parameterized import parameterized
from utils.debug import debug_print
from utils.file_loader import load_csv_test_cases
from github.api.getUnauthToken import get_request_token
from github.resources.githubSettings import LOGIN_VALIDATION_URL
from github.resources.githubSettings import INVALID_EMAIL_ERROR_MESSAGE

class ValidEmailApiTest(unittest.TestCase):
    connection = None

    @classmethod
    def setUpClass(cls):
        cls.connection = requests.Session()
        cls.token = get_request_token(open_session=cls.connection)
        debug_print('connection open', '')

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
        debug_print('connection closed', '')

    @parameterized.expand(load_csv_test_cases('../resources/invalidEmails.csv'))
    def test_valid_email(self, test_name, invalid_email):
        debug_print('test name = ', test_name)
        payload = {"authenticity_token": self.token, "value": invalid_email}
        resp = self.connection.post(LOGIN_VALIDATION_URL, data=payload)
        page_with_error = resp.text
        assert resp.status_code == 422
        assert INVALID_EMAIL_ERROR_MESSAGE in page_with_error
