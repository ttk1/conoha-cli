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


def create_port(network_id, ip_address,
                subnet_id, security_group_ids=None):
    '''
    https://www.conoha.jp/docs/neutron-add_port.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }

    # 必須項目
    data = {
        'port': {
            'network_id': network_id,
            'fixed_ips': [{
                'ip_address': ip_address,
                'subnet_id': subnet_id
            }]
        }
    }

    # Optional 項目
    if security_group_ids is not None:
        data['port']['security_groups'] = security_group_ids

    return http.post(f'{endpoint}/ports', data, headers)


def delete_port(port_id):
    '''
    https://www.conoha.jp/docs/neutron-remove_port.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/ports/{port_id}', headers)


def list_ports():
    '''
    https://www.conoha.jp/docs/neutron-get_ports_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/ports', headers)


def describe_port(port_id):
    '''
    https://www.conoha.jp/docs/neutron-get_ports_detail_specified.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/ports/{port_id}', headers)
