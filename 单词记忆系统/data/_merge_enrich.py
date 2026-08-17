#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把各 _enrich-spk-<id>.json 的 enrich(补 core/senses/roots) + add(新词) 合并进 spk-<id>.json。
安全：只加字段/追加新词，不删已有内容；新词去重、subgroup 校验；写回前 JSON 合法性有 python 保障。
用法：python3 data/_merge_enrich.py"""
import json, glob, os
from pathlib import Path

HERE = Path(__file__).resolve().parent   # .../单词记忆系统/data
IDS = ["zoo","gym","orientation","library","hotel","nature","registrar","museum","carrental","community"]

grand = {"enriched":0,"enrich_miss":0,"added":0,"dup":0}
for sid in IDS:
    main_p = HERE / f"spk-{sid}.json"
    enr_p  = HERE / f"_enrich-spk-{sid}.json"
    if not main_p.exists() or not enr_p.exists():
        print(f"⚠️  {sid}: 缺文件，跳过"); continue
    main = json.loads(main_p.read_text(encoding="utf-8"))
    enr  = json.loads(enr_p.read_text(encoding="utf-8"))
    words = main["words"]
    valid = {sg["key"] for sg in main.get("subgroups",[])} or {"general"}
    by_exact = {w["word"]: w for w in words}
    by_lower = {w["word"].lower(): w for w in words}

    # 1) enrich：给已有词补 core/senses/roots（不覆盖已有非空）
    en = enr.get("enrich",{}) or {}
    m_hit=m_miss=0
    for key, fields in en.items():
        w = by_exact.get(key) or by_lower.get(key.lower())
        if not w: m_miss+=1; continue
        for f in ("core","senses","roots"):
            if f in fields and fields[f]:
                if not w.get(f):        # 只在原字段空时写入
                    w[f]=fields[f]
        m_hit+=1

    # 2) add：追加新词（去重 + subgroup 校验）
    add = enr.get("add",[]) or []
    a_add=a_dup=0
    for nw in add:
        wd=(nw.get("word") or "").strip()
        if not wd: continue
        if wd.lower() in by_lower: a_dup+=1; continue
        if nw.get("subgroup") not in valid: nw["subgroup"]="general"
        words.append(nw); by_lower[wd.lower()]=nw; a_add+=1

    main_p.write_text(json.dumps(main, ensure_ascii=False, indent=1), encoding="utf-8")
    # 回读校验
    json.loads(main_p.read_text(encoding="utf-8"))
    print(f"✓ {sid:12} 词 {len(words):3} (enrich {m_hit} 命中/{m_miss} 未匹配 · 新增 {a_add} · 去重 {a_dup})")
    grand["enriched"]+=m_hit; grand["enrich_miss"]+=m_miss; grand["added"]+=a_add; grand["dup"]+=a_dup

print(f"\n合计：enrich 命中 {grand['enriched']} · 未匹配 {grand['enrich_miss']} · 新增词 {grand['added']} · 去重 {grand['dup']}")
