from conoha.api import compute
from conoha.util.misc import print_json


def server_list(detail):
    """
    サーバーの一覧を JSON 形式で標準出力する。

    Paramters
    ---------
    detail: bool
        詳細を表示するか

    Returns
    -------
    None
    """
    if detail:
        print_json(compute.list_servers_detail())
    else:
        print_json(compute.list_servers())


def server_search(keyword):
    """
    ネームタグをキーワード検索してヒットしたサーバーの詳細を表示する。

    Paramters
    ---------
    keyword: str
        検索キーワード

    Returns
    -------
    None
    """
    print_json(
        {
            "servers": list(
                filter(
                    lambda x: keyword
                    in x.get("metadata", {}).get("instance_name_tag", ""),
                    compute.list_servers_detail().get("servers", []),
                )
            )
        }
    )


def server_describe(server_id):
    """
    指定したサーバーの情報を JSON 形式で標準出力する。

    Paramters
    ---------
    server_id: str
        対象サーバーのID

    Returns
    -------
    None
    """
    print_json(compute.describe_server(server_id))


def server_create(
    volume_id,
    flavor_ref,
    admin_pass=None,
    key_name=None,
    security_groups=None,
    instance_name_tag=None,
    user_data=None,
):
    """
    サーバーを新規に作成する。
    作成したサーバーの情報を JSON 形式で標準出力する。

    Paramters
    ---------
    volume_id: str
        使用するブートストレージ用ボリュームの ID
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
    user_data: str
        スタートアップスクリプト
        ※ ファイル名指定でもよいかも

    Returns
    -------
    None
    """
    print_json(
        compute.create_server(
            volume_id,
            flavor_ref,
            admin_pass,
            key_name,
            security_groups,
            instance_name_tag,
            user_data,
        )
    )


def server_start(server_id):
    """
    指定したサーバーを起動する。

    Paramters
    ---------
    server_id: str
        対象サーバーのID

    Returns
    -------
    None
    """
    print_json(compute.start_server(server_id))


def server_stop(server_id, force):
    """
    指定したサーバーを停止起動する。

    Paramters
    ---------
    server_id: str
        対象サーバーのID
    force: bool
        強制停止するか

    Returns
    -------
    None
    """
    print_json(compute.stop_server(server_id, force))


def server_delete(server_id, force):
    """
    指定したサーバーを削除する。

    Paramters
    ---------
    server_id: str
        対象サーバーのID
    force: bool
        削除ロックが設定してあった場合でも削除を強行するか

    Returns
    -------
    None
    """
    if force:
        print_json(compute.delete_server(server_id))
    else:
        is_delete_locked = (
            compute.describe_server(server_id)
            .get("server", {})
            .get("metadata", {})
            .get("IsDeleteLocked", "False")
        )
        if is_delete_locked == "True":
            print("このサーバーは削除ロックされています。")
        else:
            print_json(compute.delete_server(server_id))


def server_attach_port(server_id, port_id):
    print_json(compute.attach_port(server_id, port_id))


def server_detach_port(server_id, port_id):
    print_json(compute.detach_port(server_id, port_id))


def server_list_ports(server_id):
    print_json(compute.list_ports(server_id))
