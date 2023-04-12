import requests
import unittest
from utils.debug import debug_print
from trello.resources.trelloSettings import API_KEY
from trello.resources.trelloSettings import API_TOKEN
from trello.resources.trelloSettings import BOARD_ID


class DeleteEntitiesTest(unittest.TestCase):

    _token = f'&key={API_KEY}&token={API_TOKEN}'

