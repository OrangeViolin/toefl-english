#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""听力复述题库 组装+校验器
读 data/lr-parts/<id>.json（每个=一个场景），校验难度分档/字段/词数，
拼成 data/listen-repeat.js（window.LR_SCENES=[...]）。
用法: python3 data/_build_lr.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent          # .../托福口语/data
PARTS = ROOT / "lr-parts"
OUT = ROOT / "listen-repeat.js"

ORDER = ["zoo","gym","orientation","library","hotel",
         "nature","registrar","museum","carrental","community"]

# 词数区间（音节靠人工，词数机器卡）
RANGE = {"简单":(5,7), "中等":(8,12), "困难":(13,19)}
TIER  = {"简单":"short", "中等":"medium", "困难":"long"}

def words(s):
    return [w for w in re.sub(r"[^A-Za-z0-9' ]"," ",s).split() if w]

def norm(s):  # 归一化用于 chunks 拼接比对
    return re.sub(r"[^a-z0-9]","", s.lower())

scenes, warn, err = [], [], []
for sid in ORDER:
    p = PARTS / f"{sid}.json"
    if not p.exists():
        err.append(f"[{sid}] 缺文件"); continue
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        err.append(f"[{sid}] JSON 解析失败: {e}"); continue
    items = d.get("items", [])
    cnt = {"简单":0,"中等":0,"困难":0}
    for i, it in enumerate(items):
        lv = it.get("lv","")
        if lv not in RANGE:
            err.append(f"[{sid}#{i}] lv 非法: {lv!r}"); continue
        cnt[lv]+=1
        n = len(words(it.get("en","")))
        lo,hi = RANGE[lv]
        if not (lo-1 <= n <= hi+1):   # 容忍 ±1
            warn.append(f"[{sid}#{i}] {lv} 词数={n} 超区间{lo}-{hi}: {it['en']}")
        ch, sk = it.get("chunks",[]), it.get("skeleton",[])
        if len(ch)!=len(sk):
            warn.append(f"[{sid}#{i}] chunks({len(ch)})≠skeleton({len(sk)}): {it['en']}")
        if ch and norm("".join(ch)) != norm(it.get("en","")):
            warn.append(f"[{sid}#{i}] chunks 拼接≠原句: {it['en']}")
        for k in ("en","zh","lv","chunks","skeleton"):
            if k not in it: err.append(f"[{sid}#{i}] 缺字段 {k}")
        it["tier"] = TIER[lv]
    if len(items)!=21 or cnt!={"简单":7,"中等":7,"困难":7}:
        warn.append(f"[{sid}] 分档 {cnt} 总数 {len(items)}（期望 7/7/7=21）")
    scenes.append(d)

total = sum(len(s["items"]) for s in scenes)
header = ("// 听力复述题库 · 10 场景 × 21 句（7 短 + 7 中 + 7 长）\n"
          "// 由 data/_build_lr.py 从 data/lr-parts/*.json 组装，勿手改本文件\n"
          "// 每句: {en, zh, lv(简单/中等/困难), tier(short/medium/long), chunks[], skeleton[]}\n")
OUT.write_text(header + "window.LR_SCENES = " +
               json.dumps(scenes, ensure_ascii=False, indent=1) + ";\n",
               encoding="utf-8")

print(f"✅ 组装完成：{len(scenes)} 场景 · {total} 句 → {OUT.name}")
for s in scenes:
    c={"简单":0,"中等":0,"困难":0}
    for it in s["items"]: c[it['lv']]=c.get(it['lv'],0)+1
    print(f"   {s['name']:<12} {len(s['items']):>2}句  短{c['简单']}/中{c['中等']}/长{c['困难']}")
if warn:
    print(f"\n⚠️ {len(warn)} 条提醒：")
    for w in warn[:40]: print("   "+w)
if err:
    print(f"\n❌ {len(err)} 条错误：")
    for e in err: print("   "+e)
    sys.exit(1)
print("\n无致命错误。" + ("" if not warn else f" 有 {len(warn)} 条软提醒（±1词可容忍）。"))
