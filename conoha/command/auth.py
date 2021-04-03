'''
conoha auth コマンドの処理部分
'''

from getpass import getpass
from conoha import config
from conoha.api import identity


def auth_login():
    try:
        credential = config.get_credential()
    except FileNotFoundError:
        credential = {
            'user_name': input('Enter user name: '),
            'password': getpass('Enter password: '),
            'tenant_id': input('Enter tenant id: ')
        }
        config.save_credential(credential)
    res = identity.get_token(credential['user_name'],
                             credential['password'],
                             credential['tenant_id'])
    config.save_token({
        'id': res["access"]["token"]["id"],
        'expires': res["access"]["token"]["expires"]
    })


def auth_logout():
    # 未実装
    pass
