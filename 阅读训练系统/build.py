#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
托福阅读训练系统 · 渲染器
  data/*.json  →  passages/*.html（自包含阅读页） + index.html（总目录）
用法：  python3 build.py
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT  = os.path.join(ROOT, "passages")

# ── 括号法标注预设（右侧图例 + 选区工具条共用）─────────────────────────
#   bracket: 用哪种括号包住选区；false 表示不套括号
#   under  : 主干用下划线；highlight 用背景色
MARKS = [
    {"key": "trunk",  "name": "主干 S·V·O", "hint": "句子骨架",       "color": "#c0392b", "bracket": False, "under": "double"},
    {"key": "clause", "name": "从句",        "hint": "定语/宾语/主语从句", "color": "#2565c0", "bracket": "[]"},
    {"key": "phrase", "name": "修饰 / 短语",  "hint": "介词短语·分词·后置定语", "color": "#1f8a5b", "bracket": "()"},
    {"key": "insert", "name": "插入 · 同位语", "hint": "插入语/同位语/破折号成分", "color": "#8e44ad", "bracket": "{}"},
    {"key": "hard",   "name": "生词 · 难点",  "hint": "标黄，回看",     "color": "#c98a00", "bracket": False, "highlight": "#fde7bd"},
]

TYPE_LABELS = {
    "factual": "事实信息", "negative_factual": "否定事实", "inference": "推断",
    "rhetorical_purpose": "修辞目的", "vocabulary": "词汇", "reference": "指代",
    "sentence_simplification": "句子简化", "insert_text": "句子插入", "prose_summary": "内容总结",
}

# ── 阅读页模板 ────────────────────────────────────────────────────────
PAGE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 托福阅读训练</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--bad:#c0453a}
  *{box-sizing:border-box}
  html,body{height:100%}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased;overflow:hidden}
  a{color:var(--accent);text-decoration:none}
  /* 顶栏 */
  header{display:flex;align-items:center;gap:14px;padding:10px 18px;background:var(--card);border-bottom:1px solid var(--line);height:56px}
  header .back{font-size:13px;color:var(--muted)}
  header h1{font-size:16px;margin:0;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:44vw}
  .chip{font-size:12px;padding:2px 9px;border-radius:20px;background:#efe7d6;color:#6f6552;white-space:nowrap}
  .chip.dom{background:#e7f1ee;color:#2f7d72}
  header .spacer{flex:1}
  .tbtn{font-size:13px;color:#5f574c;background:#f0e9da;border:1px solid var(--line);border-radius:8px;padding:5px 10px;cursor:pointer;white-space:nowrap}
  .tbtn:hover{background:#e8dfca}
  #timer{font-variant-numeric:tabular-nums;font-size:14px;color:var(--muted);min-width:52px;text-align:center;cursor:pointer}
  /* 主体两栏 */
  .layout{display:grid;grid-template-columns:1fr 470px;height:calc(100% - 56px)}
  .article{overflow:auto;padding:30px 40px 120px;position:relative}
  .article .intro{font-style:italic;color:#786d5c;border-left:3px solid var(--line);padding-left:12px;margin-bottom:18px;font-size:15px}
  .article h2.ptitle{font-size:15px;color:var(--core);margin:0 0 20px}
  .para{margin:0 0 18px;font-size:17px;letter-spacing:.1px;position:relative;padding-left:30px}
  .para .pnum{position:absolute;left:0;top:2px;font-size:12px;color:#c3b79c;font-variant-numeric:tabular-nums;user-select:none}
  .para.flash{animation:fl 1.4s ease}
  @keyframes fl{0%,100%{background:transparent}25%{background:#fbeecb}}
  .glossary{margin-top:30px;border-top:1px dashed var(--line);padding-top:14px;font-size:14px;color:#6f6656}
  .glossary b{color:#5a5142}
  /* 标注渲染 */
  .seg{border-radius:2px}
  .brk{user-select:none;font-weight:800;cursor:pointer;padding:0 1px}
  .brk:hover{background:#f3d9c7;border-radius:3px}
  .sq{display:inline-block;min-width:16px;height:16px;line-height:15px;text-align:center;color:#b9ad95;font-size:13px;cursor:default;user-select:none}
  .sq.on{color:#fff;background:var(--accent);border-radius:3px;width:auto;padding:0 5px}
  .ins-preview{color:var(--accent);font-style:italic;background:#fbe7d8;border-radius:4px;padding:0 4px}
  /* 选区工具条 */
  #pop{position:fixed;z-index:50;display:none;background:#332c22;border-radius:10px;padding:6px;box-shadow:0 8px 24px rgba(0,0,0,.28);gap:4px}
  #pop.show{display:flex;flex-wrap:wrap;max-width:340px}
  #pop button{border:0;border-radius:7px;padding:6px 9px;font-size:13px;cursor:pointer;color:#fff;background:#4a4034;font-family:inherit;white-space:nowrap}
  #pop button:hover{filter:brightness(1.15)}
  #pop .gl{font-weight:800;margin-right:3px}
  #pop .del{background:#5a3a3a}
  /* 右侧题目栏 */
  .qpanel{overflow:auto;border-left:1px solid var(--line);background:var(--card);display:flex;flex-direction:column}
  .qnav{position:sticky;top:0;background:var(--card);border-bottom:1px solid var(--line);padding:12px 16px;z-index:5}
  .dots{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:8px}
  .dot{width:24px;height:24px;border-radius:6px;border:1px solid var(--line);background:#f3ecdd;font-size:12px;cursor:pointer;color:#6f6656;display:flex;align-items:center;justify-content:center;font-variant-numeric:tabular-nums}
  .dot.cur{border-color:var(--accent);box-shadow:0 0 0 2px #f0d9c4}
  .dot.done{background:#e6dcc6}
  .dot.ok{background:#d8ecdd;color:#2f7d54;border-color:#a9d6b8}
  .dot.no{background:#f4dcd6;color:#b3453a;border-color:#e2b3a9}
  .qmeta{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--muted)}
  .qbody{padding:16px 18px 40px;flex:1}
  .qtype{font-size:12px;color:#fff;background:var(--core);padding:2px 8px;border-radius:20px}
  .stem{font-size:15px;margin:12px 0 14px;line-height:1.65}
  .stem b{color:var(--accent)}
  .insbox{border:1px dashed var(--accent);background:#fbf1e6;border-radius:8px;padding:8px 11px;font-size:14px;margin:10px 0}
  .opts{display:flex;flex-direction:column;gap:9px}
  .opt{display:flex;gap:9px;align-items:flex-start;border:1px solid var(--line);border-radius:10px;padding:10px 12px;cursor:pointer;font-size:14px;background:#fffef9;transition:.12s}
  .opt:hover{border-color:#d8c3a4;background:#fff}
  .opt .k{font-weight:700;color:var(--muted);flex-shrink:0}
  .opt.sel{border-color:var(--accent);background:#fdf1e6}
  .opt.ok{border-color:var(--ok);background:#e7f3ea}
  .opt.no{border-color:var(--bad);background:#f7e6e2}
  .opt .tag{margin-left:auto;font-size:12px;font-weight:700}
  .opt.ok .tag{color:var(--ok)}.opt.no .tag{color:var(--bad)}
  .qfoot{display:flex;gap:10px;margin-top:16px;align-items:center}
  .btn{border:0;border-radius:9px;padding:9px 16px;font-size:14px;cursor:pointer;font-family:inherit}
  .btn.p{background:var(--accent);color:#fff}
  .btn.p:hover{filter:brightness(1.06)}
  .btn.g{background:#efe8d8;color:#5f574c}
  .btn.g:hover{background:#e6dcc6}
  .btn:disabled{opacity:.45;cursor:default}
  .expl{margin-top:14px;border-radius:10px;padding:12px 14px;font-size:14px;line-height:1.65;display:none}
  .expl.show{display:block}
  .expl.right{background:#e7f3ea;border:1px solid #b9ddc4}
  .expl.wrong{background:#f7e6e2;border:1px solid #e6bcb2}
  .expl b{color:#4a4034}
  .navrow{display:flex;justify-content:space-between;padding:12px 18px;border-top:1px solid var(--line)}
  /* 图例 */
  #legend{position:fixed;right:16px;bottom:16px;z-index:40;background:#fffdf8;border:1px solid var(--line);border-radius:12px;box-shadow:0 8px 24px rgba(120,95,55,.16);padding:12px 14px;font-size:13px;max-width:280px;display:none}
  #legend.show{display:block}
  #legend h4{margin:0 0 8px;font-size:13px;color:var(--core)}
  #legend .lg{display:flex;align-items:center;gap:8px;margin:5px 0}
  #legend .sw{font-weight:800;width:34px;text-align:center}
  #legend .tip{margin-top:8px;color:var(--muted);font-size:12px;line-height:1.5}
  .scorebar{background:#eef6ef;border:1px solid #c6e3cf;border-radius:10px;padding:10px 14px;margin:0 18px 10px;font-size:14px;color:#2f7d54;display:none}
  .scorebar.show{display:block}
  @media(max-width:900px){.layout{grid-template-columns:1fr;height:auto;overflow:auto}body{overflow:auto}.article{padding:20px}}
</style>
</head>
<body>
<header>
  <a class="back" href="../index.html">← 目录</a>
  <h1 id="ptitle"></h1>
  <span class="chip dom" id="cdom"></span>
  <span class="chip" id="cdiff"></span>
  <span class="chip" id="cwords"></span>
  <span class="spacer"></span>
  <span id="timer" title="点击开始/暂停计时（建议 18 分钟）">18:00</span>
  <button class="tbtn" id="btnLegend">图例</button>
  <button class="tbtn" id="btnClear">清空标注</button>
  <button class="tbtn" id="btnFont">A±</button>
</header>

<div class="layout">
  <div class="article" id="article"></div>
  <div class="qpanel">
    <div class="qnav">
      <div class="dots" id="dots"></div>
      <div class="qmeta"><span id="qpos"></span><span class="spacer" style="flex:1"></span><a href="#" id="locate">定位原文 ▸</a></div>
    </div>
    <div class="scorebar" id="scorebar"></div>
    <div class="qbody" id="qbody"></div>
    <div class="navrow">
      <button class="btn g" id="prev">◀ 上一题</button>
      <button class="btn g" id="next">下一题 ▶</button>
    </div>
  </div>
</div>

<div id="pop"></div>
<div id="legend"></div>

<script>
const DATA  = __PASSAGE_JSON__;
const MARKS = __MARKS_JSON__;
const TYPE_LABELS = __TYPE_LABELS__;
const PID = DATA.id;
const AKEY = 'toefl-read:annot:' + PID;   // 标注存储
const QKEY = 'toefl-read:ans:'   + PID;   // 答题存储
const markOf = k => MARKS.find(m => m.key === k);

/* ============ 状态 ============ */
let annots = load(AKEY, {});      // { paraIdx: [{id,start,end,mark}] }
let answers = load(QKEY, {});     // { qIdx: number | number[] }
let checked = {};                 // { qIdx: true } 本次已提交
let cur = 0;                      // 当前题
let fontStep = load('toefl-read:font', 0);

function load(k, dft){ try{ return JSON.parse(localStorage.getItem(k)) ?? dft; }catch(e){ return dft; } }
function save(k, v){ localStorage.setItem(k, JSON.stringify(v)); }
function esc(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

/* ============ 文章渲染 ============ */
const artEl = document.getElementById('article');

function activeHighlight(){
  // 当前题若带 highlight（词汇/指代/句子简化），作为只读系统标注渲染
  const q = DATA.questions[cur];
  if(!q || !q.highlight || q.para == null) return null;
  const pi = q.para - 1;
  const text = DATA.paragraphs[pi].text;
  const idx = text.indexOf(q.highlight);
  if(idx < 0) return null;
  return { para: pi, start: idx, end: idx + q.highlight.length };
}

function annsFor(pi){
  const list = (annots[pi] || []).map(a => ({...a, sys:false}));
  // ■ 方块作为系统 seg 边界
  const text = DATA.paragraphs[pi].text;
  for(let i=0;i<text.length;i++) if(text[i]==='■') list.push({id:'sq'+i,start:i,end:i+1,mark:'__sq',sys:true});
  const hl = activeHighlight();
  if(hl && hl.para===pi) list.push({id:'__hl',start:hl.start,end:hl.end,mark:'__hl',sys:true});
  return list;
}

function bracketPair(mk){ const m=markOf(mk); if(!m||!m.bracket) return null; return [m.bracket[0], m.bracket[1]]; }

function renderPara(pi){
  const text = DATA.paragraphs[pi].text;
  const anns = annsFor(pi);
  const bounds = new Set([0, text.length]);
  anns.forEach(a => { bounds.add(a.start); bounds.add(a.end); });
  const pts = [...bounds].sort((x,y)=>x-y);
  let sqCount = 0;
  let out = '';
  for(let i=0;i<pts.length;i++){
    const pos = pts[i];
    // 收括号（内层先收：start 大的先）
    anns.filter(a=>a.end===pos && bracketPair(a.mark)).sort((a,b)=>b.start-a.start)
        .forEach(a=>{ const m=markOf(a.mark); out += `<span class="brk" data-aid="${a.id}" data-pi="${pi}" style="color:${m.color}">${bracketPair(a.mark)[1]}</span>`; });
    // 开括号（外层先开：跨度大的先）
    anns.filter(a=>a.start===pos && bracketPair(a.mark)).sort((a,b)=>(b.end-b.start)-(a.end-a.start))
        .forEach(a=>{ const m=markOf(a.mark); out += `<span class="brk" data-aid="${a.id}" data-pi="${pi}" style="color:${m.color}">${bracketPair(a.mark)[0]}</span>`; });
    if(i===pts.length-1) break;
    const a=pos, b=pts[i+1], segText=text.slice(a,b);
    const cover = anns.filter(x=>x.start<=a && x.end>=b);
    const sqAnn = cover.find(x=>x.mark==='__sq');
    if(sqAnn){
      sqCount++;
      out += `<span class="seg sq" data-start="${a}" data-sq="${sqCount}">■</span>`;
      continue;
    }
    // 选内层（跨度最小）决定下划线/高亮
    let style='';
    const real = cover.filter(x=>x.mark!=='__sq');
    if(real.length){
      const inner = real.slice().sort((m,n)=>(m.end-m.start)-(n.end-n.start))[0];
      const m = markOf(inner.mark);
      if(inner.mark==='__hl'){ style='background:#fff3b0;font-weight:600;border-radius:2px;'; }
      else if(m){
        if(m.highlight) style += `background:${m.highlight};`;
        if(m.under==='double') style += `border-bottom:2px double ${m.color};`;
        else if(m.bracket) style += `border-bottom:1.5px solid ${m.color};`;
      }
    }
    out += `<span class="seg" data-start="${a}" style="${style}">${esc(segText)}</span>`;
  }
  return out;
}

function renderArticle(){
  let h = '';
  if(DATA.intro) h += `<div class="intro">${esc(DATA.intro)}</div>`;
  DATA.paragraphs.forEach((p, pi) => {
    h += `<div class="para" data-para="${pi}" id="para-${pi}"><span class="pnum">${p.n}</span><span class="ptext">${renderPara(pi)}</span></div>`;
  });
  if(DATA.glossary && DATA.glossary.length){
    h += '<div class="glossary"><b>Glossary</b><br>';
    h += DATA.glossary.map(g=>`<b>${esc(g.term)}</b>: ${esc(g.def)}`).join('<br>');
    h += '</div>';
  }
  artEl.innerHTML = h;
  artEl.style.fontSize = (1 + fontStep*0.08) + 'em';
  applyInsertPreview();
}

function rerenderPara(pi){
  const el = artEl.querySelector(`#para-${pi} .ptext`);
  if(el) el.innerHTML = renderPara(pi);
}

/* ============ 选区 → 纯文本偏移 ============ */
function plainOffset(pEl, node, off){
  const segs = pEl.querySelectorAll('.seg');
  for(const s of segs){
    const base = +s.dataset.start;
    const r = document.createRange(); r.selectNodeContents(s);
    let c; try{ c = r.comparePoint(node, off); }catch(e){ continue; }
    if(c===0){ return node.nodeType===3 ? base+off : base + (off>0 ? s.textContent.length : 0); }
    if(c<0){ return base; }
  }
  return DATA.paragraphs[+pEl.dataset.para].text.length;
}

function readSelection(){
  const sel = window.getSelection();
  if(!sel.rangeCount || sel.isCollapsed) return null;
  const r = sel.getRangeAt(0);
  let node = r.commonAncestorContainer;
  let pEl = node.nodeType===3 ? node.parentElement : node;
  pEl = pEl.closest('.para');
  if(!pEl || !artEl.contains(pEl)) return null;
  const pi = +pEl.dataset.para;
  let start = plainOffset(pEl, r.startContainer, r.startOffset);
  let end   = plainOffset(pEl, r.endContainer, r.endOffset);
  if(end < start) [start,end] = [end,start];
  const text = DATA.paragraphs[pi].text;
  // 去掉首尾空白
  while(start<end && /\s/.test(text[start])) start++;
  while(end>start && /\s/.test(text[end-1])) end--;
  if(end<=start) return null;
  return { pi, start, end, rect: r.getBoundingClientRect() };
}

/* ============ 选区工具条 ============ */
const pop = document.getElementById('pop');
let curSel = null;

function buildPop(){
  let h = '';
  MARKS.forEach(m=>{
    const g = m.bracket ? m.bracket[0]+m.bracket[1] : (m.under? '＿' : '▉');
    h += `<button data-mk="${m.key}" style="background:${m.color}" title="${m.hint}"><span class="gl">${g}</span>${m.name}</button>`;
  });
  h += `<button class="del" data-mk="__del" title="清除选区内的标注">清除</button>`;
  pop.innerHTML = h;
}
buildPop();

function showPop(sel){
  curSel = sel;
  pop.classList.add('show');
  const pr = pop.getBoundingClientRect();
  let x = sel.rect.left + sel.rect.width/2 - pr.width/2;
  let y = sel.rect.top - pr.height - 8;
  x = Math.max(8, Math.min(x, innerWidth - pr.width - 8));
  if(y < 8) y = sel.rect.bottom + 8;
  pop.style.left = x+'px'; pop.style.top = y+'px';
}
function hidePop(){ pop.classList.remove('show'); curSel=null; }

pop.addEventListener('mousedown', e=>{
  const b = e.target.closest('button'); if(!b || !curSel) return;
  e.preventDefault();
  const mk = b.dataset.mk, {pi,start,end} = curSel;
  if(mk==='__del'){
    annots[pi] = (annots[pi]||[]).filter(a => a.end<=start || a.start>=end);
    if(!annots[pi].length) delete annots[pi];
  }else{
    if(!annots[pi]) annots[pi]=[];
    annots[pi].push({ id:'a'+Date.now()+Math.round(performance.now()), start, end, mark:mk });
  }
  save(AKEY, annots); rerenderPara(pi); hidePop();
  window.getSelection().removeAllRanges();
});

document.addEventListener('mouseup', e=>{
  if(pop.contains(e.target)) return;
  setTimeout(()=>{ const s = readSelection(); if(s) showPop(s); else hidePop(); }, 0);
});
document.addEventListener('mousedown', e=>{ if(!pop.contains(e.target)) hidePop(); });

// 点击括号删除该条标注
artEl.addEventListener('click', e=>{
  const b = e.target.closest('.brk'); if(!b) return;
  const pi=+b.dataset.pi, id=b.dataset.aid;
  annots[pi] = (annots[pi]||[]).filter(a=>a.id!==id);
  if(!annots[pi].length) delete annots[pi];
  save(AKEY, annots); rerenderPara(pi);
});

/* ============ 题目渲染 ============ */
const qbody = document.getElementById('qbody');
const dotsEl = document.getElementById('dots');
const KEYS = ['A','B','C','D','E','F'];

function isMulti(q){ return q.type==='prose_summary'; }

function renderDots(){
  dotsEl.innerHTML = DATA.questions.map((q,i)=>{
    let cls='dot'; if(i===cur) cls+=' cur';
    if(checked[i]){ cls += judge(i) ? ' ok' : ' no'; }
    else if(answers[i]!=null && (!isMulti(q) || answers[i].length)) cls+=' done';
    return `<div class="${cls}" data-i="${i}">${i+1}</div>`;
  }).join('');
}

function judge(i){
  const q=DATA.questions[i], a=answers[i];
  if(isMulti(q)){ const need=q.answer.slice().sort().join(','); const got=(a||[]).slice().sort().join(','); return need===got; }
  return a===q.answer;
}

function renderQ(){
  const q = DATA.questions[cur];
  document.getElementById('qpos').textContent = `第 ${cur+1} / ${DATA.questions.length} 题`;
  let h = `<span class="qtype">${TYPE_LABELS[q.type]||q.type}</span>`;
  h += `<div class="stem">${q.stem}</div>`;
  if(q.type==='insert_text' && q.insert_sentence){
    h += `<div class="insbox">待插入句：<b>${esc(q.insert_sentence)}</b></div>`;
  }
  if(q.type==='prose_summary' && q.intro_sentence){
    h += `<div class="insbox" style="border-style:solid">导语：${esc(q.intro_sentence)}</div>`;
  }
  const multi = isMulti(q);
  const sel = answers[cur];
  const done = checked[cur];
  h += '<div class="opts">';
  q.options.forEach((opt,oi)=>{
    let cls='opt';
    const chosen = multi ? (sel||[]).includes(oi) : sel===oi;
    if(chosen) cls+=' sel';
    if(done){
      const correct = multi ? q.answer.includes(oi) : oi===q.answer;
      if(correct) cls+=' ok'; else if(chosen) cls+=' no';
    }
    let tag='';
    if(done){ const correct = multi ? q.answer.includes(oi) : oi===q.answer;
      if(correct) tag='<span class="tag">✓ 正确</span>'; else if(chosen) tag='<span class="tag">✗</span>'; }
    h += `<div class="${cls}" data-oi="${oi}"><span class="k">${KEYS[oi]}</span><span>${opt}</span>${tag}</div>`;
  });
  h += '</div>';
  const submitLabel = done ? '已提交' : '提交';
  h += `<div class="qfoot">
    <button class="btn p" id="submit" ${done?'disabled':''}>${submitLabel}</button>
    ${multi?'<span style="font-size:12px;color:#8c8072">多选：选 3 项</span>':''}
  </div>`;
  h += `<div class="expl ${done?(judge(cur)?'right show':'wrong show'):''}" id="expl"><b>${done?(judge(cur)?'✓ 回答正确':'✗ 回答错误'):''}</b><br>${q.explain||''}</div>`;
  qbody.innerHTML = h;

  qbody.querySelectorAll('.opt').forEach(el=>{
    el.addEventListener('click', ()=>{
      if(checked[cur]) return;
      const oi=+el.dataset.oi;
      if(multi){
        let arr = answers[cur]||[];
        if(arr.includes(oi)) arr=arr.filter(x=>x!==oi);
        else { if(arr.length>=3){ return; } arr=[...arr,oi]; }
        answers[cur]=arr;
      }else answers[cur]=oi;
      save(QKEY, answers); renderQ(); renderDots();
    });
  });
  const sb = qbody.querySelector('#submit');
  if(sb) sb.addEventListener('click', ()=>{
    if(answers[cur]==null || (multi && answers[cur].length<3)){ sb.textContent = multi?'请选满 3 项':'请先选择'; setTimeout(()=>sb.textContent='提交',900); return; }
    checked[cur]=true; renderQ(); renderDots(); updateScore();
    if(q.type==='insert_text') applyInsertPreview();
  });
  renderDots();
  document.getElementById('prev').disabled = cur===0;
  document.getElementById('next').disabled = cur===DATA.questions.length-1;
  applyInsertPreview();
}

function updateScore(){
  const total = DATA.questions.length;
  const done = Object.keys(checked).length;
  if(done<total){ document.getElementById('scorebar').classList.remove('show'); return; }
  let ok=0; for(let i=0;i<total;i++) if(judge(i)) ok++;
  const sb=document.getElementById('scorebar');
  sb.classList.add('show');
  sb.innerHTML = `本篇完成：<b>${ok} / ${total}</b> 正确${ok>=total*0.8?' 🎉 达到高分区间':''}`;
}

/* ============ insert_text 预览 ============ */
function applyInsertPreview(){
  // 清除旧预览
  artEl.querySelectorAll('.sq.on').forEach(s=>{s.classList.remove('on');});
  artEl.querySelectorAll('.ins-preview').forEach(s=>s.remove());
  const q = DATA.questions[cur];
  if(q.type!=='insert_text' || answers[cur]==null) return;
  const oi = answers[cur];
  const sq = artEl.querySelector(`#para-${q.para-1} .sq[data-sq="${oi+1}"]`);
  if(sq){
    sq.classList.add('on');
    if(checked[cur] && q.insert_sentence){
      const span=document.createElement('span');
      span.className='ins-preview'; span.textContent=' '+q.insert_sentence+' ';
      sq.after(span);
    }
  }
}

/* ============ 导航 ============ */
document.getElementById('prev').onclick = ()=>{ if(cur>0){cur--; onQChange();} };
document.getElementById('next').onclick = ()=>{ if(cur<DATA.questions.length-1){cur++; onQChange();} };
dotsEl.addEventListener('click', e=>{ const d=e.target.closest('.dot'); if(d){ cur=+d.dataset.i; onQChange(); } });
document.getElementById('locate').onclick = e=>{ e.preventDefault(); locate(); };

function onQChange(){
  // 重渲染受 highlight 影响的段落
  DATA.paragraphs.forEach((p,pi)=>rerenderPara(pi));
  renderQ();
  locate(true);
}
function locate(soft){
  const q=DATA.questions[cur]; if(q.para==null) return;
  const el=artEl.querySelector(`#para-${q.para-1}`); if(!el) return;
  el.scrollIntoView({behavior:'smooth', block: soft?'nearest':'center'});
  if(!soft){ el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash'); }
}

/* ============ 顶栏控件 ============ */
document.getElementById('ptitle').textContent = DATA.title;
document.getElementById('cdom').textContent = DATA.domain;
document.getElementById('cdiff').textContent = '难度 ' + '★'.repeat(DATA.difficulty) + '☆'.repeat(5-DATA.difficulty);
document.getElementById('cwords').textContent = (DATA.est_words||'') + ' 词';

document.getElementById('btnClear').onclick = ()=>{
  if(!confirm('清空本篇全部括号 / 标注？')) return;
  annots={}; save(AKEY, annots); renderArticle();
};
document.getElementById('btnFont').onclick = ()=>{
  fontStep = (fontStep+1)%4; save('toefl-read:font', fontStep);
  artEl.style.fontSize = (1 + fontStep*0.08) + 'em';
};

// 图例
const legend = document.getElementById('legend');
legend.innerHTML = '<h4>括号法图例（选中原文即可标）</h4>' +
  MARKS.map(m=>{ const g=m.bracket?m.bracket[0]+m.bracket[1]:(m.under?'＿＿':'▉'); return `<div class="lg"><span class="sw" style="color:${m.color}">${g}</span><span><b>${m.name}</b> · ${m.hint}</span></div>`;}).join('') +
  '<div class="tip">用法：鼠标划选原文中的成分 → 弹出条里点对应括号；把从句/短语/插入语逐层括起来，剩下没括的就是<b>主干</b>。点括号可删除；右上「清空标注」重来。</div>';
document.getElementById('btnLegend').onclick = ()=>legend.classList.toggle('show');

// 计时器（倒计时 18 分钟，点击开始/暂停）
let tLeft=18*60, tRun=false, tId=null;
const tEl=document.getElementById('timer');
function fmt(s){ const m=Math.floor(s/60), ss=s%60; return (m<10?'0':'')+m+':'+(ss<10?'0':'')+ss; }
function tick(){ if(tLeft>0){tLeft--; tEl.textContent=fmt(tLeft); if(tLeft===0){tEl.style.color='var(--bad)'; tRun=false; clearInterval(tId);}} }
tEl.onclick=()=>{ if(tRun){clearInterval(tId); tRun=false; tEl.style.opacity=.55;} else {tId=setInterval(tick,1000); tRun=true; tEl.style.opacity=1;} };

/* ============ 键盘：← → 切题 ============ */
document.addEventListener('keydown', e=>{
  if(e.target.tagName==='INPUT') return;
  if(e.key==='ArrowRight' && cur<DATA.questions.length-1){ cur++; onQChange(); }
  if(e.key==='ArrowLeft' && cur>0){ cur--; onQChange(); }
});

/* ============ 启动 ============ */
renderArticle();
renderQ();
// 恢复已提交状态
Object.keys(answers).forEach(k=>{ /* 保留作答，但不自动判分，等用户点提交 */ });
updateScore();
</script>
</body>
</html>
"""

INDEX = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>托福阅读训练系统</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}
  .wrap{max-width:1000px;margin:0 auto;padding:40px 22px 80px}
  h1{font-size:28px;margin:0 0 4px}
  .sub{color:var(--muted);margin-bottom:22px}
  .notice{background:#fff6e8;border:1px solid #f0d9b0;border-left:5px solid var(--accent);border-radius:12px;padding:14px 16px;font-size:14px;margin-bottom:24px}
  .notice b{color:var(--accent)}
  .filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:18px}
  .filters button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:5px 14px;font-size:13px;cursor:pointer;color:#5f574c;font-family:inherit}
  .filters button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
  .cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
  a.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px;text-decoration:none;color:inherit;box-shadow:0 2px 12px rgba(150,120,70,.06);transition:.15s}
  a.card:hover{transform:translateY(-3px);box-shadow:0 8px 22px rgba(150,120,70,.15);border-color:#d8c8a8}
  .card .top{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
  .card .dom{font-size:12px;background:#e7f1ee;color:#2f7d72;padding:2px 9px;border-radius:20px}
  .card .diff{font-size:12px;color:#d99a2f}
  .card h2{font-size:18px;margin:6px 0}
  .card .meta{color:var(--muted);font-size:13px;margin-top:8px}
  .empty{color:var(--muted);padding:30px;text-align:center}
  footer{margin-top:30px;color:#a89a86;font-size:12px}
</style>
</head>
<body>
<div class="wrap">
  <h1>📖 托福阅读训练系统</h1>
  <div class="sub">左边文章可反复滚动 · 右边逐题作答 · 支持「括号法」划句标注</div>
  <div class="notice">
    <b>怎么用：</b>点开一篇文章 → 左栏读文章、右栏一道道刷题。<br>
    <b>括号法：</b>在左栏<b>用鼠标划选</b>任意成分（从句 / 短语 / 插入语）→ 弹出的小工具条里点对应<b>括号</b>，
    逐层括起，剩下没括的就是句子<b>主干</b>；生词标黄。标注自动保存，滚动来回都在。点括号即可删除。<br>
    <b>难度：</b>全部按托福真实学术难度撰写（★★★★ 起），题型齐全（事实 / 推断 / 修辞 / 词汇 / 句子简化 / 句子插入 / 内容总结）。
  </div>
  <div class="filters" id="filters"></div>
  <div class="cards" id="cards"></div>
  <div class="empty" id="empty" style="display:none">还没有文章。往 <code>data/</code> 放 JSON 后运行 <code>python3 build.py</code>。</div>
  <footer>托福阅读系统 · data/*.json → build.py → passages/*.html · 共 __COUNT__ 篇</footer>
</div>
<script>
const LIST = __LIST_JSON__;
const cardsEl=document.getElementById('cards'), fEl=document.getElementById('filters');
const doms=['全部',...[...new Set(LIST.map(x=>x.domain))]];
let curF='全部';
function stars(n){return '★'.repeat(n)+'☆'.repeat(5-n);}
function render(){
  const list=LIST.filter(x=>curF==='全部'||x.domain===curF);
  document.getElementById('empty').style.display=LIST.length?'none':'block';
  cardsEl.innerHTML=list.map(x=>`<a class="card" href="passages/${x.id}.html">
    <div class="top"><span class="dom">${x.domain}</span><span class="diff">${stars(x.difficulty)}</span></div>
    <h2>${x.title}</h2>
    <div class="meta">${x.est_words} 词 · ${x.nq} 题${x.intro?'<br>'+x.intro:''}</div>
  </a>`).join('');
  fEl.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.d===curF));
}
fEl.innerHTML=doms.map(d=>`<button data-d="${d}" class="${d==='全部'?'on':''}">${d}</button>`).join('');
fEl.addEventListener('click',e=>{const b=e.target.closest('button'); if(b){curF=b.dataset.d; render();}});
render();
</script>
</body>
</html>
"""

def build():
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    passages = []
    for f in files:
        with open(f, encoding="utf-8") as fp:
            d = json.load(fp)
        pj = json.dumps(d, ensure_ascii=False)
        page = (PAGE
                .replace("__TITLE__", html.escape(d["title"]))
                .replace("__PASSAGE_JSON__", pj)
                .replace("__MARKS_JSON__", json.dumps(MARKS, ensure_ascii=False))
                .replace("__TYPE_LABELS__", json.dumps(TYPE_LABELS, ensure_ascii=False)))
        out = os.path.join(OUT, d["id"] + ".html")
        with open(out, "w", encoding="utf-8") as fp:
            fp.write(page)
        passages.append({
            "id": d["id"], "title": d["title"], "domain": d["domain"],
            "difficulty": d["difficulty"], "est_words": d.get("est_words", ""),
            "nq": len(d["questions"]), "intro": d.get("intro", ""),
        })
        print("  ✓", d["id"], "—", len(d["questions"]), "题")
    idx = (INDEX
           .replace("__LIST_JSON__", json.dumps(passages, ensure_ascii=False))
           .replace("__COUNT__", str(len(passages))))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fp:
        fp.write(idx)
    print(f"完成：{len(passages)} 篇 → passages/，已刷新 index.html")

if __name__ == "__main__":
    build()
