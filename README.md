# ConoHa CLI

[ConoHa API](https://www.conoha.jp/docs/) を CLI で良しなに扱うための何か。

## 設定ファイル

### `~/.conoha/config.json`

```json
{
  "endpoint": {
    "identity": "https://identity.tyo1.conoha.io/v2.0",
    "compute": "https://compute.tyo1.conoha.io/v2/{tenant_id}",
    "network": "https://networking.tyo1.conoha.io/v2.0"
  }
}
```

* エンドポイントの設定等をとりあえずここに入れておく
* ConoHa のコンソール画面に表示されているものから手で作成する
* `identity`, `compute`, `network` の３つが必要
* バージョンのパスまで含める

### `~/.conoha/credential.json`

```json
{
  "user_name": "{user_name}",
  "password": "{password}",
  "tenant_id": "{tenant_id}"
}
```

* 設定が無ければプロンプトで入力を求める

### `~/.conoha/token.json`

```json
{
  "id": "{token_id}",
  "expires": "2099-09-19T09:09:09Z"
}
```

* `conoha auth login` マンド実行時に自動で作成
* `expires` は今のところ使ってない

## login

`token.json` が存在しない、またはトークンの有効期限が切れている場合、認証に失敗する。

次のコマンドで `token.json` を再作成することが出来る。

```sh
conoha auth login
```

## flavor 名について

* `g-cXmYdZ`
  * 例: `g-c2m1d100`
* `g-Xgb`
  * 例: `g-2gb`

上記の両パターンがある。

`g-cXmYdZ` の方は新プランのやつで、`X` はコア数、`Y` はメモリサイズ（GB）、`Z` はストレージサイズ（GB）を表していると思われる。

`g-Xgb` の方は旧プランのやつで、`X` はメモリーのサイズ（GB）を表していると思われる。


## jq

レスポンスが JSON 形式なので jq コマンドを活用する。

Windows OS の場合 Windows 版の jq コマンドを導入しても良いが、wsl があればそれでも良い。

### 基本

```sh
# 通常時
jq < hoge.json

# wsl 使用時はエイリアスを設定すると良い
alias jq='wsl jq'

# ダブルクオート無しで結果を表示する
jq -w < hoge.json
```

### 特定フィールドの絞り込み

```sh
# id のみ
conoha flavor list | jq -r .flavors[].id

# id, name の順に交互に表示
conoha flavor list | jq -r '.flavors[] | .id, .name'

# [id, name] の形式で表示
conoha flavor list | jq -r '.flavors[] | [.id, .name]'

# {"id": id, "name": name} の形式で表示
conoha flavor list | jq -r '.flavors[] | {id, name}'
```

### 条件で絞り込み

```sh
# name の完全一致
conoha flavor list | jq -r '.flavors[] | select(.name == "g-4gb") | .id, .name'

# 正規表現
conoha flavor list | jq -r '.flavors[] | select(.name | test("512")) | .id, .name'
```

## server create

サーバーの作成には `image_ref` と `flavor_ref` の二つが必要になる。
この二つは

```sh
conoha image search KEYWORD
conoha flavor search KEYWORD
```

で調べることが出来る。

ここでは

* イメージ: ubuntu 20.04
* プラン: メモリ512MB

のものを探してみる。

```sh
# vmi-ubuntu-20.04 を名前に含む image を抽出
# ※ ubuntu-20.04 だけだと ubuntu-20.04 ベースの色々なイメージも引っかかるので vmi を先頭に付ける
conoha image search vmi-ubuntu-20.04

# m512 を名前に含む flavor を抽出
conoha flavor search m512
```

* image name: vmi-ubuntu-20.04.02-amd64-30gb
* flavor name: g-c1m512d30

この二つが求めているものだろう。

早速サーバーを立ち上げてみる。

```sh
conoha server create \
  --image-ref '上で確認した image_id' \
  --flavor-ref '上で確認した flavor_id' \
  --instance-name-tag '分かりやすい名前を付ける'
```

コマンドのレスポンスに `adminPass` が含まれるので、忘れないようにメモする（ログイン後変更すべし！）。

## network

プライベートネットワークのみを取得したい場合、`shared` が `false` なものを選ぶと良い。

```sh
conoha network list | jq '.networks[] | select(.shared == false)'
```

* ネットワークは作成したままだと、ConoHa コンソール上で表示されないみたいなので、サブネットを作成する必要がある
* サブネットは一つのネットワークにつき１つまでしか設定できない
* プライベートネットワークは１つのアカウントにつき 10 個まで作成できる
* ConoHa コンソール上で表示されるのはサブネットの方の ID なので注意


## port

```sh
conoha port list | jq ".ports[] | select(.device_id == \"$server_id\")"
```

`conoha port list` で表示される `device_id` は `server_id` のこと。

## ネームタグからサーバーを探す

`conoha server list` コマンドに詳細を表示するオプション `-d` を追加した。

```sh
conoha server list -d | jq '.servers[] | select(.metadata | .instance_name_tag == "my_server")'
```

このようにすることで、サーバーの情報をネームタグから取得することが可能。

## 削除ロック

WebUI から削除ロックを掛けた場合 `.metadata | .IsDeleteLocked` の値が `"True"` となる。
しかし、別にシステム的に削除がロックされているわけじゃないので、API 経由なら普通に削除できてしまう。

conoha-cli ではこの値をチェックして `"True"` であれば削除しないようにする。
一方で、`--force` オプションで削除を強行することもできるようにしている。
