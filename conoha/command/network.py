'''
conoha network コマンドの処理部分
'''

from conoha.api import network
from conoha.util.misc import print_json


def network_list():
    print_json(network.list_networks())
