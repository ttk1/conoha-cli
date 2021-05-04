import argparse
from conoha.command import (
    auth,
    flavor,
    image,
    server,
    subnet,
    security_group,
    network,
    port
)


class Command():
    def __init__(self, parser=None):
        if parser is None:
            self._parser = argparse.ArgumentParser()
        else:
            self._parser = parser

        self.set_handler(self._parser.print_help)
        self._subparsers = None
        self._subcommands = {}

    def subcommand(self, name=None, description=None):
        if name in self._subcommands:
            return self._subcommands[name]

        if self._subparsers is None:
            self._subparsers = self._parser.add_subparsers()

        subparser = self._subparsers.add_parser(name=name, description=description)
        subcommand = Command(subparser)
        self._subcommands[name] = subcommand
        return subcommand

    def add_argument(self, *args, **kwargs):
        self._parser.add_argument(*args, **kwargs)
        return self

    def set_handler(self, handler):
        self._parser.set_defaults(__handler=handler)

    def execute(self):
        args = vars(self._parser.parse_args())
        handler = args.pop('__handler')
        handler(**args)


def auth_command(command):
    # conoha auth login
    command.subcommand(name='auth').subcommand(
        name='login',
        description='API トークンを取得して token.json に保存する'
    ).set_handler(auth.auth_login)

    # conoha auth logout
    # 一旦実装見送り
    # command.subcommand('auth').subcommand('logout').set_handler(nop)


def flavor_command(command):
    # conoha flavor list
    command.subcommand(name='flavor').subcommand(
        name='list',
        description='VM プランの一覧を表示する'
    ).set_handler(flavor.flavor_list)

    # conoha flavor search KEYWORD
    command.subcommand(name='flavor').subcommand(
        name='search',
        description='VM プランをプラン名の部分一致で検索する'
    ).add_argument(
        'keyword', metavar='KEYWORD', help='VM プラン名の検索キーワード(部分一致)'
    ).set_handler(flavor.flavor_search)


def image_command(command):
    # conoha image list
    command.subcommand(name='image').subcommand(
        name='list',
        description='イメージの一覧を表示する'
    ).set_handler(image.image_list)

    # conoha image search
    command.subcommand('image').subcommand('search').add_argument(
        'keyword', metavar='KEYWORD', help='イメージ名の検索キーワード(部分一致)'
    ).set_handler(image.image_search)


def server_command(command):
    # conoha server create ...
    command.subcommand(name='server').subcommand(
        name='create',
        description='VM を作成する'
    ).add_argument(
        '--image-ref', help='使用するイメージの UUID を指定', required=True
    ).add_argument(
        '--flavor-ref', help='VM プラン（flavor）の UUID を指定', required=True
    ).add_argument(
        '--admin-pass', help='VM の root パスワードを指定（使用可能な文字については要確認）'
    ).add_argument(
        # あらかじめ公開鍵を登録しておく必要あり！
        '--key-name', help='SSH キーの名前を指定'
    ).add_argument(
        # 何も設定しないと、立ち上げ直後外との通信が出来ない状態になる
        '--security-groups', help='セキュリティグループ名を指定', nargs='+'
    ).add_argument(
        '--instance-name-tag',
        help='ネームタグを入れる際に利用する。文字種：半角英数字、「 - 」、「 _ 」のみを許可。文字数：255文字以下, Default:VMに紐づくGlobalIPアドレス'
    ).add_argument(
        # API の仕様で一つしか指定できない
        '--volume-id', help='アタッチする Volume の ID を指定'
    ).add_argument(
        '--vnc-keymap', choices=['en-us', 'ja'], help='キーマップを指定'
    ).add_argument(
        # ファイル指定でも良いかもしれない
        '--user-data', help='スタートアップスクリプトを指定（BASE64 エンコードはしなくてよい）'
    ).set_handler(server.server_create)

    # conoha server start --server-id SERVER_ID
    command.subcommand(name='server').subcommand(
        name='start',
        description='VM を起動する'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(server.server_start)

    # conoha server stop --server-id SERVER_ID
    command.subcommand(name='server').subcommand(
        name='stop',
        description='VM を停止する'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).add_argument(
        '-f', '--force', action='store_true', help='強制終了する'
    ).set_handler(server.server_stop)

    # conoha server delete --server-id SERVER_ID
    command.subcommand(name='server').subcommand(
        name='delete',
        description='VM を削除する'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).add_argument(
        '-f', '--force', action='store_true', help='削除ロックがかかっていても削除を強行する'
    ).set_handler(server.server_delete)

    # conoha server list
    command.subcommand(name='server').subcommand(
        name='list',
        description='VM の一覧を表示する'
    ).add_argument(
        '-d', '--detail', action='store_true', help='詳細を取得するか'
    ).set_handler(server.server_list)

    # conoha server search KEYWORD
    command.subcommand(name='server').subcommand(
        name='search',
        description='VM をネームタグ名の部分一致で検索する'
    ).add_argument(
        'keyword', metavar='KEYWORD', help='ネームタグの検索キーワード(部分一致)'
    ).set_handler(server.server_search)

    # conha server describe --server-id SERVER_ID
    command.subcommand(name='server').subcommand(
        name='describe',
        description='VM の詳細を表示する'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(server.server_describe)

    # conoha server attach-port --server-id SERVER_ID --port-id PORT_ID
    command.subcommand(name='server').subcommand(
        name='attach-port',
        description='VM にポートをアタッチする'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).set_handler(server.server_attach_port)

    # conoha server detach-port --server-id SERVER_ID --port-id PORT_ID
    command.subcommand(name='server').subcommand(
        name='detach-port',
        description='VM からポートをでタッチする'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).set_handler(server.server_detach_port)

    # conoha server list-ports --server-id SERVER_ID
    command.subcommand(name='server').subcommand(
        name='list-ports',
        description='VM にアタッチされているポートの一覧を表示する'
    ).add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(server.server_list_ports)


def subnet_command(command):
    # conoha subnet create ...
    command.subcommand(name='subnet').subcommand(
        name='create',
        description='サブネットを作成する'
    ).add_argument(
        # ローカルネットワークには高々１つのサブネットしか割り当てることが出来ない
        '--network-id', help='ローカルネットワークのnetwork_idを指定する', required=True
    ).add_argument(
        '--cidr', help='プライベートアドレスのみ指定できます。bitmaskは21~27の間が指定できます。', required=True
    ).set_handler(subnet.subnet_create)

    # conoha subnet delete --subnet-id SUBNET_ID
    command.subcommand(name='subnet').subcommand(
        name='delete',
        description='サブネットを削除する'
    ).add_argument(
        '--subnet-id', help='サブネットID', required=True
    ).set_handler(subnet.subnet_delete)

    # conoha subnet list
    command.subcommand(name='subnet').subcommand(
        name='list',
        description='サブネットの一覧を表示する'
    ).set_handler(subnet.subnet_list)

    # conoha subnet describe --subnet-id SUBNET_ID
    command.subcommand(name='subnet').subcommand(
        name='describe',
        description='サブネットの詳細を表示する'
    ).add_argument(
        '--subnet-id', help='サブネットID', required=True
    ).set_handler(subnet.subnet_describe)


def security_group_command(command):
    # conoha security-group create ...
    command.subcommand(name='security-group').subcommand(
        name='create',
        description='セキュリティグループを作成する'
    ).add_argument(
        '--name', help='A symbolic name for the security group. 名前の重複はできません。', required=True
    ).add_argument(
        '--description', help='Describes the security group.'
    ).set_handler(security_group.security_group_create)

    # conoha security-group delete --group-id GROUP_ID
    command.subcommand(name='security-group').subcommand(
        name='delete',
        description='セキュリティグループを削除する。付属するルールもまとめて削除される。'
    ).add_argument(
        '--security-group-id', help='セキュリティグループID', required=True
    ).set_handler(security_group.security_group_delete)

    # conoha security-group list
    command.subcommand(name='security-group').subcommand(
        name='list',
        description='セキュリティグループの一覧を表示する'
    ).set_handler(security_group.security_group_list)

    # conoha security-group describe --group-id GROUP_ID
    command.subcommand(name='security-group').subcommand(
        name='describe',
        description='セキュリティグループの詳細を表示する'
    ).add_argument(
        '--security-group-id', help='セキュリティグループID', required=True
    ).set_handler(security_group.security_group_describe)

    # conoha security-group create-rule --group-id GROUP_ID ...
    command.subcommand(name='security-group').subcommand(
        name='create-rule',
        description=('セキュリティグループのルールを作成する。'
                     'port-range-min と port-range-max はセットで指定する必要がある。'
                     'port-range を指定する場合は protocol もセットで指定する必要がある。')
    ).add_argument(
        '--direction', choices=['ingress', 'egress'], help='セキュリティグループルールが反映される方向', required=True
    ).add_argument(
        '--ether-type', choices=['IPv4', 'IPv6'], help='イーサタイプ', required=True
    ).add_argument(
        '--security-group-id', help='セキュリティグループID', required=True
    ).add_argument(
        '--port-range-min', help='セキュリティグループルールを範囲で設定する場合の最小ポート番号'
    ).add_argument(
        '--port-range-max', help='セキュリティグループルールを範囲で設定する場合の最大ポート番号'
    ).add_argument(
        '--protocol', choices=['tcp', 'udp', 'icmp', 'null'],
        help='セキュリティグループルールが設定されるプロトコル。null を指定した場合すべての protocol を許可'
    ).add_argument(
        '--remote-group-id', help='指定したセキュリティグループIDに紐付いたポートからのトラフィックのみを許可'
    ).add_argument(
        '--remote-ip-prefix', help='指定した prefix を持つ IP からのトラフィックのみを許可'
    ).set_handler(security_group.secutiry_group_create_rule)

    # conoha security-group delete-rule --rule-id RULE_ID
    command.subcommand(name='security-group').subcommand(
        name='delete-rule',
        description='セキュリティグループルールを削除する'
    ).add_argument(
        '--rule-id', help='セキュリティグループルールID', required=True
    ).set_handler(security_group.security_group_delete_rule)

    # conoha security-group list-rules
    command.subcommand(name='security-group').subcommand(
        name='list-rules',
        description='セキュリティグループルールの一覧を表示する'
    ).set_handler(security_group.security_group_list_rules)

    # conoha security-group describe-rule --rule-id RULE_ID
    command.subcommand(name='security-group').subcommand(
        name='describe-rule',
        description='セキュリティグループの詳細を表示する'
    ).add_argument(
        '--rule-id', help='セキュリティグループルールID', required=True
    ).set_handler(security_group.security_group_describe_rule)


def network_command(command):
    # conoha network create
    command.subcommand(name='network').subcommand(
        name='create',
        description='ローカル通信用ネットワークを作成する'
    ).set_handler(network.network_create)

    # conoha network delete --network-id NETWORK_ID
    command.subcommand(name='network').subcommand(
        name='delete',
        description='ネットワークを削除する'
    ).add_argument(
        '--network-id', help='ネットワークID', required=True
    ).set_handler(network.network_delete)

    # conoha network list
    command.subcommand(name='network').subcommand(
        name='list',
        description='ネットワークの一覧を表示する'
    ).add_argument(
        '-l', '--local-only', action='store_true', help='ローカルネットワークのみを表示する'
    ).set_handler(network.network_list)

    # conoha network describe --network-id NETWORK_ID
    command.subcommand(name='network').subcommand(
        name='describe',
        description='ネットワークの詳細を表示する'
    ).add_argument(
        '--network-id', help='ネットワークID', required=True
    ).set_handler(network.network_describe)


def port_command(command):
    # conoha port create ...
    command.subcommand(name='port').subcommand(
        name='create',
        description='ポートを作成する。固定 IP は必須。'
    ).add_argument(
        '--network-id', help='ネットワークID', required=True
    ).add_argument(
        '--ip-address', help='IPアドレス(IPv4, IPv6)', required=True
    ).add_argument(
        '--subnet-id', help='サブネットID', required=True
    ).add_argument(
        '--security-group-ids', nargs='+', help='指定がない場合はDefaultのセキュリティグループが設定される'
    ).set_handler(port.port_create)

    # conoha port update --port-id PORT_ID --security-group-ids ...
    command.subcommand(name='port').subcommand(
        name='update',
        description='ポートのセキュリティグループを更新する（IP アドレスの更新は未実装）'
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).add_argument(
        '--security-group-ids', nargs='*', metavar='SECURITY_GROUP_ID', help='セキュリティグループID のリスト', required=True
    ).set_handler(port.port_update)

    # conoha port delete --port-id PORT_ID
    command.subcommand(name='port').subcommand(
        name='delete',
        description='ポートを削除する'
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).set_handler(port.port_delete)

    # conoha port list
    command.subcommand(name='port').subcommand(
        name='list',
        description='ポートの一覧を表示する'
    ).set_handler(port.port_list)

    # conoha port describe --port-id PORT_ID
    command.subcommand(name='port').subcommand(
        name='describe',
        description='ポートの詳細を表示する'
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).set_handler(port.port_describe)


def main():
    command = Command()
    auth_command(command)
    flavor_command(command)
    image_command(command)
    server_command(command)
    subnet_command(command)
    security_group_command(command)
    network_command(command)
    port_command(command)
    command.execute()
