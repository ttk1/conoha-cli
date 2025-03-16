import base64

from conoha import config
from conoha.util import http

endpoint = config.get_config()["endpoint"]["compute"]
token = config.get_token()


def list_flavors():
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/flavors", headers)


def list_servers():
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/servers", headers)


def list_servers_detail():
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/servers/detail", headers)


def describe_server(server_id):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/servers/{server_id}", headers)


def create_server(
    volume_id,
    flavor_ref,
    admin_pass=None,
    key_name=None,
    security_groups=None,
    instance_name_tag=None,
    user_data=None,
):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    # 必須項目
    data = {
        "server": {
            "block_device_mapping_v2": [{"uuid": volume_id}],
            "flavorRef": flavor_ref,
        }
    }
    # Optional 項目
    if admin_pass is not None:
        data["server"]["adminPass"] = admin_pass
    if key_name is not None:
        data["server"]["key_name"] = key_name
    if security_groups is not None:
        data["server"]["security_groups"] = []
        for security_group in security_groups:
            data["server"]["security_groups"].append({"name": security_group})
    if instance_name_tag is not None:
        data["server"]["metadata"] = {"instance_name_tag": instance_name_tag}
    if user_data is not None:
        # 生の文字列を BASE64 エンコードに変換する
        data["server"]["user_data"] = base64.b64encode(
            user_data.encode(encoding="utf-8")
        ).decode(encoding="utf-8")
    return http.post(f"{endpoint}/servers", data, headers)


def start_server(server_id):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    data = {"os-start": None}
    return http.post(f"{endpoint}/servers/{server_id}/action", data, headers)


def stop_server(server_id, force):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    data = {"os-stop": None}
    if force:
        data["os-stop"] = {"force_shutdown": True}  # type: ignore
    return http.post(f"{endpoint}/servers/{server_id}/action", data, headers)


def delete_server(server_id):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.delete(f"{endpoint}/servers/{server_id}", headers)


def attach_port(server_id, port_id):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    data = {"interfaceAttachment": {"port_id": port_id}}
    return http.post(f"{endpoint}/servers/{server_id}/os-interface", data, headers)


def detach_port(server_id, port_id):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.delete(
        f"{endpoint}/servers/{server_id}/os-interface/{port_id}", headers
    )


def list_ports(server_id):
    headers = {"Accept": "application/json", "X-Auth-Token": token}
    return http.get(f"{endpoint}/servers/{server_id}/os-interface", headers)
