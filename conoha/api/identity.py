"""
Identity API の呼び出し部分
"""

from conoha import config
from conoha.util import http

endpoint = config.get_config()["endpoint"]["identity"]


def get_token(user_name, password, tenant_name):
    headers = {"Accept": "application/json"}
    data = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {"user": {"name": user_name, "password": password}},
            },
            "scope": {"project": {"name": tenant_name}},
        }
    }
    return http.post_for_token(f"{endpoint}/auth/tokens", data, headers)
