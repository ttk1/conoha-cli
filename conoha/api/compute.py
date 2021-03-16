from conoha import config
from conoha.util import http

url = config.get_config()['endpoint']['compute']


def list_servers():
    token_id = config.get_token()['id']
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': token_id
    }
    return  http.get(f'{url}/servers', headers)
