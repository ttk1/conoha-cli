'''
conoha image コマンドの処理部分
'''

from conoha.api import compute
from conoha.util.misc import print_json


def image_list():
    print_json(compute.list_images())


def image_search(keyword):
    print_json({
        'images': list(filter(
            lambda x: keyword in x.get('name', ''),
            compute.list_images().get('images', [])
        ))
    })
