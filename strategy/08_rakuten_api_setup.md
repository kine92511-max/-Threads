# 楽天ウェブサービスAPI セットアップ手順(商品検索の自動化)

楽天市場の商品検索を毎回Web検索で行う代わりに、**楽天公式の商品検索API(IchibaItem Search API)**を使うと、
商品名・価格・在庫・商品ページURLを正確に取得でき、**アフィリエイトIDを指定すればアフィリエイトリンク付きで結果が返ってくる**
(`07_affiliate_link_setup.md`の手動リンク変換作業が不要になる)。

この作業は楽天アカウントでの登録が必要なため、あなた自身が行う。取得した値を渡してもらえれば、
`scripts/search_rakuten_items.py`で自動検索するスクリプトを用意する。

## 1. 楽天Developersでアプリを登録し、アプリID(applicationId)を取得

1. [楽天ウェブサービス](https://webservice.rakuten.co.jp/) にアクセスし、楽天IDでログイン
2. 「アプリID発行」に進む
3. アプリ名(何でもよい。例:papa_rakuiku_search)、URL(個人利用なら任意のURLでよい。例:ThreadsのプロフィールURL)、用途などを入力
4. **審査なし・即時発行**でアプリID(`applicationId`)が発行される

## 2. アフィリエイトID(affiliateId)を確認する(`07_affiliate_link_setup.md`の登録が前提)

1. 楽天アフィリエイトの管理画面にログイン
2. マイページ内の「アフィリエイトID確認」等のメニューを開く(過去に発行したリンクのURL中にも`affiliateId`が含まれている)
3. 表示されているIDをコピーする

- affiliateIdは省略可能(なくても商品検索はできる)。ただし**指定するとAPIレスポンスに直接アフィリエイトリンクが含まれる**ため、指定を推奨する

## 3. 俺に渡すもの

以下2つを`.env`ファイル(gitignore済み、Threads APIのトークンと同じファイルに追記でよい)に追加してください:

```
RAKUTEN_APP_ID=取得したアプリID
RAKUTEN_AFFILIATE_ID=取得したアフィリエイトID(省略可)
```

## 4. 実行方法

```
python3 scripts/search_rakuten_items.py
```

`strategy/_pipeline/affiliate_week_briefs.md`の14枠に対応するキーワードで検索し、
結果(商品名・価格・レビュー数・商品URL・アフィリエイトURL)を`data/rakuten_products/`に保存する。

## 利用制限

- 楽天APIは1秒あたり1リクエストまでの制限がある(スクリプト側で自動的に間隔を空けて対応済み)
- 取得できる情報は検索時点のものなので、価格・在庫は投稿直前に再確認するとより安全

## 参考ソース

- [Pythonで楽天APIを使った商品情報取得・アフィリエイトリンク作成ガイド](https://note.com/guda_24/n/n7167c04f3326)
- [楽天市場APIで商品情報を取得する方法【楽天Developers完全ガイド】](https://api-zukan.com/blog/rakuten-api-guide)
