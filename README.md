# -Threads

育児系アフィリエイトThreadsアカウントの運用プロジェクト。

## ペルソナ・戦略

- [strategy/01_persona.md](strategy/01_persona.md) — アカウントのペルソナ、家事・育児の分担、生活スケジュール、住まいの情報
- [strategy/02_concept_tone_ratio.md](strategy/02_concept_tone_ratio.md) — コンセプト・トーン・コンテンツ比率(バズる設計、リサーチ根拠付き)
- [strategy/03_content_calendar.md](strategy/03_content_calendar.md) — 投稿カレンダー(1日5投稿・固定時間帯:7/10/12/17/21時、10時と17時がアフィリエイト枠)
- [strategy/04_post_templates.md](strategy/04_post_templates.md) — 投稿テンプレート(バズる型のリサーチ根拠付き)
- [strategy/05_reply_guidelines.md](strategy/05_reply_guidelines.md) — リプライ対応ガイドライン(会話を伸ばす返信の型)

上記5ファイルの内容は、`knowledge/`・`planning/`配下に**参照用コピー**として整理し直したものもあります(下記「ナレッジ・企画の参照用フォルダ」を参照)。元ファイルは削除・変更していません。

## ナレッジ・企画の参照用フォルダ(`knowledge/` / `planning/` / `docs/setup/`)

`strategy/`配下の内容を、用途別に参照しやすく再編集した**コピー**です。実際にエージェントが読むルールは
引き続き`.claude/agents/`配下のファイルであり、以下は人間が全体像を把握するための参照用です。

- [knowledge/account.md](knowledge/account.md) — アカウントペルソナ・コンセプト(`strategy/01`・`02`の一部のコピー)
- [knowledge/audience.md](knowledge/audience.md) — 読者(ターゲット)情報。既存資料から確認できる範囲のみ記載し、不明点は「未確認」と明記
- [knowledge/writing-style.md](knowledge/writing-style.md) — 表記ルール・トーン・投稿テンプレート集約(ルート`CLAUDE.md`・`strategy/02`・`04`のコピー)
- [knowledge/reply-guidelines.md](knowledge/reply-guidelines.md) — リプライ対応ガイドライン(`strategy/05`のコピー)
- `knowledge/products/TEMPLATE.md` — 商品情報を記録するテンプレート(雛形のみ。実データは未投入)
- [planning/content-calendar.md](planning/content-calendar.md) — 投稿カレンダー(`strategy/02`・`03`のコピー)
- `planning/ideas.md` — ネタストック(現時点では空)
- [docs/setup/threads-api.md](docs/setup/threads-api.md) — Threads APIセットアップ手順(`strategy/06`のコピー)
- [docs/setup/affiliate-link.md](docs/setup/affiliate-link.md) — 楽天アフィリエイトリンク取得手順(`strategy/07`のコピー)
- [docs/setup/rakuten-api.md](docs/setup/rakuten-api.md) — 楽天商品検索APIセットアップ手順(`strategy/08`のコピー)

## プロジェクト全体ルール

- [CLAUDE.md](CLAUDE.md) — パイプライン全体像、全投稿共通の表記ルール、アフィリエイト投稿の構成ルール、事実確認の方針、過去の失敗事例をまとめたルートルールファイル

## 専門エージェント(`.claude/agents/`)

投稿を作るまでの工程を5つの役割に分け、それぞれ専属のエージェントとして定義している。各エージェントは
`<エージェント名>.md`(日本語名、フロントマター+役割の要約+ルール参照の指示)と、対応するフォルダ内の`CLAUDE.md`
(そのエージェント専用の詳細ルール)の2ファイルで構成される。エージェント本体は起動時に両方の`CLAUDE.md`
(自分の専用ルール、およびルート直下のプロジェクト全体ルール)を読んでから作業する。フォルダ名は英数字にしてある
(GitHubモバイルアプリで日本語名のフォルダを開くとエラーになる不具合の回避のため。エージェント定義ファイル自体
`<エージェント名>.md`とその`name`フロントマターは日本語のままで、Agentツールでの呼び出しには影響しない)。

1. [リサーチ担当](.claude/agents/リサーチ担当.md)([詳細ルール](.claude/agents/research/CLAUDE.md)) — テーマ・読者リサーチ担当(**SNS優先**: Threads/X/Instagramを`site:`検索で調べ、悩み/共感・本音/関心・話題に分類する。SNSで見つからない場合のみ一般Web検索にフォールバック)
2. [構成担当](.claude/agents/構成担当.md)([詳細ルール](.claude/agents/structure/CLAUDE.md)) — 投稿の構成担当(アフィリエイト型は悩み→商品の論理チェックも担当)
3. [共感ライター](.claude/agents/共感ライター.md)([詳細ルール](.claude/agents/empathy-writer/CLAUDE.md)) — 共感・有益情報系の投稿執筆担当
4. [アフィリエイトライター](.claude/agents/アフィリエイトライター.md)([詳細ルール](.claude/agents/affiliate-writer/CLAUDE.md)) — アフィリエイト系の投稿執筆担当
5. [校正担当](.claude/agents/校正担当.md)([詳細ルール](.claude/agents/proofread/CLAUDE.md)) — 校正担当(誤字脱字・法令リスクに加え、**事実確認(ファクトチェック)も担当**。年齢相応の発達描写か、商品特徴が商品ページの記載と一致しているか、悩みと商品が論理的につながっているかをWebSearch/WebFetchで確認し、根拠を残す)

### 基本フロー

```
リサーチ担当(リサーチ)
      ↓
構成担当(構成案作成・投稿タイプで振り分け)
      ↓                          ↓
共感ライター(共感/Tips/エッセイ)   アフィリエイトライター(商品紹介)
      ↓                          ↓
              校正担当(校正)
```

## 旧・初週試作ストック(過去の成果物、参考用)

`strategy/_pipeline/`にあった初週試作分(構成案・ドラフト・校正済み最終版、計10ファイル)は、
**担当した各エージェントフォルダ直下の`past-work/`フォルダに元のファイル名のまま移動済み**。
`strategy/_pipeline/`フォルダ自体は削除した。実投稿には使わず、
型の妥当性チェックの参考程度に留めること(過去の試作であり、現行のSNS優先リサーチ体制以前のもの)。

- リサーチ担当(`research/past-work/`) → 商品カテゴリのリサーチ・実商品候補
- 構成担当(`structure/past-work/`) → 初週/アフィリエイト固定枠の構成案
- 共感ライター(`empathy-writer/past-work/`) → 初週の共感/Tips系ドラフト
- アフィリエイトライター(`affiliate-writer/past-work/`) → アフィリエイト固定枠の本文ドラフト
- 校正担当(`proofread/past-work/`) → 校正済みの最終版

## アフィリエイトリンク・商品リサーチ

- [strategy/07_affiliate_link_setup.md](strategy/07_affiliate_link_setup.md) — 楽天アフィリエイトの登録・リンク発行手順(手動)
- [strategy/08_rakuten_api_setup.md](strategy/08_rakuten_api_setup.md) — 楽天ウェブサービスAPIのセットアップ手順(商品検索を自動化、アフィリエイトID指定でリンクも自動取得)
- `scripts/search_rakuten_items.py` — `.env`にAPI情報を設定して実行すると、14枠分の商品を自動検索し`data/rakuten_products/`に保存する

## インサイト分析(Threads API)

- [strategy/06_api_setup.md](strategy/06_api_setup.md) — アクセストークンの取得手順(要Meta Developer設定)
- `scripts/fetch_threads_insights.py` — `.env`にトークンを設定して実行すると、アカウント/投稿単位のインサイトを`data/insights/`に保存する
- `.env.example` をコピーして`.env`を作成し、`THREADS_ACCESS_TOKEN`・`THREADS_USER_ID`を設定する(`.env`はgit管理外)

## 補足(別ブランチから統合)

- `rakuten_search.py` — 楽天API接続テスト用スクリプト。**楽天のAPI仕様が2026年2月頃に変更されている**ことが判明済み(詳細は[strategy/08_rakuten_api_setup.md](strategy/08_rakuten_api_setup.md)末尾を参照)。サーバーサイドからの呼び出しが未解決の403エラーで失敗しており、楽天サポートに問い合わせ中。
- `content/` — 実際の投稿30件(2026年9月分)をスクリーンショットから全数書き起こし・検証したデータ(CSV/JSON)と、そこから抽出したテンプレート、日次の投稿ストック(`YYYY-MM-DD.md`)。旧初週試作(各エージェントフォルダの`past-work/`に移動済み)と合わせて、型の妥当性チェックに使える。

## 原稿の保存先【確定ルール】(`drafts/` / `outputs/` / `content/`)

**執筆後の下書きは`drafts/`に保存する。校正を経た原稿はユーザーに提示し、明示的な承認を得てから`outputs/`に保存する。`content/`は既存投稿・旧テンプレシステムの保管場所として維持し、今後の新規完成原稿の正式な保存先には使用しない。**

- `drafts/` — 執筆担当(共感ライター/アフィリエイトライター)の本文を、校正担当に渡す前に保存する場所(標準運用。ルート`CLAUDE.md`「原稿の保存先【確定ルール】」参照)
- `drafts/legacy/` — `content/2026-09-18.md`・`2026-09-19.md`のコピー。校正済みだが**ユーザー承認の記録が確認できていない**ため、各ファイル冒頭に「承認状況:不明(記録なし)」と明記している。本文は元ファイルから変更していない
- `outputs/` — **ユーザーが明示的に承認した完成原稿の正式な保存先**。承認済みの原稿がまだ無いため現時点では空
- `content/` — 既存投稿・旧テンプレシステムの保管場所。**新規の完成原稿は保存しない**(既存ファイルは削除・移動・書き換えをしない)
- `analytics/posts.csv` — 投稿実績記録用(現時点ではヘッダーのみ、データなし)
- `analytics/weekly-review.md`・`analytics/experiments.md` — 分析・検証記録用のテンプレート(現時点では見出しのみ)

## 日次投稿ストックの作り方(承認後は`outputs/YYYY-MM-DD.md`)

1. リサーチ担当 → 構成担当 → 共感ライター/アフィリエイトライター → 校正担当 の順で5本(7:00・10:00・12:00・17:00・21:00)を作成する。執筆後の下書きは`drafts/`に保存し、**ユーザーの明示的な承認を得てから`outputs/YYYY-MM-DD.md`に保存する**
2. **校正担当の校正時に必ずファクトチェックを行う**(発達段階の描写が年齢相応か、アフィリエイト商品の特徴が商品ページの実際の記載と一致しているか、悩みと商品が論理的につながっているか)
3. 各投稿の下に**「根拠(ファクトチェック)」欄を設け、確認した出典URLや商品ページの確認結果を残す**。創作・一般的なあるあるの範囲であることが分かっている場合はその旨明記する(書式の実例は`content/2026-09-18.md`および`drafts/legacy/2026-09-18.md`)
4. 過去の失敗事例(再発防止のため必ず確認する):
   - 「2歳児が全力疾走する」という不正確な発達描写(正しくは「よく転ぶ・小走り」)
   - 商品ページと異なる素材の誤記(シリコン製→実際はポリエステル/TPU)
   - 商品ページのSEOキーワード欄に釣られて、実際は子供向けでない商品を「2歳児向け」として紹介(セタフィル→ピジョンベビークリームに訂正)
   - 悩みと無関係な商品を当てるロジック破綻(「日陰がない/エアコンがない→暑い」にレジャーシートを当てて破綻→首かけ扇風機に訂正)
   - **具体的な事実主張・商品選定は必ず検索・商品ページ確認で裏付けを取り、悩みと商品のつながりを一段階ずつ確認する**こと
