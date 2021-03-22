# ConoHa CLI

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

* 設定が無ければプロンプトで入力を求める

### `~/.conoha/token.json`

```json
{
  "id": "hogehgoefugafuga",
  "expires": "2099-09-19T09:09:09Z"
}
```

* `conoha auth login` マンド実行時に自動で作成

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

# wsl 使用時
wsl jq < hoge.json

# ダブルクオート無し
jq -w < hoge.json
```

### 特定フィールドの絞り込み

```sh
# id のみ
conoha flavor list | wsl jq -r .flavors[].id

# id, name の順に交互に表示
conoha flavor list | wsl jq -r '.flavors[] | .id, .name'

# [id, name] の形式で表示
conoha flavor list | wsl jq -r '.flavors[] | [.id, .name]'

# {"id": id, "name": name} の形式で表示
conoha flavor list | wsl jq -r '.flavors[] | {id, name}'
```

### 条件で絞り込み

```sh
# name の完全一致
conoha flavor list | wsl jq -r '.flavors[] | select(.name == "g-4gb") | .id, .name'

# 正規表現
conoha flavor list | wsl jq -r '.flavors[] | select(.name | test("512")) | .id, .name'
```
