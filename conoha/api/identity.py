"""
Identity API の呼び出し部分
"""

from conoha import config
from conoha.util import http

endpoint = config.get_config()["endpoint"]["identity"]


def get_token(user_name, password, tenant_id):
    """
    https://www.conoha.jp/docs/identity-post_tokens.php
    """
    headers = {"Accept": "application/json"}
    data = {
        "auth": {
            "passwordCredentials": {"username": user_name, "password": password},
            "tenantId": tenant_id,
        }
    }
    return http.post(f"{endpoint}/tokens", data, headers)
