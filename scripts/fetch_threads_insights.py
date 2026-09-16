#!/usr/bin/env python3
"""Threads APIからアカウント・投稿単位のインサイトを取得して保存する。

使い方:
    python3 scripts/fetch_threads_insights.py

必要な環境変数(.envまたはシェル環境):
    THREADS_ACCESS_TOKEN - 長期アクセストークン
    THREADS_USER_ID       - ThreadsユーザーID

strategy/06_api_setup.md の手順でトークンを取得してから実行する。
"""
import datetime
import json
import os
import sys
from pathlib import Path
from urllib import error, parse, request

GRAPH_BASE = "https://graph.threads.net/v1.0"
ACCOUNT_METRICS = ["views", "likes", "replies", "reposts", "quotes", "followers_count"]
MEDIA_METRICS = ["views", "likes", "replies", "reposts", "quotes"]
REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "data" / "insights"


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def get_json(url: str) -> dict:
    try:
        with request.urlopen(url) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"HTTPエラー {exc.code}: {body}", file=sys.stderr)
        raise


def fetch_account_insights(user_id: str, token: str) -> dict:
    params = {
        "metric": ",".join(ACCOUNT_METRICS),
        "period": "day",
        "since": (datetime.date.today() - datetime.timedelta(days=7)).isoformat(),
        "until": datetime.date.today().isoformat(),
        "access_token": token,
    }
    url = f"{GRAPH_BASE}/{user_id}/threads_insights?{parse.urlencode(params)}"
    return get_json(url)


def fetch_recent_media(user_id: str, token: str, limit: int = 25) -> dict:
    params = {
        "fields": "id,text,timestamp,permalink",
        "limit": limit,
        "access_token": token,
    }
    url = f"{GRAPH_BASE}/{user_id}/threads?{parse.urlencode(params)}"
    return get_json(url)


def fetch_media_insights(media_id: str, token: str) -> dict:
    params = {
        "metric": ",".join(MEDIA_METRICS),
        "access_token": token,
    }
    url = f"{GRAPH_BASE}/{media_id}/insights?{parse.urlencode(params)}"
    return get_json(url)


def main() -> None:
    load_env_file(REPO_ROOT / ".env")

    token = os.environ.get("THREADS_ACCESS_TOKEN")
    user_id = os.environ.get("THREADS_USER_ID")
    if not token or not user_id:
        print(
            "THREADS_ACCESS_TOKEN / THREADS_USER_ID が設定されていません。\n"
            "strategy/06_api_setup.md の手順でトークンを取得し、.envに設定してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    print("アカウントインサイトを取得中...")
    account_insights = fetch_account_insights(user_id, token)

    print("直近の投稿一覧を取得中...")
    recent_media = fetch_recent_media(user_id, token)

    media_with_insights = []
    for media in recent_media.get("data", []):
        media_id = media["id"]
        try:
            insights = fetch_media_insights(media_id, token)
        except error.HTTPError:
            insights = {"error": "insights取得失敗"}
        media_with_insights.append({**media, "insights": insights})

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    out_path = OUTPUT_DIR / f"{today}.json"
    out_path.write_text(
        json.dumps(
            {
                "fetched_at": datetime.datetime.now().isoformat(),
                "account_insights": account_insights,
                "media": media_with_insights,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"保存しました: {out_path}")


if __name__ == "__main__":
    main()
