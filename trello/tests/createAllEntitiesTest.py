import random

import requests
import unittest
from trello.resources.trelloSettings import TOKEN
from trello.resources.trelloSettings import COLORS


class CreateAllEntitiesTest(unittest.TestCase):

    _num = random.randint(100, 999)
    _color = random.choice(COLORS)
    print('New object will have number ', _num, 'and color', _color)
    def test_create_detailed_list(self):
        url_create_board = f'https://api.trello.com/1/boards/?defaultLists=false' \
                           f'&prefs_background={self._color}&name=testBoard{self._num}{TOKEN}'
        resp0 = requests.post(url_create_board)
        self.assertEqual(resp0.status_code, 200)
        board_id = resp0.json()['id']

        url_create_list = f'https://api.trello.com/1/boards/{board_id}/lists?name=testList{self._num}{TOKEN}'
        resp1 = requests.post(url_create_list)
        self.assertEqual(resp1.status_code, 200)
        list_id = resp1.json()['id']

        url_create_card = f'https://api.trello.com/1/cards/?idList={list_id}&name=testCard{self._num}{TOKEN}'
        resp2 = requests.post(url_create_card)
        card_id = resp2.json()['id']

        url_create_attachment = f'https://api.trello.com/1/cards/{card_id}/attachments?{TOKEN}'
        picture = open('../resources/donkey.jpg', 'rb')
        file = {'file': picture}
        resp3 = requests.post(url_create_attachment, files=file)
        picture.close()
        self.assertEqual(resp3.status_code, 200)

        url_create_checklist = f'https://api.trello.com/1/cards/{card_id}/checklists?name=check{self._num}{TOKEN}'
        resp4 = requests.post(url_create_checklist)
        self.assertEqual(resp4.status_code, 200)
        checklist_id = resp4.json()['id']
        for i in range(1, 5):
            item_name = 'item{0}'.format(str(i))
            url = f'https://api.trello.com/1/checklists/{checklist_id}/checkItems?name={item_name}{TOKEN}'
            resp5 = requests.post(url)
            self.assertEqual(resp5.status_code, 200)

        url_add_label = f'https://api.trello.com/1/labels?name=testLabel{self._num}' \
                        f'&color={random.choice(COLORS)}&idBoard={board_id}{TOKEN}'
        resp6 = requests.post(url_add_label)
        self.assertEqual(resp6.status_code, 200)
        label_id = resp6.json()['id']

        url_link_label = f'https://api.trello.com/1/cards/{card_id}/idLabels?{TOKEN}'
        resp7 = requests.post(url_link_label, json={'value': label_id})
        self.assertEqual(resp7.status_code, 200)
