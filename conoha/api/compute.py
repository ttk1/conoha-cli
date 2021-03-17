from conoha import config
from conoha.util import http

url = config.get_config()['endpoint']['compute']


def list_flavors():
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{url}/flavors', headers)


def list_images():
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{url}/images', headers)


def list_servers():
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{url}/servers', headers)
