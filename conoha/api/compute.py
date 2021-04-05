'''
Compute API の呼び出し部分
'''

import base64
from conoha import config
from conoha.util import http

endpoint = config.get_config()['endpoint']['compute']


def list_flavors():
    '''
    https://www.conoha.jp/docs/compute-get_flavors_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/flavors', headers)

###########################################################################


def list_images():
    '''
    https://www.conoha.jp/docs/compute-get_images_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/images', headers)

###########################################################################


def list_servers():
    '''
    通常: https://www.conoha.jp/docs/compute-get_vms_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/servers', headers)


def list_servers_detail():
    '''
    詳細表示: https://www.conoha.jp/docs/compute-get_vms_detail.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/servers/detail', headers)


def describe_server(server_id):
    '''
    https://www.conoha.jp/docs/compute-get_vms_detail_specified.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/servers/{server_id}', headers)


def create_server(image_ref, flavor_ref,
                  admin_pass=None, key_name=None,
                  security_groups=None,
                  instance_name_tag=None, volume_id=None,
                  vnc_keymap=None, user_data=None):
    '''
    https://www.conoha.jp/docs/compute-create_vm.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }

    # 必須項目
    data = {
        'server': {
            'imageRef': image_ref,
            'flavorRef': flavor_ref
        }
    }

    # Optional 項目
    if admin_pass is not None:
        data['server']['adminPass'] = admin_pass
    if key_name is not None:
        data['server']['key_name'] = key_name
    if security_groups is not None:
        data['server']['security_groups'] = []
        for security_group in security_groups:
            data['server']['security_groups'].append({
                'name': security_group
            })
    if instance_name_tag is not None:
        data['server']['metadata'] = {
            'instance_name_tag': instance_name_tag
        }
    if volume_id is not None:
        data['server']['block_device_mapping'] = {
            'volume_id': volume_id
        }
    if vnc_keymap is not None:
        data['server']['vncKeymap'] = vnc_keymap
    if user_data is not None:
        # 生の文字列を BASE64 エンコードに変換する
        data['server']['user_data'] = base64.b64encode(
            user_data.encode(encoding='utf-8')
        ).decode(encoding='utf-8')
    return http.post(f'{endpoint}/servers', data, headers)


def start_server(server_id):
    '''
    https://www.conoha.jp/docs/compute-power_on_vm.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    data = {
        'os-start': None
    }
    return http.post(f'{endpoint}/servers/{server_id}/action', data, headers)


def stop_server(server_id, force):
    '''
    通常停止: https://www.conoha.jp/docs/compute-stop_cleanly_vm.php
    強制停止: https://www.conoha.jp/docs/compute-stop_forcibly_vm.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    data = {
        'os-stop': None
    }
    if force:
        data['os-stop'] = {
            'force_shutdown': True
        }
    return http.post(f'{endpoint}/servers/{server_id}/action', data, headers)


def delete_server(server_id):
    '''
    https://www.conoha.jp/docs/compute-delete_vm.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/servers/{server_id}', headers)

###########################################################################


def attach_port(server_id, port_id):
    '''
    https://www.conoha.jp/docs/compute-attach_port.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    data = {
        'interfaceAttachment': {
            'port_id': port_id
        }
    }
    return http.post(f'{endpoint}/servers/{server_id}/os-interface', data, headers)


def detach_port(server_id, port_id):
    '''
    https://www.conoha.jp/docs/compute-dettach_port.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.delete(f'{endpoint}/servers/{server_id}/os-interface/{port_id}', headers)


def list_ports(server_id):
    '''
    https://www.conoha.jp/docs/compute-get_attached_ports_list.php
    '''
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': config.get_token()['id']
    }
    return http.get(f'{endpoint}/servers/{server_id}/os-interface', headers)
