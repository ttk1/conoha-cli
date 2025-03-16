from conoha import config
from conoha.util import http

endpoint = config.get_config()["endpoint"]["image"]
token = config.get_token()


def list_images():
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    # TODO: クエリパラメータでいい感じに検索できるようにしたい
    return http.get(f"{endpoint}/images?limit=200", headers)
