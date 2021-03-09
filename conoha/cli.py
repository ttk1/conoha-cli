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

    # command.subcommand('security-group').subcommand('create').add_argument(
    # ).set_handler(nop)
    # command.subcommand('security-group').subcommand('delete').add_argument(
    # ).set_handler(nop)
    # command.subcommand('security-group').subcommand('list').add_argument(
    # ).set_handler(nop)
    # command.subcommand('security-group').subcommand('describe').add_argument(
    # ).set_handler(nop)

    ###########
    # network #
    ###########

    # command.subcommand('network').subcommand('create').add_argument(
    # ).set_handler(nop)
    # command.subcommand('network').subcommand('delete').add_argument(
    # ).set_handler(nop)
    # command.subcommand('network').subcommand('list').add_argument(
    # ).set_handler(nop)
    # command.subcommand('network').subcommand('describe').add_argument(
    # ).set_handler(nop)

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
