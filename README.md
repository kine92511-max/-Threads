# -Threads

育児系アフィリエイトThreadsアカウントの運用プロジェクト。

## ペルソナ・戦略

- [strategy/01_persona.md](strategy/01_persona.md) — アカウントのペルソナ、家事・育児の分担、生活スケジュール、住まいの情報
- [strategy/02_concept_tone_ratio.md](strategy/02_concept_tone_ratio.md) — コンセプト・トーン・コンテンツ比率(バズる設計、リサーチ根拠付き)

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
