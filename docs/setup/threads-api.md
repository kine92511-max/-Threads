# Threads API セットアップ手順(インサイト自動取得用)

このファイルは`strategy/06_api_setup.md`のコピーです。元ファイルは削除・変更していません。

---

@papa_rakuiku のインサイト(インプレッション・いいね・リプライ数など)を自動取得するための、
Meta公式「Threads API」を使ったセットアップ手順。**この作業はMetaアカウントへのログインが必要なため、あなた自身が行う必要がある。**
トークンを取得したら俺に渡してもらえれば、`scripts/fetch_threads_insights.py`で自動分析する。

## 前提条件

- Facebookアカウント(個人アカウント)
- @papa_rakuiku のThreadsアカウントが、Facebookアカウントと連携済みであること
- Threadsアカウントが**プロフェッショナルアカウント(クリエイター/ビジネス)**になっていること(個人アカウントのままだとインサイトAPIが使えない可能性がある。Threadsアプリの設定から切り替え可能)

## 手順

### 1. Meta for Developersでアプリを作成

1. https://developers.facebook.com/ にFacebookアカウントでログイン
2. 「アプリを作成」→ ユースケースは**「Threads APIにアクセス」**を選択
3. アプリ名を適当に設定(例:papa_rakuiku_insights)して作成

### 2. Threadsテスターとして自分のアカウントを追加

1. 作成したアプリのダッシュボードで「Threads API」の設定画面を開く
2. 「Threadsテスター」に自分の@papa_rakuikuアカウントを追加
3. Threadsアプリ側(スマホ)で、テスター招待の承認を行う(設定 > アプリとWebサイトの通知、またはメールで届く招待を承認)

### 3. アクセストークン(短期)を取得

1. Meta の Graph API Explorer(https://developers.facebook.com/tools/explorer/)を開く
2. 接続先を「graph.facebook.com」から「graph.threads.net」に切り替える
3. 作成したアプリを選択し、「Generate Threads Access Token」をクリック
4. スコープ(権限)として以下を選択:
   - `threads_basic`
   - `threads_manage_insights`
5. Threadsアカウントでログインして許可すると、**短期アクセストークン(有効期限1時間)**が発行される

### 4. 長期トークン(60日間有効)に交換

短期トークンのままだとすぐ切れるため、長期トークンに交換する。ブラウザで以下のURLにアクセス(値は自分のものに置き換える):

```
https://graph.threads.net/access_token
  ?grant_type=th_exchange_token
  &client_secret=<アプリのシークレット>
  &access_token=<短期トークン>
```

レスポンスで返ってくる `access_token` が60日間有効な長期トークン。

- アプリID・アプリシークレットは、Meta for Developersのアプリダッシュボード「設定 > ベーシック」から確認できる

### 5. Threadsユーザー(アカウント)IDを確認

以下にアクセスすると自分のThreadsユーザーIDが分かる:

```
https://graph.threads.net/v1.0/me?fields=id,username&access_token=<長期トークン>
```

### 6. 俺に渡すもの

以下2つを、**このリポジトリには直接書き込まず**、`.env`ファイル(gitignore済み)として渡してください:

```
THREADS_ACCESS_TOKEN=取得した長期トークン
THREADS_USER_ID=取得したユーザーID
```

`.env.example`を参考に、リポジトリのルートに`.env`を作成して値を貼り付けてもらえれば、俺が`scripts/fetch_threads_insights.py`を実行して分析する。

## トークンの有効期限に関する注意

- 長期トークンは60日で失効する。期限が切れる前に**リフレッシュ**が必要:
  ```
  https://graph.threads.net/refresh_access_token
    ?grant_type=th_refresh_token
    &access_token=<現在の長期トークン>
  ```
- 60日ごとにこの手順でトークンを更新する運用が必要(忘れると再度手順3からやり直しになる)

## 参考ソース

- [Threads APIの登録方法:アクセストークン(短期トークン)の発行方法](https://wporz.com/threads-api-regist/)
- [【2026年5月版】Threads APIのアクセストークン取得手順を解説!](https://note.com/kazu_t/n/n6d1df495dde8)
- [Threads APIの取得方法を解説!初心者でも分かるステップバイステップガイド](https://note.com/hottarita/n/nb82e3a0afe35)

---

## 出典

`strategy/06_api_setup.md` 全文(文言の変更なし)
