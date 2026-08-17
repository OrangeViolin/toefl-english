#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""同步 + 生成「听力复述 · 场景词汇（深度版）」入口页。
把 单词记忆系统/groups/spk-*.html（voca 引擎产出的自包含深度页）复制到本目录，
用中文名命名，并生成 index.html 卡片入口。voca 那边重建后，跑一次本脚本即可同步。
用法：python3 场景词汇/_sync_vocab.py
"""
import json, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent                       # 托福口语/场景词汇
VOCA = HERE.parent.parent / "单词记忆系统"                    # 托福英语/单词记忆系统
GROUPS, DATA = VOCA / "groups", VOCA / "data"

# id → (中文文件名, emoji, 英文名, 一句话)
SCENES = [
 ("library",    "图书馆",     "📚", "Library",            "开放时间·借阅·罚款·安静区·预约·数据库·续借"),
 ("hotel",      "酒店前台",   "🏨", "Hotel Front Desk",   "入住·早餐·房间·钥匙·退房·预订·停车·叫醒"),
 ("registrar",  "教务处",     "🏛", "Registrar's Office", "取号·填表·门户·盖章·邮寄·选退课·成绩单"),
 ("orientation","迎新咨询台", "🎓", "Orientation",        "领资料·校园导览·学生证·选课·宿舍·社团"),
 ("library",    None, None, None, None),  # placeholder removed below
]
# 用完整表覆盖（上面占位仅示意，真正用下面这张）
SCENES = [
 ("zoo",        "动物园",     "🦒", "Zoo",                "喂食·参观规则·导览·馆区·闭园·门票"),
 ("gym",        "健身房",     "🏋️", "Gym",               "签到·器械·更衣室·团课·预约·安全"),
 ("orientation","迎新咨询台", "🎓", "Orientation",        "领资料·校园导览·学生证·选课·宿舍·社团"),
 ("library",    "图书馆",     "📚", "Library",            "开放时间·借阅·罚款·安静区·预约·续借"),
 ("hotel",      "酒店前台",   "🏨", "Hotel Front Desk",   "入住·早餐·房间·钥匙·退房·预订·叫醒"),
 ("nature",     "自然保护区", "🌿", "Nature Reserve",     "步道·保护规则·观鸟·野生动物·防火·垃圾"),
 ("registrar",  "教务处",     "🏛", "Registrar's Office", "取号·填表·门户·盖章·邮寄·选退课"),
 ("museum",     "博物馆画廊", "🖼", "Museum / Gallery",   "票务·参观规则·寄存·展区·导览·特展"),
 ("carrental",  "租车行",     "🚗", "Car Rental Agency",  "驾照·满油归还·保险·还车·加驾·车型"),
 ("community",  "社区中心",   "🏢", "Community Centre",   "会员·泳池·报名·订场·活动·押金·志愿者"),
]

cards, total, ok = [], 0, 0
for sid, zh, emoji, en, desc in SCENES:
    src = GROUPS / f"spk-{sid}.html"
    dj  = DATA / f"spk-{sid}.json"
    if not src.exists():
        print(f"⚠️ 缺 {src.name}，跳过"); continue
    n = len(json.loads(dj.read_text(encoding='utf-8'))["words"]) if dj.exists() else 0
    total += n; ok += 1
    dst = HERE / f"{zh}.html"
    shutil.copyfile(src, dst)
    cards.append((zh, emoji, en, desc, n))

cards_html = "\n".join(
 f'''    <a class="card" href="./{zh}.html">
      <div class="emoji">{emoji}</div>
      <h2>{zh}</h2>
      <div class="en">{en} · {n} 词条</div>
      <p>{desc}</p>
    </a>''' for zh, emoji, en, desc, n in cards)

INDEX = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>场景词汇（深度版）· 听力复述配套</title>
<style>
  :root{{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83}}
  *{{box-sizing:border-box}}
  body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:960px;margin:0 auto;padding:34px 22px 80px}}
  .top{{font-size:13px;color:var(--muted)}}
  .top a{{color:var(--muted);text-decoration:none}}
  h1{{font-size:26px;margin:10px 0 4px}}
  .sub{{color:var(--muted);margin-bottom:6px}}
  .intro{{background:#fbf7ee;border:1px solid var(--line);border-radius:12px;padding:13px 16px;font-size:13.5px;color:#5f574c;margin:16px 0 22px;line-height:1.7}}
  .intro b{{color:var(--accent)}}
  .cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}
  a.card{{display:block;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;text-decoration:none;color:inherit;box-shadow:0 2px 12px rgba(150,120,70,.06);transition:.15s}}
  a.card:hover{{transform:translateY(-3px);box-shadow:0 8px 22px rgba(150,120,70,.15);border-color:#d8c8a8}}
  .card .emoji{{font-size:34px}}
  .card h2{{font-size:18px;margin:8px 0 4px}}
  .card .en{{color:var(--accent);font-weight:600;font-size:13px}}
  .card p{{color:#5f574c;font-size:13px;margin:6px 0 0}}
  footer{{margin-top:28px;color:#a89a86;font-size:12px}}
</style>
</head>
<body>
<div class="wrap">
  <div class="top"><a href="../index.html">← 返回口语主页</a></div>
  <h1>📚 场景词汇 · 深度版</h1>
  <div class="sub">听力复述 10 场景配套 · 共 {total} 词条（单词 + 常见短语）</div>
  <div class="intro">
    每个场景一页，用 <b>voca 单词拆解卡</b>呈现：音标 · 词源故事 · 词根词缀 · 发音要点 · 造句/搭配例句 · <b>近义辨析</b>，
    并自带 <b>美式女声朗读</b>、<b>记忆模式</b>、<b>英译中四选一测验</b>、<b>不熟悉标记</b>。
    做「听力复述」前先过一遍对应场景词，听懂率与复述准确率都会立涨。（轻量速记版见口语主页「场景高频词」卡片。）
  </div>
  <div class="cards">
{cards_html}
  </div>
  <footer>voca 引擎产出 · 自包含离线可用 · 数据在 单词记忆系统/data/spk-*.json，重建后跑 场景词汇/_sync_vocab.py 同步</footer>
</div>
</body>
</html>
'''
(HERE / "index.html").write_text(INDEX, encoding="utf-8")
print(f"✅ 同步 {ok} 页 · 合计 {total} 词条 → {HERE}/  (index.html 已生成)")
for zh, emoji, en, desc, n in cards:
    print(f"   {emoji} {zh:<10} {n} 词  → {zh}.html")
