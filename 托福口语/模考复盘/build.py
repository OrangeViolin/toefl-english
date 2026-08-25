#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""口语模考复盘 · 每场一页（Task1 跟读 + Task2 面试 同页）
data/<mock-id>.json → 复盘页/<mock-id>.html + index.html
每个 mock：{id,time,title,total,t1score,t2score,task1[],task2[]}
  task1 句：{en,zh,chunks[],skeleton[],err(她上次听成的),score}
  task2 题：{q,outline,model,words,outline2,model2,words2,frames,vocab,my(她的作答),score}
用法：python3 build.py
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "复盘页")
os.makedirs(OUT, exist_ok=True)

def e(s): return html.escape(str(s if s is not None else ""))

PAGE = r"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 口语模考复盘</title>
<script src="../../speech-core.js"></script>
<style>
:root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--blue:#4a5cc7;--ok:#4a9e6f;--bad:#c04a3a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}
.wrap{max-width:860px;margin:0 auto;padding:30px 20px 90px}
a.back{color:var(--core);text-decoration:none;font-size:13px}
h1{font-size:23px;margin:8px 0 2px}
.meta{color:var(--muted);font-size:13.5px;margin-bottom:6px}
.scores{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0 20px}
.scores span{background:#eef6f3;border:1px solid #cfe3db;border-radius:20px;padding:4px 12px;font-size:13px;color:#2c6a60}
.scores b{color:var(--accent)}
.tabbar{display:flex;gap:8px;margin:0 0 16px;position:sticky;top:0;background:var(--bg);padding:8px 0;z-index:5}
.tab{flex:1;border:1px solid var(--line);background:var(--card);border-radius:12px;padding:11px;font-size:15px;font-weight:800;cursor:pointer;text-align:center;color:#5f574c}
.tab.on{background:var(--core);color:#fff;border-color:var(--core)}
.sec{display:none}.sec.on{display:block}
.hint{background:#fff6e8;border:1px solid #f0d9b0;border-left:4px solid var(--accent);border-radius:10px;padding:10px 13px;font-size:13px;margin-bottom:16px}
/* Task1 */
.s-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:15px 16px;margin-bottom:13px}
.s-top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px}
.s-no{font-weight:800;font-size:14px;color:var(--core)}
.s-sc{margin-left:auto;font-size:12px;background:#eef6f3;border:1px solid #cfe3db;color:#2c6a60;border-radius:20px;padding:2px 9px}
.btnrow{display:flex;gap:7px;flex-wrap:wrap;margin:6px 0}
.btn{border:1px solid var(--line);background:#fff;border-radius:9px;padding:6px 11px;font-size:13px;cursor:pointer;font-family:inherit;color:#5f574c}
.btn:hover{border-color:var(--accent)}
.btn.rec{background:var(--accent);color:#fff;border:0}
.btn.rec.on{background:var(--bad)}
.en{font-family:Georgia,serif;font-size:16px;color:#2f2a24;margin:4px 0}
.en.hidden{filter:blur(6px);cursor:pointer}
.zh{font-size:13.5px;color:var(--muted)}
.chunks{margin:8px 0;display:none}.chunks.show{display:block}
.chunk{display:inline-block;background:#eef6f3;border:1px solid #cfe3db;border-radius:8px;padding:3px 9px;margin:3px;font-size:13.5px;cursor:pointer}
.chunk .sk{color:var(--core);font-size:11px;display:block}
.err{font-size:12.5px;color:var(--bad);background:#fbecea;border-radius:7px;padding:6px 9px;margin-top:7px}
.mine{font-size:12.5px;color:#5f574c;background:#f4f1ea;border-radius:7px;padding:6px 9px;margin-top:6px}
/* Task2 */
.q-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin-bottom:15px}
.q-txt{font-size:15px;font-weight:700;margin-bottom:6px}
details.fold{border-top:1px dashed var(--line);margin-top:10px;padding-top:8px}
summary{cursor:pointer;font-weight:700;font-size:14px;color:var(--core)}
.vlabel{display:inline-block;background:#eef6f3;border:1px solid #cfe3db;color:#2c6a60;font-size:12.5px;font-weight:700;border-radius:6px;padding:3px 10px;margin:11px 0 5px}
.vlabel.v3{background:#f5ecdd;border-color:#e3ce9f;color:#9a6a1f}
.vlabel.v4{background:#eaf2f8;border-color:#bcd6e8;color:#3a6b8f}
table.ol{width:100%;border-collapse:collapse;font-size:13.5px;margin-top:4px}
table.ol td{padding:6px 9px;border:1px solid var(--line);vertical-align:top}
table.ol .r{width:70px;font-weight:700;color:#fff;text-align:center;background:var(--blue)}
.ln{margin:6px 0;font-size:15px}.ln .mk{font-weight:700;color:var(--accent)}
.playall{background:var(--core);color:#fff;border:0;border-radius:8px;padding:4px 11px;font-size:12.5px;cursor:pointer;margin:6px 0}
.wc{font-size:12px;color:var(--muted);margin-top:4px}
.frames div,.vocab div{font-size:13px;margin:4px 0}.vocab .w{color:var(--core);cursor:pointer;font-weight:700}.vocab .ipa{color:var(--muted);margin:0 6px}
.say{cursor:pointer}
.live{font-size:12.5px;color:var(--muted);margin:6px 0}
</style></head><body><div class="wrap">
<a class="back" href="../index.html">← 全部模考</a>
<h1>__TITLE__</h1>
<div class="meta">🕒 模考时间 __TIME__</div>
<div class="scores">__SCORES__</div>
<div class="tabbar"><div class="tab on" data-t="t1" onclick="tab('t1')">🎧 Task 1 跟读</div><div class="tab" data-t="t2" onclick="tab('t2')">🎤 Task 2 面试</div></div>
<div class="sec on" id="t1"><div class="hint">听一句→逐字复述。🔊播放 / 🐢慢读 / 🧩分块 / 🦴骨架都能反复用；🎙录音后点句子看标准答案。<b>你这次错在实词听不住</b>，分块时把耳朵全压在名词/动词上。</div>__TASK1__</div>
<div class="sec" id="t2"><div class="hint">读题→看思路自己说→点范文对照（①单理由 ②两理由，先背单理由）→🎙录音→复制报告发 cc 判分。~80 词、~40 秒说顺。</div>__TASK2__</div>
</div>
<script>
const V=window.VocaSpeech;
let voices=[];function lv(){voices=window.speechSynthesis?speechSynthesis.getVoices():[]}
if(window.speechSynthesis){lv();speechSynthesis.onvoiceschanged=lv}
function say(t,rate){if(!window.speechSynthesis)return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=rate||0.95;const v=voices.find(v=>/en-US/i.test(v.lang)&&/Samantha|Aria|Jenny|Google US|female/i.test(v.name))||voices.find(v=>/en-US/i.test(v.lang));if(v)u.voice=v;speechSynthesis.speak(u)}
function tab(t){document.querySelectorAll('.tab').forEach(x=>x.classList.toggle('on',x.dataset.t===t));document.querySelectorAll('.sec').forEach(x=>x.classList.toggle('on',x.id===t));window.scrollTo(0,0)}
function reveal(el){el.classList.remove('hidden')}
function toggleChunks(id){document.getElementById(id).classList.toggle('show')}
// 录音（复用 speech-core）
async function rec(btn,ref){
  if(!V||!V.supported){alert('请用 Chrome 打开、并先双击 start.command 启动录音服务');return}
  if(btn.dataset.on==='1'){return}
  btn.dataset.on='1';btn.classList.add('on');btn.textContent='⏹ 停止';
  const live=btn.closest('.s-card,.q-card').querySelector('.live');
  try{
    await V.record(15,s=>{if(live)live.textContent='录音中… '+s+'s'},async url=>{
      btn.dataset.on='';btn.classList.remove('on');btn.textContent='🎙 录音';
      if(live)live.textContent='转写中…';
      try{const tr=await V.transcribe(url);if(live)live.innerHTML='你说的：<b>'+(tr||'(空)')+'</b>'+(ref?'<br>标准：'+ref:'')}
      catch(e){if(live)live.textContent='（转写失败，可回听）'}
    });
  }catch(e){btn.dataset.on='';btn.classList.remove('on');btn.textContent='🎙 录音';if(live)live.textContent='（录音需要 start.command 启动服务）'}
}
function copyRep(q){
  const full=v=>v.map(l=>(l.mk?l.mk+' ':'')+l.en).join(' ');
  let r='【口语模考·面试题练习判分】\n题目：'+q.q+'\n\n参考范文（①单理由）：\n'+full(q.model)+'\n';
  if(q.model2)r+='\n参考范文（②两理由）：\n'+full(q.model2)+'\n';
  r+='\n我录音说的（粘贴转写）：\n____\n\n请 cc 按维度打分(切题/展开/流利度/语法词汇/发音韵律)+指出问题+给~80词修改稿。';
  (navigator.clipboard?navigator.clipboard.writeText(r).then(()=>alert('已复制，粘贴给 cc'),()=>prompt('复制：',r)):prompt('复制：',r))
}
window.__Q={};
document.querySelectorAll('[data-say]').forEach(el=>el.onclick=e=>{e.stopPropagation();say(el.dataset.say)});
</script>
</body></html>"""

def task1_html(t1):
    out = []
    for i, s in enumerate(t1):
        en = e(s["en"]); zh = e(s.get("zh", ""))
        cid = f"ck{i}"
        chunks = "".join(f'<span class="chunk say" data-say="{e(c)}">{e(c)}<span class="sk">{e(s["skeleton"][j] if j < len(s.get("skeleton",[])) else "")}</span></span>'
                          for j, c in enumerate(s.get("chunks", [])))
        skel = " / ".join(s.get("skeleton", []))
        err = f'<div class="err">⚠️ 你这次听成：{e(s["err"])}</div>' if s.get("err") else ""
        out.append(f'''<div class="s-card">
  <div class="s-top"><span class="s-no">句 {i+1}</span>{f'<span class="s-sc">{e(s.get("score"))}/5</span>' if s.get("score") else ""}</div>
  <div class="btnrow">
    <button class="btn say" data-say="{en}">🔊 播放</button>
    <button class="btn" onclick="say('{en}',0.6)">🐢 慢读</button>
    <button class="btn" onclick="toggleChunks('{cid}')">🧩 分块</button>
    <button class="btn" onclick="alert('骨架：{e(skel)}')">🦴 骨架</button>
    <button class="btn rec" onclick="rec(this,'{en}')">🎙 录音</button>
  </div>
  <div class="chunks" id="{cid}">{chunks}</div>
  <div class="en hidden" onclick="reveal(this)">{en}</div>
  <div class="zh">{zh}</div>
  {err}
  <div class="live"></div>
</div>''')
    return "\n".join(out)

def outline_tbl(o):
    rows = "".join(f'<tr><td class="r">{e(r["role"])}</td><td>{"<ul>"+"".join("<li>"+e(b)+"</li>" for b in r["bullets"])+"</ul>" if r.get("bullets") else e(r.get("text",""))}</td></tr>' for r in o)
    return f'<table class="ol">{rows}</table>'

def model_block(model, words):
    full = " ".join((l.get("mk","")+" "+l["en"]).strip() for l in model)
    lns = "".join(f'<div class="ln"><span class="mk">{e(l.get("mk",""))}</span> {e(l["en"])}</div>' for l in model)
    return f'<button class="playall say" data-say="{e(full)}">🔊 整段朗读</button><div>{lns}</div><div class="wc">共 {words or "~"} 词 · 约 {round((words or 80)/2)} 秒</div>'

def task2_html(t2):
    out = []
    for i, q in enumerate(t2):
        mine = f'<div class="mine">🎙 你这次答的：{e(q["my"])}</div>' if q.get("my") else ""
        sc = f'<span class="s-sc" style="float:right">{e(q.get("score"))}/6</span>' if q.get("score") else ""
        ol2 = f'<div class="vlabel">② 两理由版</div>{outline_tbl(q["outline2"])}' if q.get("outline2") else ""
        mo2 = f'<div class="vlabel">② 两理由版 · {q.get("words2","")} 词</div>{model_block(q["model2"], q.get("words2"))}' if q.get("model2") else ""
        ol3 = f'<div class="vlabel v3">③ 高级版（进阶词句）</div>{outline_tbl(q["outline3"])}' if q.get("outline3") else ""
        mo3 = f'<div class="vlabel v3">③ 高级版（进阶词句）· {q.get("words3","")} 词</div>{model_block(q["model3"], q.get("words3"))}' if q.get("model3") else ""
        ol4 = f'<div class="vlabel v4">④ 精简口语版</div>{outline_tbl(q["outline4"])}' if q.get("outline4") else ""
        mo4 = f'<div class="vlabel v4">④ 精简口语版 · {q.get("words4","")} 词</div>{model_block(q["model4"], q.get("words4"))}' if q.get("model4") else ""
        lbl1o = '<div class="vlabel">① 单理由版</div>' if q.get("outline2") else ""
        lbl1m = f'<div class="vlabel">① 单理由版 · {q.get("words","")} 词</div>' if q.get("model2") else ""
        frames = ("<div class=\"frames\">"+"".join(f'<div><b>{e(f["t"])}</b> — {e(f["zh"])}</div>' for f in q.get("frames",[]))+"</div>") if q.get("frames") else ""
        vocab = ("<div class=\"vocab\">"+"".join(f'<div><span class="w say" data-say="{e(v["w"])}">{e(v["w"])}</span><span class="ipa">{e(v.get("ipa",""))}</span>{e(v["zh"])}</div>' for v in q.get("vocab",[]))+"</div>") if q.get("vocab") else ""
        qj = json.dumps({"q": q["q"], "model": q["model"], "model2": q.get("model2")}, ensure_ascii=False).replace('"', "&quot;")
        expr_block = ('<details class="fold"><summary>🔑 常见表达 &amp; 单词</summary>' + frames + vocab + '</details>') if (frames or vocab) else ""
        out.append(f'''<div class="q-card">
  <div class="q-txt">{sc}题 {i+1}：{e(q["q"])}</div>
  {mine}
  <details class="fold" open><summary>💡 思路表格</summary>{lbl1o}{outline_tbl(q["outline"])}{ol2}{ol3}{ol4}</details>
  <details class="fold"><summary>📖 范文（① 单理由 / ② 两理由{" / ③ 高级版" if q.get("model3") else ""}{" / ④ 精简口语版" if q.get("model4") else ""}）</summary>{lbl1m}{model_block(q["model"], q.get("words"))}{mo2}{mo3}{mo4}</details>
  {expr_block}
  <div class="btnrow"><button class="btn rec" onclick="rec(this,'')">🎙 录音</button><button class="btn" onclick='copyRep({qj})'>📋 复制报告给 cc</button></div>
  <div class="live"></div>
</div>''')
    return "\n".join(out)

def build_page(d):
    scores = f'<span>总分 <b>{e(d.get("total","—"))}</b></span><span>Task1 {e(d.get("t1score","—"))}</span><span>Task2 {e(d.get("t2score","—"))}</span>'
    return (PAGE.replace("__TITLE__", e(d["title"]))
                .replace("__TIME__", e(d["time"]))
                .replace("__SCORES__", scores)
                .replace("__TASK1__", task1_html(d.get("task1", [])))
                .replace("__TASK2__", task2_html(d.get("task2", []))))

INDEX = r"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>口语模考复盘</title><style>
:root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC",sans-serif;line-height:1.6}
.wrap{max-width:820px;margin:0 auto;padding:38px 20px 80px}h1{font-size:25px;margin:0 0 4px}.sub{color:var(--muted);margin-bottom:22px}
.cards{display:grid;gap:13px}
a.mk{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;text-decoration:none;color:inherit}
a.mk:hover{border-color:var(--accent)}
.mk .t{font-size:12.5px;color:var(--core)}.mk h2{font-size:18px;margin:3px 0 6px}
.mk .sc{font-size:13px;color:var(--muted)}.mk .sc b{color:var(--accent)}
footer{margin-top:24px;color:#a89a86;font-size:12px}
</style></head><body><div class="wrap">
<h1>🎤 口语模考复盘</h1>
<div class="sub">每一场口语模考 → 一页练完 <b>Task 1 跟读 + Task 2 面试</b>。按模考时间排列，对应你哪一次做的。</div>
<div class="cards">__CARDS__</div>
<footer>data/*.json → build.py → 复盘页/*.html ｜ 共 __N__ 场</footer>
</div></body></html>"""

def main():
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    mocks = []
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        mocks.append(d)
        open(os.path.join(OUT, d["id"] + ".html"), "w", encoding="utf-8").write(build_page(d))
        print(f"  ✓ {d['title']}（{d['time']}）· T1 {len(d.get('task1',[]))}句 · T2 {len(d.get('task2',[]))}题")
    mocks.sort(key=lambda x: x.get("time", ""), reverse=True)
    cards = "".join(f'<a class="mk" href="复盘页/{e(d["id"])}.html"><div class="t">🕒 {e(d["time"])}</div><h2>{e(d["title"])}</h2>'
                    f'<div class="sc">总分 <b>{e(d.get("total","—"))}</b> · Task1 {e(d.get("t1score","—"))} · Task2 {e(d.get("t2score","—"))} · T1 {len(d.get("task1",[]))}句/T2 {len(d.get("task2",[]))}题</div></a>'
                    for d in mocks)
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(INDEX.replace("__CARDS__", cards).replace("__N__", str(len(mocks))))
    print(f"完成：{len(mocks)} 场 → 复盘页/ + index.html")

if __name__ == "__main__":
    main()
