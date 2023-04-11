import requests
import unittest
from parameterized import parameterized
from utils.debug import debug_print
from utils.file_loader import load_csv_test_cases
from github.api.getUnauthToken import get_request_token
from github.resources.githubSettings import LOGIN_VALIDATION_URL

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

    @parameterized.expand(load_csv_test_cases('../resources/validEmails.csv'))
    def test_valid_email(self, name, valid_email):
        debug_print('test name = ', name)
        payload = {"authenticity_token": self.token, "value": valid_email}
        resp = self.connection.post(LOGIN_VALIDATION_URL, data=payload)
        assert resp.status_code == requests.codes.ok

