"""
conoha port コマンドの処理部分
"""

from conoha.api import network
from conoha.util.misc import print_json


def port_create(network_id, ip_address, subnet_id, security_group_ids=None):
    print_json(
        network.create_port(network_id, ip_address, subnet_id, security_group_ids)
    )


def port_update(port_id, security_group_ids):
    print_json(network.update_port(port_id, security_group_ids))


def port_delete(port_id):
    print_json(network.delete_port(port_id))


def port_list():
    print_json(network.list_ports())


def port_describe(port_id):
    print_json(network.describe_port(port_id))
