# Skill: TikTok 创作者主页爬取

从用户输入中提取创作者链接和数量，然后运行 run.py 采集该创作者的作品和评论。

## 参数提取规则
- URL（含 tiktok.com 或 vm.tiktok.com）→ url（必填）
- 数字 → count（默认 20）

## 执行命令
```
python3 run.py --url "<创作者主页链接>" --count <数量>
```

## 完成后
告知用户：任务已提交，在浏览器 http://localhost:8000 查看实时日志。
