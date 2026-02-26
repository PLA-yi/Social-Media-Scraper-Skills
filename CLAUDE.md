# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A collection of AI Agent Skills for the [Social Media Scraper](https://github.com/PLA-yi/social-media-scraper) project. Each skill is a self-contained folder that triggers a scrape job on a locally running FastAPI server (`http://localhost:8000`).

## Skill Structure

Every skill folder follows the same two-file pattern:

```
scrape-{platform}-{mode}/
├── prompt.md   ← parameter extraction rules + CLI command template for the AI agent
└── run.py      ← standalone Python script; calls POST /api/scrape, no external deps
```

`run.py` files use only stdlib (`argparse`, `json`, `urllib.request`) — no pip installs needed.

## Adding a New Skill

1. Create a new folder: `scrape-{platform}-{mode}/`
2. Write `prompt.md` following the existing pattern:
   - Parameter extraction rules (what user phrases map to which flags)
   - The exact CLI command template
   - A "完成后" section telling the agent what to report back
3. Write `run.py`:
   - Use `check_server()` at the top (copy from any existing skill)
   - Build the JSON payload matching the `/api/scrape` schema (see below)
   - Print `✅`, `📋`, `📁` status lines at the end
4. Add an entry to the Skills table in both `README.md` and `README.zh-CN.md`

## `/api/scrape` Payload Schema

```python
{
    "platform":     "douyin" | "tiktok" | "reddit" | "youtube" | "x",
    "target":       str,          # keyword or URL
    "mode":         "keyword" | "blogger",
    "count":        int,          # default 20
    "scrape_mode":  "safe" | "fast",   # douyin/tiktok keyword only
    "sort_by":      "0" | "1" | "2",   # 0=default 1=latest 2=top; douyin/tiktok only
    "time_filter":  int,          # hours, 0=no limit; douyin/tiktok only
}
```

Fields `scrape_mode`, `sort_by`, `time_filter` are ignored by reddit/youtube/x — safe to include or omit.

## Server Dependency

All `run.py` scripts call `check_server()` before doing anything. If `http://localhost:8000` is unreachable the script exits with a clear message. The server is started from the main project:

```bash
cd /path/to/social-media-scraper
python3 server.py
```

## Modifying prompt.md

The AI agent reads `prompt.md` verbatim. Keep the three sections intact:
- **参数提取规则** — natural language → CLI flag mappings
- **执行命令** — the literal command template (must match `run.py` flags exactly)
- **完成后** — what to tell the user after submitting the job
