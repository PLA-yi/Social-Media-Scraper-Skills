#!/usr/bin/env python3
"""抖音博主主页爬取 — 调用本地 scraper 服务 API"""

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


def main():
    parser = argparse.ArgumentParser(description="抖音博主主页爬取")
    parser.add_argument("--url", required=True, help="博主主页链接（支持短链）")
    parser.add_argument("--count", type=int, default=20, help="采集视频数量")
    args = parser.parse_args()

    if not check_server():
        print("❌ 服务未启动，请先在项目目录执行：python3 server.py")
        sys.exit(1)

    print(f"▶ 抖音博主主页爬取")
    print(f"  链接：{args.url}  数量：{args.count}")

    payload = json.dumps({
        "platform": "douyin",
        "target": args.url,
        "mode": "blogger",
        "count": args.count,
    }).encode()

    req = urllib.request.Request(
        f"{SERVER}/api/scrape",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        result = json.loads(resp.read())

    print(f"✅ 任务已提交：{result}")
    print(f"📋 实时日志：{SERVER}")


if __name__ == "__main__":
    main()
