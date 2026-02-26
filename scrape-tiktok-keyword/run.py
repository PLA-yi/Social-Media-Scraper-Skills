#!/usr/bin/env python3
"""TikTok 关键词爬取 — 调用本地 scraper 服务 API"""

import argparse
import json
import sys
import urllib.request

SERVER = "http://localhost:8000"


def check_server():
    try:
        urllib.request.urlopen(SERVER, timeout=3)
        return True
    except Exception:
        return False


def start_scrape(keyword, count, mode, sort_by, time_filter):
    payload = json.dumps({
        "platform": "tiktok",
        "target": keyword,
        "mode": "keyword",
        "count": count,
        "scrape_mode": mode,
        "sort_by": str(sort_by),
        "time_filter": time_filter,
    }).encode()

    req = urllib.request.Request(
        f"{SERVER}/api/scrape",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())


def main():
    parser = argparse.ArgumentParser(description="TikTok 关键词爬取")
    parser.add_argument("--keyword", required=True, help="搜索关键词")
    parser.add_argument("--count", type=int, default=20, help="采集视频数量")
    parser.add_argument("--mode", choices=["safe", "fast"], default="safe", help="爬取模式")
    parser.add_argument("--sort", choices=["0", "1", "2"], default="0",
                        help="排序：0=默认推荐 1=最新发布 2=最多点赞")
    parser.add_argument("--time_filter", type=int, default=0,
                        help="时间限制（小时），0=不限")
    args = parser.parse_args()

    if not check_server():
        print("❌ 服务未启动，请先在项目目录执行：python3 server.py")
        sys.exit(1)

    print(f"▶ TikTok 关键词爬取")
    print(f"  关键词：{args.keyword}")
    print(f"  数量：{args.count}  模式：{args.mode}  排序：{args.sort}  时间限制：{args.time_filter}h")

    result = start_scrape(args.keyword, args.count, args.mode, args.sort, args.time_filter)
    print(f"✅ 任务已提交：{result}")
    print(f"📋 实时日志：{SERVER}")
    print(f"📁 数据目录：<项目路径>/data/")


if __name__ == "__main__":
    main()
