#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单词记忆系统 · 渲染器
读取 data/*.json（每个文件 = 一个「按逻辑分组」的词表），
渲染成自包含、双击即开的学习页 groups/<id>.html，并重建总目录 index.html。

用法：
    python3 build.py            # 渲染全部
    python3 build.py aw         # 只渲染 data/aw.json
"""
import json, sys, html, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
GROUPS = ROOT / "groups"
GROUPS.mkdir(exist_ok=True)

# ---------------------------------------------------------------- 学习页模板
PAGE_TMPL = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 单词拆解卡片</title>
<style>
  :root{
    --bg:#f7f1e7; --card:#fffdf8; --ink:#2f2a24; --muted:#8c8072;
    --line:#eaddc9; --accent:#c1662f; --accent2:#e0913c; --amber:#fbe6c4;
    --core:#2f8f83; --exc:#b0603f; --ok:#4a9a5e;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;background:var(--bg);color:var(--ink);
    font-family:-apple-system,"PingFang SC","Helvetica Neue",Segoe UI,sans-serif;
    line-height:1.6;-webkit-font-smoothing:antialiased}
  .wrap{max-width:1180px;margin:0 auto;padding:26px 20px 90px}
  a{color:var(--accent);text-decoration:none}
  .top{display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--muted)}
  .top a{color:var(--muted)}
  /* header */
  header.hero{margin:14px 0 22px}
  .combo{display:inline-flex;align-items:baseline;gap:14px}
  .combo .big{font-family:Georgia,"Times New Roman",serif;font-size:60px;font-weight:700;
    background:var(--amber);color:var(--accent);padding:2px 20px;border-radius:18px;line-height:1.1}
  .combo .snd{font-size:30px;color:var(--core);font-weight:700}
  h1{font-size:23px;margin:14px 0 4px}
  .intro{color:#5f574c;max-width:860px;font-size:15px}
  /* rule cards */
  .rules{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin:18px 0}
  .rule{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;font-size:14px}
  .rule.core{border-left:5px solid var(--core)}
  .rule.exc{border-left:5px solid var(--exc)}
  .rule b{display:block;margin-bottom:4px;font-size:14px}
  .rule.core b{color:var(--core)} .rule.exc b{color:var(--exc)}
  /* rhyme chains */
  .rhymes{background:linear-gradient(135deg,#fff6e8,#fdeede);border:1px dashed var(--accent2);
    border-radius:14px;padding:14px 16px;margin-bottom:20px}
  .rhymes h3{margin:0 0 8px;font-size:15px;color:var(--accent)}
  .chain{margin:6px 0;font-size:14px}
  .chain .lab{color:var(--muted);margin-right:8px}
  .chip{display:inline-block;background:#fff;border:1px solid var(--line);border-radius:20px;
    padding:2px 11px;margin:3px 4px 3px 0;cursor:pointer;font-family:Georgia,serif;font-size:15px;transition:.15s}
  .chip:hover{background:var(--amber);border-color:var(--accent2)}
  /* toolbar */
  .toolbar{position:sticky;top:0;z-index:20;background:rgba(247,241,231,.94);backdrop-filter:blur(6px);
    border-bottom:1px solid var(--line);padding:12px 0;margin-bottom:18px;
    display:flex;flex-wrap:wrap;gap:10px;align-items:center}
  .search{flex:1;min-width:180px;padding:8px 13px;border:1px solid var(--line);border-radius:10px;
    font-size:14px;background:#fff}
  .filters{display:flex;flex-wrap:wrap;gap:6px}
  .f{padding:6px 12px;border:1px solid var(--line);background:#fff;border-radius:20px;font-size:13px;
    cursor:pointer;color:#6b6154;transition:.15s}
  .f.on{background:var(--accent);color:#fff;border-color:var(--accent)}
  select.f{max-width:170px;color:#6b6154;cursor:pointer}
  .btn{padding:7px 14px;border:1px solid var(--accent);background:#fff;color:var(--accent);
    border-radius:20px;font-size:13px;cursor:pointer;font-weight:600}
  .btn.on{background:var(--accent);color:#fff}
  .prog{font-size:13px;color:var(--muted);white-space:nowrap}
  .bar{height:6px;background:var(--line);border-radius:6px;width:120px;overflow:hidden;display:inline-block;vertical-align:middle}
  .bar>i{display:block;height:100%;background:var(--ok);width:0}
  /* cards */
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px 17px;
    box-shadow:0 2px 10px rgba(150,120,70,.06);display:flex;flex-direction:column;gap:10px;position:relative}
  .card.unfamiliar{border-color:#e08a3c;background:#fff7ec;box-shadow:0 2px 14px rgba(210,120,40,.20)}
  .card .sub-tag{position:absolute;top:0;right:16px;transform:translateY(-50%);
    font-size:11px;padding:2px 9px;border-radius:10px;color:#fff}
  .sub-core{background:var(--core)} .sub-exc{background:var(--exc)}
  .whead{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
  .word{font-family:Georgia,"Times New Roman",serif;font-size:30px;font-weight:700;letter-spacing:.5px}
  .word .hl{background:var(--amber);color:var(--accent);border-radius:6px;padding:0 3px}
  .ipa{color:var(--core);font-size:16px;font-weight:600}
  .say{margin-left:auto;border:none;background:var(--amber);color:var(--accent);border-radius:50%;
    width:34px;height:34px;font-size:16px;cursor:pointer;flex:none}
  .say:hover{background:var(--accent2);color:#fff}
  .tags{display:flex;gap:5px;flex-wrap:wrap}
  .tag{font-size:11px;padding:1px 8px;border-radius:9px;background:#f0e7d6;color:#8a6a3c}
  .tag.lv6{background:#e6f0ec;color:#2f8f83}
  .tag.tfl{background:#eae6f5;color:#6a52a8}
  .tag.gre{background:#f7e6ea;color:#b0507a}
  .mean{font-size:15.5px;font-weight:600;color:#3a332b}
  .sec{font-size:13.5px;color:#4d463c;border-top:1px dashed var(--line);padding-top:8px}
  .sec .l{font-size:11.5px;color:var(--accent);font-weight:700;letter-spacing:.5px;display:block;margin-bottom:2px}
  .roots{display:flex;flex-wrap:wrap;gap:6px}
  .root{background:#f6efe1;border-radius:8px;padding:3px 9px;font-size:12.5px}
  .root b{font-family:Georgia,serif;color:var(--accent)}
  .tip{background:#fff6e8;border-left:3px solid var(--accent2);padding:5px 10px;border-radius:0 8px 8px 0;font-size:13px}
  /* 一词多义 · 核心意象 */
  .coreimg{background:#f4f0e5;border-radius:8px;padding:6px 10px;font-size:13.5px;color:#5a4a2e;margin-bottom:7px}
  .sense{border-left:3px solid var(--accent2);padding:3px 0 3px 10px;margin:6px 0}
  .sense .s-gloss{font-size:14px}
  .sense .s-gloss b{color:#3a332b}
  .sense .s-logic{color:var(--accent);font-size:12.5px}
  .sense .s-ex{margin-top:2px;font-size:13px}
  .sense .s-en{font-family:Georgia,serif;color:#2f2a24}
  .sense .s-zh{color:#6b6154}
  .ex{margin:7px 0}
  .ex .en{font-family:Georgia,serif;font-size:14px;color:#2f2a24}
  .ex .zh{color:#6b6154;font-size:13px}
  .ex .src{display:inline-block;font-size:11px;color:#a89a86;margin-top:1px}
  .ex.famous{background:#fbf4e7;border-radius:8px;padding:7px 10px}
  /* 近义词辨析 / 反义词 */
  .lexgroup{display:flex;gap:8px;margin:4px 0;align-items:flex-start}
  .lextag{flex:none;font-size:11px;font-weight:700;padding:1px 8px;border-radius:8px;margin-top:3px}
  .lextag.syn{background:#e6f0ec;color:#2f8f83}
  .lextag.ant{background:#f7e6ea;color:#b0507a}
  .lexlist{display:flex;flex-direction:column;gap:3px;font-size:13.5px;flex:1}
  .lexlist.antline{flex-direction:row;flex-wrap:wrap;gap:6px;align-items:center}
  .lex .lw{font-family:Georgia,serif;color:var(--accent);cursor:pointer;font-weight:600}
  .lex .lw:hover{text-decoration:underline}
  .lex .lip{color:var(--core);font-size:12px}
  .lex .ln{color:#5f574c}
  .antchip{background:#faf0f2;border-radius:8px;padding:2px 9px;cursor:pointer;font-family:Georgia,serif;font-size:13px;color:#b0507a}
  .antchip:hover{background:#f6e3e8}
  .antchip i{font-style:normal;color:#9a8f86;font-size:12px}
  .nuance{background:#eef6f3;border-left:3px solid var(--core);padding:6px 10px;border-radius:0 8px 8px 0;font-size:13px;margin-top:7px;color:#33463f}
  /* memorize mode hides meaning+detail until hover/click */
  body.mem .mean, body.mem .sec{filter:blur(5px);transition:.15s;cursor:pointer}
  body.mem .card:hover .mean, body.mem .card.reveal .mean,
  body.mem .card:hover .sec, body.mem .card.reveal .sec{filter:none}
  .check{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--muted);cursor:pointer;margin-top:2px}
  .check input{width:16px;height:16px;accent-color:#c1662f}
  .card.unfamiliar .check{color:#c1662f;font-weight:600}
  .empty{text-align:center;color:var(--muted);padding:40px;grid-column:1/-1}
  footer{margin-top:36px;font-size:12px;color:var(--muted);border-top:1px solid var(--line);padding-top:14px}
  /* 测验 */
  #quizOv{display:none;position:fixed;inset:0;background:rgba(47,42,36,.55);z-index:50;
    align-items:center;justify-content:center;padding:18px}
  .qbox{background:var(--card);border-radius:20px;max-width:560px;width:100%;padding:22px 24px 20px;
    box-shadow:0 24px 70px rgba(0,0,0,.32);max-height:92vh;overflow:auto}
  .qtop{display:flex;justify-content:space-between;align-items:center;color:var(--muted);font-size:13px;margin-bottom:8px}
  .qbar2{height:6px;background:var(--line);border-radius:6px;overflow:hidden;margin-bottom:16px}
  .qbar2>i{display:block;height:100%;background:var(--accent);width:0;transition:.3s}
  .qword{font-family:Georgia,serif;font-size:40px;font-weight:700;text-align:center;margin:4px 0 2px}
  .qipa{text-align:center;color:var(--core);font-size:16px;margin-bottom:16px}
  .qopts{display:grid;gap:10px}
  .qopt{border:1.5px solid var(--line);background:#fff;border-radius:12px;padding:11px 14px;font-size:14.5px;
    cursor:pointer;text-align:left;transition:.12s;display:flex;gap:10px;align-items:flex-start;font-family:inherit;color:var(--ink)}
  .qopt:hover{border-color:var(--accent2);background:#fffaf0}
  .qopt .k{font-weight:700;color:var(--accent);flex:none}
  .qopt.right{border-color:var(--ok);background:#eafaef}
  .qopt.wrong{border-color:var(--exc);background:#fdeeea}
  .qopt.dim{opacity:.45}
  .qnext{margin-top:14px;width:100%;padding:12px;border:none;border-radius:12px;background:var(--accent);
    color:#fff;font-size:15px;font-weight:600;cursor:pointer;font-family:inherit}
  .qend{text-align:center}
  .qscore{font-size:46px;font-weight:800;color:var(--accent);margin:4px 0}
  .qwrong{text-align:left;margin:14px 0;max-height:34vh;overflow:auto}
  .qwrong .r{border-top:1px dashed var(--line);padding:7px 0;font-size:14px}
  .qwrong .r b{font-family:Georgia,serif;color:var(--exc)}
  .hint{text-align:center;color:var(--muted);font-size:12px;margin-top:10px}
  /* 精读 · 文章 + 句法分析 */
  .passage{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--accent);
    border-radius:14px;padding:18px 20px;margin:0 0 22px}
  .passage h2{margin:0 0 10px;font-size:18px;color:var(--accent)}
  .passage .p-title{font-family:Georgia,serif;font-size:20px;font-weight:700;color:var(--ink);margin-bottom:10px}
  .passage p{font-size:15px;line-height:1.9;margin:10px 0}
  .passage .en{color:#3a332b;font-family:Georgia,"Times New Roman",serif}
  .passage .zh{color:var(--muted);font-size:13.5px}
  .passage .kw{cursor:pointer;color:var(--accent);font-weight:600;border-bottom:1px dotted var(--accent2)}
  .readall{background:var(--accent);color:#fff;border:none;border-radius:20px;padding:4px 14px;font-size:13px;
    cursor:pointer;margin-left:10px;vertical-align:middle;transition:.15s}
  .readall:hover{background:var(--core)}
  .sents{background:linear-gradient(135deg,#f3f8f6,#eef3f0);border:1px solid var(--line);
    border-radius:14px;padding:18px 20px;margin:0 0 22px}
  .sents h2{margin:0 0 6px;font-size:18px;color:var(--core)}
  .sents .s-sub{color:var(--muted);font-size:13px;margin-bottom:14px}
  .sent{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0}
  .sent .s-en{font-family:Georgia,"Times New Roman",serif;font-size:15.5px;line-height:1.7;cursor:pointer;color:#3a332b}
  .sent .s-en:hover{color:var(--accent)}
  .sent .s-zh{color:var(--muted);font-size:13.5px;margin:6px 0 10px}
  .sent .s-parts{display:flex;flex-wrap:wrap;gap:6px}
  .spart{display:inline-flex;align-items:center;gap:6px;border-radius:9px;padding:4px 9px;font-size:13px;line-height:1.4}
  .spart .st{font-family:Georgia,serif;font-weight:600}
  .spart .sr{font-size:11px;color:#fff;border-radius:5px;padding:0 5px;white-space:nowrap}
  .spart .sn{font-size:12px;color:var(--muted)}
  .snotes{margin-top:10px;padding-top:8px;border-top:1px dashed var(--line);font-size:13px;color:#5f574c}
  .snotes b{color:var(--accent)}
  /* 句子内括号标注 */
  .s-flow{font-family:Georgia,"Times New Roman",serif;font-size:16px;line-height:2.1;cursor:pointer;color:#3a332b;padding:2px 0}
  .s-flow:hover{color:var(--accent)}
  .brkbox{border-radius:4px;padding:1px 1px;transition:.15s}
  .brk{font-weight:700;font-size:17px;padding:0 1px}
  .say-mini{background:none;border:none;cursor:pointer;font-size:15px;padding:0 4px;vertical-align:middle}
  @media(max-width:680px){.rules{grid-template-columns:1fr}.combo .big{font-size:44px}}
</style>
</head>
<body>
<div class="wrap">
  <div class="top">
    <a href="../index.html">← 返回总目录</a>
    <span>六级 · 托福单词记忆系统</span>
  </div>

  <header class="hero" id="hero"></header>

  <div id="passage"></div>
  <div id="sents"></div>

  <div class="toolbar">
    <input class="search" id="q" placeholder="🔎 搜索单词或释义…">
    <div class="filters" id="lvf"></div>
    <div class="filters" id="sgf"></div>
    <select class="f" id="voiceSel" title="选择发音音色（美式女声）"></select>
    <button class="btn" id="quizBtn">📝 测验</button>
    <button class="btn" id="memBtn">🧠 记忆模式</button>
    <button class="btn" id="unfamBtn">🔺 只看不熟悉 (<span id="unfamN">0</span>)</button>
  </div>

  <div class="grid" id="grid"></div>
  <footer id="foot"></footer>
</div>

<div id="quizOv"><div class="qbox" id="qbox"></div></div>

<script id="data" type="application/json">__DATA_JSON__</script>
<script>
const G = JSON.parse(document.getElementById('data').textContent);
const KEY = 'vocab-unfam-' + G.id;
let unfam = new Set(JSON.parse(localStorage.getItem(KEY) || '[]'));
let curLv = '全部', curSg = '全部', curQ = '', onlyUnfam = false;

const LVCLASS = {'六级':'lv6','托福':'tfl','GRE拓展':'gre','基础':''};
// 发音分组配色（按 subgroups 顺序循环取用）
const SGCOLORS = ['#2f8f83','#b0603f','#6a52a8','#c1662f','#3a7bd5'];
const SUBG = G.subgroups || [];
function sgIndex(key){ const i=SUBG.findIndex(s=>s.key===key); return i<0?0:i; }
function sgColor(key){ return SGCOLORS[sgIndex(key)%SGCOLORS.length]; }
function sgOf(key){ return SUBG.find(s=>s.key===key); }

// ---------- header
function renderHero(){
  const h = document.getElementById('hero');
  const rules = SUBG.map((s,i)=>{
    const c = SGCOLORS[i%SGCOLORS.length];
    return `<div class="rule" style="border-left:5px solid ${c}"><b style="color:${c}">${s.label}</b>${s.desc||''}</div>`;
  }).join('');
  const rhymes = (G.rhymeChains && G.rhymeChains.length)
    ? `<div class="rhymes"><h3>🎵 同韵顺口溜 · 点单词听发音，成串背最快</h3>${
        G.rhymeChains.map(c=>`<div class="chain"><span class="lab">${c.label}</span>${
          c.words.map(w=>`<span class="chip" onclick="say('${w}')">${w}</span>`).join('')
        }</div>`).join('')}</div>`
    : '';
  h.innerHTML = `
    <div class="combo"><span class="big">${G.combo}</span><span class="snd">${G.sound}</span></div>
    <h1>${G.title} · ${G.subtitle||''}</h1>
    <p class="intro">${G.intro}</p>
    <div class="rules">${rules}</div>
    ${rhymes}`;
}

// ---------- 精读：文章 + 句法分析
let speaking=false;
function sayPassage(btn){
  if(speaking){ speechSynthesis.cancel(); speaking=false; if(btn) btn.textContent='🔊 朗读全文'; return; }
  const P = G.passage; if(!P) return;
  const texts = (P.paragraphs||[]).map(p=>p.en).filter(Boolean);
  if(!texts.length) return;
  if(!VOICE) pickVoice();
  speaking=true; if(btn) btn.textContent='⏹ 停止朗读';
  let last=null;
  texts.forEach((t,i)=>{
    const u = new SpeechSynthesisUtterance(t);
    u.lang='en-US'; if(VOICE) u.voice=VOICE; u.rate=.95; u.pitch=1.0;
    if(i===texts.length-1) last=u;
    speechSynthesis.speak(u);
  });
  if(last) last.onend=()=>{ speaking=false; if(btn) btn.textContent='🔊 朗读全文'; };
}
function renderPassage(){
  const el = document.getElementById('passage');
  const P = G.passage; if(!P){ el.style.display='none'; return; }
  const paras = (P.paragraphs||[]).map(p=>{
    let en = p.en||'';
    // 高亮关键词（p.kws 或自动匹配词表词）
    const kws = p.kws || [];
    kws.forEach(k=>{ en = en.replace(new RegExp('('+k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','gi'), '<span class="kw" onclick="say(\'$1\')">$1</span>'); });
    return `<p><div class="en">${en}</div>${p.zh?`<div class="zh">${p.zh}</div>`:''}</p>`;
  }).join('');
  el.innerHTML = `<div class="passage"><h2>📖 精读原文</h2>
    <div class="p-title">${P.title||''} <button class="readall" onclick="sayPassage(this)">🔊 朗读全文</button></div>
    ${paras}</div>`;
}
const ROLECOLOR = { '主语':'#2f8f83','谓语':'#c1662f','宾语':'#3a7bd5','状语':'#6a52a8','定语':'#b0603f','补语':'#c1662f','从句':'#8c8072','连词':'#8c8072','介词':'#8c8072','插入语':'#8c8072','同位语':'#b0603f' };
function roleColor(r){ return ROLECOLOR[r] || '#6a52a8'; }
function escAttr(s){ return String(s||'').replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
// 句子内括号标注：介词短语 ( ) · 从句 [ ] · 非谓语 { }
const BRK = {'pp':['(',')'], 'cl':['[',']'], 'nf':['{','}']};
const BRKC = {'pp':'#6a52a8', 'cl':'#3a7bd5', 'nf':'#b0603f'};
function renderFlow(s){
  let html='';
  (s.flow||[]).forEach(it=>{
    if(it.open){ const k=it.open; html+=`<span class="brkbox" style="background:${BRKC[k]}16;border-bottom:2px solid ${BRKC[k]}66"><b class="brk" style="color:${BRKC[k]}">${BRK[k][0]}</b>`; }
    else if(it.close){ const k=it.close; html+=`<b class="brk" style="color:${BRKC[k]}">${BRK[k][1]}</b></span>`; }
    else { html+=escAttr(it.t); }
  });
  return html;
}
function renderSents(){
  const el = document.getElementById('sents');
  const S = G.sentences; if(!S || !S.length){ el.style.display='none'; return; }
  const items = S.map((s,i)=>{
    const flowHtml = (s.flow && s.flow.length) ? renderFlow(s) : escAttr(s.en);
    const parts = (s.parts||[]).map(p=>{
      const c = roleColor(p.r);
      return `<span class="spart" style="background:${c}18;border:1px solid ${c}55">
        <span class="st" style="color:${c}">${escAttr(p.t)}</span>
        <span class="sr" style="background:${c}">${p.r}</span>
        ${p.n?`<span class="sn">${p.n}</span>`:''}</span>`;
    }).join('');
    return `<div class="sent">
      <div class="s-flow" data-en="${escAttr(s.en)}" onclick="say(this.dataset.en)" title="点句子朗读">${flowHtml} <button class="say-mini" data-en="${escAttr(s.en)}" onclick="event.stopPropagation();say(this.dataset.en)" title="朗读">🔊</button></div>
      ${s.zh?`<div class="s-zh">${s.zh}</div>`:''}
      <div class="s-parts">${parts}</div>
      ${s.note?`<div class="snotes">${s.note}</div>`:''}</div>`;
  }).join('');
  el.innerHTML = `<div class="sents"><h2>🔍 长难句 · 句法分析</h2>
    <div class="s-sub">点英文句可朗读 · 括号标注：<b style="color:#6a52a8">( ) 介词短语</b> · <b style="color:#3a7bd5">[ ] 从句</b> · <b style="color:#b0603f">{ } 非谓语动词</b> · 下方色块=成分功能</div>
    ${items}</div>`;
}

// ---------- filters
function renderFilters(){
  const lvs = ['全部','六级','托福','GRE拓展','基础'];
  document.getElementById('lvf').innerHTML = lvs.map(l=>
    `<span class="f${l===curLv?' on':''}" onclick="setLv('${l}')">${l}</span>`).join('');
  const sgs = [['全部','全部'], ...SUBG.map(s=>[s.tag||s.label, s.key])];
  document.getElementById('sgf').innerHTML = sgs.map(([t,v])=>
    `<span class="f${v===curSg?' on':''}" onclick="setSg('${v}')">${t}</span>`).join('');
}
function setLv(l){curLv=l;renderFilters();renderGrid();}
function setSg(s){curSg=s;renderFilters();renderGrid();}

// ---------- speech：优先自然美式女声
let VOICE=null, VOICES=[];
// 各浏览器/系统里公认自然的美式女声，按优先级排序
const PREF=[
  'Google US English',                 // Chrome：自然女声
  'Microsoft Aria Online (Natural) - English (United States)',
  'Microsoft Jenny Online (Natural) - English (United States)',
  'Microsoft Ava Online (Natural) - English (United States)',
  'Microsoft Aria','Microsoft Jenny','Microsoft Michelle',
  'Ava (Premium)','Ava (Enhanced)','Ava',   // macOS Siri 女声
  'Samantha',                          // macOS 经典美式女声
  'Allison','Susan','Nicky','Zoe','Karen','Victoria'
];
const MALE=/(alex|daniel|fred|tom|david|mark|male|aaron|arthur|gordon|oliver|rishi|junior|ralph)/i;
function usPool(){
  VOICES = speechSynthesis.getVoices()||[];
  let us = VOICES.filter(v=>/en[-_]US/i.test(v.lang)||/United States/i.test(v.name));
  if(!us.length) us = VOICES.filter(v=>/^en/i.test(v.lang));
  return us;
}
function pickVoice(){
  const pool=usPool(); if(!pool.length) return;
  VOICE=null;
  for(const n of PREF){ const h=pool.find(v=>v.name===n)||pool.find(v=>v.name.indexOf(n)===0); if(h){VOICE=h;break;} }
  if(!VOICE) VOICE = pool.find(v=>/(samantha|ava|allison|susan|nicky|zoe|karen|victoria|aria|jenny|michelle|female|google us)/i.test(v.name))
                   || pool.find(v=>!MALE.test(v.name)) || pool[0];
  fillVoiceSel(pool);
}
function fillVoiceSel(pool){
  const s=document.getElementById('voiceSel'); if(!s) return;
  s.innerHTML = pool.map(v=>{
    const nm=v.name.replace(/ - English.*/,'').replace(/Online \(Natural\)/,'✨');
    return `<option value="${v.name}"${VOICE&&v.name===VOICE.name?' selected':''}>🎙 ${nm}</option>`;
  }).join('');
}
document.getElementById('voiceSel').addEventListener('change',e=>{
  VOICE = VOICES.find(v=>v.name===e.target.value)||VOICE; say(G.combo==='aw'?'awesome':'natural');
});
if('onvoiceschanged' in speechSynthesis) speechSynthesis.onvoiceschanged = pickVoice;
pickVoice();
function say(w){
  try{
    if(!VOICE) pickVoice();
    const u = new SpeechSynthesisUtterance(w);
    u.lang='en-US'; if(VOICE) u.voice=VOICE; u.rate=.95; u.pitch=1.0;
    speechSynthesis.cancel(); speechSynthesis.speak(u);
  }catch(e){}
}

// 高亮单词里的目标拼写：优先用该词自带的 hl（音位页里每词各自的拼写），否则用组的 combo
function hlWord(word, spell){
  const c = (spell||'').replace(/[.*+?^${}()|[\]\\\/·\s]/g,'');  // 只取干净字母做高亮，去掉 / · 空格等
  if(!c) return word;
  try{ return word.replace(new RegExp('('+c+')','i'), '<span class="hl">$1</span>'); }
  catch(e){ return word; }
}

// ---------- card
function card(w){
  const tags = (w.levels||[]).map(l=>`<span class="tag ${LVCLASS[l]||''}">${l}</span>`).join('');
  const roots = (w.roots||[]).map(r=>`<span class="root"><b>${r.part}</b> ${r.meaning}</span>`).join('');
  const exs = (w.examples||[]).map(e=>{
    const fam = /造句/.test(e.source)? '' : ' famous';
    return `<div class="ex${fam}"><div class="en">${e.en}</div><div class="zh">${e.zh}</div><span class="src">— ${e.source}</span></div>`;
  }).join('');
  const syns = (w.synonyms||[]).map(s=>
    `<div class="lex"><b class="lw" onclick="event.stopPropagation();say('${s.w}')">${s.w}</b>`+
    `${s.ipa?` <span class="lip">${s.ipa}</span>`:''}${s.note?` <span class="ln">— ${s.note}</span>`:''}</div>`).join('');
  const ants = (w.antonyms||[]).map(a=>
    `<span class="antchip" onclick="event.stopPropagation();say('${a.w}')">${a.w}${a.note?` <i>${a.note}</i>`:''}</span>`).join('');
  const lexSec = (syns||ants||w.nuance)
    ? `<div class="sec"><span class="l">🔗 近义词辨析 · 反义词</span>`+
      `${syns?`<div class="lexgroup"><span class="lextag syn">近义</span><div class="lexlist">${syns}</div></div>`:''}`+
      `${ants?`<div class="lexgroup"><span class="lextag ant">反义</span><div class="lexlist antline">${ants}</div></div>`:''}`+
      `${w.nuance?`<div class="nuance">🎯 ${w.nuance}</div>`:''}</div>`
    : '';
  const senses = (w.senses||[]).map(s=>
    `<div class="sense"><div class="s-gloss"><b>${s.gloss}</b>${s.logic?` <span class="s-logic">← ${s.logic}</span>`:''}</div>`+
    `${s.en?`<div class="s-ex"><span class="s-en">${s.en}</span> <span class="s-zh">${s.zh||''}</span></div>`:''}</div>`).join('');
  const senseSec = (w.core||senses)
    ? `<div class="sec"><span class="l">🧠 一词多义 · 核心意象串解</span>`+
      `${w.core?`<div class="coreimg">🎯 核心感觉：${w.core}</div>`:''}${senses}</div>`
    : '';
  const isU = unfam.has(w.word);
  const so = sgOf(w.subgroup);
  return `<div class="card${isU?' unfamiliar':''}" data-w="${w.word}" onclick="if(document.body.classList.contains('mem'))this.classList.toggle('reveal')">
    <span class="sub-tag" style="background:${sgColor(w.subgroup)}">${so?(so.tag||so.label):''}</span>
    <div class="whead">
      <span class="word">${hlWord(w.word, w.hl || G.combo)}</span>
      <span class="ipa">${w.ipa}</span>
      <button class="say" onclick="event.stopPropagation();say('${w.word}')" title="朗读">🔊</button>
    </div>
    <div class="tags">${tags}</div>
    <div class="mean">${w.meaning}</div>
    ${senseSec}
    ${w.etymology?`<div class="sec"><span class="l">🏛 造词来源 · 词源故事</span>${w.etymology}</div>`:''}
    ${roots?`<div class="sec"><span class="l">🧩 词根词缀</span><div class="roots">${roots}</div></div>`:''}
    ${w.phonetics?`<div class="sec"><span class="l">🗣 发音规律</span>${w.phonetics}</div>`:''}
    ${w.tip?`<div class="sec"><span class="l">💡 记忆钩子</span><div class="tip">${w.tip}</div></div>`:''}
    ${exs?`<div class="sec"><span class="l">✍️ 造句 · 名著/影视例句</span>${exs}</div>`:''}
    ${lexSec}
    <label class="check" onclick="event.stopPropagation()">
      <input type="checkbox" ${isU?'checked':''} onchange="toggleUnfam('${w.word}',this.checked)"> 🔺 标记不熟悉
    </label>
  </div>`;
}

function match(w){
  if(onlyUnfam && !unfam.has(w.word)) return false;
  if(curLv!=='全部' && !(w.levels||[]).includes(curLv)) return false;
  if(curSg!=='全部' && w.subgroup!==curSg) return false;
  if(curQ){
    const s=(w.word+' '+w.meaning).toLowerCase();
    if(!s.includes(curQ.toLowerCase())) return false;
  }
  return true;
}

function renderGrid(){
  const list = G.words.filter(match);
  // 不熟悉的置顶（稳定排序，保持各自原有相对顺序）
  list.sort((a,b)=>(unfam.has(b.word)?1:0)-(unfam.has(a.word)?1:0));
  const g = document.getElementById('grid');
  g.innerHTML = list.length? list.map(card).join('') : '<div class="empty">没有匹配的单词，换个筛选试试～</div>';
  updateUnfamCount();
}

function toggleUnfam(word, on){
  if(on) unfam.add(word); else unfam.delete(word);
  localStorage.setItem(KEY, JSON.stringify([...unfam]));
  const c = document.querySelector(`.card[data-w="${word}"]`);
  if(c) c.classList.toggle('unfamiliar', on);   // 立即变色，卡片原位不跳动；置顶在下次渲染/筛选时生效
  updateUnfamCount();
}
function updateUnfamCount(){
  const n = G.words.filter(w=>unfam.has(w.word)).length;
  const el = document.getElementById('unfamN');
  if(el) el.textContent = n;
}

document.getElementById('q').addEventListener('input',e=>{curQ=e.target.value;renderGrid();});
document.getElementById('unfamBtn').addEventListener('click',e=>{
  onlyUnfam=!onlyUnfam;
  e.currentTarget.classList.toggle('on',onlyUnfam);
  renderGrid();
});
document.getElementById('memBtn').addEventListener('click',e=>{
  document.body.classList.toggle('mem');
  e.target.classList.toggle('on');
  e.target.textContent = document.body.classList.contains('mem')?'🧠 记忆模式(开)·悬停显形':'🧠 记忆模式';
});

// ---------- 测验：英文 → 中文四选一（覆盖当前筛选到的全部单词）
let quiz=null;
function shuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
// 测验池 = 本页(筛选后)全部词 + 它们的同义词 + 衍生词（去重）
function quizPool(){
  const base = G.words.filter(match);
  const items=[]; const seen=new Set();
  const add=(word,ipa,meaning)=>{const k=(word||'').toLowerCase();
    if(!word||!meaning||seen.has(k))return; seen.add(k); items.push({word,ipa:ipa||'',meaning});};
  base.forEach(w=>{
    add(w.word,w.ipa,w.meaning);
    (w.synonyms||[]).forEach(s=>add(s.w,s.ipa,s.gloss||s.note));
    (w.derivatives||[]).forEach(dv=>add(dv.w,dv.ipa,dv.gloss||dv.note));
  });
  return items;
}
function startQuiz(src){
  const pool = src || quizPool();
  if(pool.length<4){ alert('至少要有 4 个词才能测验，请先放宽上方筛选～'); return; }
  quiz={list:shuffle(pool), i:0, score:0, wrong:[], done:false, next:null, pool:quizPool()};
  document.getElementById('quizOv').style.display='flex';
  renderQ();
}
function renderQ(){
  quiz.done=false; quiz.next=null;
  const q=quiz.list[quiz.i];
  const others=(quiz.pool||[]).filter(w=>w.meaning!==q.meaning);
  const opts=shuffle([q.meaning, ...shuffle(others).slice(0,3).map(w=>w.meaning)]);
  const K=['1','2','3','4'];
  document.getElementById('qbox').innerHTML=`
    <div class="qtop"><span>第 ${quiz.i+1} / ${quiz.list.length} 题 · 已答对 ${quiz.score}</span>
      <span style="cursor:pointer" onclick="closeQuiz()">✕ 关闭</span></div>
    <div class="qbar2"><i style="width:${quiz.i/quiz.list.length*100}%"></i></div>
    <div class="qword">${q.word} <button class="say" style="vertical-align:middle;width:30px;height:30px;font-size:14px" onclick="say('${q.word}')">🔊</button></div>
    <div class="qipa">${q.ipa}</div>
    <div class="qopts" id="qopts">${opts.map((o,k)=>
      `<button class="qopt" data-m="${encodeURIComponent(o)}" onclick="answer(this,'${encodeURIComponent(q.meaning)}')">
        <span class="k">${K[k]}</span><span>${o}</span></button>`).join('')}</div>
    <div class="hint">按 1–4 键作答 · 回车进入下一题</div>`;
  say(q.word);
}
function answer(el, correctEnc){
  if(quiz.done) return; quiz.done=true;
  const correct=decodeURIComponent(correctEnc);
  const chosen=decodeURIComponent(el.dataset.m);
  if(chosen===correct) quiz.score++; else quiz.wrong.push(quiz.list[quiz.i]);
  document.querySelectorAll('#qopts .qopt').forEach(b=>{
    const m=decodeURIComponent(b.dataset.m);
    if(m===correct) b.classList.add('right');
    else if(b===el) b.classList.add('wrong');
    else b.classList.add('dim');
    b.style.pointerEvents='none';
  });
  const btn=document.createElement('button');
  btn.className='qnext';
  btn.textContent = quiz.i<quiz.list.length-1 ? '下一题 →' : '看结果 →';
  btn.onclick=nextQ;
  document.getElementById('qbox').appendChild(btn);
  quiz.next=btn;
}
function nextQ(){
  if(quiz.i<quiz.list.length-1){ quiz.i++; renderQ(); } else endQuiz();
}
function endQuiz(){
  const tot=quiz.list.length, pct=Math.round(quiz.score/tot*100);
  const wrongHtml = quiz.wrong.length
    ? quiz.wrong.map(w=>`<div class="r"><b>${w.word}</b> ${w.ipa} — ${w.meaning}</div>`).join('')
    : '<div class="r">全部答对，太强了！🎉</div>';
  const wrongCopy = quiz.wrong.slice();
  document.getElementById('qbox').innerHTML=`
    <div class="qend">
      <div class="qtop" style="justify-content:flex-end"><span style="cursor:pointer" onclick="closeQuiz()">✕ 关闭</span></div>
      <div>本轮得分</div><div class="qscore">${quiz.score}/${tot}</div>
      <div style="color:var(--muted)">正确率 ${pct}%</div>
      <div class="qwrong"><div style="color:var(--exc);font-weight:700;margin-bottom:4px">错题（${quiz.wrong.length}）</div>${wrongHtml}</div>
      <div id="qendBtns"></div>
    </div>`;
  const box=document.getElementById('qendBtns');
  if(wrongCopy.length){
    const b1=document.createElement('button'); b1.className='qnext'; b1.textContent='只测这些错题';
    b1.onclick=()=>startQuiz(wrongCopy); box.appendChild(b1);
  }
  const b2=document.createElement('button'); b2.className='qnext';
  b2.style.cssText='background:#fff;color:var(--accent);border:1.5px solid var(--accent);margin-top:8px';
  b2.textContent='再来一轮（当前筛选）'; b2.onclick=()=>startQuiz(); box.appendChild(b2);
}
function closeQuiz(){ document.getElementById('quizOv').style.display='none'; quiz=null; }
document.getElementById('quizBtn').addEventListener('click',()=>startQuiz());
document.getElementById('quizOv').addEventListener('click',e=>{ if(e.target.id==='quizOv') closeQuiz(); });
document.addEventListener('keydown',e=>{
  if(!quiz || document.getElementById('quizOv').style.display==='none') return;
  if(quiz.next && (e.key==='Enter'||e.key===' ')){ e.preventDefault(); quiz.next.click(); return; }
  if(!quiz.done && /^[1-4]$/.test(e.key)){ const b=document.querySelectorAll('#qopts .qopt')[+e.key-1]; if(b) b.click(); }
});

document.getElementById('foot').innerHTML =
  `共 ${G.words.length} 词 · 数据源：托福 4264 词表（真实词库）+ 六级核心词 · `+
  `发音由浏览器语音合成朗读 · 名著/影视例句均为真实出处，「造句」为学习例句，「高频搭配」为常用短语。`;

renderHero(); renderPassage(); renderSents(); renderFilters(); renderGrid();
</script>
</body>
</html>
"""

# ---------------------------------------------------------------- 目录页模板
INDEX_TMPL = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>英语发音规律总表 · voca 学习系统</title>
<style>
  :root{--bg:#f7f1e7;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#eaddc9;--accent:#c1662f;--core:#2f8f83;--vio:#6a52a8}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}
  .wrap{max-width:1120px;margin:0 auto;padding:34px 20px 90px}
  h1{font-size:27px;margin:0 0 4px}
  .sub{color:var(--muted);margin-bottom:16px}
  .intro{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--accent);border-radius:12px;padding:14px 16px;font-size:14px;margin-bottom:18px}
  .built{margin-bottom:14px;font-size:14px}
  .built b{color:var(--accent)}
  .built a{display:inline-block;background:#fbe6c4;color:var(--accent);font-weight:700;border-radius:20px;padding:4px 14px;margin:6px 6px 0 0;text-decoration:none;font-family:Georgia,serif}
  .built a:hover{background:var(--accent);color:#fff}
  .legend{font-size:12px;color:var(--muted);margin-bottom:8px}
  .legend b{background:#e6f0ec;color:var(--core);border-radius:6px;padding:0 6px;font-family:Georgia,serif}
  h2.sec{font-size:20px;margin:26px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--line)}
  h2.sec.v{color:var(--core)} h2.sec.c{color:var(--vio)}
  .pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(325px,1fr));gap:14px}
  .pcard{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 15px;box-shadow:0 2px 10px rgba(150,120,70,.06)}
  .phead{display:flex;align-items:baseline;gap:10px}
  .phead .ipa{font-family:Georgia,serif;font-size:23px;font-weight:700;color:var(--accent);cursor:pointer}
  .phead .kw{color:var(--muted);font-size:13px}
  .pzh{color:#5f574c;font-size:12.5px;margin:2px 0 8px}
  .srow{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:5px 0;border-top:1px dashed var(--line);font-size:13.5px}
  .combo{flex:none;font-family:Georgia,serif;font-weight:700;background:#f2ece0;color:#7a6a4c;border-radius:7px;padding:1px 8px;min-width:62px;text-align:center}
  a.combo.has{background:#e6f0ec;color:var(--core);text-decoration:none}
  a.combo.has:hover{background:var(--core);color:#fff}
  .exs{display:flex;flex-wrap:wrap;gap:4px 9px}
  .w{font-family:Georgia,serif;color:#3a332b;cursor:pointer}
  .w:hover{color:var(--accent);text-decoration:underline}
  .cnote{width:100%;color:#a08b6a;font-size:11.5px;padding-left:2px}
  footer{margin-top:36px;color:#a89a86;font-size:12px;border-top:1px solid var(--line);padding-top:14px}
</style></head><body><div class="wrap">
  <h1>🔤 __TITLE__</h1>
  <div class="sub">__SUB__</div>
  <div class="intro">__INTRO__</div>
  <div class="built"><b>已建深度复习页（完整拆解＋近义辨析＋英译中测验）：</b><br>__BUILT__</div>
  <div class="legend">图例：<b>aw ✓</b> = 已有深度页，点开即学 · 灰底组合 = 例词可点听、深度页待建（对 cc 说「新建一组 &lt;组合&gt;」即可生成）· 点任意例词/音标听美式女声</div>
  <h2 class="sec v">🅰️ 元音 Vowels</h2>
  <div class="pgrid">__VOWELS__</div>
  <h2 class="sec c">🅱️ 辅音 Consonants</h2>
  <div class="pgrid">__CONS__</div>
  <h2 class="sec c">🔀 特别专题（不发音字母 · 软化规律 …）</h2>
  <div class="pgrid">__EXTRA__</div>
  <footer>__FOOT__</footer>
</div>
<script>
let V=null;
const PREF=['Google US English','Microsoft Aria','Microsoft Jenny','Samantha','Ava','Allison','Susan','Zoe','Karen'];
function pick(){const vs=speechSynthesis.getVoices()||[];let us=vs.filter(v=>/en[-_]US/i.test(v.lang)||/United States/i.test(v.name));if(!us.length)us=vs.filter(v=>/^en/i.test(v.lang));for(const n of PREF){const h=us.find(v=>v.name===n)||us.find(v=>v.name.indexOf(n)===0);if(h){V=h;break;}}if(!V)V=us.find(v=>/samantha|google us|female|ava|zoe|karen|allison|susan/i.test(v.name))||us[0]||vs[0]||null;}
if('onvoiceschanged'in speechSynthesis)speechSynthesis.onvoiceschanged=pick;pick();
function say(w){try{const u=new SpeechSynthesisUtterance(w);u.lang='en-US';if(V)u.voice=V;u.rate=.95;speechSynthesis.cancel();speechSynthesis.speak(u);}catch(e){}}
</script>
</body></html>
"""

def esc(s): return html.escape(str(s))

def build_group(fp):
    data = json.loads(fp.read_text(encoding="utf-8"))
    # 安全地把 JSON 塞进 <script> 标签（避免 </script> 截断）
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = (PAGE_TMPL
           .replace("__TITLE__", esc(data.get("title", data["id"])))
           .replace("__DATA_JSON__", payload))
    dest = GROUPS / f"{data['id']}.html"
    dest.write_text(out, encoding="utf-8")
    print(f"  ✓ groups/{data['id']}.html  ({len(data['words'])} 词)")
    return data

def render_pcard(p, built):
    rows = ""
    for s in p.get("spellings", []):
        exs = "".join(f'<span class="w" onclick="say(\'{esc(w)}\')">{esc(w)}</span>' for w in s.get("ex", []))
        combo, pg = s.get("combo", ""), s.get("page")
        if pg and pg in built:
            comboh = f'<a class="combo has" href="groups/{esc(pg)}.html">{esc(combo)} ✓</a>'
        else:
            comboh = f'<span class="combo">{esc(combo)}</span>'
        note = f'<span class="cnote">💡 {esc(s["note"])}</span>' if s.get("note") else ""
        rows += f'<div class="srow">{comboh}<span class="exs">{exs}</span>{note}</div>'
    return (f'<div class="pcard"><div class="phead">'
            f'<span class="ipa" onclick="say(\'{esc(p["key"])}\')">{esc(p["ipa"])} 🔊</span>'
            f'<span class="kw">如 {esc(p["key"])}</span></div>'
            f'<div class="pzh">{esc(p.get("zh",""))}</div>{rows}</div>')

def build_index(groups):
    built = {g["id"] for g in groups}
    sm_path = DATA / "_soundmap.json"
    sm = json.loads(sm_path.read_text(encoding="utf-8")) if sm_path.exists() else {"vowels": [], "consonants": [], "extra": []}
    vowels = "".join(render_pcard(p, built) for p in sm.get("vowels", []))
    cons   = "".join(render_pcard(p, built) for p in sm.get("consonants", []))
    extra  = "".join(render_pcard(p, built) for p in sm.get("extra", []))
    builtlinks = "".join(
        f'<a href="groups/{esc(g["id"])}.html">{esc(g["combo"])} {esc(g["sound"])}</a>'
        for g in sorted(groups, key=lambda x: x["id"])) or "（暂无）"
    foot = (f'{len(sm.get("vowels",[]))} 元音 + {len(sm.get("consonants",[]))} 辅音 · '
            f'已建 {len(groups)} 张深度页 · 数据 data/_soundmap.json + data/*.json · 运行 python3 build.py 重生成')
    out = (INDEX_TMPL
           .replace("__TITLE__", esc(sm.get("title", "英语发音规律总表")))
           .replace("__SUB__", esc(sm.get("subtitle", "")))
           .replace("__INTRO__", esc(sm.get("intro", "")))
           .replace("__BUILT__", builtlinks)
           .replace("__VOWELS__", vowels)
           .replace("__CONS__", cons)
           .replace("__EXTRA__", extra)
           .replace("__FOOT__", foot))
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print(f"  ✓ index.html  (发音总表: {len(sm.get('vowels',[]))}元音/{len(sm.get('consonants',[]))}辅音 · {len(groups)} 深度页)")

def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    # 词表组 = data/*.json，但排除以 _ 开头的配置文件（如 _soundmap.json）
    files = sorted(f for f in DATA.glob("*.json") if not f.name.startswith("_"))
    if only:
        files = [f for f in files if f.stem == only]
    if not files and not only:
        print("data/ 下没有找到词表 JSON"); return
    print("渲染中…")
    groups = [build_group(f) for f in files]
    # 目录页（发音规律总表）需要知道全部已建组
    all_groups = [json.loads(f.read_text(encoding="utf-8"))
                  for f in sorted(DATA.glob("*.json")) if not f.name.startswith("_")]
    build_index(all_groups)
    print("完成。用浏览器打开 index.html 或 groups/<id>.html 即可。")

if __name__ == "__main__":
    main()
