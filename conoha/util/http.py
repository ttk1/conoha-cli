import json
import urllib.request


def post(url, data, headers):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode('utf-8'), headers=headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        return json.loads(body.decode('utf-8'))


def get(url, headers):
    pass
