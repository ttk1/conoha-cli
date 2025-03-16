# ConoHa CLI

[ConoHa VPS Ver.3.0 の公開 API](https://doc.conoha.jp/reference/api-vps3/) を CLI で良しなに扱うための何か。

自分が使うために作ったものなので、使わない機能は実装していません。

## 設定ファイル

### `~/.conoha/config.json`

```json
{
  "endpoint": {
    "identity": "https://identity.c3j1.conoha.io/v3",
    "compute": "https://compute.c3j1.conoha.io/v2.1",
    "network": "https://networking.c3j1.conoha.io/v2.0",
    "image": "https://image-service.c3j1.conoha.io/v2",
    "volume": "https://block-storage.c3j1.conoha.io/v3/{テナントID}"
  }
}
```

エンドポイントの設定をここに記述します。
ConoHa のコンソール画面に表示されているものを使って作成してください。
`identity`, `compute`, `network`, `image`, `volume` が必要です。

### `~/.conoha/credential.json`

```json
{
  "user_name": "{user_name}",
  "tenant_name": "{tenant_name}",
  "password": "{password}"
}
```

API ユーザのユーザ名、テナント名、パスワードをここに記述します。
ファイルが無ければ `conoha auth login` コマンド実行時に入力を求められます。
入力された内容は `credential.json` に保存されます。

### `~/.conoha/token.json`

```json
{
  "id": "{token_id}",
  "expires": "2099-09-19T09:09:09Z"
}
```

`conoha auth login` マンド実行時に自動で作成されます。
ここに保存されたトークンを使って API の呼び出しが行われることになります。
`expires` は今のところ使っていません。

## コマンド

```
$ conoha -h
usage: conoha [-h] {auth,flavor,image,server,subnet,security-group,network,port} ...

positional arguments:
  {auth,flavor,image,server,subnet,security-group,network,port}

optional arguments:
  -h, --help            show this help message and exit
```

各コマンドのオプションに `-h` を指定することで、コマンドの説明を表示することが出来ます。
どの機能が使えるかは `-h` を指定して調べるか、ソースコードを見て確認してください。

## 使用例

メモリ 512 MB プランで Ubuntu 20.04 イメージを使ってサーバーを作成してみます。

デフォルトのセキュリティグループだと SSH 接続ができないので、
あらかじめ SSH 接続用のルールを追加したセキュリティグループを作成しておきます。

`conoha image search` と `conoha flavor search` で目的のイメージとプランの ID を探し、
それを使い `conoha server create` でサーバーを作成します。

```sh
# セキュリティグループの作成
sg_id=$(
  conoha security-group create \
    --name 'test-sg' |
  jq -r '.security_group | .id'
)

# SSH 接続用のルールを追加
conoha security-group create-rule \
  --direction ingress \
  --ether-type IPv4 \
  --security-group-id "$sg_id" \
  --port-range-min 22 \
  --port-range-max 22 \
  --protocol tcp

# イメージとプランの ID を取得
image_ref=$(
  conoha image search 'vmi-ubuntu-20.04-amd64-30gb' |
  jq -r '.images[0] | .id'
)
flavor_ref=$(
  conoha flavor search 'g-c1m512d30' |
  jq -r '.flavors[0] | .id'
)

# サーバーの作成
conoha server create \
  --image-ref "$image_ref" \
  --flavor-ref "$flavor_ref" \
  --security-groups 'test-sg' \
  --instance-name-tag 'test-server'
```

## 作成できるリソースの上限

* サブネットは 1 つのローカルネットワークにつき 1 つまでしか作成できない
* ローカルネットワーク（プライベートネットワーク）は 1 つのアカウントにつき 10 個まで作成できる
* ローカルネットワークのポートは 1 つのサーバーに 2 つまでアタッチできる
* セキュリティグループは一つのアカウントにつき 50 個まで作成できる

## 使っていないリソースを見つける

コンソールからは見ることが出来ないリソースがあるため、うっかりしていると削除し忘れたままになってしまいます。

ここではそういったリソースを見つける方法を紹介します。

### 使っていないローカルネットワークを見つける

ローカルネットの一覧は `conoha network list -l` で取得出来ます。
この中からサブネットが作成されていないものを取り出せば良いでしょう。

```sh
conoha network list -l |
jq -r '.networks[] | select(.subnets | length == 0)'
```

### 使っていないローカルサブネットを見つける

コンソール上でどのサーバーとも接続していないプライベートネットワークがあれば、
それは使われていないローカルサブネットです。

### 使っていないポートを見つける

ポートの一覧は `conoha port list` 出来ます。
`device_id` が空（`""`）のポートがあれば、それは使われていないポートです。

```sh
conoha port list | jq -r '.ports[] | select(.device_id == "")'
```

### 使っていないセキュリティグループを見つける

ポートにアタッチされているセキュリティグループの ID の一覧は次のコマンドで調べることが出来ます。

```sh
conoha port list | jq -r '.ports[] | .security_groups[]' | sort | uniq
```

またセキュリティグループの ID の一覧は次のコマンドで調べることが出来ます。

```sh
conoha security-group list | jq -r '.security_groups[] | .id'
```

二つのコマンドの結果を比較すると良いでしょう。

```sh
diff <(
  conoha port list |
  jq -r '.ports[] | .security_groups[]' |
  sort | uniq
) <(
  conoha security-group list |
  jq -r '.security_groups[] | .id' |
  sort
)
```

## 免責事項

このツールを使ったことによって生じた結果について、いかなる責任も負いません。
ご使用は自己責任でお願いします。
