import requests
from stepic.resources.stepicSettings import STEPIC_EMAIL
from stepic.resources.stepicSettings import STEPIC_PASSWORD
from stepic.resources.stepicSettings import STEPIC_AUTH_URL

def get_auth_cookies(ui_cookies: list) -> dict:
    current_session = requests.Session()
    headers_dict: dict[str, str] = {}
    for cookie in ui_cookies:
        current_session.cookies.set(cookie['name'], cookie['value'], domain='stepik.org', path='/')
        if cookie['name'] in 'sessionid, csrftoken':
            headers_dict[cookie['name']] = cookie['value']
            if cookie['name'] == 'csrftoken':
                headers_dict['x-csrftoken'] = cookie['value']
    credentials = {"email": STEPIC_EMAIL, "password": STEPIC_PASSWORD}
    headers_dict['referer'] = 'https://stepik.org/catalog?auth=login'
    headers_dict['authority'] = 'stepik.org'
    headers_dict['origin'] = 'https://stepik.org'
    req = requests.Request('POST', STEPIC_AUTH_URL, json=credentials, headers=headers_dict)
    prepped = current_session.prepare_request(req)
    resp = current_session.send(prepped)
    result_cookies = {
        'sessionid': resp.cookies.get('sessionid'),
        'csrftoken': resp.cookies.get('csrftoken')
    }
    current_session.close()
    return result_cookies
