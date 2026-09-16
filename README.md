# -Threads

育児系アフィリエイトThreadsアカウントの運用プロジェクト。

## ペルソナ・戦略

- [strategy/01_persona.md](strategy/01_persona.md) — アカウントのペルソナ、家事・育児の分担、生活スケジュール、住まいの情報
- [strategy/02_concept_tone_ratio.md](strategy/02_concept_tone_ratio.md) — コンセプト・トーン・コンテンツ比率(バズる設計、リサーチ根拠付き)
- [strategy/03_content_calendar.md](strategy/03_content_calendar.md) — 投稿カレンダー(1日5投稿・固定時間帯:7/10/12/17/21時、10時と17時がアフィリエイト枠)
- [strategy/04_post_templates.md](strategy/04_post_templates.md) — 投稿テンプレート(バズる型のリサーチ根拠付き)
- [strategy/05_reply_guidelines.md](strategy/05_reply_guidelines.md) — リプライ対応ガイドライン(会話を伸ばす返信の型)

## 専門エージェント(`.claude/agents/`)

投稿を作るまでの工程を5つの役割に分け、それぞれ専属のエージェントとして定義している。

1. [research-analyst](.claude/agents/research-analyst.md) — テーマ・読者リサーチ担当
2. [content-structurer](.claude/agents/content-structurer.md) — 投稿の構成担当
3. [empathy-writer](.claude/agents/empathy-writer.md) — 共感・有益情報系の投稿執筆担当
4. [affiliate-writer](.claude/agents/affiliate-writer.md) — アフィリエイト系の投稿執筆担当
5. [proofreader](.claude/agents/proofreader.md) — 校正担当

### 基本フロー

```
research-analyst(リサーチ)
      ↓
content-structurer(構成案作成・投稿タイプで振り分け)
      ↓                              ↓
empathy-writer(共感/Tips/エッセイ)   affiliate-writer(商品紹介)
      ↓                              ↓
                proofreader(校正)
```

## 投稿ストック(`strategy/_pipeline/`)

### 初週の基本枠(7:00/12:00/21:00相当、17本)

- [week1_briefs.md](strategy/_pipeline/week1_briefs.md) — content-structurerによる構成案
- [week1_drafts_empathy.md](strategy/_pipeline/week1_drafts_empathy.md) — empathy-writerによる本文(17本)
- [week1_drafts_affiliate.md](strategy/_pipeline/week1_drafts_affiliate.md) — 旧アフィリエイト2本を有益・共感系に書き直したもの
- **[week1_final.md](strategy/_pipeline/week1_final.md) — proofreader校正済みの最終版**

### アフィリエイト固定枠(10:00/17:00、全14本)

- [affiliate_research.md](strategy/_pipeline/affiliate_research.md) — research-analystによる商品カテゴリのリサーチ(15カテゴリ)
- [affiliate_week_briefs.md](strategy/_pipeline/affiliate_week_briefs.md) — content-structurerによる構成案
- [affiliate_week_drafts.md](strategy/_pipeline/affiliate_week_drafts.md) — affiliate-writerによる本文
- **[affiliate_week_final.md](strategy/_pipeline/affiliate_week_final.md) — proofreader校正済みの最終版(コピペ用はこれを使う。リプ欄用のPR付き案内文もセットで記載)**

`week1_final.md`(7:00/12:00/21:00枠)と`affiliate_week_final.md`(10:00/17:00枠)を組み合わせると、1日5投稿×7日分のストックが揃う。

## インサイト分析(Threads API)

- [strategy/06_api_setup.md](strategy/06_api_setup.md) — アクセストークンの取得手順(要Meta Developer設定)
- `scripts/fetch_threads_insights.py` — `.env`にトークンを設定して実行すると、アカウント/投稿単位のインサイトを`data/insights/`に保存する
- `.env.example` をコピーして`.env`を作成し、`THREADS_ACCESS_TOKEN`・`THREADS_USER_ID`を設定する(`.env`はgit管理外)
