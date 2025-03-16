import json
from os import makedirs
from os.path import exists, expanduser

conoha_home = expanduser("~/.conoha")
config_path = f"{conoha_home}/config.json"
credential_path = f"{conoha_home}/credential.json"
token_path = f"{conoha_home}/token.json"

if not exists(conoha_home):
    makedirs(conoha_home)


def get_config():
    with open(config_path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def get_credential():
    with open(credential_path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def save_credential(credential):
    with open(credential_path, mode="w", encoding="utf-8") as f:
        json.dump(credential, f)


def get_token():
    with open(token_path, mode="r", encoding="utf-8") as f:
        return json.load(f)


def save_token(token):
    with open(token_path, mode="w", encoding="utf-8") as f:
        json.dump(token, f)
