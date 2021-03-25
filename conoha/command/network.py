'''
conoha network コマンドの処理部分
'''

from conoha.api import network
from conoha.util.misc import print_json


def network_list():
    print_json(network.list_networks())


def network_create():
    print_json(network.create_network())


def network_delete(network_id):
    print_json(network.delete_network(network_id))


def network_describe(network_id):
    print_json(network.describe_network(network_id))
