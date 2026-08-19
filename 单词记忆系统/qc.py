#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
voca 满配质检 · sheep 样板丰富度检查
  每个词是否达到满配标准（音标·难度·释义·词源·词根·发音规律·记忆钩子·例句≥2·辨析）。
用法：
  python3 qc.py <id>     # 只检 data/<id>.json
  python3 qc.py          # 扫全部 data/*.json（跳过 _ 开头的配置文件）
硬项缺失 → 退出码 1（阻断 build/交付）；软项（近义词）只提醒。
标准定义见 voca 技能「满配卡片标准·质检」。
"""
import json, os, sys, glob

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

# 硬项：非空字符串
HARD_STR = ["ipa", "meaning", "etymology", "phonetics", "tip", "nuance"]

def _nonempty_str(v):
    return isinstance(v, str) and v.strip() != ""

def check_word(w):
    miss = []
    for f in HARD_STR:
        if not _nonempty_str(w.get(f)):
            miss.append(f)
    if not (isinstance(w.get("levels"), list) and w.get("levels")):
        miss.append("levels")
    if not (isinstance(w.get("roots"), list) and w.get("roots")):
        miss.append("roots")
    ex = w.get("examples")
    if not (isinstance(ex, list) and len(ex) >= 2):
        miss.append("examples(≥2)")
    warn = []
    if not (isinstance(w.get("synonyms"), list) and w.get("synonyms")):
        warn.append("synonyms")
    return miss, warn

def qc_file(path):
    d = json.load(open(path, encoding="utf-8"))
    words = d.get("words", [])
    fails, warns = [], []
    for w in words:
        miss, warn = check_word(w)
        if miss:
            fails.append((w.get("word", "?"), miss))
        if warn:
            warns.append((w.get("word", "?"), warn))
    return words, fails, warns

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    if arg:
        name = arg if arg.endswith(".json") else arg + ".json"
        files = [os.path.join(DATA, name)]
    else:
        files = [f for f in sorted(glob.glob(os.path.join(DATA, "*.json")))
                 if not os.path.basename(f).startswith("_")]

    total_words = total_fail_words = total_warn = 0
    verbose = bool(arg)  # 单文件时逐词列出；批量时只给汇总
    for f in files:
        if not os.path.isfile(f):
            print(f"✗ 找不到 {os.path.basename(f)}")
            sys.exit(2)
        words, fails, warns = qc_file(f)
        total_words += len(words)
        total_fail_words += len(fails)
        total_warn += len(warns)
        base = os.path.basename(f)
        if not fails and not warns:
            print(f"✅ {base}：{len(words)} 词全部满配")
        else:
            rate = round((len(words) - len(fails)) / max(len(words), 1) * 100)
            print(f"— {base}：{len(words)} 词 · 满配 {rate}% · ❌缺项 {len(fails)} · ⚠️软提醒 {len(warns)}")
            if verbose:
                for wd, miss in fails:
                    print(f"    ❌ {wd}: 缺 {', '.join(miss)}")
                for wd, warn in warns:
                    print(f"    ⚠️ {wd}: 建议补 {', '.join(warn)}")

    print()
    print(f"合计 {total_words} 词 · 硬缺项词 {total_fail_words} · 软提醒 {total_warn}")
    if total_fail_words:
        print(f"🔴 质检未过：{total_fail_words} 个词有硬缺项，补齐后再 build / 交付。")
        sys.exit(1)
    print("🟢 质检通过：无硬缺项，可交付。")

if __name__ == "__main__":
    main()
