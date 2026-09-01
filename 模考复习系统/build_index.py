# -*- coding: utf-8 -*-
"""模考复习系统 · 总索引页生成器
扫描 data/*.json → 生成 index.html（全部场次倒序 + 四科模块入口 + 背词入口）。
旧格式（无 scores，用 passages）标为「早期文段复习页」。
用法：python3 build_index.py
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "复习页")

MODULES = ["听力", "口语", "阅读", "写作"]

def _meta(d):
    """返回 (is_new, 日期, 标题, 副标题, 分数串)"""
    is_new = "scores" in d
    date = d.get("date", "")
    title = d.get("title", "")
    if is_new:
        sc = d["scores"]
        parts = []
        for k, lab in [("reading","阅"),("listening","听"),("writing","写"),("speaking","口")]:
            v = sc.get(k)
            if v and v != "—":
                parts.append(f"{lab}{v}")
        score = " · ".join(parts)
        ntask = sum(len(s.get("tasks", [])) for s in d.get("sections", []))
        nq = sum(len(t.get("questions", [])) + len(t.get("blanks", [])) for s in d.get("sections", []) for t in s.get("tasks", []))
        nv = sum(len(t.get("vocab", [])) for s in d.get("sections", []) for t in s.get("tasks", []))
        sub = f"{len(d.get('sections', []))} 科 · {ntask} 篇 · {nq} 题/空 · {nv} 生词"
    else:
        score = "早期"
        nw = sum(len(p.get("words", [])) for p in d.get("passages", []))
        sub = f"{len(d.get('passages', []))} 篇文段 · {nw} 词"
    return is_new, date, title, sub, score

def build():
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    cards = []
    for f in files:
        base = os.path.basename(f)
        if base.startswith("_") or base.startswith("module-"):
            continue  # 跳过配置文件（module-profile.json 等）
        d = json.load(open(f, encoding="utf-8"))
        mid = d.get("id") or os.path.splitext(os.path.basename(f))[0]
        is_new, date, title, sub, score = _meta(d)
        tag = "" if is_new else '<span class="old">早期</span>'
        cards.append((date, mid, title, sub, score, tag, is_new))

    # 按日期倒序（无日期的排最后）
    def key(x):
        return x[0] or "0000-00-00"
    cards.sort(key=key, reverse=True)

    cards_html = []
    for date, mid, title, sub, score, tag, is_new in cards:
        cards_html.append(
            f'<a class="card" href="复习页/{html.escape(mid)}.html">'
            f'<div class="c-top"><h2>{html.escape(title)}</h2>{tag}</div>'
            f'<div class="score">{html.escape(score)}</div>'
            f'<div class="m">{html.escape(date)} · {html.escape(sub)}</div></a>')

    # 四科模块入口
    module_btns = "".join(
        f'<a class="mod" href="模块/{m}.html"><span class="ic">{"🎧" if m=="听力" else "🎤" if m=="口语" else "📖" if m=="阅读" else "✍️"}</span>{m}</a>'
        for m in MODULES)

    html_doc = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>托福模考复习系统</title><style>
:root{{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}}
.wrap{{max-width:880px;margin:0 auto;padding:34px 22px 80px}}
h1{{font-size:24px;margin:0 0 4px}}.sub{{color:var(--muted);margin-bottom:20px}}
.sec-h{{font-size:15px;color:var(--core);font-weight:700;margin:26px 0 10px;border-bottom:2px solid var(--line);padding-bottom:6px}}
.modrow{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:8px}}
a.mod{{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;text-align:center;text-decoration:none;color:inherit;font-size:16px;font-weight:700}}
a.mod:hover{{border-color:var(--accent)}}a.mod .ic{{display:block;font-size:28px;margin-bottom:6px}}
.vocab-entry{{display:block;background:linear-gradient(135deg,#fff6e8,#fdf3e7);border:1px solid #f0d9b0;border-left:5px solid var(--accent);border-radius:12px;padding:15px 18px;text-decoration:none;color:inherit;margin-bottom:8px;font-size:15px;font-weight:600}}
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}}
a.card{{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;text-decoration:none;color:inherit}}
a.card:hover{{border-color:#d8c8a8}}
a.card h2{{font-size:15.5px;margin:0 0 4px}}
.c-top{{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}}
.old{{flex:none;font-size:11px;background:#ece7f7;color:#6b5bb5;border-radius:20px;padding:1px 9px;font-weight:600}}
.score{{font-size:13px;color:var(--accent);font-weight:700;margin:2px 0}}
.m{{color:var(--muted);font-size:12.5px}}
footer{{margin-top:28px;color:#a89a86;font-size:12px}}
</style></head><body><div class="wrap">
<h1>📚 托福模考复习系统</h1>
<div class="sub">每一次模考 → 题目级复盘页 · 四科模块沉淀 · 背词计划联动</div>

<div class="sec-h">🎯 四科模块沉淀</div>
<div class="modrow">{module_btns}</div>
<a class="vocab-entry" href="../背词计划/index.html">🔤 背词计划（全项目生词 + 句型表达统一汇聚点）→</a>

<div class="sec-h">📝 全部模考场次（{len(cards)} 场 · 按日期倒序）</div>
<div class="cards">{''.join(cards_html)}</div>
<footer>data/*.json → build_index.py / build_review.py / build_module.py ｜ 总索引自动生成</footer>
</div></body></html>'''

    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html_doc)
    print(f"✅ index.html — {len(cards)} 场（新格式 {sum(1 for c in cards if c[6])} · 早期 {sum(1 for c in cards if not c[6])}）")

if __name__ == "__main__":
    build()
