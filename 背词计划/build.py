#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
背词计划 · 渲染器
  data/green-book.json + data/beat-vocab.json  →  index.html（自包含 SPA，双击即用）
从 english-learner.html 的「背词计划」迁移而来：只保留「按 List 分组 + 一组组过词 + 掌握进度」，
去掉每日计划 / 循环 / 打卡。UI 换成本项目暖色纸感。
用法：  python3 build.py
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

# voca 标准富化叠加层：data/enrich.json = { "<word-id>": {ety,ph,tip,xex,syn,ant,nu,...} }
ENRICH = {}
_ep = os.path.join(DATA, "enrich.json")
if os.path.exists(_ep):
    with open(_ep, encoding="utf-8") as fp:
        ENRICH = json.load(fp)

def _merge(base):
    e = ENRICH.get(base["id"])
    if e:
        for k, v in e.items():
            if v not in (None, "", [], {}):
                base[k] = v
    return base

def trim_green(w):
    return _merge({"id": w["id"], "l": w["wl"], "w": w["word"], "p": w.get("pronunciation", ""),
            "d": w["definition"], "m": w.get("memory", ""),
            "c": w.get("collocations", []), "e": w.get("examples", [])})

def trim_beat(w):
    return _merge({"id": w["id"], "l": w["list"], "w": w["word"], "p": w.get("pronunciation", ""),
            "d": w["definition"], "m": w.get("memory", ""), "c": [], "e": []})

def load_source(fname, trim, kw):
    with open(os.path.join(DATA, fname), encoding="utf-8") as fp:
        d = json.load(fp)
    words = [trim(w) for w in d.get("words", []) if w.get("word")]
    return {"name": d.get("book", kw), "words": words}

PAGE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>背词计划 · 托福词库</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--bad:#c0453a;--gold:#c98a00}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
  a{color:var(--accent);text-decoration:none}
  .wrap{max-width:1000px;margin:0 auto;padding:0 20px 100px}
  /* 顶栏 */
  header{position:sticky;top:0;z-index:20;background:var(--card);border-bottom:1px solid var(--line);padding:12px 20px}
  .hdr-in{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
  header h1{font-size:18px;margin:0;font-weight:700}
  .src{display:flex;gap:6px}
  .src button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:5px 14px;font-size:13px;cursor:pointer;color:#5f574c;font-family:inherit}
  .src button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
  .ovprog{flex:1;min-width:180px;display:flex;align-items:center;gap:10px;font-size:13px;color:var(--muted)}
  .bar{flex:1;height:8px;background:#ece3d2;border-radius:6px;overflow:hidden}
  .bar>i{display:block;height:100%;background:linear-gradient(90deg,#2f8f5b,#7bc47f);border-radius:6px;transition:.3s}
  /* 总览分组网格 */
  .intro{color:var(--muted);font-size:14px;margin:18px 0 14px}
  .search{width:100%;max-width:340px;border:1px solid var(--line);border-radius:10px;padding:9px 12px;font-size:14px;font-family:inherit;background:var(--card);margin-bottom:16px}
  .search:focus{outline:none;border-color:var(--accent)}
  .markrow{margin:0 0 14px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
  .markall{background:var(--ok);color:#fff;border:0;border-radius:10px;padding:9px 15px;font-size:13.5px;cursor:pointer;font-family:inherit}
  .markall:hover{filter:brightness(1.05)}
  .reviewbtn{background:var(--bad);color:#fff;border:0;border-radius:10px;padding:9px 15px;font-size:13.5px;cursor:pointer;font-family:inherit;font-weight:600}
  .reviewbtn:hover{filter:brightness(1.06)}
  .markrow .hint{font-size:12.5px;color:var(--muted)}
  .rev-list{font-size:13px;font-weight:700;color:var(--muted);margin:18px 0 8px;border-bottom:1px dashed var(--line);padding-bottom:4px}
  .rev-list:first-child{margin-top:0}
  .clozebtn{background:var(--core);color:#fff;border:0;border-radius:10px;padding:9px 15px;font-size:13.5px;cursor:pointer;font-family:inherit;font-weight:600}
  .clozebtn:hover{filter:brightness(1.06)}
  /* 填词测验 */
  .cz-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;box-shadow:0 2px 10px rgba(150,120,70,.05)}
  .cz-clue{font-size:14px;color:#5f574c;margin-bottom:12px}
  .cz-clue b{color:var(--ink)}
  .cz-sent{font-family:Georgia,"Times New Roman",serif;font-size:20px;line-height:2;margin:6px 0 14px}
  .czb{display:inline-flex;align-items:baseline;gap:1px;margin:0 3px}
  .czb b{font-weight:800;color:var(--accent);font-family:Georgia,serif}
  .czb i{display:inline-block;width:12px;border-bottom:2px solid var(--accent);margin:0 1px 4px}
  .czb sub{font-size:9px;color:var(--muted);margin-left:3px}
  .cz-fill{font-weight:800}
  .cz-fill.ok{color:var(--ok)} .cz-fill.bad{color:var(--bad);text-decoration:underline}
  .cz-hintline{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:12px}
  .cz-zh{font-size:13.5px;color:#6f6656}
  .cz-input{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px}
  .cz-input input{flex:1;min-width:160px;border:1px solid var(--line);border-radius:10px;padding:10px 13px;font-size:16px;font-family:Georgia,serif;background:var(--card)}
  .cz-input input:focus{outline:none;border-color:var(--accent)}
  .cz-res{min-height:22px;font-size:15px;margin-bottom:6px}
  .cz-ok{color:var(--ok);font-weight:700} .cz-bad{color:var(--bad);font-weight:700}
  .cz-summary{text-align:center;padding:30px 20px;font-size:16px}
  .cz-acts{margin-top:16px;display:flex;gap:10px;justify-content:center}
  /* 文段填空 */
  .pz-card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;box-shadow:0 2px 10px rgba(150,120,70,.05)}
  .pz-text{font-size:17px;line-height:2.5;color:var(--ink)}
  .pz-b{display:inline-flex;align-items:baseline;gap:2px;margin:0 2px;white-space:nowrap}
  .pz-b>b{font-weight:800;color:var(--accent);font-family:Georgia,serif}
  .pz-in{border:0;border-bottom:2px solid var(--accent);background:#fbf7ee;font-size:16px;font-family:Georgia,serif;padding:0 3px 1px;color:var(--ink);text-align:center;letter-spacing:1px}
  .pz-in:focus{outline:none;background:#fff4e0}
  .pz-in.ok{border-color:var(--ok);color:var(--ok);background:#f2faf4}
  .pz-in.bad{border-color:var(--bad);color:var(--bad);background:#fdf1ef}
  .pz-b>sub{font-size:9px;color:var(--muted);margin-left:2px}
  .pz-ans{font-size:12px;color:var(--ok);margin-left:3px;font-family:Georgia,serif}
  .pz-bar{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
  .pz-res{margin-top:12px;font-size:15px}
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
  .gcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;cursor:pointer;transition:.15s;box-shadow:0 2px 10px rgba(150,120,70,.05)}
  .gcard:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(150,120,70,.13);border-color:#d8c8a8}
  .gcard.done{border-color:#a9d6b8;background:#f2faf4}
  .gcard .no{font-size:16px;font-weight:700}
  .gcard .ct{font-size:12px;color:var(--muted);margin:2px 0 8px}
  .gcard .pct{font-size:12px;color:var(--core);font-weight:700;margin-top:5px}
  .gcard.done .pct{color:var(--ok)}
  .gcard .bar{height:6px;margin-top:2px}
  /* 搜索结果 */
  .sres{display:none;flex-direction:column;gap:6px;margin-bottom:16px}
  .sres.show{display:flex}
  .srow{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 12px;cursor:pointer;font-size:14px;display:flex;gap:10px;align-items:baseline}
  .srow:hover{border-color:#d8c8a8}
  .srow b{color:var(--accent)}.srow .sl{margin-left:auto;font-size:12px;color:var(--muted)}
  /* 学习视图 */
  .study-top{position:sticky;top:57px;z-index:15;background:var(--bg);padding:14px 0 10px}
  .stitle{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
  .back{font-size:14px;color:var(--muted);cursor:pointer}
  .stitle h2{font-size:18px;margin:0}
  .stitle .cnt{font-size:13px;color:var(--muted)}
  .tools{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
  .tbtn{border:1px solid var(--line);background:var(--card);border-radius:8px;padding:6px 12px;font-size:13px;cursor:pointer;color:#5f574c;font-family:inherit}
  .tbtn.on{background:var(--core);color:#fff;border-color:var(--core)}
  .tbtn:hover{filter:brightness(.98)}
  .nav{margin-left:auto;display:flex;gap:8px}
  /* 单词卡 */
  .cards{margin-top:14px;display:flex;flex-direction:column;gap:12px}
  .wcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;box-shadow:0 2px 10px rgba(150,120,70,.04)}
  .wcard.ok{opacity:.7;border-color:#cfe6d5;background:#f7fbf8}
  .wcard.no{border-left:4px solid var(--bad);background:#fdf4f2}
  .wc-head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
  .wc-word{font-size:22px;font-weight:700;cursor:pointer;letter-spacing:.2px}
  .wc-word:hover{color:var(--accent)}
  .wc-word::after{content:"🔊";font-size:13px;margin-left:7px;opacity:.45}
  .wc-pron{color:var(--core);font-size:15px}
  .wc-idx{font-size:12px;color:#c3b79c}
  .wc-marks{margin-left:auto;display:flex;gap:6px}
  .wc-mark{border:1px solid var(--line);background:#f3ecdd;border-radius:20px;padding:5px 12px;font-size:13px;cursor:pointer;color:#6f6552;font-family:inherit;white-space:nowrap}
  .wc-mark:hover{filter:brightness(.97)}
  .wc-mark.ok.on{background:var(--ok);color:#fff;border-color:var(--ok)}
  .wc-mark.no.on{background:var(--bad);color:#fff;border-color:var(--bad)}
  .seg{display:flex;gap:4px}
  .wc-pos{font-size:11px;color:var(--core);background:#e7f1ee;border-radius:20px;padding:1px 9px;align-self:center}
  .wc-chev{margin-left:2px;color:#c3b79c;font-size:13px;transition:.2s;align-self:center}
  .wcard.expandable{cursor:pointer}
  .wcard.open .wc-chev{transform:rotate(90deg)}
  .wc-def{font-size:16px;margin-top:8px;font-weight:600}
  .wc-detail{display:none;margin-top:10px;border-top:1px dashed var(--line);padding-top:10px}
  .wcard.open .wc-detail{display:block}
  .wc-detail:empty{display:none}
  .sec{margin:12px 0}
  .sec:first-child{margin-top:0}
  .sec-h{font-size:12.5px;font-weight:700;margin-bottom:4px}
  .sec-h.mem{color:var(--gold)}.sec-h.col{color:var(--core)}.sec-h.ex{color:var(--accent)}
  .sec-b{font-size:14px;color:#4d463c;line-height:1.65}
  .sec-b>div{margin:3px 0}
  .sec-h.ph{color:#2565c0}.sec-h.syn{color:var(--core)}.sec-h.tip{color:var(--gold)}
  .wc-mem-box{background:#faf5ea;border-radius:8px;padding:8px 11px}
  .chips-line{margin-bottom:9px;display:flex;gap:6px}
  .lvl-chip{font-size:11px;background:#efe9fb;color:#6b5bb5;border-radius:20px;padding:2px 10px}
  .ex-item{margin:7px 0}
  .ex-item.colloc{background:#faf5ea;border-radius:8px;padding:8px 11px}
  .ex-zh{color:#6f6656;font-size:13px}
  .ex-src{color:#c3b79c;font-size:12px;margin-top:1px}
  .syn-row{margin:6px 0;font-size:14px;line-height:1.6}
  .syn-chip{font-size:11px;background:#e7f1ee;color:#2f7d72;border-radius:6px;padding:1px 8px;margin-right:6px}
  .syn-chip.ant{background:#fbe6df;color:#b3543f}
  .syn-w{font-weight:700;cursor:pointer}.syn-w:hover{color:var(--accent)}
  .syn-ipa{color:var(--core);font-size:13px;margin:0 3px}
  .nuance{background:#eef6f0;border-left:3px solid var(--core);border-radius:8px;padding:10px 13px;font-size:13.5px;color:#4d463c;margin-top:10px;line-height:1.65}
  .empty{color:var(--muted);text-align:center;padding:40px}
  footer{margin-top:24px;color:#a89a86;font-size:12px}
  @media(max-width:600px){.grid{grid-template-columns:repeat(auto-fill,minmax(120px,1fr))}}
</style>
</head>
<body>
<header><div class="hdr-in">
  <h1>📚 背词计划</h1>
  <div class="src" id="src"></div>
  <div class="ovprog"><span id="ovtxt"></span><span class="bar"><i id="ovbar"></i></span></div>
</div></header>
<div class="wrap"><div id="view"></div></div>

<script>
const VOCAB = __DATA__;
const M_KEY = 'bcplan:state';
const $ = s => document.querySelector(s);
const view = $('#view');
function esc(s){ return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function load(k,d){ try{ return JSON.parse(localStorage.getItem(k)) ?? d; }catch(e){ return d; } }
function save(k,v){ localStorage.setItem(k, JSON.stringify(v)); }

let source = load('bcplan:source','green');
if(!VOCAB[source]) source='green';
let state = load(M_KEY, {});         // {id:'ok'|'no'}  ok=已掌握 no=未掌握(生词)
(function(){ const old=load('bcplan:mastered',null); if(old && Object.keys(state).length===0){ for(const k in old) state[k]='ok'; save(M_KEY,state); } })(); // 兼容旧版
let recite = load('bcplan:recite', false);
let filter = 'all';                  // all | ok | no
let reviewMode = 'no';               // 全局未掌握视图：no=已标未掌握 | un=未学未标记
let curList = null;                  // null=总览 | 'review'=全部未掌握 | 数字=某组

/* ── 数据辅助 ── */
function words(){ return VOCAB[source].words; }
function listMeta(){ const m={}; words().forEach(w=>{ m[w.l]=(m[w.l]||0)+1; });
  return Object.keys(m).map(Number).sort((a,b)=>a-b).map(n=>({no:n,count:m[n]})); }
function listWords(no){ return words().filter(w=>w.l===no); }
function doneCount(arr){ let c=0; for(const w of arr) if(state[w.id]==='ok') c++; return c; }
function noCount(arr){ let c=0; for(const w of arr) if(state[w.id]==='no') c++; return c; }

/* ── 语音 ── */
let voices=[]; function lv(){ voices = window.speechSynthesis? speechSynthesis.getVoices():[]; }
if(window.speechSynthesis){ lv(); speechSynthesis.onvoiceschanged=lv; }
// 与听力系统一致的自然女声（美音）
function pickVoice(){
  const pref=['Samantha','Ava','Allison','Susan','Zoe','Nicky','Serena','Karen','Google US English','Microsoft Aria','Microsoft Jenny','Microsoft Zira'];
  const en=voices.filter(v=>v.lang==='en-US');
  const pool=en.length?en:voices.filter(v=>v.lang&&v.lang.toLowerCase().startsWith('en'));
  for(const nm of pref){ const v=pool.find(x=>x.name&&x.name.includes(nm)); if(v) return v; }
  const fem=pool.find(x=>/female|woman/i.test(x.name||'')); if(fem) return fem;
  return pool[0]||voices[0]||null;
}
function say(t){ if(!window.speechSynthesis) return; speechSynthesis.cancel();
  const u=new SpeechSynthesisUtterance(t); const v=pickVoice(); if(v)u.voice=v; u.lang='en-US'; u.rate=.95; speechSynthesis.speak(u); }

/* ── 顶栏 ── */
function renderHeader(){
  $('#src').innerHTML = Object.keys(VOCAB).map(k=>`<button data-s="${k}" class="${k===source?'on':''}">${esc(VOCAB[k].name)} · ${VOCAB[k].words.length}</button>`).join('');
  $('#src').querySelectorAll('button').forEach(b=> b.onclick=()=>{ source=b.dataset.s; save('bcplan:source',source); curList=null; renderHeader(); render(); });
  const all=words(), dc=doneCount(all), nc=noCount(all);
  $('#ovtxt').innerHTML = `掌握 <b style="color:var(--ok)">${dc}</b> · 未掌握 <b style="color:var(--bad)">${nc}</b> / ${all.length}`;
  $('#ovbar').style.width = (all.length? dc/all.length*100:0)+'%';
}

/* ── 路由 ── */
function render(){ renderHeader(); if(curList==null) renderOverview(); else if(curList==='review') renderReview(); else if(curList==='cloze') renderCloze(); else renderStudy(curList); window.scrollTo(0,0); }

/* ── 总览：分组网格 ── */
function renderOverview(){
  const metas=listMeta();
  const nUn = noCount(words());
  const nOk = doneCount(words());
  let h = `<div class="intro">按 <b>List 分组</b>，一组一组过。点一组进去，逐词看释义/词源/例句；不会的点「未掌握」，剩下的可一键记为「已掌握」。进度自动保存。</div>
    <div class="markrow"><button class="reviewbtn" id="goReview">🔴 查看全部未掌握（${nUn}）</button>
      <button class="clozebtn" id="goCloze">📝 文段填空（${PASSAGES.length} 篇）</button>
      <button class="markall" id="markAll">✅ 其余一键记为「已掌握」</button>
      <span class="hint">把当前词库里<b>没标「未掌握」</b>的词全部记为已掌握（浏览完再点）</span></div>
    <input class="search" id="q" placeholder="🔎 搜单词（跳到它所在的 List）…" value="">
    <div class="sres" id="sres"></div>
    <div class="grid" id="grid"></div>`;
  view.innerHTML = h;
  $('#goReview').onclick=()=>{ curList='review'; reviewMode='no'; render(); };
  $('#goCloze').onclick=()=>{ curList='cloze'; render(); };
  $('#markAll').onclick=()=>{
    const all=words();
    const un=all.filter(w=>state[w.id]!=='no'&&state[w.id]!=='ok').length;
    const no=all.filter(w=>state[w.id]==='no').length;
    if(!un){ alert('当前词库已经没有「未标记」的词了。'); return; }
    if(!confirm(`把「${VOCAB[source].name}」中除 ${no} 个已标『未掌握』之外的所有词，记为「已掌握」？\n（含你可能还没浏览的词，约 ${un} 个未标记词会被记为已掌握）`)) return;
    all.forEach(w=>{ if(state[w.id]!=='no') state[w.id]='ok'; });
    save(M_KEY,state); render();
  };
  const grid=$('#grid');
  grid.innerHTML = metas.map(m=>{ const lw=listWords(m.no); const dc=doneCount(lw); const nc=noCount(lw); const pct=Math.round(dc/m.count*100);
    return `<div class="gcard ${dc===m.count?'done':''}" data-no="${m.no}">
      <div class="no">List ${String(m.no).padStart(2,'0')}</div>
      <div class="ct">${m.count} 词</div>
      <div class="bar"><i style="width:${pct}%"></i></div>
      <div class="pct">${dc===m.count?'✓ 已完成':'掌握 '+dc+(nc?' · <span style="color:var(--bad)">未掌握 '+nc+'</span>':'')+' / '+m.count}</div>
    </div>`; }).join('');
  grid.querySelectorAll('.gcard').forEach(c=> c.onclick=()=>{ curList=+c.dataset.no; render(); });
  // 搜索
  const q=$('#q'), sres=$('#sres');
  q.oninput=()=>{ const kw=q.value.trim().toLowerCase(); if(kw.length<2){ sres.classList.remove('show'); grid.style.display=''; return; }
    const hits=words().filter(w=>w.w.toLowerCase().includes(kw)).slice(0,40);
    grid.style.display='none'; sres.classList.add('show');
    sres.innerHTML = hits.length? hits.map(w=>`<div class="srow" data-no="${w.l}"><b>${esc(w.w)}</b><span>${esc(w.d).slice(0,42)}</span><span class="sl">List ${String(w.l).padStart(2,'0')}</span></div>`).join('') : '<div class="empty">没找到</div>';
    sres.querySelectorAll('.srow').forEach(r=> r.onclick=()=>{ curList=+r.dataset.no; render(); }); };
}

/* ── 全部未掌握：横跨所有 List，把标了「未掌握」的生词集中复习 ── */
function renderReview(){
  const all=words();
  const noList=all.filter(w=>state[w.id]==='no');       // 已标 ✕ 未掌握（生词）
  const unList=all.filter(w=>!state[w.id]);              // 未学 / 未标记
  const cur = reviewMode==='un'? unList : noList;
  const byList={}; cur.forEach(w=>{ (byList[w.l]=byList[w.l]||[]).push(w); });
  const nos=Object.keys(byList).map(Number).sort((a,b)=>a-b);
  const body = nos.length
    ? nos.map(no=>`<div class="rev-list">List ${String(no).padStart(2,'0')} · ${byList[no].length} 词</div><div class="cards">${byList[no].map(w=>cardHtml(w)).join('')}</div>`).join('')
    : `<div class="empty">${reviewMode==='un'?'🎉 这个词库已经没有「未学/未标记」的词了。':'还没有标「未掌握」的生词。<br>学习时点某个词的「✕ 未掌握」，它就会自动收集到这里，方便集中复习。'}</div>`;
  view.innerHTML = `<div class="study-top">
    <div class="stitle"><span class="back" id="back">← 返回总览</span>
      <h2>🔴 全部未掌握</h2>
      <span class="cnt">${esc(VOCAB[source].name)} · 未掌握 <b style="color:var(--bad)">${noList.length}</b> · 未学 ${unList.length}</span></div>
    <div class="tools">
      <button class="tbtn ${recite?'on':''}" id="tRecite">背记模式（遮释义）</button>
      <button class="tbtn" id="tExpand">展开/收起全部</button>
      <span class="seg">
        <button class="tbtn ${reviewMode==='no'?'on':''}" data-r="no">✕ 未掌握 ${noList.length}</button>
        <button class="tbtn ${reviewMode==='un'?'on':''}" data-r="un">○ 未学 ${unList.length}</button>
      </span></div></div>
    <div id="revBody">${body}</div>
    <div class="tools" style="margin-top:16px"><span class="back" id="back2">← 返回总览</span></div>`;
  wireCards(view);
  $('#back').onclick=$('#back2').onclick=()=>{ curList=null; render(); };
  $('#tRecite').onclick=()=>{ recite=!recite; save('bcplan:recite',recite); render(); };
  $('#tExpand').onclick=()=>{ const cs=[...view.querySelectorAll('.wcard.expandable')]; const anyClosed=cs.some(c=>!c.classList.contains('open')); cs.forEach(c=>c.classList.toggle('open',anyClosed)); };
  view.querySelectorAll('.seg [data-r]').forEach(bn=> bn.onclick=()=>{ reviewMode=bn.dataset.r; render(); });
}

/* ── 文段填空：cc 用（含你已掌握的）词造一篇短文，10 空，填完一次判定 ── */
const PASSAGES = __PASSAGES__;
let pzList=[], pzIdx=0, pzCur=null, pzGraded=false;
function pzShuffle(a){ a=a.slice(); for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];} return a; }
function pzParse(text){ const parts=[],ws=[]; const re=/\{\{([^}]+)\}\}/g; let last=0,m;
  while((m=re.exec(text))){ if(m.index>last)parts.push({t:'t',s:text.slice(last,m.index)}); const w=m[1].trim(); parts.push({t:'b',word:w,i:ws.length}); ws.push(w); last=re.lastIndex; }
  if(last<text.length)parts.push({t:'t',s:text.slice(last)}); return {parts,words:ws}; }
function pzMastered(){ const s=new Set(); words().forEach(w=>{ if(state[w.id]==='ok') s.add((w.w||'').toLowerCase()); }); return s; }

function renderCloze(){
  if(!PASSAGES.length){ view.innerHTML=`<div class="study-top"><div class="stitle"><span class="back" id="back">← 返回总览</span><h2>📝 文段填空</h2></div></div><div class="empty">还没有文段题。跟 cc 说一声「用我已掌握的词出文段填空」，它造好一篇就能在这里做。</div>`; $('#back').onclick=()=>{curList=null;render();}; return; }
  if(!pzList.length){ pzList=pzShuffle(PASSAGES); pzIdx=0; }
  renderPassage();
}
function renderPassage(){
  pzCur=pzList[pzIdx%pzList.length]; pzGraded=false;
  const parsed=pzParse(pzCur.text); pzCur._p=parsed;
  const mset=pzMastered(); const known=parsed.words.filter(w=>mset.has(w.toLowerCase())).length;
  let body=''; parsed.parts.forEach(p=>{
    if(p.t==='t'){ body+=esc(p.s); return; }
    const w=p.word, len=w.length, rest=len-1;
    body+=`<span class="pz-b"><b>${esc(w[0])}</b><input class="pz-in" data-i="${p.i}" maxlength="${rest}" style="width:${Math.max(26,rest*12+6)}px" placeholder="${'‗'.repeat(rest)}" autocomplete="off" autocapitalize="off" spellcheck="false"><sub>${len}</sub></span>`;
  });
  view.innerHTML=`<div class="study-top"><div class="stitle"><span class="back" id="back">← 返回总览</span>
      <h2>📝 文段填空</h2><span class="cnt">${esc(pzCur.topic||'')} · 第 ${(pzIdx%pzList.length)+1}/${pzList.length} 篇 · 含你已掌握 ${known}/${parsed.words.length} 词</span></div>
    <div class="intro" style="margin:8px 0 0">读整段，靠<b>上下文语境</b>把 10 个词补全：每空<b>已给首字母</b>，方格/角标示总字母数。<b>全部填完</b>点「判定答案」一次性批改。</div></div>
    <div class="pz-card"><div class="pz-text" id="pzText">${body}</div>
      <div class="pz-bar"><button class="clozebtn" id="pzGrade">✅ 判定答案</button>
        <button class="tbtn" id="pzShow">显示全部答案</button>
        <button class="tbtn" id="pzSay">🔊 读全文</button>
        <button class="tbtn" id="pzNext">换一篇 →</button></div>
      <div class="pz-res" id="pzRes"></div></div>`;
  $('#back').onclick=()=>{ curList=null; render(); };
  $('#pzGrade').onclick=()=>pzGrade(false);
  $('#pzShow').onclick=()=>pzGrade(true);
  $('#pzNext').onclick=()=>{ pzIdx++; renderPassage(); window.scrollTo(0,0); };
  $('#pzSay').onclick=()=>say(pzCur.text.replace(/\{\{|\}\}/g,''));
  const ins=[...view.querySelectorAll('.pz-in')];
  ins.forEach((inp,k)=> inp.onkeydown=e=>{ if(e.key==='Enter'){ e.preventDefault(); if(k+1<ins.length) ins[k+1].focus(); else pzGrade(false); } });
  if(ins[0]) ins[0].focus();
}
function pzGrade(reveal){
  if(pzGraded && !reveal) return;
  const parsed=pzCur._p; let right=0; const wrong=[];
  view.querySelectorAll('.pz-in').forEach(inp=>{
    const i=+inp.dataset.i, w=parsed.words[i];
    const ok=((w[0]+(inp.value||'')).toLowerCase()===w.toLowerCase());
    if(reveal) inp.value=w.slice(1);
    inp.classList.remove('ok','bad'); inp.classList.add((ok||reveal)?'ok':'bad'); inp.disabled=true;
    if(ok) right++; else { if(!reveal) wrong.push(w);
      const b=inp.parentNode; if(b&&!b.querySelector('.pz-ans')){ const t=document.createElement('span'); t.className='pz-ans'; t.textContent='('+w+')'; b.appendChild(t); } }
  });
  pzGraded=true;
  const total=parsed.words.length, res=$('#pzRes');
  res.innerHTML = reveal ? '已显示全部答案（本篇不计分）。'
    : `得分 <b style="color:var(--ok)">${right}</b> / ${total} · 正确率 <b>${Math.round(right/total*100)}%</b>`+(wrong.length?` · 待复习：${wrong.map(esc).join('、')}`:' 🎉 全对！');
  const g=$('#pzGrade'); if(g&&!reveal) g.disabled=true;
}

/* ── 学习视图：一组单词卡 ── */
function renderStudy(no){
  const metas=listMeta(); const idx=metas.findIndex(m=>m.no===no);
  const prev=idx>0?metas[idx-1].no:null, next=idx<metas.length-1?metas[idx+1].no:null;
  let lw=listWords(no); const total=lw.length; const dc=doneCount(lw); const nc=noCount(lw);
  const shown = filter==='ok'? lw.filter(w=>state[w.id]==='ok')
              : filter==='no'? lw.filter(w=>state[w.id]==='no')
              : lw;
  view.innerHTML = `<div class="study-top">
    <div class="stitle"><span class="back" id="back">← 返回总览</span>
      <h2>List ${String(no).padStart(2,'0')}</h2>
      <span class="cnt" id="cnt">${total} 词 · 掌握 ${dc}${nc?' · 未掌握 '+nc:''}</span></div>
    <div class="bar" style="margin-top:8px"><i id="lbar" style="width:${Math.round(dc/total*100)}%"></i></div>
    <div class="tools">
      <button class="tbtn ${recite?'on':''}" id="tRecite">背记模式（遮释义）</button>
      <button class="tbtn" id="tExpand">展开/收起全部</button>
      <span class="seg">
        <button class="tbtn ${filter==='all'?'on':''}" data-f="all">全部</button>
        <button class="tbtn ${filter==='no'?'on':''}" data-f="no">未掌握</button>
        <button class="tbtn ${filter==='ok'?'on':''}" data-f="ok">已掌握</button>
      </span>
      <button class="tbtn" id="tAll">本组·其余记为已掌握</button>
      <span class="nav">
        <button class="tbtn" id="pv" ${prev==null?'disabled':''}>◀ 上一组</button>
        <button class="tbtn" id="nx" ${next==null?'disabled':''}>下一组 ▶</button>
      </span>
    </div></div>
    <div class="cards" id="cards"></div>
    <div class="tools" style="margin-top:16px"><span class="back" id="back2">← 返回总览</span><span class="nav">
      <button class="tbtn" id="pv2" ${prev==null?'disabled':''}>◀ 上一组</button>
      <button class="tbtn" id="nx2" ${next==null?'disabled':''}>下一组 ▶</button></span></div>`;
  const cards=$('#cards');
  const emptyMsg = filter==='no'?'本组还没有标记「未掌握」的词':filter==='ok'?'本组还没有标记「已掌握」的词':'本组没有单词';
  cards.innerHTML = shown.length? shown.map(w=>cardHtml(w)).join('') : `<div class="empty">${emptyMsg}</div>`;
  wireCards(cards);
  $('#back').onclick=$('#back2').onclick=()=>{ curList=null; render(); };
  const go=n=>{ curList=n; render(); };
  $('#pv').onclick=$('#pv2').onclick=()=>prev!=null&&go(prev);
  $('#nx').onclick=$('#nx2').onclick=()=>next!=null&&go(next);
  $('#tRecite').onclick=()=>{ recite=!recite; save('bcplan:recite',recite); render(); };
  $('#tExpand').onclick=()=>{ const cs=[...view.querySelectorAll('.wcard.expandable')]; const anyClosed=cs.some(c=>!c.classList.contains('open')); cs.forEach(c=>c.classList.toggle('open',anyClosed)); };
  view.querySelectorAll('.seg [data-f]').forEach(bn=> bn.onclick=()=>{ filter=bn.dataset.f; render(); });
  $('#tAll').onclick=()=>{ const un=lw.filter(w=>state[w.id]!=='no'&&state[w.id]!=='ok').length;
    if(un && !confirm(`把本组除已标『未掌握』外的词记为「已掌握」？（${un} 个未标记词会记为已掌握）`)) return;
    lw.forEach(w=>{ if(state[w.id]!=='no') state[w.id]='ok'; }); save(M_KEY,state); render(); };
}

const POS_MAP={n:'名词',v:'动词',vt:'动词',vi:'动词',adj:'形容词',a:'形容词',adv:'副词',ad:'副词',prep:'介词',pron:'代词',conj:'连词',art:'冠词',num:'数词',int:'感叹词'};
function posChip(def){ const m=(def||'').match(/^\s*([a-z]+)\s*\./i); return m? (POS_MAP[m[1].toLowerCase()]||'') : ''; }
function sec(icon,cls,title,inner){ return `<div class="sec"><div class="sec-h ${cls}">${icon} ${title}</div><div class="sec-b">${inner}</div></div>`; }
function exHtml(list){ return list.map(x=>{
    if(typeof x==='string') return `<div class="ex-item">${esc(x)}</div>`;
    const src=x.src||x.source||''; const cc=(src==='高频搭配'||src==='搭配')?' colloc':'';
    return `<div class="ex-item${cc}"><div>${esc(x.en||'')}</div>${x.zh?`<div class="ex-zh">${esc(x.zh)}</div>`:''}${src?`<div class="ex-src">— ${esc(src)}</div>`:''}</div>`;
  }).join(''); }

// 默认收起，只显示单词行；点击展开 voca 标准的丰富信息（词源/发音规律/例句/近义辨析/辨析总结）
function cardHtml(w){
  const st=state[w.id]||''; const cls=(st==='ok'?' ok':st==='no'?' no':'');
  const pos=posChip(w.d);
  let d='';
  if(recite) d += sec('📖','','释义',`<div style="font-size:16px;font-weight:600">${esc(w.d)}</div>`);
  d += '<div class="chips-line"><span class="lvl-chip">托福</span></div>';
  // 词源
  if(w.ety) d += sec('🏛','mem','造词来源 · 词源故事', esc(w.ety));
  else if(w.m) d += sec('🏛','mem','词根 · 联想记忆', `<div class="wc-mem-box">${esc(w.m)}</div>`);
  // 发音规律
  if(w.ph) d += sec('🗣','ph','发音规律', esc(w.ph));
  // 记忆钩子
  if(w.tip) d += sec('💡','tip','记忆钩子', esc(w.tip));
  // 例句（富化用结构化 xex；否则退回基础 e + 搭配 c）
  let exList;
  if(w.xex&&w.xex.length) exList=w.xex;
  else { exList=[]; (w.e||[]).forEach(s=>exList.push(s)); (w.c||[]).forEach(s=>exList.push({en:s,src:'高频搭配'})); }
  if(exList.length) d += sec('✍️','ex','造句 · 名著/影视例句', exHtml(exList));
  // 近义辨析 · 反义词
  if((w.syn&&w.syn.length)||(w.ant&&w.ant.length)){
    let inner='';
    (w.syn||[]).forEach(s=> inner+=`<div class="syn-row"><span class="syn-chip">近义</span><span class="syn-w" data-say="${esc(s.w)}">${esc(s.w)}</span>${s.ipa?`<span class="syn-ipa">${esc(s.ipa)}</span>`:''}— ${esc(s.note||s.gloss||'')}</div>`);
    (w.ant||[]).forEach(s=> inner+=`<div class="syn-row"><span class="syn-chip ant">反义</span><span class="syn-w" data-say="${esc(s.w)}">${esc(s.w)}</span> — ${esc(s.note||s.gloss||'')}</div>`);
    d += sec('🔗','syn','近义词辨析 · 反义词', inner);
  }
  if(w.nu) d += `<div class="nuance">🎯 ${esc(w.nu)}</div>`;
  const expandable = ' expandable';
  return `<div class="wcard${cls}${expandable}" data-id="${esc(w.id)}">
    <div class="wc-head">
      <span class="wc-word" data-say="${esc(w.w)}">${esc(w.w)}</span>
      <span class="wc-pron">${esc(w.p)}</span>
      ${pos?`<span class="wc-pos">${pos}</span>`:''}
      <span class="wc-marks">
        <button class="wc-mark ok${st==='ok'?' on':''}">✓ 掌握</button>
        <button class="wc-mark no${st==='no'?' on':''}">✕ 未掌握</button>
      </span>
      <span class="wc-chev">▸</span>
    </div>
    ${recite?'':`<div class="wc-def">${esc(w.d)}</div>`}
    <div class="wc-detail">${d}</div>
  </div>`;
}

function wireCards(box){
  box.querySelectorAll('.wcard').forEach(card=>{
    const id=card.dataset.id;
    card.querySelector('.wc-word').onclick=e=>{ e.stopPropagation(); say(e.target.dataset.say); };
    card.querySelectorAll('.syn-w').forEach(sw=> sw.onclick=e=>{ e.stopPropagation(); say(sw.dataset.say); });
    function setState(ns){
      state[id] = (state[id]===ns) ? undefined : ns;   // 再点一次取消
      if(state[id]===undefined) delete state[id];
      save(M_KEY, state);
      card.classList.remove('ok','no'); if(state[id]) card.classList.add(state[id]);
      card.querySelector('.wc-mark.ok').classList.toggle('on', state[id]==='ok');
      card.querySelector('.wc-mark.no').classList.toggle('on', state[id]==='no');
      const lw=listWords(curList), dc=doneCount(lw), nc=noCount(lw);
      const cnt=$('#cnt'); if(cnt) cnt.textContent=`${lw.length} 词 · 掌握 ${dc}`+(nc?` · 未掌握 ${nc}`:'');
      const lb=$('#lbar'); if(lb) lb.style.width=Math.round(dc/lw.length*100)+'%';
      renderHeader();
    }
    card.querySelector('.wc-mark.ok').onclick=e=>{ e.stopPropagation(); setState('ok'); };
    card.querySelector('.wc-mark.no').onclick=e=>{ e.stopPropagation(); setState('no'); };
    if(card.classList.contains('expandable')) card.addEventListener('click', ()=>card.classList.toggle('open'));
  });
}

/* ── 启动 ── */
render();
</script>
</body>
</html>
"""

def build():
    green = load_source("green-book.json", trim_green, "托福单词绿皮书")
    beat  = load_source("beat-vocab.json", trim_beat, "BEAT 必考2000词")
    # 名称精简
    green["name"] = "绿皮书"
    beat["name"]  = "BEAT 2000"
    payload = {"green": green, "beat": beat}
    import os as _os
    _pz = _os.path.join(DATA, "cloze-passages.json")
    passages = json.load(open(_pz, encoding="utf-8")).get("passages", []) if _os.path.exists(_pz) else []
    html = PAGE.replace("__DATA__", json.dumps(payload, ensure_ascii=False)).replace("__PASSAGES__", json.dumps(passages, ensure_ascii=False))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fp:
        fp.write(html)
    gl = len({w["l"] for w in green["words"]}); bl = len({w["l"] for w in beat["words"]})
    print(f"完成：绿皮书 {len(green['words'])}词/{gl}组 + BEAT {len(beat['words'])}词/{bl}组 → index.html "
          f"({os.path.getsize(os.path.join(ROOT,'index.html'))/1024/1024:.2f} MB)"
          f"；voca富化 {len(ENRICH)} 词")

if __name__ == "__main__":
    build()
