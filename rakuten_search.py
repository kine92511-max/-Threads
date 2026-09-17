"""Rakuten Ichiba Item Search API client.

Credentials are read from environment variables only (see .env.example):
  RAKUTEN_APPLICATION_ID, RAKUTEN_ACCESS_KEY, RAKUTEN_AFFILIATE_ID (optional),
  RAKUTEN_REFERER (must match the app's registered "許可されたWebサイト" domain).
"""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260701"


def search_items(keyword: str, hits: int = 5) -> dict:
    application_id = os.environ.get("RAKUTEN_APPLICATION_ID")
    access_key = os.environ.get("RAKUTEN_ACCESS_KEY")
    affiliate_id = os.environ.get("RAKUTEN_AFFILIATE_ID")
    referer = os.environ.get("RAKUTEN_REFERER")

    if not application_id or not access_key:
        raise RuntimeError(
            "RAKUTEN_APPLICATION_ID / RAKUTEN_ACCESS_KEY が環境変数に設定されていません。"
            ".env を用意するか、環境変数を export してください。"
        )

    params = {
        "format": "json",
        "keyword": keyword,
        "genreId": 0,
        "hits": hits,
        "applicationId": application_id,
        "accessKey": access_key,
    }
    if affiliate_id:
        params["affiliateId"] = affiliate_id

    headers = {}
    if referer:
        headers["Referer"] = referer

    response = requests.get(API_URL, params=params, headers=headers, timeout=15)
    return {
        "status_code": response.status_code,
        "body": _safe_json(response),
    }


def _safe_json(response: requests.Response):
    try:
        return response.json()
    except ValueError:
        return {"raw_text": response.text[:500]}


def print_report(keyword: str, hits: int) -> None:
    result = search_items(keyword, hits)
    status = result["status_code"]
    body = result["body"]

    if status != 200 or "Items" not in body:
        print(f"[FAILED] HTTP {status}")
        print(body)
        return

    items = body["Items"]
    print(f"[OK] HTTP {status} - {len(items)} 件取得")
    for entry in items:
        item = entry["Item"]
        print("-" * 40)
        print("商品名:", item.get("itemName"))
        print("価格:", item.get("itemPrice"))
        print("レビュー件数:", item.get("reviewCount"))
        print("レビュー平均:", item.get("reviewAverage"))
        print("affiliateUrl:", item.get("affiliateUrl") or "(なし)")


if __name__ == "__main__":
    keyword_arg = sys.argv[1] if len(sys.argv) > 1 else "補助便座"
    hits_arg = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    print_report(keyword_arg, hits_arg)
