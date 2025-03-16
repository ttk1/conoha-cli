"""
conoha auth コマンドの処理部分
"""

from getpass import getpass

from conoha import config
from conoha.api import identity


def auth_login():
    try:
        credential = config.get_credential()
    except FileNotFoundError:
        credential = {
            "user_name": input("Enter user name: "),
            "tenant_name": input("Enter tenant name: "),
            "password": getpass("Enter password: "),
        }
        config.save_credential(credential)
    token = identity.get_token(
        credential["user_name"], credential["password"], credential["tenant_name"]
    )
    config.save_token(token)


def auth_logout():
    # 未実装
    pass
