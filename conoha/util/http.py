import json
import urllib.request


def post(url, data, headers):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode("utf-8"), headers=headers
    )
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            # JSON のデーコードに失敗したら文字列のまま返す
            return body


def get(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            # JSON のデーコードに失敗したら文字列のまま返す
            return body


def delete(url, headers):
    req = urllib.request.Request(url, headers=headers, method="DELETE")
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            # JSON のデーコードに失敗したら文字列のまま返す
            return body


def put(url, data, headers):
    req = urllib.request.Request(
        url, data=json.dumps(data).encode("utf-8"), headers=headers, method="PUT"
    )
    with urllib.request.urlopen(req) as res:
        body = res.read().decode("utf-8")
        try:
            return json.loads(body)
        except json.JSONDecodeError:
            # JSON のデーコードに失敗したら文字列のまま返す
            return body
