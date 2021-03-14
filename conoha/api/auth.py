from getpass import getpass
import conoha.api.config as config


def auth_login():
    try:
        credential = config.get_credential()
    except FileNotFoundError:
        with open(config.credential_path, mode='w', encoding='utf-8') as f:
            credential = {
                'user_name': input('Enter user name: '),
                'password': getpass('Enter password: '),
                'tenant_id': input('Enter tenant id: ')
            }
            config.save_credential(credential)

    data = {
        'auth': {
            'passwordCredentials': {
                'username': credential['user_name'],
                'password': credential['password']
            },
            'tenantId': credential['tenant_id']
        }
    }

    print(data)


def auth_logout():
    pass
