import requests
import unittest
from trello.resources.trelloSettings import API_TOKEN
from trello.resources.trelloSettings import TOKEN


class CreateEntitiesTest(unittest.TestCase):
    _get_member_info_url = f'https://api.trello.com/1/tokens/{API_TOKEN}/member?fields=all{TOKEN}'
    def test_1create_board(self):
        create_board_url = f'https://api.trello.com/1/boards/?defaultLists=false' \
                           f'&prefs_background=lime&name=testBoard001{TOKEN}'
        resp = requests.post(create_board_url)
        self.assertEqual(resp.status_code, 200)

    def test_2create_list(self):
        board = requests.get(self._get_member_info_url).json()['idBoards'][0]
        create_list_url = f'https://api.trello.com/1/boards/{board}/lists?name=testList05{TOKEN}'
        resp = requests.post(create_list_url)
        self.assertEqual(resp.status_code, 200)

    def test_3create_card(self):
        board = requests.get(self._get_member_info_url).json()['idBoards'][0]
        get_list_url = f'https://api.trello.com/1/boards/{board}/lists?{TOKEN}'
        list_id = requests.get(get_list_url).json()[0]['id']
        url = f'https://api.trello.com/1/cards/?idList={list_id}&name=testCard03{TOKEN}'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200)

    def test_4create_attachment(self):
        board = requests.get(self._get_member_info_url).json()['idBoards'][0]
        get_list_url = f'https://api.trello.com/1/boards/{board}/lists?{TOKEN}'
        list_id = requests.get(get_list_url).json()[0]['id']
        get_card_url = f'https://api.trello.com/1/lists/{list_id}/cards?{TOKEN}'
        card_id = requests.get(get_card_url).json()[0]['id']
        url = f'https://api.trello.com/1/cards/{card_id}/attachments?{TOKEN}'
        picture = open('../resources/bird.jpg', 'rb')
        file = {'file': picture}
        resp = requests.post(url, files=file)
        picture.close()
        self.assertEqual(resp.status_code, 200)

    def test_5create_checklist(self):
        board = requests.get(self._get_member_info_url).json()['idBoards'][0]
        get_list_url = f'https://api.trello.com/1/boards/{board}/lists?{TOKEN}'
        list_id = requests.get(get_list_url).json()[0]['id']
        get_card_url = f'https://api.trello.com/1/lists/{list_id}/cards?{TOKEN}'
        card_id = requests.get(get_card_url).json()[0]['id']
        url = f'https://api.trello.com/1/cards/{card_id}/checklists?name=check05{TOKEN}'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200)

    def test_6create_checkItems(self):
        board = requests.get(self._get_member_info_url).json()['idBoards'][0]
        get_list_url = f'https://api.trello.com/1/boards/{board}/lists?{TOKEN}'
        list_id = requests.get(get_list_url).json()[0]['id']
        get_card_url = f'https://api.trello.com/1/lists/{list_id}/cards?{TOKEN}'
        card_id = requests.get(get_card_url).json()[0]['id']
        get_checklist_url = f'https://api.trello.com/1/cards/{card_id}?{TOKEN}'
        checklist_id = requests.get(get_checklist_url).json()['idChecklists'][0]
        for i in range(1, 5):
            item_name = 'item{0}'.format(str(i))
            url = f'https://api.trello.com/1/checklists/{checklist_id}/checkItems?name={item_name}{TOKEN}'
            resp = requests.post(url)
            self.assertEqual(resp.status_code, 200)
