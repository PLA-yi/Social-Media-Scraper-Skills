# Social Media Scraper Skills

AI Agent Skills for the [Social Media Scraper](https://github.com/PLA-yi/social-media-scraper) project.

Each skill is a self-contained folder with two files:
- **`prompt.md`** — instructions for the AI agent (parameter parsing rules, how to call the script)
- **`run.py`** — standalone Python script that calls the local scraper server API

---

## Prerequisites

1. Clone and start the [Social Media Scraper](https://github.com/PLA-yi/social-media-scraper) server:
   ```bash
   git clone https://github.com/PLA-yi/social-media-scraper
   cd social-media-scraper
   python3 server.py
   ```
2. Server must be running at `http://localhost:8000` before executing any skill.

---

## Skills

| Skill 文件夹 | 功能 | 平台 |
|-------------|------|------|
| `scrape-douyin-keyword` | 关键词搜索采集视频和评论 | 抖音 |
| `scrape-douyin-blogger` | 博主主页作品采集 | 抖音 |
| `scrape-tiktok-keyword` | 关键词搜索采集视频和评论 | TikTok |
| `scrape-tiktok-blogger` | 创作者主页作品采集 | TikTok |
| `scrape-reddit` | 关键词搜索 / subreddit 采集 | Reddit |
| `scrape-youtube` | 关键词搜索 / 频道采集 | YouTube |
| `scrape-x` | 关键词搜索 / 用户主页采集 | X（推特） |

---

## Usage

### Run directly
```bash
python3 scrape-douyin-keyword/run.py --keyword "新能源汽车" --count 20 --mode fast
python3 scrape-tiktok-keyword/run.py --keyword "Claude AI" --count 20 --mode safe
python3 scrape-douyin-blogger/run.py --url "https://v.douyin.com/xxxxx" --count 30
python3 scrape-tiktok-blogger/run.py --url "https://www.tiktok.com/@username" --count 20
python3 scrape-reddit/run.py --target "AI tools" --mode keyword --count 20
python3 scrape-youtube/run.py --target "https://www.youtube.com/@channel" --mode blogger --count 10
python3 scrape-x/run.py --target "Anthropic Claude" --mode keyword --count 50
```

### As Agent Skills
Point your AI agent to a skill folder. The agent reads `prompt.md` for instructions, extracts parameters from user input, then executes `run.py`.

---

## Parameters

### Douyin / TikTok Keyword
| Parameter | Default | Description |
|-----------|---------|-------------|
| `--keyword` | required | 搜索关键词 |
| `--count` | 20 | 采集视频数量 |
| `--mode` | `safe` | `safe` 顺序采集 / `fast` 3路并发（约3倍速） |
| `--sort` | `0` | `0` 默认推荐 / `1` 最新发布 / `2` 最多点赞 |
| `--time_filter` | `0` | 时间限制（小时），`0` 不限 |

### Douyin / TikTok Blogger
| Parameter | Default | Description |
|-----------|---------|-------------|
| `--url` | required | 主页链接（支持短链） |
| `--count` | 20 | 采集视频数量 |

### Reddit / YouTube / X
| Parameter | Default | Description |
|-----------|---------|-------------|
| `--target` | required | 关键词或主页/频道链接 |
| `--mode` | `keyword` | `keyword` 搜索 / `blogger` 主页采集 |
| `--count` | 20 | 采集数量 |

---

## Auth Notes

| Platform | Auth Method |
|----------|-------------|
| 抖音 / TikTok | 首次运行时浏览器自动弹出，手动登录后 Cookie 自动保存 |
| Reddit / X | 需提前用 [Cookie-Editor](https://cookie-editor.com) 导出登录 Cookie 保存为 `data/cookies.json` |
| YouTube | 无需登录 |

---

## Related

- Main project: [PLA-yi/social-media-scraper](https://github.com/PLA-yi/social-media-scraper)
