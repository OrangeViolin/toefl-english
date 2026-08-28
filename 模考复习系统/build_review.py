# -*- coding: utf-8 -*-
"""模考·题目级复盘引擎  data/<id>.json → 复习页/<id>.html（自包含）
每道题结合：原文(每词可点读) + 你的答案vs正确答案 + 考点分析 + 生词 + 关键句 + 范文。
新一场模考：写 data/<总分>-<日期>.json（结构见样板），跑 python3 build_review.py <id>。
"""
import json, os, sys, html, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = os.path.join(HERE, "复习页")

def e(s): return html.escape(str(s or ""), quote=True)

def _load_hard_words():
    """六级/托福等「稍难」词形集合（含常见屈折），用于正文里重点划线高亮。"""
    p = os.path.join(HERE, "hard_words.json")
    try:
        with open(p, encoding="utf-8") as fp:
            return set(json.load(fp))
    except Exception:
        return set()

def clk(text):
    """整段文字：每词可点『就地展开满配卡』(JS) + 整段🔊。附一个 .det 展开容器。"""
    if not text: return ""
    return f'<div class="clkwrap"><div class="clk" data-say="{e(text)}">{e(text)}</div><div class="det"></div></div>'

def clk_paras(text):
    """阅读原文分段渲染：passage 里用空行/\\n 分隔段落，每段一个 clkwrap（点词展开照旧），顶部加『🔊读全文』。"""
    if not text: return ""
    paras = [p.strip() for p in re.split(r"\n+", text) if p.strip()]
    if len(paras) <= 1:
        return clk(text)
    full = re.sub(r"\s*\n+\s*", " ", text).strip()
    body = "".join(f'<div class="para">{clk(p)}</div>' for p in paras)
    return f'<div class="pwrap"><button class="replay say" data-say="{e(full)}">🔊 读全文</button>{body}</div>'

# ---- 长难句精拆：@X{} 彩色成分 + 每词可点展开（预渲染 .wd）----
GLABEL = {"S": "主语", "V": "谓语", "O": "宾语", "C": "从句", "P": "介词/修饰", "M": "状语"}

def _wd(tok):
    w = re.sub(r"[^A-Za-z'-]", "", tok)
    return f'<span class="wd" data-w="{e(w.lower())}">{e(tok)}</span>' if w else e(tok)

def _wds(text):
    return "".join(_wd(t) if not t.isspace() else t for t in re.split(r"(\s+)", text) if t)

def lsent_tok(en):
    out, i = [], 0
    for m in re.finditer(r"@([SVOCPM])\{([^}]*)\}", en):
        if m.start() > i: out.append(_wds(en[i:m.start()]))
        out.append(f'<span class="g g-{m.group(1)}">{_wds(m.group(2))}</span>')
        i = m.end()
    if i < len(en): out.append(_wds(en[i:]))
    return "".join(out)

def transblock(zh, label="全文翻译"):
    """整篇中文翻译（先自己读英文→点开对照）。"""
    if not zh: return ""
    return f'<details class="tzh"><summary>🇨🇳 {e(label)}（先自己读，点开中英对照）</summary><div class="tzhb">{e(zh)}</div></details>'

def longsentblock(ls):
    if not ls: return ""
    legend = '<div class="lslegend">' + "".join(f'<span class="g g-{k}">{v}</span>' for k, v in GLABEL.items()) + "</div>"
    rows = []
    for s in ls:
        full = re.sub(r"@[SVOCPM]\{([^}]*)\}", r"\1", s["en"])
        read = f'<div class="lsread">🧭 <b>怎么读懂：</b>{e(s["read"])}</div>' if s.get("read") else ""
        rows.append(f'<div class="lsi"><div class="clkwrap"><div class="clk pre" data-say="{e(full)}">{lsent_tok(s["en"])}</div><div class="det"></div></div>'
                    f'<details class="lsrev"><summary>先自己拆，再点开看直译 + 读法</summary>'
                    f'<div class="lszh">直译：{e(s.get("zh",""))}</div>{read}</details></div>')
    return '<div class="lsent"><div class="mh">🔬 长难句精拆 · 点彩块看成分 · 点词展开卡</div>' + legend + "".join(rows) + "</div>"

def stepsblock(q):
    if not q.get("steps"): return ""
    ic = {"定位": "📍", "推理": "🧠", "排除": "✂️"}
    rows = "".join(f'<div class="step"><span class="sk">{ic.get(st["k"], "·")} {e(st["k"])}</span><span class="sv">{e(st["v"])}</span></div>' for st in q["steps"])
    return f'<div class="steps">{rows}</div>'

def weakfixblock(t):
    w = f'<div class="wf-w">🔴 <b>你的漏洞：</b>{e(t["weak"])}</div>' if t.get("weak") else ""
    fx = f'<div class="wf-f">🛠 <b>补强：</b>{e(t["fix"])}</div>' if t.get("fix") else ""
    return f'<div class="weakfix">{w}{fx}</div>' if (w or fx) else ""

def repeatblock(reps):
    if not reps: return ""
    rows = []
    for r in reps:
        heard = f'<div class="rp-h">👂 你听成：<span class="rp-x">{e(r["heard"])}</span></div>' if r.get("heard") else ""
        why = f'<div class="rp-w">🔎 {e(r["why"])}</div>' if r.get("why") else ""
        phon = f'<div class="rp-p">🗣 {e(r["phon"])}</div>' if r.get("phon") else ""
        sc = f'<span class="rp-sc">{e(r.get("score"))}</span>' if r.get("score") else ""
        rows.append(f'<div class="rp">{sc}<div class="clkwrap"><div class="clk" data-say="{e(r["en"])}">{e(r["en"])}</div><div class="det"></div></div>{heard}{why}{phon}</div>')
    return '<div class="repeats"><div class="mh">🗣 跟读逐句 · 你听成 vs 实际 · 怎么练</div>' + "".join(rows) + "</div>"

def interviewblock(ivs):
    if not ivs: return ""
    rows = []
    for q in ivs:
        sc = f'<span class="tsc">{e(q.get("score"))}</span>' if q.get("score") else ""
        your = f'<div class="iv-y">🎙 你答的：{e(q["your"])}</div>' if q.get("your") else ""
        dg = f'<div class="iv-d">🔎 <b>诊断：</b>{e(q["diagnose"])}</div>' if q.get("diagnose") else ""
        model = f'<div class="mh">✍️ 老师范文（点词展开·可背）</div>{clk(q["model"])}' if q.get("model") else ""
        mzh = f'<div class="mzh">{e(q["model_zh"])}</div>' if q.get("model_zh") else ""
        dl = f'<div class="iv-dl">🎧 <b>表达建议：</b>{e(q["delivery"])}</div>' if q.get("delivery") else ""
        rows.append(f'<div class="iv"><div class="iv-q">{sc}{e(q["q"])}</div>{your}{dg}{model}{mzh}{dl}</div>')
    return '<div class="interviews"><div class="mh">💬 面试逐题 · 诊断 + 老师范文 + 表达建议</div>' + "".join(rows) + "</div>"

def corrblock(corrs):
    if not corrs: return ""
    rows = "".join(f'<div class="corr"><span class="c-x">✗ {e(c["wrong"])}</span> → <span class="c-r">✓ {e(c["right"])}</span><div class="c-w">{e(c["why"])}</div></div>' for c in corrs)
    return '<div class="corrs"><div class="mh">🖊 逐处红笔改</div>' + rows + "</div>"

def diagblock(dg):
    if not dg: return ""
    w = "".join(f"<li>{e(x)}</li>" for x in dg.get("weak", []))
    fx = "".join(f"<li>{e(x)}</li>" for x in dg.get("fix", []))
    return (f'<div class="secdiag"><div class="dg-w"><b>🔴 本科漏洞清单</b><ul>{w}</ul></div>'
            f'<div class="dg-f"><b>🛠 补强处方</b><ul>{fx}</ul></div></div>')

def sentblock(sents):
    """关键句：英文(可点读) + 中文 + 分析。"""
    if not sents: return ""
    rows = []
    for s in sents:
        note = f'<div class="snote">🔑 {e(s["note"])}</div>' if s.get("note") else ""
        rows.append(f'<div class="sent">{clk(s["en"])}'
                    f'<div class="szh">{e(s.get("zh",""))}</div>{note}</div>')
    return '<div class="sents"><div class="mh">📝 关键句 · 点词展开卡 · 学表达</div>' + "".join(rows) + "</div>"

def vocabblock(vocab):
    if not vocab: return ""
    cards = []
    for v in vocab:
        note = f'<div class="vnote">{e(v["note"])}</div>' if v.get("note") else ""
        cards.append(f'<div class="vcard" data-mk="v:{e(v["w"])}"><span class="vmk"><button class="mk ok" data-m="ok">✓</button><button class="mk no" data-m="no">✕</button></span>'
                     f'<span class="w say" data-say="{e(v["w"])}">{e(v["w"])}</span>'
                     f'<span class="ipa">{e(v.get("ipa",""))}</span>'
                     f'<div class="vzh">{e(v.get("zh",""))}</div>{note}</div>')
    return '<div class="vocab"><div class="mh">📚 生词 · 点词朗读 · ✓ 掌握 / ✕ 未掌握</div><div class="vgrid">' + "".join(cards) + "</div></div>"

def blanksblock(blanks):
    if not blanks: return ""
    rows = []
    for b in blanks:
        ok = b.get("ok")
        cls = "ok" if ok else "no"
        mark = "✓" if ok else "✗"
        pt = f'<td class="pt">{e(b["point"])}</td>' if b.get("point") else '<td class="pt"></td>'
        cor = f'<span class="spoil" title="点击显形">{mark} {e(b["correct"])}</span>' if not ok else f'{mark} {e(b["correct"])}'
        rows.append(f'<tr class="{cls}"><td class="num">{e(b["n"])}</td>'
                    f'<td class="yr">{e(b.get("your",""))}</td><td class="ar">{cor}</td>{pt}</tr>')
    return ('<div class="blanks"><div class="mh">🖊 逐空对照 · ✍️ 正确答案已遮住，先回忆再点开核对</div>'
            '<table class="btab"><tr><th>#</th><th>你写的</th><th>正确</th><th>考点</th></tr>'
            + "".join(rows) + "</table></div>")

def optsblock(q):
    opts = q.get("options", {})
    yourk, corrk = q.get("your"), q.get("correct")
    ok = (yourk == corrk)
    verdict = ('<span class="qverdict ok">✅ 你答对了</span>' if ok
               else '<span class="qverdict no">❌ 你答错了</span>')
    neutral = "".join(f'<div class="opt"><b>{e(k)}.</b> {e(opts[k])}</div>' for k in sorted(opts.keys()))
    ans = []
    for k in sorted(opts.keys()):
        cls = ""; tag = ""
        if k == corrk: cls = "correct"; tag = '<span class="tag t-ok">✓ 正确</span>'
        if k == yourk and yourk != corrk: cls = "wrong"; tag = '<span class="tag t-no">✗ 你选的</span>'
        ans.append(f'<div class="opt {cls}"><b>{e(k)}.</b> {e(opts[k])} {tag}</div>')
    # 错题重点：醒目的「你错在哪」分析块（放在答案对照之前，一眼看到）
    wrongblk = ""
    if not ok:
        cause = q.get("trap") or q.get("why") or ""
        if cause:
            wrongblk = f'<div class="wrongwhy">❌ <b>你错在哪：</b>{e(cause)}</div>'
    pt = f'<div class="qpt"><b>考点：</b>{e(q["point"])}</div>' if q.get("point") else ""
    why = f'<div class="qwhy">{e(q["why"])}</div>' if q.get("why") else ""
    typ = f'<span class="qtype">{e(q["type"])}</span>' if q.get("type") else ""
    reveal = (f'<details class="reveal"><summary>🙈 先自己判断，再点开看答案 &amp; 老师精讲</summary>'
              f'<div class="revbody">{wrongblk}{"".join(ans)}{stepsblock(q)}{pt}{why}</div></details>')
    return f'<div class="q"><div class="qtxt">{typ}{e(q["q"])} {verdict}</div>{neutral}{reveal}</div>'

def modelblock(m):
    if not m: return ""
    zh = f'<div class="mzh">{e(m["zh"])}</div>' if m.get("zh") else ""
    lbl = e(m.get("label", "范文 · 可学可背"))
    return (f'<div class="model"><div class="mh">✍️ {lbl}</div>'
            f'<div class="mbody">{clk(m["en"])}</div>{zh}</div>')

def task_html(t, tid=""):
    parts = [f'<button class="mastery" data-tid="{e(tid)}">✓ 标这篇已吃透</button>']
    if t.get("prompt"): parts.append(f'<div class="prompt"><b>题目：</b>{e(t["prompt"])}</div>')
    if t.get("passage"): parts.append('<div class="mh">📖 原文 · 点任意词展开满配卡 · 🔊 读全文</div>' + clk_paras(t["passage"]) + transblock(t.get("passage_zh")))
    if t.get("transcript"): parts.append(f'<div class="mh">🎧 听力原文 · 点词展开 · <button class="replay say" data-say="{e(t["transcript"])}">🎧 再听整段（二遍精听）</button></div>' + clk(t["transcript"]) + transblock(t.get("transcript_zh"), "听力原文翻译"))
    parts.append(longsentblock(t.get("longsent")))
    if t.get("your_answer"): parts.append(f'<div class="youranswer"><div class="mh">🎙 你的作答</div><div class="ya">{e(t["your_answer"])}</div></div>')
    parts.append(blanksblock(t.get("blanks")))
    for q in t.get("questions", []): parts.append(optsblock(q))
    parts.append(repeatblock(t.get("repeats")))
    parts.append(interviewblock(t.get("interviews")))
    parts.append(corrblock(t.get("corrections")))
    parts.append(sentblock(t.get("sentences")))
    parts.append(modelblock(t.get("model")))
    parts.append(vocabblock(t.get("vocab")))
    parts.append(weakfixblock(t))
    if t.get("takeaway"):
        parts.append(f'<div class="takeaway">💡 <b>这道/这篇的收获：</b>{e(t["takeaway"])}</div>')
    sc = f'<span class="tsc">{e(t["score"])}</span>' if t.get("score") else ""
    tm = f'<span class="ttime">⏱ {e(t["time"])}</span>' if t.get("time") else ""
    return (f'<details class="task" data-tid="{e(tid)}"><summary><span class="mflag">✓</span><span class="ttitle">{e(t["title"])}</span>{sc}{tm}</summary>'
            f'<div class="tbody">{"".join(parts)}</div></details>')

LISTEN_STRATEGY = '''<details class="lstrat" open><summary>🎧 完全听不懂时·边听边抓（尤其学术讲座）——尽量多理解的 5 步</summary><div class="lsbody">
<div class="lsstep"><b>① 开头一句定主题</b>：学术讲座第一句几乎必点主题——<i>"Today we'll focus on X" / "Let's talk about X"</i>。抓住 <b>X 是什么</b>，后面全围着它转。细节没听懂，至少知道在讲什么，主旨题就能拿下。</div>
<div class="lsstep"><b>② 顺信号词拼骨架</b>（配合上面🚦分色高亮）：
<ul><li>🔴 <b>but/however/instead</b> → 前面被转折/否定，<b>后面才是重点</b></li>
<li>🔵 <b>because/so/therefore</b> → 因果，抓「因为什么 → 所以什么」</li>
<li>🟢 <b>for example/such as/called</b> → 要举例或下定义了，例子帮你理解前面的抽象点；<b>"a X called Y" 必考 Y 是什么</b></li>
<li>🟣 <b>first/then/also/another</b> → 在列点，心里数 1、2、3</li>
<li>🟠 <b>the key/importantly/actually</b> → 划重点，这句最可能考</li></ul></div>
<div class="lsstep"><b>③ 抓实词、放虚词</b>：名词+动词是内容，介词冠词不用抠。<b>某句没听懂就别卡住</b>——等下一个信号词/例子，它常会换句话再解释一遍。</div>
<div class="lsstep"><b>④ 重复 = 重点</b>：反复出现的词（stalagmite、algal bloom…）就是核心概念，围着它记；数字/人名先记下，但「为什么提它」比它本身更重要。</div>
<div class="lsstep"><b>⑤ 学术讲座万能骨架</b>：<b>现象/定义 → 原因/机制 → 例子/证据 → 影响/结论</b>。就算只抓到「讲某现象、有原因、举了例、最后有个启示」，也够答对<b>主旨题 + 修辞目的题 + 推断题</b>（占大头）。</div>
</div></details>'''

def section_html(s):
    intro = f'<div class="sintro">{e(s["intro"])}</div>' if s.get("intro") else ""
    points = ""
    if s.get("points"):
        lis = "".join(f"<li>{e(p)}</li>" for p in s["points"])
        points = f'<div class="spoints"><b>🎯 本科考点总结</b><ul>{lis}</ul></div>'
    tasks = "".join(task_html(t, f'{s["key"]}-{ti}') for ti, t in enumerate(s.get("tasks", [])))
    strat = LISTEN_STRATEGY if any(t.get("transcript") for t in s.get("tasks", [])) else ""
    return (f'<section class="sec" id="sec-{e(s["key"])}"><h2>{e(s["label"])}</h2>{intro}{diagblock(s.get("diagnosis"))}{strat}{points}{tasks}</section>')

def build(d):
    sc = d["scores"]
    navs = "".join(f'<a href="#sec-{e(s["key"])}" class="nav">{e(s["label"])}</a>' for s in d["sections"])
    secs = "".join(section_html(s) for s in d["sections"])
    # WORDMAP：每个生词的每个词元(小写)→满配对象；用于原文/句子里点词就地展开满配卡
    wm = {}
    def _add(v):
        key = "v:" + v["w"]
        obj = dict(v); obj["_key"] = key
        for tk in re.findall(r"[a-zA-Z']+", v["w"].lower()) + [v["w"].lower()]:
            if len(tk) >= 1 and tk not in wm:
                wm[tk] = obj
    for s in d["sections"]:
        for t in s.get("tasks", []):
            for v in t.get("vocab", []): _add(v)
    for v in d.get("wordbank", []): _add(v)  # 全词库：覆盖原文每一个词
    wmjson = json.dumps(wm, ensure_ascii=False).replace("</", "<\\/")
    # 六级/托福「稍难」词形集合（用于正文重点划线高亮，而非逐词划线）
    hardwords = _load_hard_words()
    hardjson = json.dumps(sorted(hardwords), ensure_ascii=False)
    # 错因分布：做错的题/空按类型统计
    tally = {}
    for s in d["sections"]:
        for t in s.get("tasks", []):
            for b in t.get("blanks", []):
                if not b.get("ok"): tally["阅读填词·补词"] = tally.get("阅读填词·补词", 0) + 1
            for q in t.get("questions", []):
                if q.get("your") and q.get("correct") and q["your"] != q["correct"]:
                    tally[q.get("type", "选择题")] = tally.get(q.get("type", "选择题"), 0) + 1
            for r in t.get("repeats", []):
                try:
                    if r.get("score") and float(str(r["score"]).split("/")[0]) < 5:
                        tally["口语跟读·实词听不住"] = tally.get("口语跟读·实词听不住", 0) + 1
                except Exception: pass
    bars = sorted(tally.items(), key=lambda x: -x[1])
    mx = max([c for _, c in bars] + [1])
    barhtml = "".join(f'<div class="bar"><span class="bl">{e(k)}</span><span class="bt"><span class="bf" style="width:{round(c/mx*100)}%"></span></span><span class="bn">{c}</span></div>' for k, c in bars)
    pris = "".join(f'<div class="pri"><b>{i+1}. {e(p["t"])}</b><div class="prw">{e(p.get("why",""))}</div></div>' for i, p in enumerate(d.get("priorities", [])))
    ntask = sum(len(s.get("tasks", [])) for s in d["sections"])
    # 逐题对错清单：错题置顶展示 + 对题折叠
    wrong_qs, right_qs = [], []
    for s in d["sections"]:
        for t in s.get("tasks", []):
            for q in t.get("questions", []):
                if not (q.get("your") and q.get("correct")): continue
                title = t.get("title", "").split("（")[0].split("·")[0].strip()
                item = {"title": title, "q": q}
                (right_qs if q["your"] == q["correct"] else wrong_qs).append(item)
    empty = '<div class="empty">无</div>'
    wrong_items = "".join(
        f'<div class="qlist-item wrong"><span class="qi-mark">❌</span><b>{e(i["title"])} · 题{i["q"]["n"]}</b>'
        f'<span class="qi-ans">你选 {e(i["q"]["your"])} → 正确 {e(i["q"]["correct"])}</span>'
        f'<div class="qi-why">{e(i["q"].get("trap", i["q"].get("why", "")))}</div></div>'
        for i in wrong_qs)
    right_items = "".join(
        f'<div class="qlist-item right"><span class="qi-mark">✅</span><b>{e(i["title"])} · 题{i["q"]["n"]}</b>'
        f'<span class="qi-ans">选 {e(i["q"]["your"])} ✓</span></div>'
        for i in right_qs)
    qlist = (f'<div class="qlist"><div class="dh">📋 逐题对错清单 · 错题置顶（共 {len(wrong_qs)+len(right_qs)} 题）</div>'
             f'<div class="qlist-wrong"><div class="qlist-sub">❌ 错题 · {len(wrong_qs)} 道 · 重点看</div>{wrong_items or empty}</div>'
             f'<details class="qlist-right"><summary>✅ 做对的题 · {len(right_qs)} 道（点开查看）</summary>{right_items}</details>'
             f'</div>') if (wrong_qs or right_qs) else ""
    dash = (f'<div class="dash"><div class="dh">📊 本场诊断仪表盘</div>'
            f'<div class="dgrid"><div class="dcol"><div class="dct">错因分布（做错的题/空按类型）</div>{barhtml}</div>'
            f'<div class="dcol pcol"><div class="dct">🎯 本场最该补的 3 件事</div>{pris}</div></div>'
            f'{qlist}'
            f'<div class="prog"><span>吃透进度</span><span class="pbar"><span class="pfill" id="pfill"></span></span><b id="ptxt">0 / {ntask}</b></div>'
            f'<div class="siglegend"><b>🚦 信号词高亮（听不懂时靠这些画骨架）：</b>'
            f'<span class="wd sig sig-turn">转折/对比</span><span class="wd sig sig-cause">因果/结论</span>'
            f'<span class="wd sig sig-eg">举例/定义</span><span class="wd sig sig-list">列举/递进</span>'
            f'<span class="wd sig sig-emph">强调</span></div></div>')
    return PAGE.replace("__TITLE__", e(d["title"])).replace("__DATE__", e(d["date"])) \
        .replace("__TOTAL__", e(sc["total"])).replace("__R__", e(sc["reading"])) \
        .replace("__L__", e(sc["listening"])).replace("__W__", e(sc["writing"])) \
        .replace("__S__", e(sc["speaking"])).replace("__NAV__", navs).replace("__SECS__", secs) \
        .replace("__DASH__", dash).replace("__WORDMAP__", wmjson).replace("__HARDWORDS__", hardjson)

PAGE = r'''<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__</title><style>
:root{--bg:#f6f3ed;--card:#fffdf9;--ink:#2c2620;--sub:#8a7f70;--accent:#c1662f;--core:#2f8f83;--line:#e7dfd2;--gold:#d9a441;--red:#c0453b;--green:#2f8f6a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.6}
header{position:sticky;top:0;z-index:9;background:rgba(246,243,237,.97);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 18px}
h1{margin:0 0 6px;font-size:18px}
.scores{display:flex;gap:8px;flex-wrap:wrap;font-size:13px;margin-bottom:8px}
.scores span{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:3px 11px}
.scores .tot{background:var(--core);color:#fff;border-color:var(--core);font-weight:700}
.scores .low{color:var(--red);border-color:#e6b9b4}
.navbar{display:flex;gap:7px;flex-wrap:wrap}
.nav{text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:16px;padding:4px 12px;font-size:13px}
.nav:hover{border-color:var(--accent);color:var(--accent)}
main{max-width:940px;margin:0 auto;padding:14px 18px 80px}
h2{font-size:17px;margin:26px 0 8px;padding-bottom:6px;border-bottom:2px solid var(--line)}
.sintro{color:var(--sub);font-size:13.5px;margin-bottom:10px}
.spoints{background:#fbf4e9;border:1px solid #ecdcbf;border-radius:12px;padding:11px 15px;margin-bottom:12px;font-size:14px}
.spoints ul{margin:6px 0 0;padding-left:20px}.spoints li{margin:3px 0}
.task{background:var(--card);border:1px solid var(--line);border-radius:14px;margin:11px 0;overflow:hidden}
.task>summary{cursor:pointer;padding:13px 16px;font-weight:600;list-style:none;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.task>summary::-webkit-details-marker{display:none}
.task>summary::before{content:"▸";color:var(--accent);font-weight:700}
.task[open]>summary::before{content:"▾"}
.ttitle{font-size:15px}.tsc{color:var(--accent);font-weight:700;font-size:13.5px}.ttime{color:var(--sub);font-size:12.5px;font-weight:400}
.tbody{padding:4px 16px 16px;border-top:1px solid var(--line)}
.mh{font-size:13px;color:var(--core);font-weight:700;margin:15px 0 6px}
.prompt{background:#f1f6f4;border-left:3px solid var(--core);padding:9px 13px;border-radius:8px;font-size:14px;margin-top:12px}
.clkwrap{margin-top:2px}
.pwrap{display:flex;flex-direction:column;gap:10px;margin-top:6px}
.pwrap .replay{align-self:flex-start}
.para .clkwrap{margin:0}
.para .clk{background:#fffdf8}
.clk{font-size:15px;background:#fbfaf6;border:1px solid var(--line);border-radius:10px;padding:11px 30px 11px 13px;position:relative}
.clk .wd{cursor:pointer;border-radius:3px}.clk .wd:hover{background:#ffe9cf}
.clk .wd.voc{background:#fff3dd;box-shadow:inset 0 -1.5px 0 #e0a63c;padding:0 2px}
.clk .wd.on{background:#d9f0e6}
.wd.sig{border-radius:3px;padding:0 1px;font-weight:600}
.wd.sig-turn{background:#fbe0da;color:#a83f36}
.wd.sig-cause{background:#d9e8f2;color:#2b6480}
.wd.sig-eg{background:#daf0e2;color:#2a8560}
.wd.sig-list{background:#e9e1f2;color:#6f52a8}
.wd.sig-emph{background:#fbe8cc;color:#a97a1a}
body.nosig .wd.sig{background:none!important;color:inherit!important;font-weight:400}
.siglegend{display:flex;gap:7px;flex-wrap:wrap;font-size:12px;margin-top:9px;padding-top:9px;border-top:1px solid var(--line);align-items:center}
.siglegend b{font-size:12px;color:var(--sub)}
.siglegend span{border-radius:4px;padding:1px 8px;font-weight:600}
.lstrat{background:#f1f6f4;border:1px solid #bfe0d7;border-radius:12px;padding:2px 16px;margin-bottom:14px}
.lstrat>summary{cursor:pointer;font-weight:700;color:var(--core);font-size:14.5px;padding:10px 0;list-style:none}
.lstrat>summary::-webkit-details-marker{display:none}
.lstrat>summary::before{content:"▸ ";color:var(--accent)}.lstrat[open]>summary::before{content:"▾ "}
.lsbody{padding-bottom:10px}
.lsstep{margin:9px 0;font-size:14px;line-height:1.7}.lsstep b{color:var(--accent)}
.lsstep ul{margin:5px 0;padding-left:20px}.lsstep li{margin:3px 0}.lsstep i{color:var(--sub)}
.clk .say-all{position:absolute;top:7px;right:9px;cursor:pointer;opacity:.6;font-size:13px}
.det:empty{display:none}
.det{background:#fff;border:1px solid var(--gold);border-radius:10px;padding:11px 13px;margin-top:6px;font-size:13.5px;box-shadow:0 3px 10px rgba(150,120,70,.1)}
.swd-head{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:5px}
.swd-w{font-size:17px;font-weight:800;cursor:pointer}.swd-p{color:var(--core);font-size:13px}
.swd-marks{margin-left:auto}.wc-mark{border:1px solid var(--line);background:#fff;border-radius:14px;padding:2px 10px;font-size:12px;cursor:pointer}
.wc-mark.on{background:var(--core);color:#fff;border-color:var(--core)}
.swd-def{font-weight:600;margin-bottom:3px}
.swd-sec{margin:5px 0;line-height:1.6}.swd-sec b{color:var(--accent)}
.swd-ex{margin:3px 0 3px 6px}.swd-ex i{color:#4a4038}.swd-ex-zh{color:var(--sub)}.swd-ex-src{color:#b0a596;font-size:11.5px}
.swd-say{cursor:pointer}.swd-say:hover{color:var(--accent)}
.swd-nu{background:#fbf4e9;border-radius:7px;padding:6px 9px;color:var(--ink)}
.swd-sense{margin:3px 0 3px 6px}.swd-sense>b{color:var(--core)}
.tzh{margin-top:7px}
.tzh>summary{cursor:pointer;color:var(--core);font-size:13px;font-weight:700;list-style:none;padding:5px 0}
.tzh>summary::-webkit-details-marker{display:none}.tzh>summary::before{content:"▸ ";color:var(--accent)}.tzh[open]>summary::before{content:"▾ "}
.tzhb{background:#f3faf7;border:1px solid #cfe3db;border-radius:9px;padding:11px 13px;font-size:14px;line-height:1.85;color:#3a4a44;white-space:pre-wrap}
.fam-root{margin:3px 0}.fam-r{font-weight:700;color:var(--core)}.fam-w{display:inline-block;margin:2px 6px 2px 0;cursor:pointer;background:#f3efe6;border-radius:6px;padding:1px 7px}.fam-w:hover{background:#ffe9cf}.fam-g{color:var(--sub);font-size:11.5px;margin-left:3px}
.swd-dict{color:var(--core);font-size:12.5px;text-decoration:none;border-bottom:1px dashed var(--core)}
.youranswer .ya{background:#fdf4f2;border:1px solid #ecc7c1;border-radius:10px;padding:11px 13px;font-size:14px;font-style:italic;color:#6b4a45}
.blanks{margin-top:8px}
.btab{width:100%;border-collapse:collapse;font-size:13.5px}
.btab th{text-align:left;color:var(--sub);font-weight:600;padding:4px 8px;border-bottom:1px solid var(--line)}
.btab td{padding:5px 8px;border-bottom:1px solid #f0ebe0;vertical-align:top}
.btab .num{color:var(--sub);width:24px}.btab .yr{color:var(--red)}.btab tr.ok .yr{color:var(--green)}
.btab .ar{color:var(--green);font-weight:600;white-space:nowrap}.btab tr.ok .ar{color:var(--sub);font-weight:400}
.btab .pt{color:var(--ink)}
.q{border:1px solid var(--line);border-radius:11px;padding:12px 14px;margin:12px 0;background:#fdfcf8}
.qtype{display:inline-block;background:#efe7d6;color:#8a6d2f;font-size:11.5px;font-weight:700;border-radius:5px;padding:1px 7px;margin-right:7px;vertical-align:middle}
.qtxt{font-weight:600;font-size:14.5px;margin-bottom:9px}
.qverdict{display:inline-block;font-weight:800;font-size:12px;border-radius:6px;padding:2px 9px;margin-left:6px;vertical-align:middle;white-space:nowrap}
.qverdict.ok{background:#dff3e6;color:#1d7a44;border:1px solid #b5dfc5}
.qverdict.no{background:#fde7e2;color:#b03a2a;border:1px solid #f3b9ac}
.wrongwhy{background:#fdeeea;border:1px solid #f0c3b5;border-left:4px solid var(--red);border-radius:8px;padding:10px 13px;margin:4px 0 10px;font-size:13.5px;line-height:1.7;color:#7c3a2e}
.wrongwhy b{color:var(--red)}
.opt{border:1px solid var(--line);border-radius:8px;padding:7px 11px;margin:5px 0;font-size:14px}
.opt.correct{background:#eef7f1;border-color:#b6e0c8}
.opt.wrong{background:#fdeeec;border-color:#eec3bd}
.tag{font-size:11px;font-weight:700;border-radius:5px;padding:1px 6px;margin-left:6px}
.t-ok{background:var(--green);color:#fff}.t-no{background:var(--red);color:#fff}
.qpt{background:#fbf4e9;border-radius:8px;padding:8px 11px;margin-top:9px;font-size:13.5px}
.qwhy{color:var(--sub);font-size:13px;margin-top:6px}
.sents{margin-top:6px}.sent{margin:9px 0}.szh{color:var(--sub);font-size:13px;margin-top:3px}.snote{font-size:13px;color:var(--core);margin-top:3px}
.vocab{margin-top:6px}.vgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:9px}
.vcard{position:relative;background:#fbfaf6;border:1px solid var(--line);border-radius:10px;padding:10px 11px 9px}
.vcard .w{font-size:15px;font-weight:700;cursor:pointer}.vcard .w:hover{color:var(--accent)}
.vcard .ipa{color:var(--core);font-size:12px;margin-left:6px}.vzh{font-size:13px;color:var(--sub);margin-top:2px}
.vnote{font-size:12.5px;color:var(--ink);margin-top:4px;border-top:1px dashed var(--line);padding-top:4px}
.vcard .vmk{position:absolute;top:7px;right:8px;display:flex;gap:3px}
.vcard .mk{border:1px solid var(--line);background:#fff;border-radius:50%;width:20px;height:20px;font-size:11px;cursor:pointer;padding:0;line-height:1;color:var(--sub)}
.vcard .mk.ok.on{background:var(--green);color:#fff;border-color:var(--green)}
.vcard .mk.no.on{background:#d98b2b;color:#fff;border-color:#d98b2b}
.vcard.ok{background:#eef6f3;border-color:#bfe0d7}.vcard.no{background:#fdf4ea;border-color:#eccfa6}
.wd.mok{box-shadow:inset 0 -2px 0 var(--green)}.wd.mno{box-shadow:inset 0 -2px 0 #d98b2b;background:#fdf4ea}
.wc-mark.no.on{background:#d98b2b!important;border-color:#d98b2b!important;color:#fff}
.model{margin-top:6px}.mbody{font-size:15px;line-height:1.75}.mzh{color:var(--sub);font-size:13px;margin-top:6px}
.takeaway{background:#f1f6f4;border-radius:10px;padding:11px 14px;margin-top:15px;font-size:14px}
.tools{position:fixed;right:14px;bottom:16px;display:flex;flex-direction:column;gap:8px;z-index:20}
.tools button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:8px 13px;font-size:13px;cursor:pointer;box-shadow:0 2px 8px rgba(150,120,70,.12)}
/* 长难句精拆 */
.g{border-radius:4px;padding:0 2px;color:#fff}
.g-S{background:#2f6f8f}.g-V{background:#c1662f}.g-O{background:#2f8f6a}.g-C{background:#7a5bb0}.g-P{background:#b8860b}.g-M{background:#8a7f70}
.lslegend{display:flex;gap:6px;flex-wrap:wrap;font-size:12px;margin:2px 0 8px}
.lsent .lsi{margin:10px 0 14px}.clk.pre{line-height:2.1}
.lszh{color:var(--sub);font-size:13px;margin-top:5px}
.lsread{background:#f1f6f4;border-radius:8px;padding:7px 11px;margin-top:5px;font-size:13.5px}.lsread b{color:var(--core)}
/* 三步精讲 */
.steps{margin-top:10px;border-left:3px solid var(--gold);padding-left:11px}
.step{margin:6px 0;font-size:13.5px}.sk{display:inline-block;font-weight:700;color:var(--accent);margin-right:7px;white-space:nowrap}
.trap{background:#fdf4f2;border-radius:7px;padding:6px 10px;margin-top:7px;font-size:13px;color:#8a4a42}.trap b{color:var(--red)}
/* 漏洞+补强 */
.weakfix{margin-top:13px;background:#fbf4e9;border:1px solid #ecdcbf;border-radius:10px;padding:10px 14px;font-size:13.5px}
.wf-w{margin-bottom:4px}.wf-w b{color:var(--red)}.wf-f b{color:var(--core)}
/* 口语跟读 */
.repeats .rp{position:relative;background:#fbfaf6;border:1px solid var(--line);border-radius:10px;padding:11px 13px;margin:9px 0}
.rp-sc{position:absolute;top:9px;right:11px;color:var(--accent);font-weight:700;font-size:12.5px}
.rp-h{font-size:13.5px;margin-top:6px}.rp-x{color:var(--red);font-style:italic}
.rp-w{font-size:13px;color:var(--sub);margin-top:3px}.rp-p{font-size:13px;color:var(--core);margin-top:3px}
/* 口语面试 */
.interviews .iv{border:1px solid var(--line);border-radius:11px;padding:12px 14px;margin:10px 0;background:#fdfcf8}
.iv-q{font-weight:600;font-size:14.5px;margin-bottom:7px}
.iv-y{background:#fdf4f2;border-radius:8px;padding:8px 11px;font-size:13.5px;font-style:italic;color:#6b4a45}
.iv-d{margin:8px 0;font-size:13.5px}.iv-d b{color:var(--accent)}
.iv-dl{background:#f1f6f4;border-radius:8px;padding:7px 11px;margin-top:8px;font-size:13px}.iv-dl b{color:var(--core)}
/* 写作红笔改 */
.corrs .corr{margin:7px 0;font-size:14px}.c-x{color:var(--red);text-decoration:line-through}.c-r{color:var(--green);font-weight:600}
.c-w{font-size:12.5px;color:var(--sub);margin-top:2px}
/* 本科总诊断 */
.secdiag{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-bottom:14px}
@media(max-width:640px){.secdiag{grid-template-columns:1fr}}
.dg-w,.dg-f{border:1px solid var(--line);border-radius:12px;padding:11px 15px;font-size:13.5px}
.dg-w{background:#fdf4f2}.dg-f{background:#f1f6f4}
.dg-w b{color:var(--red)}.dg-f b{color:var(--core)}
.secdiag ul{margin:6px 0 0;padding-left:19px}.secdiag li{margin:4px 0}
/* 诊断仪表盘 */
.dash{background:var(--card);border:2px solid var(--accent);border-radius:14px;padding:14px 18px;margin-bottom:16px}
.dh{font-size:16px;font-weight:800;color:var(--accent);margin-bottom:10px}
.dgrid{display:grid;grid-template-columns:1.1fr 1fr;gap:16px}
@media(max-width:680px){.dgrid{grid-template-columns:1fr}}
.dct{font-size:12.5px;color:var(--sub);font-weight:700;margin-bottom:7px}
.bar{display:flex;align-items:center;gap:8px;margin:5px 0;font-size:12.5px}
.bl{width:130px;flex:none;text-align:right;color:var(--ink)}
.bt{flex:1;background:#f0ebe0;border-radius:6px;height:12px;overflow:hidden}
.bf{display:block;height:100%;background:linear-gradient(90deg,#e0913c,#c0453b)}
.bn{width:20px;flex:none;font-weight:700;color:var(--red)}
.pcol{border-left:1px solid var(--line);padding-left:14px}
.pri{margin:7px 0;font-size:13.5px}.pri b{color:var(--accent)}.prw{color:var(--sub);font-size:12.5px;margin-top:1px}
.prog{display:flex;align-items:center;gap:10px;margin-top:12px;padding-top:11px;border-top:1px solid var(--line);font-size:13px}
.qlist{margin-top:14px;padding-top:12px;border-top:1px solid var(--line)}
.qlist .dh{font-size:13.5px;color:var(--core);font-weight:700;margin-bottom:8px}
.qlist-sub{font-size:13px;font-weight:700;color:var(--red);margin:8px 0 5px}
.qlist-item{border-radius:8px;padding:8px 12px;margin:5px 0;font-size:13px}
.qlist-item b{display:inline-block;margin-right:6px}
.qlist-item.wrong{background:#fdf0ec;border:1px solid #f2c6b9;border-left:4px solid var(--red)}
.qlist-item.wrong .qi-mark{font-weight:800;margin-right:4px}
.qlist-item.wrong .qi-ans{color:var(--red);font-weight:600;margin-left:6px}
.qlist-item .qi-why{color:#7c4a3a;font-size:12.5px;margin-top:4px;line-height:1.6}
.qlist-item.right{background:#f2f8f3;border:1px solid #cfe3d6;color:#5f6f66}
.qlist-item.right .qi-ans{color:var(--ok);font-weight:600;margin-left:6px}
.qlist-right{margin-top:8px}
.qlist-right summary{cursor:pointer;font-size:13px;color:var(--ok);font-weight:700;padding:6px 0}
.qlist-right summary::-webkit-details-marker{display:none}
.qlist-right summary::before{content:"▸ "}
.qlist-right[open] summary::before{content:"▾ "}
.pbar{flex:1;background:#f0ebe0;border-radius:8px;height:10px;overflow:hidden}
.pfill{display:block;height:100%;width:0;background:var(--core);transition:width .3s}
/* 先想后看 / 先读后看 */
.reveal,.lsrev{margin-top:9px}
.reveal>summary,.lsrev>summary{cursor:pointer;color:var(--core);font-size:13px;font-weight:700;list-style:none;padding:5px 0}
.reveal>summary::-webkit-details-marker,.lsrev>summary::-webkit-details-marker{display:none}
.reveal>summary::before,.lsrev>summary::before{content:"▸ ";color:var(--accent)}
.reveal[open]>summary::before,.lsrev[open]>summary::before{content:"▾ "}
.revbody{border-top:1px dashed var(--line);padding-top:8px;margin-top:2px}
/* 填词遮罩 */
.spoil{filter:blur(5px);cursor:pointer;border-radius:3px;transition:filter .15s;background:#f3efe6}
.spoil.show{filter:none;background:none}
/* 已吃透 */
.mastery{border:1px solid var(--core);background:#fff;color:var(--core);border-radius:16px;padding:4px 13px;font-size:12.5px;cursor:pointer;margin-bottom:8px}
.mastery.on{background:var(--core);color:#fff}
.mflag{display:none;color:var(--core);font-weight:800}
.task.done>summary{background:#eef6f3}.task.done .mflag{display:inline}
.replay{border:1px solid var(--accent);background:#fff5ec;color:var(--accent);border-radius:14px;padding:2px 10px;font-size:12px;cursor:pointer;font-weight:600}
</style></head><body>
<header><h1>🩺 __TITLE__ · <span style="color:var(--sub);font-weight:400">__DATE__</span></h1>
<div class="scores"><span class="tot">总分 __TOTAL__</span><span>阅读 __R__</span><span>听力 __L__</span><span class="low">写作 __W__</span><span>口语 __S__</span></div>
<div class="navbar">__NAV__</div></header>
<main>__DASH__ __SECS__</main>
<div class="tools"><button id="sigtog">🚦 信号词</button><button id="expno">📋 导出未掌握词</button><button id="rate">🐢 语速</button><button onclick="scrollTo(0,0)">↑ 顶部</button></div>
<script>
const WM=__WORDMAP__;
const HARD=new Set(__HARDWORDS__);   // 六级/托福「稍难」词形：只给这些词加重点划线
// 🚦 信号词（听力骨架）：word→类别
const SIG={but:'turn',however:'turn',yet:'turn',instead:'turn',although:'turn',though:'turn',unlike:'turn',whereas:'turn',nonetheless:'turn',nevertheless:'turn',conversely:'turn',
because:'cause',since:'cause',so:'cause',therefore:'cause',thus:'cause',hence:'cause',consequently:'cause',
called:'eg',like:'eg',
first:'list',firstly:'list',second:'list',secondly:'list',third:'list',then:'list',next:'list',finally:'list',another:'list',also:'list',moreover:'list',furthermore:'list',additionally:'list',besides:'list',
importantly:'emph',actually:'emph',notably:'emph',remarkably:'emph',especially:'emph',particularly:'emph',indeed:'emph',ultimately:'emph',overall:'emph',essentially:'emph'};
const SIGPH=[[['for','example'],'eg'],[['for','instance'],'eg'],[['such','as'],'eg'],[['in','fact'],'eg'],[['known','as'],'eg'],[['referred','to','as'],'eg'],
[['on','the','other','hand'],'turn'],[['in','contrast'],'turn'],[['rather','than'],'turn'],[['even','though'],'turn'],[['on','the','contrary'],'turn'],
[['as','a','result'],'cause'],[['thats','why'],'cause'],[['due','to'],'cause'],[['leading','to'],'cause'],
[['in','addition'],'list'],[['not','only'],'list'],[['but','also'],'list'],
[['of','course'],'emph'],[['in','short'],'emph'],[['in','conclusion'],'emph'],[['the','key'],'emph'],[['the','clever','part'],'emph'],[['most','importantly'],'emph']];
function markSig(box){
  const wds=[...box.querySelectorAll(".wd")]; if(!wds.length)return;
  const cl=wds.map(sp=>(sp.dataset.w||sp.textContent).toLowerCase().replace(/[^a-z]/g,''));
  for(let i=0;i<wds.length;i++){ for(const [ph,cat] of SIGPH){ let ok=ph.every((p,j)=>cl[i+j]===p);
    if(ok){ ph.forEach((p,j)=>wds[i+j].classList.add("sig","sig-"+cat)); i+=ph.length-1; break; } } }
  wds.forEach((sp,i)=>{ if(sp.classList.contains("sig"))return; if(SIG[cl[i]]) sp.classList.add("sig","sig-"+SIG[cl[i]]); });
}
const LS="mockreview-3521";
let state=(()=>{let s=JSON.parse(localStorage.getItem(LS)||"{}");if(Array.isArray(s)){let o={};s.forEach(k=>o[k]='ok');return o;}return s;})();
function setState(k,m){state[k]=(state[k]===m)?'':m;if(!state[k])delete state[k];paint();}
let voices=[],vi=0,rate=.92;
function lv(){voices=speechSynthesis.getVoices().filter(v=>v.lang.startsWith("en"));const p=voices.findIndex(v=>/Samantha|Ava|Google US|United States/i.test(v.name));if(p>=0)vi=p;}
lv();if(speechSynthesis.onvoiceschanged!==undefined)speechSynthesis.onvoiceschanged=lv;
function say(t){if(!t)return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);if(voices[vi])u.voice=voices[vi];u.rate=rate;speechSynthesis.speak(u);}
function esc(s){return (s==null?'':''+s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
// 满配卡（收录词）/ 最小卡（其余词）
function cardHtml(o,word,key){
  const st=state[key]||'';
  let h=`<div class="swd-head"><span class="swd-w swd-say" data-say="${esc(word)}">${esc(o&&o.w||word)} 🔊</span>`;
  if(o&&o.ipa) h+=`<span class="swd-p">${esc(o.ipa)}</span>`;
  h+=`<span class="swd-marks"><button class="wc-mark ok${st==='ok'?' on':''}" data-m="ok">✓ 掌握</button><button class="wc-mark no${st==='no'?' on':''}" data-m="no">✕ 未掌握</button></span></div>`;
  if(!o){ return h+`<div class="swd-def" style="color:#8c8072;font-weight:400">未单独收录释义 — 点 🔊 听音；<a class="swd-dict" target="_blank" href="https://dictionary.cambridge.org/dictionary/english/${encodeURIComponent(word)}">查词典 ↗</a></div>`; }
  if(o.zh) h+=`<div class="swd-def">${esc(o.zh)}</div>`;
  if(o.core) h+=`<div class="swd-sec">🎯 <b>核心意象</b>：${esc(o.core)}</div>`;
  if(Array.isArray(o.senses)&&o.senses.length){ h+=`<div class="swd-sec">🧠 <b>一词多义</b>`; o.senses.forEach(s=>{ if(typeof s==='string')s={gloss:s}; if(!s||typeof s!=='object')return; h+=`<div class="swd-sense"><b>${esc(s.gloss||'')}</b>${s.logic?` — ${esc(s.logic)}`:''}${s.en?`<div class="swd-ex"><span class="swd-say" data-say="${esc(s.en)}"><i>${esc(s.en)}</i> 🔊</span>${s.zh?` <span class="swd-ex-zh">${esc(s.zh)}</span>`:''}</div>`:''}</div>`;}); h+=`</div>`; }
  if(o.ety) h+=`<div class="swd-sec">🏛 <b>词源</b>：${esc(o.ety)}</div>`;
  if(o.ph) h+=`<div class="swd-sec">🗣 <b>发音</b>：${esc(o.ph)}</div>`;
  if(o.tip) h+=`<div class="swd-sec">💡 <b>记忆钩子</b>：${esc(o.tip)}</div>`;
  if(o.note) h+=`<div class="swd-sec">✍️ <b>用法</b>：${esc(o.note)}</div>`;
  if(o.xex&&o.xex.length){ h+=`<div class="swd-sec">✍️ <b>例句</b>`; o.xex.forEach(x=>{ h+=`<div class="swd-ex"><span class="swd-say" data-say="${esc(x.en)}"><i>${esc(x.en)}</i> 🔊</span>${x.zh?` <span class="swd-ex-zh">${esc(x.zh)}</span>`:''}${x.src?` <span class="swd-ex-src">— ${esc(x.src)}</span>`:''}</div>`;}); h+=`</div>`; }
  if(o.syn&&o.syn.length){ const p=o.syn.map(s=> (typeof s==='string')?esc(s):`<span class="swd-say" data-say="${esc(s.w)}">${esc(s.w)} 🔊</span>${s.ipa?` <span class="swd-p">${esc(s.ipa)}</span>`:''}${s.note?` — ${esc(s.note)}`:''}`); h+=`<div class="swd-sec">🔗 <b>近义</b>：${p.join('<br>')}</div>`; }
  if(Array.isArray(o.rootfam)&&o.rootfam.length){ h+=`<div class="swd-sec">🌳 <b>词根家族</b>`; o.rootfam.forEach(r=>{ if(!r||typeof r!=='object')return; const ws=Array.isArray(r.words)?r.words:[]; h+=`<div class="fam-root"><span class="fam-r">${esc(r.root)}</span> ${esc(r.meaning||'')}：`+ws.map(x=>`<span class="fam-w swd-say" data-say="${esc(x.w)}">${esc(x.w)}<span class="fam-g">${esc(x.g||'')}</span></span>`).join('')+`</div>`;}); h+=`</div>`; }
  if(o.nu) h+=`<div class="swd-sec swd-nu">🎯 ${esc(o.nu)}</div>`;
  return h;
}
function openDetail(word,det){
  const clean=word.toLowerCase().replace(/[^a-z']/g,''); if(!clean) return;
  const o=WM[clean]||null, key=o?o._key:('w:'+clean);
  if(det.dataset.open===key){ det.innerHTML=''; det.dataset.open=''; return; }
  try{ det.innerHTML=cardHtml(o,clean,key); }catch(err){ try{det.innerHTML=cardHtml(null,clean,key);}catch(e2){det.innerHTML='';} }
  det.dataset.open=key; say(clean);
  det.querySelectorAll(".swd-say").forEach(el=>el.onclick=ev=>{ev.stopPropagation();say(el.dataset.say);});
  det.querySelectorAll(".wc-mark").forEach(b=> b.onclick=()=>{ setState(key,b.dataset.m); det.querySelectorAll(".wc-mark").forEach(x=>x.classList.toggle("on",x.dataset.m===(state[key]||''))); });
}
// 每个词切成可点 span：点词→就地展开卡（.pre=长难句已预渲染 .wd，不再切）
document.querySelectorAll(".clkwrap").forEach(wrap=>{
  const box=wrap.querySelector(".clk"), det=wrap.querySelector(".det"), full=box.dataset.say;
  if(!box.classList.contains("pre")){
    const txt=box.textContent; box.textContent="";
    txt.split(/(\s+)/).forEach(tok=>{
      if(/^\s+$/.test(tok)){box.appendChild(document.createTextNode(tok));return;}
      const sp=document.createElement("span"); sp.className="wd"; sp.textContent=tok;
      sp.dataset.w=tok.toLowerCase().replace(/[^a-z']/g,''); box.appendChild(sp);
    });
  }
  box.querySelectorAll(".wd").forEach(sp=>{
    const clean=(sp.dataset.w||sp.textContent).toLowerCase().replace(/[^a-z']/g,'');
    sp.dataset.k=WM[clean]?WM[clean]._key:('w:'+clean);
    if(HARD.has(clean)) sp.classList.add("voc");
    sp.onclick=ev=>{ev.stopPropagation();openDetail(clean,det);};
  });
  markSig(box);
  const sa=document.createElement("span"); sa.className="say-all"; sa.textContent="🔊"; sa.title="读整段/句";
  sa.onclick=ev=>{ev.stopPropagation();say(full);}; box.appendChild(sa);
});
document.querySelectorAll(".say").forEach(el=>el.onclick=e=>{e.stopPropagation();say(el.dataset.say);});
function paint(){
  document.querySelectorAll(".vcard").forEach(c=>{const s=state[c.dataset.mk]||'';c.classList.toggle("ok",s==='ok');c.classList.toggle("no",s==='no');c.querySelectorAll(".mk").forEach(b=>b.classList.toggle("on",b.dataset.m===s));});
  document.querySelectorAll(".wd").forEach(w=>{const s=state[w.dataset.k]||'';w.classList.toggle("mok",s==='ok');w.classList.toggle("mno",s==='no');});
  localStorage.setItem(LS,JSON.stringify(state));
  const nno=Object.values(state).filter(v=>v==='no').length,eb=document.getElementById("expno");if(eb)eb.textContent="📋 导出未掌握词 ("+nno+")";
}
document.querySelectorAll(".vcard .mk").forEach(b=>b.onclick=e=>{e.stopPropagation();setState(b.closest(".vcard").dataset.mk,b.dataset.m);});
paint();
document.getElementById("expno").onclick=function(){
  const out=[];for(const k in state){if(state[k]!=='no')continue;const w=k.replace(/^[vw]:/,'').toLowerCase();const o=WM[w]||{w:k.replace(/^[vw]:/,'')};
    out.push({w:o.w||w,ipa:o.ipa||'',zh:o.zh||'',core:o.core||'',ety:o.ety||'',ph:o.ph||'',tip:o.tip||'',xex:o.xex||[],syn:o.syn||[],nu:o.nu||'',senses:o.senses||[]});}
  if(!out.length){alert("你还没标记任何『未掌握』的词。点单词卡里的『✕ 未掌握』来标记。");return;}
  const txt=JSON.stringify(out,null,1);
  (navigator.clipboard?navigator.clipboard.writeText(txt):Promise.reject()).then(()=>alert("已复制 "+out.length+" 个未掌握词到剪贴板，发给 cc 汇入背词计划")).catch(()=>{prompt("复制以下未掌握词（发给 cc 汇入背词计划）：",txt);});
};
// 填词遮罩：点击显形
document.querySelectorAll(".spoil").forEach(sp=>sp.onclick=e=>{e.stopPropagation();sp.classList.toggle("show");});
// 已吃透 + 进度
const MK="mockreview-mastered";let mset=new Set(JSON.parse(localStorage.getItem(MK)||"[]"));
const ntask=document.querySelectorAll(".task[data-tid]").length;
function mpaint(){
  document.querySelectorAll(".task[data-tid]").forEach(t=>{const on=mset.has(t.dataset.tid);t.classList.toggle("done",on);const b=t.querySelector(".mastery");if(b){b.classList.toggle("on",on);b.textContent=on?"✓ 已吃透（点取消）":"✓ 标这篇已吃透";}});
  const n=mset.size,pf=document.getElementById("pfill"),pt=document.getElementById("ptxt");
  if(pf)pf.style.width=Math.round(n/Math.max(ntask,1)*100)+"%";
  if(pt)pt.textContent=n+" / "+ntask;
  localStorage.setItem(MK,JSON.stringify([...mset]));
}
document.querySelectorAll(".mastery").forEach(b=>b.onclick=e=>{e.stopPropagation();const tid=b.dataset.tid;mset.has(tid)?mset.delete(tid):mset.add(tid);mpaint();});
mpaint();
document.getElementById("sigtog").onclick=function(){document.body.classList.toggle("nosig");this.style.opacity=document.body.classList.contains("nosig")?".5":"1";};
document.getElementById("rate").onclick=function(){rate=rate>=1.1?.7:rate+.2;this.textContent="🐢 "+rate.toFixed(1)+"x";say("speed check");};
</script></body></html>'''

def main():
    mid = sys.argv[1] if len(sys.argv) > 1 else "3.5分-2026-08-21"
    d = json.load(open(os.path.join(DATA, mid + ".json"), encoding="utf-8"))
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, mid + ".html"), "w", encoding="utf-8").write(build(d))
    nq = sum(len(t.get("questions", [])) + len(t.get("blanks", [])) for s in d["sections"] for t in s.get("tasks", []))
    nv = sum(len(t.get("vocab", [])) for s in d["sections"] for t in s.get("tasks", []))
    print(f"✅ 复习页/{mid}.html — {len(d['sections'])} 科 · {sum(len(s.get('tasks',[])) for s in d['sections'])} 篇/任务 · {nq} 题/空 · {nv} 生词")

if __name__ == "__main__":
    main()
