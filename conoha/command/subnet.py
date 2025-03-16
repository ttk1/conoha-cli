from conoha.api import network
from conoha.util.misc import print_json


def subnet_create(network_id, cidr):
    print_json(network.create_subnet(network_id, cidr))


def subnet_delete(subnet_id):
    print_json(network.delete_subnet(subnet_id))


def subnet_list(local_only):
    if local_only:
        # local で始まる subnet のみを表示する
        print_json(
            {
                "subnets": list(
                    filter(
                        lambda x: x.get("name", "").startswith("local"),
                        network.list_subnets().get("subnets", []),
                    )
                )
            }
        )
    else:
        print_json(network.list_subnets())


def subnet_describe(subnet_id):
    print_json(network.describe_subnet(subnet_id))
