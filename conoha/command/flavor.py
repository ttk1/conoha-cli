from conoha import config
from conoha.api import compute
from conoha.util.misc import print_json


def flavor_list():
    print_json(compute.list_flavors())
