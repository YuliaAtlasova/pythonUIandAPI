import requests
import unittest
from utils.debug import debug_print
from trello.resources.trelloSettings import API_KEY
from trello.resources.trelloSettings import API_TOKEN
from trello.resources.trelloSettings import BOARD_ID


class CreateEntitiesTest(unittest.TestCase):
    _token = f'&key={API_KEY}&token={API_TOKEN}'

    def test_create_detailed_list(self):
        url_create_list = f'https://api.trello.com/1/boards/{BOARD_ID}/lists?name=testList001{self._token}'
        resp1 = requests.post(url_create_list)
        self.assertEqual(resp1.status_code, 200)
        list_id = resp1.json()['id']

        url_create_card = f'https://api.trello.com/1/cards/?idList={list_id}&name=testCard001{self._token}'
        resp2 = requests.post(url_create_card)
        card_id = resp2.json()['id']

        url_create_attachment = f'https://api.trello.com/1/cards/{card_id}/attachments?{self._token}'
        picture = {'file': open('../resources/bird.jpg', 'rb')}
        resp3 = requests.post(url_create_attachment, files=picture)
        self.assertEqual(resp3.status_code, 200)

        url_create_checklist = f'https://api.trello.com/1/cards/{card_id}/checklists?name=check001{self._token}'
        resp4 = requests.post(url_create_checklist)
        self.assertEqual(resp4.status_code, 200)
        checklist_id = resp4.json()['id']
        for i in range(1, 5):
            item_name = 'item{0}'.format(str(i))
            url = f'https://api.trello.com/1/checklists/{checklist_id}/checkItems?name={item_name}{self._token}'
            resp5 = requests.post(url)
            self.assertEqual(resp5.status_code, 200)

        url_add_label = f'https://api.trello.com/1/labels?name=testLabel001&color=red&idBoard={BOARD_ID}{self._token}'
        resp6 = requests.post(url_add_label)
        self.assertEqual(resp6.status_code, 200)
        label_id = resp6.json()['id']

        url_link_label = f'https://api.trello.com/1/cards/{card_id}/idLabels?{self._token}'
        resp7 = requests.post(url_link_label, json={'value': label_id})
        self.assertEqual(resp7.status_code, 200)
