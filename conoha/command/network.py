'''
conoha network コマンドの処理部分
'''

from conoha.api import network
from conoha.util.misc import print_json


def network_list(local_only):
    if local_only:
        # local で始まる network のみを表示する
        print_json({
            'networks': list(filter(
                lambda x: x.get('name', '').startswith('local'),
                network.list_networks().get('networks', [])
            ))
        })
    else:
        print_json(network.list_networks())


def network_create():
    print_json(network.create_network())


def network_delete(network_id):
    print_json(network.delete_network(network_id))


def network_describe(network_id):
    print_json(network.describe_network(network_id))
