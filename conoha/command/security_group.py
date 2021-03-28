'''
conoha subnet コマンドの処理部分
'''

from conoha.api import network
from conoha.util.misc import print_json


def secutiry_group_list_rules():
    print_json(network.list_security_group_rules())


def secutiry_group_describe_rule(rule_id):
    print_json(network.describe_security_group_rule(rule_id))
