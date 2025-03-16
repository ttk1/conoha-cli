from conoha import config
from conoha.util import http

endpoint = config.get_config()["endpoint"]["volume"]
token = config.get_token()


def list_types():
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/types", headers)


def list_volumes():
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/volumes", headers)


def create_volume(size, description, name, image_ref):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    data = {
        "volume": {
            "size": size,
            "description": description,
            "name": name,
            "imageRef": image_ref,
            # ブートストレージ用ボリュームは c3j1-ds02-boot 固定
            # ref: https://doc.conoha.jp/reference/api-vps3/api-blockstorage-vps3/volume-get_types_list-v3/
            "volume_type": "c3j1-ds02-boot",
        }
    }
    return http.post(f"{endpoint}/volumes", data, headers)


def delete_volume(volume_id, force):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    if force:
        return http.delete(f"{endpoint}/volumes/{volume_id}?force=true", headers)
    else:
        return http.delete(f"{endpoint}/volumes/{volume_id}", headers)
