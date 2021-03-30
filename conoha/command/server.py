'''
conoha server コマンドの処理部分
'''

from conoha.api import compute
from conoha.util.misc import print_json


def server_list():
    '''
    サーバーの一覧を JSON 形式で標準出力する。

    Returns
    -------
    None
    '''
    print_json(compute.list_servers())


def server_describe(server_id):
    '''
    指定したサーバーの情報を JSON 形式で標準出力する。

    Paramters
    ---------
    server_id: str
        対象サーバーのID

    Returns
    -------
    None
    '''
    print_json(compute.describe_server(server_id))


def server_create(image_ref, flavor_ref,
                  admin_pass=None, key_name=None,
                  security_groups=None,
                  instance_name_tag=None, volume_id=None,
                  vnc_keymap=None, user_data=None):
    '''
    サーバーを新規に作成する。
    作成したサーバーの情報を JSON 形式で標準出力する。

    Paramters
    ---------
    image_ref: str
        【必須項目】使用するイメージの UUID
    flavor_ref: str
        【必須項目】VM プランの UUID
    admin_pass: str
        VM の root パスワード
        指定しなかったら
        * パブリックイメージの場合ランダムなパスワード
        * プライベートイメージの場合元のパスワード
        が設定される
    key_name: str
        SSH キーの名前
    security_groups: list of str
        アタッチするセキュリティグループのリスト
        多分デフォルトで作成されるポートに適用されるやつ
    instance_name_tag: str
        VM に設定するネームタグ
    volume_id: str
        アタッチする Volume の ID
    vnc_keymap: str
        キーマップ（en-us, ja のいずれか）
    user_data: str
        スタートアップスクリプト
        ※ ファイル名指定でもよいかも

    Returns
    -------
    None
    '''
    print_json(compute.create_server(image_ref, flavor_ref,
                                     admin_pass, key_name,
                                     security_groups,
                                     instance_name_tag, volume_id,
                                     vnc_keymap, user_data))


def server_start(server_id):
    '''
    指定したサーバーを起動する。

    Paramters
    ---------
    server_id: str
        対象サーバーのID

    Returns
    -------
    None
    '''
    print_json(compute.start_server(server_id))


def server_stop(server_id):
    '''
    指定したサーバーを停止起動する。
    現状実装されているのは通常停止のみ。
    TODO: force パラメータを追加して強制停止を実装

    Paramters
    ---------
    server_id: str
        対象サーバーのID

    Returns
    -------
    None
    '''
    print_json(compute.stop_server(server_id))


def server_delete(server_id):
    '''
    指定したサーバーを削除する。
    WebUI で削除ロックかけてても消せるので注意。
    TODO: 削除ロックのチェック(可能？)

    Paramters
    ---------
    server_id: str
        対象サーバーのID

    Returns
    -------
    None
    '''
    print_json(compute.delete_server(server_id))

###########################################################################


def server_attach_port(server_id, port_id):
    print_json(compute.attach_port(server_id, port_id))


def server_detach_port(server_id, port_id):
    print_json(compute.detach_port(server_id, port_id))


def server_list_ports(server_id):
    print_json(compute.list_ports(server_id))
