#!/usr/bin/env python3
"""楽天市場商品検索API(IchibaItem Search)で、アフィリエイト14枠分の商品を検索する。

使い方:
    python3 scripts/search_rakuten_items.py

必要な環境変数(.envまたはシェル環境):
    RAKUTEN_APP_ID        - 楽天Developersで発行したアプリID(必須)
    RAKUTEN_AFFILIATE_ID  - 楽天アフィリエイトID(任意。指定するとアフィリエイトURLが取得できる)

docs/setup/rakuten-api.md(strategy/08_rakuten_api_setup.md のコピー)の手順でIDを取得してから実行する。
"""
import datetime
import json
import os
import sys
import time
from pathlib import Path
from urllib import error, parse, request

API_URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
REQUEST_INTERVAL_SEC = 1.1  # 楽天APIのレート制限(1秒1リクエスト)対策
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "data" / "rakuten_products"

# 旧アフィリエイト固定枠14枠分の構成案(現在は.claude/agents/structure/past-work/affiliate_week_briefs.mdに移動済み)の14枠に対応する検索キーワード
SLOTS = [
    ("Day1・10:00", "工事不要 食洗機 据え置き"),
    ("Day1・17:00", "ヒップシート 抱っこ紐"),
    ("Day2・10:00", "おもちゃ収納 ラック 高さ調整"),
    ("Day2・17:00", "幼児食 パウチ 冷凍"),
    ("Day3・10:00", "スリーパー ベビー 着る布団"),
    ("Day3・17:00", "バランスバイク 三輪車 キッズ"),
    ("Day4・10:00", "お風呂おもちゃ セット 収納ケース付き"),
    ("Day4・17:00", "ミールキット 宅配"),
    ("Day5・10:00", "防災グッズ 子供 備蓄セット"),
    ("Day5・17:00", "知育玩具 ブロック 型はめ"),
    ("Day6・10:00", "加湿空気清浄機 チャイルドロック"),
    ("Day6・17:00", "レインコート キッズ 長靴"),
    ("Day7・10:00", "トイトレ 補助便座 3in1"),
    ("Day7・17:00", "写真 動画 管理 フォトフレーム 家族"),
]


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def search_items(keyword: str, app_id: str, affiliate_id: str | None, hits: int = 5) -> dict:
    params = {
        "applicationId": app_id,
        "keyword": keyword,
        "hits": hits,
        "sort": "-reviewCount",
        "format": "json",
    }
    if affiliate_id:
        params["affiliateId"] = affiliate_id
    url = f"{API_URL}?{parse.urlencode(params)}"
    try:
        with request.urlopen(url) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"  HTTPエラー {exc.code}: {body}", file=sys.stderr)
        return {"error": body}


def main() -> None:
    load_env_file(REPO_ROOT / ".env")

    app_id = os.environ.get("RAKUTEN_APP_ID")
    affiliate_id = os.environ.get("RAKUTEN_AFFILIATE_ID")
    if not app_id:
        print(
            "RAKUTEN_APP_ID が設定されていません。\n"
            "docs/setup/rakuten-api.md(strategy/08_rakuten_api_setup.md のコピー)の手順でアプリIDを取得し、.envに設定してください。",
            file=sys.stderr,
        )
        sys.exit(1)
    if not affiliate_id:
        print("RAKUTEN_AFFILIATE_ID未設定。アフィリエイトURLなしの結果になります。", file=sys.stderr)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for label, keyword in SLOTS:
        print(f"検索中: {label} ({keyword})")
        data = search_items(keyword, app_id, affiliate_id)
        items = []
        for entry in data.get("Items", []):
            item = entry.get("Item", entry)
            items.append(
                {
                    "itemName": item.get("itemName"),
                    "itemPrice": item.get("itemPrice"),
                    "shopName": item.get("shopName"),
                    "reviewCount": item.get("reviewCount"),
                    "itemUrl": item.get("itemUrl"),
                    "affiliateUrl": item.get("affiliateUrl"),
                }
            )
        results.append({"slot": label, "keyword": keyword, "items": items})
        time.sleep(REQUEST_INTERVAL_SEC)

    today = datetime.date.today().isoformat()
    out_path = OUTPUT_DIR / f"{today}.json"
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"保存しました: {out_path}")


if __name__ == "__main__":
    main()
