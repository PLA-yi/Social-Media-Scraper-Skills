# Skill: 抖音关键词爬取

从用户输入中提取参数，然后运行 run.py 脚本采集抖音数据。

## 参数提取规则
- 第一个非选项词 → keyword（必填）
- 数字 → count（默认 20）
- "fast" 或 "快速" → scrape_mode=fast（默认 safe）
- "最新" 或 "latest" → sort_by=1
- "最热" 或 "hot" → sort_by=2（默认 0）
- "N小时" 或 "Nh" → time_filter=N（默认 0 不限）

## 执行命令
```
python3 run.py --keyword "<关键词>" --count <数量> --mode <safe|fast> --sort <0|1|2> --time_filter <小时数>
```

## 完成后
告知用户：任务已提交，在浏览器 http://localhost:8000 查看实时日志，数据保存在项目 data/ 目录。
