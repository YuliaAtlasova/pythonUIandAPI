import requests
import unittest
from utils.debug import debug_print
from trello.resources.trelloSettings import TOKEN
from trello.resources.trelloSettings import API_TOKEN


class DeleteEntitiesTest(unittest.TestCase):

    def test_delete_all_boards(self):
        get_member_info_url = f'https://api.trello.com/1/tokens/{API_TOKEN}/member?fields=all{TOKEN}'
        boards = requests.get(get_member_info_url).json()['idBoards']
        debug_print('boards for deletion', boards)
        for board in boards:
            delete_url = f'https://api.trello.com/1/boards/{board}?{TOKEN}'
            resp = requests.delete(delete_url)
            self.assertEqual(resp.status_code, 200)
        boards = requests.get(get_member_info_url).json()['idBoards']
        self.assertEqual(len(boards), 0)
