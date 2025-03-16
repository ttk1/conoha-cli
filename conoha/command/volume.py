from conoha.api import volume
from conoha.util.misc import print_json


def volume_list_types():
    print_json(volume.list_types())


def volume_list():
    print_json(volume.list_volumes())


def volume_create(size, description, name, image_ref):
    print_json(volume.create_volume(size, description, name, image_ref))


def volume_delete(volume_id, force):
    print_json(volume.delete_volume(volume_id, force))
