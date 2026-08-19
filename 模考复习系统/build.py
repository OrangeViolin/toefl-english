#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
托福模考复习系统 · 渲染器（文段中心版）
  data/<得分-日期>.json  →  复习页/<得分-日期>.html + index.html
用法：  python3 build.py
布局：每篇阅读文段 → ①原文(生词可点击,跳到下方词卡) → ②翻译 → ③单词卡(音标/释义/记忆钩子/掌握状态/错词标注)
      + 美音 TTS + 背记模式 + 拼写测验(全部/只练拼错词)。配套文字分析见 学习方法论/模考分析/。
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT  = os.path.join(ROOT, "复习页")
os.makedirs(OUT, exist_ok=True)

PAGE = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--bad:#c0453a;--blue:#4a5cc7}
  *{box-sizing:border-box}html,body{margin:0}
  body{background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
  a{color:var(--accent);text-decoration:none}
  .wrap{max-width:840px;margin:0 auto;padding:22px 20px 120px}
  h1{font-size:23px;margin:0 0 2px}
  .sub{color:var(--muted);font-size:13px;margin-bottom:12px}
  .ana{font-size:12.5px;color:var(--muted)}
  .bar{position:sticky;top:0;z-index:20;background:var(--bg);padding:10px 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center;border-bottom:1px solid var(--line);margin-bottom:6px}
  .bar button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:6px 13px;font-size:13px;cursor:pointer;color:#5f574c;font-family:inherit}
  .bar button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
  .bar .spacer{flex:1}.count{font-size:13px;color:var(--muted)}
  /* 文段 */
  .pg{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin-top:20px;box-shadow:0 2px 12px rgba(150,120,70,.05)}
  .pgh{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:8px}
  .pgh h2{font-size:18px;margin:0}
  .pgmeta{font-size:12px;color:#fff;background:var(--core);border-radius:20px;padding:2px 9px}
  .seclbl{font-size:12.5px;color:var(--core);font-weight:700;margin:14px 0 6px}
  .en{font-size:15.5px;line-height:2;background:#faf7ef;border:1px solid var(--line);border-radius:10px;padding:12px 14px}
  .zhp{font-size:14.5px;color:#5f574c;background:#f4f1ea;border-radius:10px;padding:11px 14px}
  .hs{border-left:3px solid var(--core);background:#eef6f4;border-radius:0 10px 10px 0;padding:10px 13px;margin:9px 0}
  .hs-en{font-size:15px;line-height:1.95}
  .hs-an{font-size:12.8px;color:#2c6a60;margin-top:7px;background:#fff;border-radius:8px;padding:7px 10px}
  .hs-zh{font-size:13.5px;color:#5f574c;margin-top:6px}
  .pw{cursor:pointer;border-bottom:1.5px dotted var(--accent);padding:0 1px}
  .pw:not(.done){background:#fde7d6}
  .pw.done{border-bottom-color:#cbb;background:transparent;color:#6f6656}
  .pw:hover{background:#f7cfa8}
  /* 词卡 */
  .cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-top:4px}
  .card{border:1px solid var(--line);border-radius:12px;padding:11px 13px;background:#fffef9;scroll-margin-top:70px}
  .card.done{opacity:.6}
  .card.flash{animation:fl 1.1s}
  @keyframes fl{0%,60%{box-shadow:0 0 0 3px var(--accent)}100%{box-shadow:none}}
  .whead{display:flex;align-items:center;gap:7px;flex-wrap:wrap}
  .w{font-size:19px;font-weight:800}
  .ipa{color:var(--core);font-size:13.5px}.pos{color:var(--muted);font-size:12px;font-style:italic}
  .spk{background:var(--blue);color:#fff;border:0;border-radius:8px;padding:3px 9px;font-size:12px;cursor:pointer;font-family:inherit}
  .zh{font-size:15px;font-weight:700;margin:6px 0 2px}
  body.recite .zh{filter:blur(6px);cursor:pointer}
  .hook{font-size:12.5px;color:#6f6656;background:#faf7ef;border-radius:7px;padding:6px 9px;margin-top:6px}
  .err{font-size:12.5px;color:var(--bad);background:#fbecea;border-radius:7px;padding:5px 9px;margin-top:6px}
  .err s{opacity:.8}
  .mbtn{border:1px solid var(--line);background:#fff;border-radius:8px;padding:4px 10px;font-size:12px;cursor:pointer;font-family:inherit;color:#5f574c;margin-top:7px}
  .mbtn.on{background:var(--ok);color:#fff;border-color:var(--ok)}
  /* 拼写测验 */
  .quiz{position:fixed;inset:0;background:rgba(40,36,30,.5);z-index:50;display:flex;align-items:center;justify-content:center;padding:20px}
  .qbox{background:var(--card);border-radius:16px;padding:22px;max-width:460px;width:100%}
  .qprog{font-size:12.5px;color:var(--muted)}
  .qzh{font-size:20px;font-weight:800;margin:6px 0 4px}
  .qpos{font-size:13px;color:var(--muted)}
  .qin{width:100%;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:17px;font-family:inherit;margin-top:12px}
  .qin:focus{outline:none;border-color:var(--accent)}
  .qres{margin-top:10px;font-size:15px;min-height:24px}
  .qres.ok{color:var(--ok)}.qres.no{color:var(--bad)}
  .qbtns{display:flex;gap:8px;margin-top:14px}
  .qbtns button{flex:1;border:0;border-radius:10px;padding:10px;font-size:14px;cursor:pointer;font-family:inherit}
  .qbtns .p{background:var(--accent);color:#fff}.qbtns .g{background:#efe8d8;color:#5f574c}
</style></head>
<body>
<div class="wrap">
  <h1>📚 __TITLE__</h1>
  <div class="sub">每篇：原文（<b>点橙色词</b>跳到词卡）→ 翻译 → 单词。🔊美音 · 🙈背记遮释义 · ✍️拼写测验。<span class="ana">__ANALYSIS__</span></div>
  <div class="bar">
    <button id="recite">🙈 背记模式</button>
    <button id="quizAll">✍️ 拼写测验</button>
    <button id="quizErr">🔴 只练拼错词</button>
    <span class="spacer"></span><span class="count" id="count"></span>
  </div>
  <div id="body"></div>
</div>
<div id="quizmount"></div>
<script>
const DATA = __DATA__;
const KEY = 'toefl-review:' + DATA.id;
const $ = s => document.querySelector(s);
const esc = s => (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
let mastered = new Set(JSON.parse(localStorage.getItem(KEY)||'[]'));
const saveM = ()=> localStorage.setItem(KEY, JSON.stringify([...mastered]));
let recite=false;

/* TTS 美音 */
let voices=[]; const lv=()=>{voices=window.speechSynthesis?speechSynthesis.getVoices():[]};
if(window.speechSynthesis){ lv(); speechSynthesis.onvoiceschanged=lv; }
function say(t){ if(!window.speechSynthesis)return; speechSynthesis.cancel();
  const u=new SpeechSynthesisUtterance(t); u.lang='en-US'; u.rate=0.9;
  const v=voices.find(v=>/en-US/i.test(v.lang)&&/Samantha|Aria|Jenny|Google US|female/i.test(v.name))||voices.find(v=>/en-US/i.test(v.lang)); if(v)u.voice=v;
  speechSynthesis.speak(u); }

const allWords = ()=> DATA.passages.flatMap((p,pi)=>p.words.map((w,wi)=>({...w,pi,wi})));
function totalCount(){ const all=allWords(); return `已掌握 ${all.filter(w=>mastered.has(w.w)).length}/${all.length}`; }

/* 原文/长难句里把生词包成可点击 span（共用一套词表 map） */
function buildMap(p){ const map={}; p.words.forEach((w,wi)=>{ map[(w.form||w.w).toLowerCase()]=wi; map[w.w.toLowerCase()]=wi; }); return map; }
function linkText(text, p, pi, map){
  return esc(text).replace(/[A-Za-z][A-Za-z'’-]*/g, tok=>{
    const wi=map[tok.toLowerCase()];
    if(wi==null) return tok;
    return `<span class="pw" data-w="${esc(p.words[wi].w)}" data-c="card-${pi}-${wi}">${tok}</span>`;
  });
}

function render(){
  $('#count').textContent = totalCount();
  $('#body').innerHTML = DATA.passages.map((p,pi)=>{
    const map=buildMap(p);
    const hardHtml = (p.hard&&p.hard.length)
      ? `<div class="seclbl">🔍 长难句精析（在句子里记词）</div>` + p.hard.map(h=>
          `<div class="hs"><div class="hs-en">${linkText(h.en,p,pi,map)}</div>`+
          `<div class="hs-an">🧩 ${esc(h.analysis)}</div>`+
          `<div class="hs-zh">${esc(h.zh)}</div></div>`).join('')
      : '';
    return `<section class="pg">
      <div class="pgh"><h2>${esc(p.title)}</h2>${p.meta?`<span class="pgmeta">${esc(p.meta)}</span>`:''}</div>
      <div class="seclbl">📄 原文</div>
      <div class="en">${linkText(p.en,p,pi,map)}</div>
      <div class="seclbl">🀄 翻译</div>
      <div class="zhp">${esc(p.zh)}</div>
      ${hardHtml}
      <div class="seclbl">📓 单词（${p.words.length}）</div>
      <div class="cards">${p.words.map((w,wi)=>card(w,pi,wi)).join('')}</div>
    </section>`;
  }).join('');
  wire();
  paint();
}
function card(w,pi,wi){
  const done=mastered.has(w.w);
  return `<div class="card ${done?'done':''}" id="card-${pi}-${wi}">
    <div class="whead"><span class="w">${esc(w.w)}</span><span class="ipa">${esc(w.ipa||'')}</span><span class="pos">${esc(w.pos||'')}</span>
      <button class="spk" data-say="${esc(w.w)}">🔊</button></div>
    <div class="zh">${esc(w.zh)}</div>
    ${w.hook?`<div class="hook">🔑 ${esc(w.hook)}</div>`:''}
    ${w.err?`<div class="err">⚠️ 本次拼错：你写成 <s>${esc(w.err)}</s></div>`:''}
    <button class="mbtn ${done?'on':''}" data-m="${esc(w.w)}">${done?'✓ 已掌握':'标记已掌握'}</button>
  </div>`;
}
function paint(){ document.querySelectorAll('.pw').forEach(el=>el.classList.toggle('done', mastered.has(el.dataset.w))); }
function wire(){
  document.querySelectorAll('[data-say]').forEach(b=>b.onclick=()=>say(b.dataset.say));
  document.querySelectorAll('.zh').forEach(el=>el.onclick=()=>{ if(recite) el.style.filter='none'; });
  document.querySelectorAll('[data-m]').forEach(b=>b.onclick=()=>{ const w=b.dataset.m;
    mastered.has(w)?mastered.delete(w):mastered.add(w); saveM();
    const card=b.closest('.card'); const on=mastered.has(w);
    card.classList.toggle('done',on); b.classList.toggle('on',on); b.textContent=on?'✓ 已掌握':'标记已掌握';
    $('#count').textContent=totalCount(); paint(); });
  document.querySelectorAll('.pw').forEach(el=>el.onclick=()=>{
    const c=document.getElementById(el.dataset.c); if(!c)return;
    c.scrollIntoView({behavior:'smooth',block:'center'}); c.classList.remove('flash'); void c.offsetWidth; c.classList.add('flash'); });
}
$('#recite').onclick=()=>{ recite=!recite; document.body.classList.toggle('recite',recite); $('#recite').classList.toggle('on',recite);
  if(recite) document.querySelectorAll('.zh').forEach(el=>el.style.filter=''); };

/* 拼写测验：看中文+听音→打出英文 */
function spell(pool){
  if(!pool.length){ alert('没有可测的词'); return; }
  let i=0, sc=0;
  function step(){
    if(i>=pool.length){ $('#quizmount').innerHTML=`<div class="quiz"><div class="qbox"><div class="qzh">✅ 完成：${sc}/${pool.length} 拼对</div>
      <div class="qbtns"><button class="p" onclick="document.getElementById('quizmount').innerHTML=''">关闭</button></div></div></div>`; return; }
    const q=pool[i];
    $('#quizmount').innerHTML=`<div class="quiz"><div class="qbox">
      <div class="qprog">第 ${i+1}/${pool.length} 题 · 拼对 ${sc}</div>
      <div class="qzh">${esc(q.zh)} <button class="spk" id="qs">🔊</button></div>
      <div class="qpos">${esc(q.pos||'')} ${q.err?'· ⚠️上次拼错':''}</div>
      <input class="qin" id="qin" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="打出英文单词…">
      <div class="qres" id="qres"></div>
      <div class="qbtns"><button class="g" id="qskip">跳过/看答案</button><button class="p" id="qok">提交</button></div>
    </div></div>`;
    const inp=$('#qin'); inp.focus(); $('#qs').onclick=()=>say(q.w);
    say(q.w);
    function judge(reveal){
      const got=(inp.value||'').trim().toLowerCase(); const ok=got===q.w.toLowerCase();
      const r=$('#qres');
      if(ok){ r.className='qres ok'; r.textContent='✓ 正确：'+q.w; sc++; }
      else { r.className='qres no'; r.innerHTML=(reveal?'答案：':'✗ ')+`<b>${esc(q.w)}</b>`+(got?` （你写：${esc(got)}）`:''); }
      inp.disabled=true; $('#qok').textContent='下一题'; $('#qok').onclick=()=>{ i++; step(); };
    }
    $('#qok').onclick=()=>judge(false);
    $('#qskip').onclick=()=>judge(true);
    inp.onkeydown=e=>{ if(e.key==='Enter'){ if(inp.disabled){i++;step();} else judge(false); } };
  }
  step();
}
$('#quizAll').onclick=()=>spell(allWords());
$('#quizErr').onclick=()=>spell(allWords().filter(w=>w.err));

render();
</script>
</body></html>
"""

INDEX = r"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>托福模考复习系统</title><style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f}
  *{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}
  .wrap{max-width:820px;margin:0 auto;padding:40px 22px 80px}h1{font-size:26px;margin:0 0 4px}.sub{color:var(--muted);margin-bottom:22px}
  .notice{background:#fff6e8;border:1px solid #f0d9b0;border-left:5px solid var(--accent);border-radius:12px;padding:13px 15px;font-size:13.5px;margin-bottom:22px}
  .cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
  a.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;text-decoration:none;color:inherit}
  a.card:hover{border-color:#d8c8a8}a.card h2{font-size:18px;margin:0 0 6px}.card .m{color:var(--muted);font-size:13px}
  footer{margin-top:26px;color:#a89a86;font-size:12px}
</style></head><body><div class="wrap">
  <h1>📚 托福模考复习系统</h1>
  <div class="sub">每场模考 → 文段中心复习页：原文(词可点)→翻译→单词卡 · TTS · 背记 · 拼写测验</div>
  <div class="notice">用法：模考后把<b>内容截图</b>发 cc，cc 抽词按文段建页。配套文字分析在 <code>学习方法论/模考分析/</code>。</div>
  <div class="cards">__CARDS__</div>
  <footer>data/*.json → build.py → 复习页/*.html ｜ 共 __COUNT__ 场</footer>
</div></body></html>
"""

def build():
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    cards=[]
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        ps = d.get("passages", [])
        nw = sum(len(p.get("words",[])) for p in ps)
        ana = d.get("analysis")
        ana_html = f'配套分析：<a href="../../{html.escape(ana)}">{html.escape(os.path.basename(ana))}</a>' if ana else ''
        page = (PAGE.replace("__TITLE__", html.escape(d["title"]))
                    .replace("__DATA__", json.dumps(d, ensure_ascii=False))
                    .replace("__ANALYSIS__", ana_html))
        open(os.path.join(OUT, d["id"]+".html"), "w", encoding="utf-8").write(page)
        nerr = sum(1 for p in ps for w in p.get("words",[]) if w.get("err"))
        cards.append(f'<a class="card" href="复习页/{d["id"]}.html"><h2>{html.escape(d["title"])}</h2>'
                     f'<div class="m">{len(ps)} 篇文段 · {nw} 词 · {nerr} 个拼错词</div></a>')
        print("  ✓", d["id"], "—", len(ps), "篇", nw, "词")
    idx = INDEX.replace("__CARDS__", "\n".join(cards) or '<div>放 JSON 后运行 build.py</div>').replace("__COUNT__", str(len(files)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(idx)
    print(f"完成：{len(files)} 场 → 复习页/，已刷新 index.html")

if __name__ == "__main__":
    build()
