# Skill: YouTube 爬取

从用户输入中提取目标和数量，然后运行 run.py 采集 YouTube 评论数据。

## 参数提取规则
- 若输入包含 youtube.com 或 youtu.be → url，mode=blogger（采集频道）
- 否则 → keyword，mode=keyword（关键词搜索）
- 数字 → count（默认 10）

## 执行命令
```
python3 run.py --target "<关键词或频道链接>" --mode <keyword|blogger> --count <数量>
```

## 前置条件
需要系统安装 yt-dlp：`brew install yt-dlp`

## 完成后
告知用户：任务已提交，在浏览器 http://localhost:8000 查看实时日志。
