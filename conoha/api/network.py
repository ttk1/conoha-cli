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

###########################################################################


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


def update_port(port_id, security_group_ids):
    '''
    https://www.conoha.jp/docs/neutron-update_port.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    data = {
        'port': {
            'security_groups': security_group_ids
        }
    }
    return http.put(f'{endpoint}/ports/{port_id}', data, headers)


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

###########################################################################


def create_subnet(network_id, cidr):
    '''
    https://www.conoha.jp/docs/neutron-add_subnet.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    data = {
        'subnet': {
            'network_id': network_id,
            'cidr': cidr
        }
    }
    return http.post(f'{endpoint}/subnets', data, headers)


def delete_subnet(subnet_id):
    '''
    https://www.conoha.jp/docs/neutron-remove_subnet.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/subnets/{subnet_id}', headers)


def list_subnets():
    '''
    https://www.conoha.jp/docs/neutron-get_subnets_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/subnets', headers)


def describe_subnet(subnet_id):
    '''
    https://www.conoha.jp/docs/neutron-get_subnets_detail_specified.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/subnets/{subnet_id}', headers)

###########################################################################


def create_security_group(name, description=None):
    '''
    https://www.conoha.jp/docs/neutron-create_secgroup.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }

    # 必須項目
    data = {
        'security_group': {
            'name': name
        }
    }

    # Optional 項目
    if description is not None:
        data['security_group']['description'] = description

    return http.post(f'{endpoint}/security-groups', data, headers)


def delete_security_group(security_group_id):
    '''
    https://www.conoha.jp/docs/neutron-delete_secgroup.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/security-groups/{security_group_id}', headers)


def list_security_groups():
    '''
    https://www.conoha.jp/docs/neutron-get_secgroups_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/security-groups', headers)


def describe_security_group(security_group_id):
    '''
    https://www.conoha.jp/docs/neutron-get_secgroups_detail_specified.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/security-groups/{security_group_id}', headers)

###########################################################################


def create_security_group_rule(direction, ether_type, security_group_id,
                               port_range_min=None, port_range_max=None, protocol=None,
                               remote_group_id=None, remote_ip_prefix=None):
    '''
    https://www.conoha.jp/docs/neutron-create_rule_on_secgroup.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }

    # 必須項目
    data = {
        'security_group_rule': {
            'direction': direction,
            'ethertype': ether_type,
            'security_group_id': security_group_id
        }
    }

    # Optional 項目
    if port_range_min is not None:
        data['security_group_rule']['port_range_min'] = port_range_min
    if port_range_max is not None:
        data['security_group_rule']['port_range_max'] = port_range_max
    if protocol is not None and protocol != 'null':
        data['security_group_rule']['protocol'] = protocol
    if remote_group_id is not None:
        data['security_group_rule']['remote_group_id'] = remote_group_id
    if remote_ip_prefix is not None:
        data['security_group_rule']['remote_ip_prefix'] = remote_ip_prefix

    return http.post(f'{endpoint}/security-group-rules', data, headers)


def delete_security_group_rule(rule_id):
    '''
    https://www.conoha.jp/docs/neutron-delete_rule_on_secgroup.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/security-group-rules/{rule_id}', headers)


def list_security_group_rules():
    '''
    https://www.conoha.jp/docs/neutron-get_rules_on_secgroup.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/security-group-rules', headers)


def describe_security_group_rule(rule_id):
    '''
    https://www.conoha.jp/docs/neutron-get_rules_detail_specified.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/security-group-rules/{rule_id}', headers)
