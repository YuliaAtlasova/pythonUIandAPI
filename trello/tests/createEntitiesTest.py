import requests
import unittest
from trello.resources.trelloSettings import API_KEY
from trello.resources.trelloSettings import API_TOKEN
from trello.resources.trelloSettings import BOARD_ID


class CreateEntitiesTest(unittest.TestCase):
    _token = f'&key={API_KEY}&token={API_TOKEN}'

    def test_create_list(self):
        url = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?name=testList05{self._token}'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_card(self):
        get_list_url = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?{self._token}'
        list_id = requests.get(get_list_url).json()[0]['id']
        url = f'https://api.trello.com/1/cards/?idList={list_id}&name=testCard03{self._token}'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_attachment(self):
        get_list_url = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?{self._token}'
        list_id = requests.get(get_list_url).json()[0]['id']
        get_card_url = f'https://api.trello.com/1/lists/{list_id}/cards?{self._token}'
        card_id = requests.get(get_card_url).json()[0]['id']
        url = f'https://api.trello.com/1/cards/{card_id}/attachments?{self._token}'
        picture = {'file': open('../resources/donkey.jpg', 'rb')}
        resp = requests.post(url, files=picture)
        self.assertEqual(resp.status_code, 200)

    def test_create_checklist(self):
        get_list_url = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?{self._token}'
        list_id = requests.get(get_list_url).json()[0]['id']
        get_card_url = f'https://api.trello.com/1/lists/{list_id}/cards?{self._token}'
        card_id = requests.get(get_card_url).json()[0]['id']
        url = f'https://api.trello.com/1/cards/{card_id}/checklists?name=check05{self._token}'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_checkItems(self):
        get_list_url = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?{self._token}'
        list_id = requests.get(get_list_url).json()[0]['id']
        get_card_url = f'https://api.trello.com/1/lists/{list_id}/cards?{self._token}'
        card_id = requests.get(get_card_url).json()[0]['id']
        get_checklist_url = f'https://api.trello.com/1/cards/{card_id}?{self._token}'
        checklist_id = requests.get(get_checklist_url).json()['idChecklists'][0]
        for i in range(1, 5):
            item_name = 'item{0}'.format(str(i))
            url = f'https://api.trello.com/1/checklists/{checklist_id}/checkItems?name={item_name}{self._token}'
            resp = requests.post(url)
            self.assertEqual(resp.status_code, 200)
