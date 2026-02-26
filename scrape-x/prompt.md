# Skill: X（推特）爬取

从用户输入中提取目标和数量，然后运行 run.py 采集 X 推文数据。

## 参数提取规则
- 若输入包含 x.com 或 twitter.com → url，mode=blogger（采集用户主页）
- 否则 → keyword，mode=keyword（关键词搜索）
- 数字 → count（默认 20）

## 执行命令
```
python3 run.py --target "<关键词或用户主页链接>" --mode <keyword|blogger> --count <数量>
```

## 前置条件
需要提前用 Cookie-Editor 导出 X 登录 Cookie，保存为项目 data/cookies.json。
需要 Python 3.10+。

## 完成后
告知用户：任务已提交，在浏览器 http://localhost:8000 查看实时日志。
