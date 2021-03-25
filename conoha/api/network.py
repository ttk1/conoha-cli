'''
Network API の呼び出し部分
'''

from conoha import config
from conoha.util import http

endpoint = config.get_config()['endpoint']['network']


def list_networks():
    '''
    https://www.conoha.jp/docs/neutron-get_networks_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/networks', headers)
