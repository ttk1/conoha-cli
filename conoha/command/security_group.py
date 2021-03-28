'''
conoha subnet コマンドの処理部分
'''

from conoha.api import network
from conoha.util.misc import print_json


def security_group_create(name, description=None):
    print_json(network.create_security_group(name, description))


def security_group_delete(security_group_id):
    print_json(network.delete_security_group(security_group_id))


def security_group_list():
    print_json(network.list_security_groups())


def security_group_describe(security_group_id):
    print_json(network.describe_security_group(security_group_id))


def secutiry_group_list_rules():
    print_json(network.list_security_group_rules())


def secutiry_group_describe_rule(rule_id):
    print_json(network.describe_security_group_rule(rule_id))
