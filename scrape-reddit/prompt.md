# Skill: Reddit 爬取

从用户输入中提取目标和数量，然后运行 run.py 采集 Reddit 数据。

## 参数提取规则
- 若输入包含 reddit.com → url，mode=blogger（采集 subreddit）
- 否则 → keyword，mode=keyword（关键词搜索）
- 数字 → count（默认 20）

## 执行命令
```
python3 run.py --target "<关键词或链接>" --mode <keyword|blogger> --count <数量>
```

## 前置条件
需要提前用浏览器 Cookie-Editor 插件导出 Reddit 登录 Cookie，保存为项目 data/cookies.json。

## 完成后
告知用户：任务已提交，在浏览器 http://localhost:8000 查看实时日志。
