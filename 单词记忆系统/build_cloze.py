#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""阅读填词题 · 烘焙脚本

把 data/cloze.json（填词题数据 + 单词卡）内嵌进 阅读填词.html，
生成一个可离线（file://）直接打开的独立页面——与 build.py 同一哲学。

用法：python3 build_cloze.py
改题/加题后：改 data/cloze.json，再跑一次本脚本。
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    data_path = ROOT / "data" / "cloze.json"
    tmpl_path = ROOT / "阅读填词.html"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    html = tmpl_path.read_text(encoding="utf-8")
    if "__CLOZE_DATA__" not in html:
        print("✗ 未在 阅读填词.html 中找到 __CLOZE_DATA__ 占位符")
        return
    payload = json.dumps(data, ensure_ascii=False)
    out = html.replace("__CLOZE_DATA__", payload)
    tmpl_path.write_text(out, encoding="utf-8")
    n = sum(len(p["blanks"]) for p in data["passages"])
    print(f"✓ 阅读填词.html 已烘焙（{len(data['passages'])} 篇 · 共 {n} 个空）")


if __name__ == "__main__":
    main()
