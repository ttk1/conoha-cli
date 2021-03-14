from os.path import expanduser, exists
from os import makedirs

config_path = expanduser('~/.conoha')
credential_path = f'{config_path}/credential.json'

if not exists(config_path):
    makedirs(config_path)
