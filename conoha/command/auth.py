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

    # これは API の方で記述すべし
    data = {
        'auth': {
            'passwordCredentials': {
                'username': credential['user_name'],
                'password': credential['password']
            },
            'tenantId': credential['tenant_id']
        }
    }
    res = identity.get_token(data)
    token = {
        'id': res["access"]["token"]["id"],
        'expires': res["access"]["token"]["expires"]
    }
    config.save_token(token)


def auth_logout():
    # 未実装
    pass
