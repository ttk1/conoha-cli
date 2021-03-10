from executor import Command


def nop(*args, **kwargs):
    pass


def get_command():
    command = Command()

    ########
    # auth #
    ########

    # conoha auth login
    command.subcommand('auth').subcommand('login').set_handler(nop)

    # conoha auth logout
    command.subcommand('auth').subcommand('logout').set_handler(nop)

    ##########
    # server #
    ##########

    # conoha server create ...
    command.subcommand('server').subcommand('create').add_argument(
        '--image-ref', help='image 参照先。対象 image の UUID を指定', required=True
    ).add_argument(
        '--flavor-ref', help='VMプラン(flavor) の UUID を指定', required=True
    ).add_argument(
        '--admin-pass', help='VMのrootパスワード'
    ).add_argument(
        '--key-name', help='SSHキーを利用する場合に指定する '
    ).add_argument(
        '--security-groups', help='keyに”name“を、valueにセキュリティグループ名を指定する'
    ).add_argument(
        '--metadata', help='metadata の key:value ペア。'
    ).add_argument(
        '--instance-name-tag',
        help='ネームタグを入れる際に利用する。文字種：半角英数字、「 - 」、「 _ 」のみを許可。文字数：255文字以下, Default:VMに紐づくGlobalIPアドレス'
    ).add_argument(
        '--block-device-mapping', nargs='+', help='deviceは１つのみマッピングできる'
    ).add_argument(
        '--volume-id', help='アタッチしたいVolumeのIDを指定する'
    ).add_argument(
        '--vnc-keymap', choices=['en-us', 'ja'], help='keymap 設定'
    ).add_argument(
        '--user-data', help='base64 encoded Cloud-Init script'
    ).set_handler(nop)

    # conoha server start --server-id SERVER_ID
    command.subcommand('server').subcommand('start').add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(nop)

    # conoha server stop --server-id SERVER_ID
    command.subcommand('server').subcommand('stop').add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(nop)

    # conoha server delete --server-id SERVER_ID
    command.subcommand('server').subcommand('delete').add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(nop)

    # conoha server list
    command.subcommand('server').subcommand('list').set_handler(nop)

    # conha server describe --server-id SERVER_ID
    command.subcommand('server').subcommand('describe').add_argument(
        '--server-id', help='サーバーID', required=True
    ).set_handler(nop)

    # conoha sercer attach-port --server-id SERVER_ID --port-id PORT_ID
    command.subcommand('server').subcommand('attach-port').add_argument(
        '--server-id', help='サーバーID', required=True
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).set_handler(nop)

    # conoha sercer detach-port --server-id SERVER_ID --port-id PORT_ID
    command.subcommand('server').subcommand('detach-port').add_argument(
        '--server-id', help='サーバーID', required=True
    ).add_argument(
        '--port-id', help='ポートID', required=True
    ).set_handler(nop)

    ##########
    # subnet #
    ##########

    # conoha subnet create ...
    command.subcommand('subnet').subcommand('create').add_argument(
        '--network-id', help='ローカルネットワークのnetwork_idを指定する', required=True
    ).add_argument(
        '--cidr', help='プライベートアドレスのみ指定できます。bitmaskは21~27の間が指定できます。', required=True
    ).set_handler(nop)

    # conoha subnet delete --subnet-id SUBNET_ID
    command.subcommand('subnet').subcommand('delete').add_argument(
        '--subnet-id', help='サブネットID', required=True
    ).set_handler(nop)

    # conoha subnet describe --subnet-id SUBNET_ID
    command.subcommand('subnet').subcommand('describe').add_argument(
        '--subnet-id', help='サブネットID', required=True
    ).set_handler(nop)

    ##################
    # security-group #
    ##################

    # conoha security-group create ...
    command.subcommand('security-group').subcommand('create').add_argument(
        '--name', help='A symbolic name for the security group. 名前の重複はできません。', required=True
    ).add_argument(
        '--description', help='Describes the security group.'
    ).set_handler(nop)

    # conoha security-group delete --group-id GROUP_ID
    command.subcommand('security-group').subcommand('delete').add_argument(
        '--security-group-id', help='セキュリティグループID', required=True
    ).set_handler(nop)

    # conoha security-group list
    command.subcommand('security-group').subcommand('list').set_handler(nop)

    # conoha security-group describe --group-id GROUP_ID
    command.subcommand('security-group').subcommand('describe').add_argument(
        '--security-group-id', help='セキュリティグループID', required=True
    ).set_handler(nop)

    # conoha security-group create-rule --group-id GROUP_ID ...
    command.subcommand('security-group').subcommand('create-rule').add_argument(
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
    ).set_handler(nop)

    # conoha security-group delete-rule --rule-id RULE_ID
    command.subcommand('security-group').subcommand('delete-rule').add_argument(
        '--rule-id', help='セキュリティグループルールID', required=True
    ).set_handler(nop)

    # conoha security-group describe-rule --rule-id RULE_ID
    command.subcommand('security-group').subcommand('describe-rule').add_argument(
        '--rule-id', help='セキュリティグループルールID', required=True
    ).set_handler(nop)

    ###########
    # network #
    ###########

    # conoha network create
    command.subcommand('network').subcommand('create').set_handler(nop)

    # conoha network delete
    command.subcommand('network').subcommand('delete').add_argument(
        '--network-id', help='ネットワークID', required=True
    ).set_handler(nop)

    # conoha network list
    command.subcommand('network').subcommand('list').set_handler(nop)

    # conoha network describe
    command.subcommand('network').subcommand('describe').add_argument(
        '--network-id', help='ネットワークID', required=True
    ).set_handler(nop)

    ########
    # port #
    ########

    # command.subcommand('port').subcommand('create').add_argument(
    # ).set_handler(nop)
    # command.subcommand('port').subcommand('delete').add_argument(
    # ).set_handler(nop)
    # command.subcommand('port').subcommand('list').add_argument(
    # ).set_handler(nop)
    # command.subcommand('port').subcommand('describe').add_argument(
    # ).set_handler(nop)

    return command


def main():
    get_command().execute()
