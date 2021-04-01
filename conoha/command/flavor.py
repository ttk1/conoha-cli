'''
conoha flavor コマンドの処理部分
'''

from conoha.api import compute
from conoha.util.misc import print_json


def flavor_list():
    print_json(compute.list_flavors())


def flavor_search(keyword):
    print_json({
        'flavors': list(filter(
            lambda x: keyword in x.get('name'),
            compute.list_flavors().get('flavors', [])
        ))
    })
