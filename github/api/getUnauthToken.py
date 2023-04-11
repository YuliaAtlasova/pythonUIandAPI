import requests
from github.resources.githubSettings import START_URL
from github.resources.githubSettings import REQUEST_TOKEN_URL


def get_request_token(open_session: requests.Session) -> str:
    open_session.get(START_URL)
    resp = open_session.get(REQUEST_TOKEN_URL)
    page_with_token = resp.text
    before_token1 = 'type="email" name="user[email]" />'
    found_token_string = page_with_token.find(before_token1)
    assert not found_token_string == -1
    first_split_res = page_with_token.split(before_token1)[1]
    before_token2 = 'value="'
    second_split_res = first_split_res.split(before_token2)[1]
    token = second_split_res.split('"')[0]
    print(token)
    return token
