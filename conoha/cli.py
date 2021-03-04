import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand")


    # auth
    auth = subparsers.add_parser('auth').add_subparsers(dest="subsubcommand")
    auth_login = auth.add_parser('login')
    auth_logout = auth.add_parser('logout')


    # conoha server
    server = subparsers.add_parser('server').add_subparsers(dest="subsubcommand")

    # conoha server create options...
    # https://www.conoha.jp/docs/compute-create_vm.php
    server_create = server.add_parser('create')
    server_create.add_argument('--image-ref', help='image 参照先。対象 image の UUID を指定', required=True)
    server_create.add_argument('--flavor-ref', help='VMプラン(flavor) の UUID を指定', required=True)
    server_create.add_argument('--admin-pass', help='VMのrootパスワード')
    server_create.add_argument('--key-name', help='SSHキーを利用する場合に指定する ')
    server_create.add_argument('--security-groups', help='keyに”name“を、valueにセキュリティグループ名を指定する')
    server_create.add_argument('--metadata', help='metadata の key:value ペア。')
    server_create.add_argument('--instance-name-tag', help='ネームタグを入れる際に利用する。文字種：半角英数字、「 - 」、「 _ 」のみを許可。文字数：255文字以下, Default:VMに紐づくGlobalIPアドレス ')
    server_create.add_argument('--block-device-mapping', nargs='+', help='deviceは１つのみマッピングできる')
    server_create.add_argument('--volume-id', help='アタッチしたいVolumeのIDを指定する')
    server_create.add_argument('--vnc-keymap', choices=['en-us', 'ja'], help='keymap 設定')
    server_create.add_argument('--user-data', help='base64 encoded Cloud-Init script')

    # conoha server start --server-id SERVER_ID
    server_start = server.add_parser('start')
    server_start.add_argument('--server-id', required=True)

    # conoha server stop --server-id SERVER_ID
    server_stop = server.add_parser('stop')
    server_stop.add_argument('--server-id', required=True)

    # conoha server delete --server-id SERVER_ID
    server_delete = server.add_parser('delete')
    server_delete.add_argument('--server-id', required=True)

    # conoha server list
    server_list = server.add_parser('list')

    # conha server describe --server-id SERVER_ID
    server_describe = server.add_parser('describe')
    server_describe.add_argument('--server-id', required=True)

    # conoha sercer attach-port --server-id SERVER_ID --port-id PORT_ID
    server_attach_port = server.add_parser('attach-port')
    server_attach_port.add_argument('--server-id', required=True)
    server_attach_port.add_argument('--port-id', required=True)

    # conoha sercer detach-port --server-id SERVER_ID --port-id PORT_ID
    server_detach_port = server.add_parser('detach-port')
    server_detach_port.add_argument('--server-id', required=True)
    server_detach_port.add_argument('--port-id', required=True)


    # subnet
    subnet = subparsers.add_parser('subnet').add_subparsers()
    subnet_create = subnet.add_parser('create')
    subnet_delete = subnet.add_parser('delete')
    subnet_describe = subnet.add_parser('describe')


    # security-group
    security_group = subparsers.add_parser('security-group').add_subparsers()
    security_group_create = security_group.add_parser('create')
    security_group_delete = security_group.add_parser('delete')
    security_group_list = security_group.add_parser('list')
    security_group_describe = security_group.add_parser('describe')


    # network
    network = subparsers.add_parser('network').add_subparsers()
    network_create = network.add_parser('create')
    network_delete = network.add_parser('delete')
    network_list = network.add_parser('list')
    network_describe = network.add_parser('describe')


    # port
    port = subparsers.add_parser('port').add_subparsers()
    port_create = port.add_parser('create')
    port_delete = port.add_parser('delete')
    port_list = port.add_parser('list')
    port_describe = port.add_parser('describe')

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(vars(args))
    #args.handler(**vars(args))
