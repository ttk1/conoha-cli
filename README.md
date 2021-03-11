# CONOHA CLI

ConoHa API を CLI で良しなに扱うための何か。

## 設定

### `~/.conoha/config.json`

```json
{
  "endpoint": {
    "identity": "https://hogehoge",
    "compute": "https://hogehoge",
    "network": "https://hogehoge"
  }
}
```

* エンドポイントの設定等をとりあえずここに入れておく
* **今は手動で作成する**ようになっているが、今後は API から自動で取得するようにしたい
* 現状実装済みなのは `identity`, `compute`, `network` の三つのみ

### `~/.conoha/credential.json`

```json
{
  "user_name": "hoge",
  "password": "fuga",
  "tenant_id": "piyo"
}
```

* `tenant_id` は不要かもしれない
* 設定が無ければプロンプトで入力を求める

### `~/.conoha/token.json`

```json
{
  "token_id": "hogehgoefugafuga",
  "expires": "2099-09-19T09:09:09Z"
}
```

* ログインコマンド実行時に自動で作成
