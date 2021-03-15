from conoha import config
from conoha.util import http

url = config.get_config()['endpoint']['identity']


def get_token(data):
    headers = {
        'Accept': 'application/json'
    }
    return http.post(f'{url}/tokens', data, headers)
