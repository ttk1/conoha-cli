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


def create_network():
    '''
    https://www.conoha.jp/docs/neutron-add_network.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.post(f'{endpoint}/networks', None, headers)


def delete_network(network_id):
    '''
    https://www.conoha.jp/docs/neutron-remove_network.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/networks/{network_id}', headers)


def describe_network(network_id):
    '''
    https://www.conoha.jp/docs/neutron-get_networks_detail_specified.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/networks/{network_id}', headers)
