'''
conoha subnet コマンドの処理部分
'''

from conoha.api import network
from conoha.util.misc import print_json


def subnet_create(network_id, cidr):
    print_json(network.create_subnet(network_id, cidr))


def subnet_delete(subnet_id):
    print_json(network.delete_subnet(subnet_id))


def subnet_list():
    print_json(network.list_subnets())


def subnet_describe(subnet_id):
    print_json(network.describe_subnet(subnet_id))
