import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # auth
    auth = subparsers.add_parser('auth').add_subparsers()
    auth_login = auth.add_parser('login')
    auth_logout = auth.add_parser('logout')

    # server
    server = subparsers.add_parser('server').add_subparsers()
    server_create = server.add_parser('create')
    server_start = server.add_parser('start')
    server_stop = server.add_parser('stop')
    server_delete = server.add_parser('delete')
    server_list = server.add_parser('list')
    server_describe = server.add_parser('describe')
    server_attach_port = server.add_parser('attach-port')
    server_detach_port = server.add_parser('detach-port')

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
    print(args)
