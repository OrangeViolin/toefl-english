# -*- coding: utf-8 -*-
"""分模块沉淀：读所有 data，按四科聚合，复用 build_review.build() 生成模块页 + 模块总览。
核心思路：把「该科所有场次的 task」合成一个 data，交给 build_review.build() 渲染
（点词展开/满配卡/逐题对错清单/三步推理/信号词高亮全部免费复用），
再在顶部注入「动态画像」（水平走势 + 常犯错误定性 + 建议，来自 module-profile.json）。
用法：python3 build_module.py
"""
import json, os, glob, html
import build_review as br

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "模块")
BC = os.path.join(HERE, "..", "背词计划", "data", "项目生词.json")
PROFILE = os.path.join(DATA, "module-profile.json")

MODS = ["reading", "listening", "speaking", "writing"]
MOD_CN = {"reading": "阅读", "listening": "听力", "speaking": "口语", "writing": "写作"}
MOD_ICON = {"reading": "📖", "listening": "🎧", "speaking": "🎤", "writing": "✍️"}

def classify(data_id, section):
    sk = (section.get("key") or "").lower()
    if sk in MODS:
        return sk
    fid = data_id.lower()
    for m in MODS:
        if MOD_CN[m] in data_id:
            return m
    # section key 别名 + 文件名兜底
    if "阅读" in fid or "reading" in fid: return "reading"
    if "听力" in fid or "listening" in fid: return "listening"
    if "写作" in fid or "writing" in fid: return "writing"
    if "口语" in fid or "speaking" in fid: return "speaking"
    return "reading"

def load_profile():
    try:
        return json.load(open(PROFILE, encoding="utf-8"))
    except Exception:
        return {}

def load_vocab_counts():
    try:
        proj = json.load(open(BC, encoding="utf-8"))
    except Exception:
        return {m: 0 for m in MODS}, 0
    cnt = {m: 0 for m in MODS}; expr = 0
    for w in proj.get("words", []):
        src = (w.get("src_from") or "")
        if "句型·" in src:
            expr += 1
        matched = False
        for m in MODS:
            if MOD_CN[m] in src or MOD_CN[m] in (w.get("word") or ""):
                cnt[m] += 1; matched = True; break
        if not matched and not src.startswith("句型"):
            pass
    # 更准确：按 src_from 含「阅读/听力/口语/写作」计数
    cnt = {m: 0 for m in MODS}
    for w in proj.get("words", []):
        src = (w.get("src_from") or "")
        for m in MODS:
            if MOD_CN[m] in src:
                cnt[m] += 1; break
    return cnt, expr

SPEAK_DATA = os.path.join(HERE, "..", "托福口语", "模考复盘", "data")

def _speak_to_tasks():
    """把口语模考 data 转成 build_review 的 task 结构（task1→repeats, task2→interviews）。"""
    tasks = []
    if not os.path.isdir(SPEAK_DATA):
        return tasks
    for f in sorted(glob.glob(os.path.join(SPEAK_DATA, "*.json")), reverse=True):
        d = json.load(open(f, encoding="utf-8"))
        time = d.get("time", "")
        title = d.get("title", "")
        # Task1 跟读
        reps = []
        for r in d.get("task1", []):
            reps.append({
                "en": r.get("en", ""),
                "heard": r.get("err", ""),
                "why": r.get("zh", ""),
                "score": r.get("score", ""),
            })
        if reps:
            tasks.append({
                "title": f"[{time}] Task1 跟读 · {title}（{len(reps)}句）",
                "score": d.get("t1score", ""),
                "type": "口语·跟读",
                "repeats": reps,
            })
        # Task2 面试
        ivs = []
        for q in d.get("task2", []):
            iv = {"q": q.get("q", ""), "your": q.get("my", ""), "score": q.get("score", "")}
            # model2 是两理由范文（list of {mk, role, en}），转成一段
            m2 = q.get("model2", [])
            if m2:
                full = " ".join((x.get("mk","") + " " + x.get("en","")).strip() for x in m2 if isinstance(x, dict))
                iv["model"] = full
            ivs.append(iv)
        if ivs:
            tasks.append({
                "title": f"[{time}] Task2 面试 · {title}（{len(ivs)}题）",
                "score": d.get("t2score", ""),
                "type": "口语·面试",
                "interviews": ivs,
            })
    return tasks

def collect(mod):
    """返回该科所有 task（含 data_id/date），按日期倒序。"""
    if mod == "speaking":
        # 口语用独立的 托福口语/模考复盘/data
        return _speak_to_tasks()
    tasks = []
    for f in glob.glob(os.path.join(DATA, "*.json")):
        if os.path.basename(f).startswith(("_", "module-")): continue
        d = json.load(open(f, encoding="utf-8"))
        if "scores" not in d: continue
        data_id = os.path.basename(f)[:-5]
        date = d.get("date", "")
        for s in d.get("sections", []):
            if classify(data_id, s) != mod: continue
            for t in s.get("tasks", []):
                # 给 task 标题前缀加场次日期，便于识别来源
                t2 = dict(t)
                t2["title"] = f"[{date}] {t.get('title','')}"
                tasks.append(t2)
    tasks.sort(key=lambda t: t.get("title",""), reverse=True)
    return tasks

def collect_vocab(mod):
    seen = set(); out = []
    if mod == "speaking" and os.path.isdir(SPEAK_DATA):
        for f in glob.glob(os.path.join(SPEAK_DATA, "*.json")):
            d = json.load(open(f, encoding="utf-8"))
            for q in d.get("task2", []):
                for v in q.get("vocab", []):
                    w = (v.get("w") or "").lower()
                    if w and w not in seen:
                        seen.add(w); out.append(v)
        return out
    for f in glob.glob(os.path.join(DATA, "*.json")):
        if os.path.basename(f).startswith(("_", "module-")): continue
        d = json.load(open(f, encoding="utf-8"))
        if "scores" not in d: continue
        data_id = os.path.basename(f)[:-5]
        for s in d.get("sections", []):
            if classify(data_id, s) != mod: continue
            for t in s.get("tasks", []):
                for v in t.get("vocab", []):
                    w = (v.get("w") or "").lower()
                    if w and w not in seen:
                        seen.add(w); out.append(v)
    return out

def wrong_stats(mod):
    tally = {}
    if mod == "speaking" and os.path.isdir(SPEAK_DATA):
        for f in glob.glob(os.path.join(SPEAK_DATA, "*.json")):
            d = json.load(open(f, encoding="utf-8"))
            for r in d.get("task1", []):
                try:
                    if r.get("score") and float(str(r["score"]).split("/")[0]) < 5:
                        tally["跟读·实词听不住"] = tally.get("跟读·实词听不住", 0) + 1
                except Exception: pass
            for q in d.get("task2", []):
                try:
                    if q.get("score") and float(str(q["score"]).split("/")[0]) < 3.5:
                        tally["面试·展开不足"] = tally.get("面试·展开不足", 0) + 1
                except Exception: pass
        return sorted(tally.items(), key=lambda x: -x[1])
    for f in glob.glob(os.path.join(DATA, "*.json")):
        if os.path.basename(f).startswith(("_", "module-")): continue
        d = json.load(open(f, encoding="utf-8"))
        if "scores" not in d: continue
        data_id = os.path.basename(f)[:-5]
        for s in d.get("sections", []):
            if classify(data_id, s) != mod: continue
            for t in s.get("tasks", []):
                for q in t.get("questions", []):
                    if q.get("your") and q.get("correct") and q["your"] != q["correct"]:
                        k = q.get("type", "选择题")
                        tally[k] = tally.get(k, 0) + 1
                for b in t.get("blanks", []):
                    if not b.get("ok"):
                        tally["拼写填空·错空"] = tally.get("拼写填空·错空", 0) + 1
                for r in t.get("repeats", []):
                    try:
                        if r.get("score") and float(str(r["score"]).split("/")[0]) < 5:
                            tally["口语跟读·实词听不住"] = tally.get("口语跟读·实词听不住", 0) + 1
                    except Exception: pass
    return sorted(tally.items(), key=lambda x: -x[1])

def level_trend(mod):
    out = []; seen = set()
    for f in sorted(glob.glob(os.path.join(DATA, "*.json")), reverse=True):
        if os.path.basename(f).startswith(("_", "module-")): continue
        d = json.load(open(f, encoding="utf-8"))
        if "scores" not in d: continue
        data_id = os.path.basename(f)[:-5]
        has = any(classify(data_id, s) == mod for s in d.get("sections", []))
        if not has: continue
        sc = d["scores"].get(mod, "")
        if sc and sc != "—" and data_id not in seen:
            seen.add(data_id)
            out.append((d.get("date", ""), sc))
    return out

def profile_html(mod, profile, vocab_cnt, expr_cnt):
    prof = profile.get(mod, {})
    cn = MOD_CN[mod]; icon = MOD_ICON[mod]
    trend = level_trend(mod)
    trend_html = ""
    if trend:
        chips = "".join(f'<span class="tc"><b>{html.escape(sc)}</b><i>{html.escape(dt[:5])}</i></span>' for dt, sc in trend)
        trend_html = f'<div class="p-row"><b>📈 水平走势</b><div class="trend">{chips}</div></div>'
    errs = wrong_stats(mod)
    err_html = ""
    if errs:
        mx = max(c for _, c in errs)
        bars = "".join(f'<div class="bar"><span class="bl">{html.escape(k)}</span><span class="bt"><span class="bf" style="width:{round(c/mx*100)}%"></span></span><span class="bn">{c}</span></div>' for k, c in errs)
        err_html = f'<div class="p-row"><b>🔴 常犯错误 TOP（自动聚合）</b><div class="bars">{bars}</div></div>'
    common = "".join(f'<li>{html.escape(x)}</li>' for x in prof.get("common_errors", []))
    advice = prof.get("advice", "")
    return f'''<div class="profile">
  <div class="p-head">{icon} {cn}模块 · 当前水平 <b>{html.escape(prof.get("level","—"))}</b> <span class="upd">更新 {html.escape(prof.get("updated",""))}</span></div>
  {trend_html}
  {err_html}
  <div class="p-row"><b>📊 需背</b>：生词 <b>{vocab_cnt[mod]}</b> 个 · 句型表达 <b>{expr_cnt}</b> 条（已统一归入背词计划）</div>
  <div class="p-row"><b>💡 常犯错误（定性）</b><ul class="ce">{common}</ul></div>
  <div class="p-row advice"><b>🎯 下一步建议</b><div>{html.escape(advice)}</div></div>
</div>'''

CSS = '''
.profile{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin:14px 0 20px}
.p-head{font-size:15px;margin-bottom:10px}.p-head b{color:var(--accent)}.upd{color:var(--muted);font-size:11.5px;margin-left:8px}
.p-row{margin:9px 0;font-size:13.5px}
.trend{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.tc{background:#fbf6ec;border:1px solid var(--line);border-radius:8px;padding:5px 10px;font-size:12.5px;text-align:center}
.tc b{display:block;color:var(--accent);font-size:14px}.tc i{color:var(--muted);font-size:10.5px;font-style:normal}
.bars{margin-top:6px}.bar{display:flex;align-items:center;gap:8px;margin:4px 0;font-size:12.5px}
.bl{width:150px;flex:none;color:var(--muted)}.bt{flex:1;background:#ece3d2;border-radius:6px;height:10px;overflow:hidden}
.bf{display:block;height:100%;background:var(--bad)}.bn{width:24px;flex:none;font-weight:700;color:var(--bad)}
ul.ce{margin:4px 0 0;padding-left:18px}.ce li{margin:3px 0}
.advice{background:#fdf3e7;border:1px solid #f0d9b8;border-radius:8px;padding:10px 13px;line-height:1.75}
.back{color:var(--accent);text-decoration:none;font-size:13px;font-weight:600}
'''

def build_module_page(mod):
    tasks = collect(mod)
    vocab = collect_vocab(mod)
    profile = load_profile()
    vocab_cnt, expr_cnt = load_vocab_counts()

    # 合成 data 交给 build_review
    synthetic = {
        "id": f"模块-{MOD_CN[mod]}", "date": "持续沉淀", "title": f"{MOD_ICON[mod]} {MOD_CN[mod]}模块 · 分模块沉淀",
        "scores": {"total": "—", "reading": "—", "listening": "—", "writing": "—", "speaking": "—"},
        "priorities": [],
        "sections": [{
            "key": mod, "label": f"{MOD_ICON[mod]} {MOD_CN[mod]}模块 · 全部题目积累",
            "intro": f"该模块所有历史题目的跨场聚合（{len(tasks)} 篇任务）。",
            "tasks": tasks,
        }],
        "wordbank": vocab,
    }
    html = br.build(synthetic)

    # 注入画像 CSS + 画像板块到 <body> 开头（在第一个 <header> 之后或 nav 之后）
    prof = profile_html(mod, profile, vocab_cnt, expr_cnt)
    # 在 <body> 后插入画像
    css_tag = f"<style>{CSS}</style>"
    html = html.replace("</head>", css_tag + "</head>", 1)
    # 在 <h1> 或 <header> 后插入画像（找 nav 结束的位置）
    # 简单：在 body 第一个 <div class="wrap"> 或 header 后插入
    import re
    m = re.search(r'<body[^>]*>', html)
    if m:
        # 找到 title 的 <header> 结束
        h_end = html.find("</header>")
        if h_end > 0:
            html = html[:h_end+9] + '<div class="wrap" style="max-width:900px;margin:0 auto;padding:14px 22px"><a class="back" href="index.html">← 模块总览</a>' + prof + '</div>' + html[h_end+9:]
        else:
            html = html[:m.end()] + prof + html[m.end():]
    out = os.path.join(OUT, f"{MOD_CN[mod]}.html")
    open(out, "w", encoding="utf-8").write(html)
    print(f"  ✓ 模块/{MOD_CN[mod]}.html — {len(tasks)} 任务 · {len(vocab)} 生词")

def build_overview():
    profile = load_profile()
    vocab_cnt, expr_cnt = load_vocab_counts()
    cards = []
    for mod in MODS:
        tasks = collect(mod)
        errs = wrong_stats(mod)
        nerr = sum(c for _, c in errs)
        prof = profile.get(mod, {})
        cards.append(f'''<a class="mcard" href="{MOD_CN[mod]}.html">
  <div class="ic">{MOD_ICON[mod]}</div>
  <h2>{MOD_CN[mod]}</h2>
  <div class="lv">当前 {html.escape(prof.get("level","—"))}</div>
  <div class="m">错题 <b>{nerr}</b> · 生词 <b>{vocab_cnt[mod]}</b> · 句型 <b>{expr_cnt}</b></div>
  <div class="m2">{html.escape(prof.get("common_errors",[""])[0] if prof.get("common_errors") else "")}</div>
</a>''')
    doc = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>四科模块总览</title><style>
:root{{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}}
.wrap{{max-width:880px;margin:0 auto;padding:30px 22px 80px}}
h1{{font-size:22px;margin:0 0 4px}}.sub{{color:var(--muted);font-size:13px;margin-bottom:20px}}
a.back{{color:var(--accent);text-decoration:none;font-size:13px;font-weight:600}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:16px}}
a.mcard{{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;text-decoration:none;color:inherit}}
a.mcard:hover{{border-color:var(--accent)}}
.ic{{font-size:30px}}.mcard h2{{font-size:17px;margin:6px 0 2px}}
.lv{{font-size:13px;color:var(--accent);font-weight:700;margin-bottom:4px}}
.m{{font-size:12.5px;color:var(--muted)}}.m b{{color:var(--ink)}}
.m2{{font-size:12px;color:#a89a86;margin-top:8px;line-height:1.5}}
</style></head><body><div class="wrap">
<a class="back" href="../index.html">← 模考复习系统</a>
<h1>🎯 四科模块沉淀</h1>
<div class="sub">听力 · 口语 · 阅读 · 写作 ｜ 动态画像随每场模考刷新 ｜ 生词句型统一汇入背词计划</div>
<div class="grid">{''.join(cards)}</div>
</div></body></html>'''
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(doc)
    print(f"  ✓ 模块/index.html — 四科总览")

def build():
    os.makedirs(OUT, exist_ok=True)
    for mod in MODS:
        build_module_page(mod)
    build_overview()

if __name__ == "__main__":
    build()
