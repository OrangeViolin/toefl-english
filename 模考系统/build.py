#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新版 TOEFL iBT 模考系统 · 渲染器
  data/*.json  →  mocks/*.html（自包含整场模考运行器） + index.html（总目录）
用法：  python3 build.py
"""
import json, os, glob, html

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
OUT  = os.path.join(ROOT, "mocks")

# ── 科目 / 题型元数据 ─────────────────────────────────────────────
SECTIONS = [
    {"key": "reading",   "name": "阅读 Reading",   "time_min": 27},
    {"key": "listening", "name": "听力 Listening", "time_min": 27},
    {"key": "writing",   "name": "写作 Writing",   "time_min": 23},
    {"key": "speaking",  "name": "口语 Speaking",  "time_min": 8},
]
TYPE_LABELS = {
    "complete_words": "补全单词 Complete the Words",
    "read_daily": "生活阅读 Read in Daily Life",
    "read_academic": "学术短文 Read an Academic Passage",
    "listen_choose": "选回应 Listen & Choose a Response",
    "listen_conversation": "听对话 Listen to a Conversation",
    "listen_announcement": "听通知 Listen to an Announcement",
    "listen_talk": "听讲座 Listen to an Academic Talk",
    "build_sentence": "连词成句 Build a Sentence",
    "write_email": "写邮件 Write an Email",
    "write_discussion": "学术讨论 Write for an Academic Discussion",
    "listen_repeat": "跟读 Listen and Repeat",
    "take_interview": "面试 Take an Interview",
}
TYPE_SECTION = {
    "complete_words": "reading", "read_daily": "reading", "read_academic": "reading",
    "listen_choose": "listening", "listen_conversation": "listening",
    "listen_announcement": "listening", "listen_talk": "listening",
    "build_sentence": "writing", "write_email": "writing", "write_discussion": "writing",
    "listen_repeat": "speaking", "take_interview": "speaking",
}

# ── 官方 band 换算表（Overview Table 3：band → 旧 0–30 分段）────────
BAND_READING = [[6,29,30],[5.5,27,28],[5,24,26],[4.5,22,23],[4,18,21],[3.5,12,17],[3,6,11],[2.5,4,5],[2,3,3],[1.5,2,2],[1,0,1]]
BAND_LISTEN  = [[6,28,30],[5.5,26,27],[5,22,25],[4.5,20,21],[4,17,19],[3.5,13,16],[3,9,12],[2.5,6,8],[2,4,5],[1.5,2,3],[1,0,1]]
CEFR = [[6,"C2"],[5.5,"C1"],[5,"C1"],[4.5,"B2"],[4,"B2"],[3.5,"B1"],[3,"B1"],[2.5,"A2"],[2,"A2"],[1.5,"A1"],[1,"A1"]]
OVERALL120 = {"6":"114","5.5":"107+","5":"95+","4.5":"86+","4":"72+","3.5":"58+","3":"44+","2.5":"34+","2":"24+","1.5":"12+","1":"0+"}

# ── 官方 0–5 评分量规（供报告嵌入 & cc 打分）─────────────────────
RUBRICS = {
 "write_email": "Write an Email（0–5）\n5 完全成功：有效清晰、语言驾驭稳定；论述有效支撑沟通目的；句式多样用词精准地道；社交惯例得体；几乎无错。\n4 大体成功：基本有效易懂；论述较充分；句式多样得体；少量词法/语法错。\n3 部分成功：基本完成但语言局限使部分信息不清；论述部分支撑；句式词汇中等；结构/词形/习语/社交惯例有明显错。\n2 大体不成功：尝试但大体无效；论述有限或跑题；范围窄；错误累积。\n1 不成功：近乎不可懂；几无论述；电报式；严重频繁出错。\n0：空白/离题/非英文/照抄/乱敲。",
 "write_discussion": "Write for an Academic Discussion（0–5）\n5 完全成功：贴题清楚的讨论贡献、语言稳定；解释/举例/细节充分相关；句式多样用词地道；几乎无错。\n4 大体成功：相关易懂；解释举例较充分；句式多样得体；少量错。\n3 部分成功：大体相关可懂；例证有缺失/不清/不相关；词法句法习语有明显错。\n2 大体不成功：尝试贡献但语言局限使观点难懂；论述差或部分相关；范围有限；错误累积。\n1 不成功：贡献无效；几无连贯观点；极受限；严重频繁错。\n0：空白/离题/非英文/照抄/乱敲。",
 "listen_repeat": "Listen and Repeat（0–5）\n5：逐字精确复述、完全可懂。\n4：抓住原意但非逐字：一两个功能词缺失/替换、时态数标记误、两词互换；个别实词发音模糊但完成。\n3：句子基本完整但未准确传意；含多数要点但多个功能词变动、个别实词缺失/大改；可懂度偶有问题。\n2：缺失重要部分且/或高度不准；非独立完整句；可懂度低。\n1：几乎没抓住或大体不可懂。\n0：无作答/不可懂/非英文/无关。",
 "take_interview": "Take an Interview（0–5）\n5 完全成功：充分回答、清楚流利、切题、语速自然停顿得当、发音清晰节奏语调有效、语法词汇多样准确。\n4 大体成功：切题有展开但衔接欠佳；语速大体流畅偶停顿；个别词句需费力听；语法词汇大体够用。\n3 部分成功：切题但展开/清晰有限；停顿多节奏碎、填充词多；发音偶影响可懂；语法词汇受限。\n2 大体不成功：支撑不足/不够可懂；关联弱多借题干；可懂度低。\n1 不成功：仅勉强触及、掌控极弱、多孤立词句。\n0：无作答/不可懂/非英文/离题。",
}

# ═══════════════════════ 页面模板 ═══════════════════════
PAGE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__ · 托福模考</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--bad:#c0453a;--blue:#4a5cc7}
  *{box-sizing:border-box}
  html,body{margin:0;height:100%}
  body{background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
  a{color:var(--accent);text-decoration:none}
  .wrap{max-width:900px;margin:0 auto;padding:0 20px 120px}
  /* 顶栏 */
  header{position:sticky;top:0;z-index:20;background:var(--card);border-bottom:1px solid var(--line);display:flex;align-items:center;gap:14px;padding:10px 20px}
  header .sec{font-weight:700;font-size:15px}
  header .prog{font-size:13px;color:var(--muted)}
  header .spacer{flex:1}
  #timer{font-variant-numeric:tabular-nums;font-size:15px;background:#efe7d6;border-radius:8px;padding:4px 10px;color:#6f6552}
  #timer.warn{background:#f4dcd6;color:var(--bad)}
  .exit{font-size:13px;color:var(--muted);cursor:pointer}
  /* 开始菜单 */
  .menu{padding:44px 20px 80px;max-width:900px;margin:0 auto}
  .menu h1{font-size:26px;margin:0 0 4px}
  .menu .sub{color:var(--muted);margin-bottom:20px}
  .menu .notice{background:#fff6e8;border:1px solid #f0d9b0;border-left:5px solid var(--accent);border-radius:12px;padding:13px 15px;font-size:13.5px;margin-bottom:22px}
  .menu .notice b{color:var(--accent)}
  .bigbtn{display:block;width:100%;text-align:left;background:var(--accent);color:#fff;border:0;border-radius:16px;padding:20px 22px;font-size:19px;font-weight:700;cursor:pointer;font-family:inherit;margin-bottom:22px}
  .bigbtn small{display:block;font-weight:400;font-size:13px;opacity:.9;margin-top:4px}
  .menu h3{font-size:14px;color:var(--core);margin:18px 0 10px}
  .chips{display:flex;flex-wrap:wrap;gap:8px}
  .chips button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:7px 14px;font-size:13px;cursor:pointer;color:#5f574c;font-family:inherit}
  .chips button:hover{background:#f0e9da;border-color:#d8c8a8}
  /* 题目区 */
  .block{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px;margin-top:22px;box-shadow:0 2px 12px rgba(150,120,70,.05)}
  .tasklabel{display:inline-block;font-size:12px;color:#fff;background:var(--core);padding:2px 10px;border-radius:20px;margin-bottom:12px}
  .instr{font-size:14px;color:var(--muted);margin-bottom:12px}
  .passage{background:#faf7ef;border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:15.5px;white-space:pre-wrap;margin-bottom:16px}
  .passage .ttl{font-weight:700;margin-bottom:8px}
  .qblock{margin:16px 0;padding-top:14px;border-top:1px dashed var(--line)}
  .qstem{font-size:15px;font-weight:600;margin-bottom:10px}
  .opts{display:flex;flex-direction:column;gap:8px}
  .opt{display:flex;gap:9px;align-items:flex-start;border:1px solid var(--line);border-radius:10px;padding:9px 12px;cursor:pointer;font-size:14px;background:#fffef9}
  .opt:hover{border-color:#d8c3a4}
  .opt .k{font-weight:700;color:var(--muted)}
  .opt.sel{border-color:var(--accent);background:#fdf1e6}
  /* 补全单词 */
  .cw{font-size:16px;line-height:2.8}
  .cwword{white-space:nowrap}
  .cw .pre{font-weight:600}
  .cwc{width:15px;text-align:center;border:0;border-bottom:2px dashed var(--accent);background:transparent;font-size:15px;padding:0 0 1px;margin:0 1.5px;font-family:inherit;color:var(--accent);text-transform:lowercase;caret-color:var(--accent)}
  .cwc:focus{outline:none;border-bottom-color:var(--core);background:#fbf1e6}
  .cwc.done{border-bottom-style:solid}
  /* 连词成句 */
  .bs-prompt{background:#eef1fb;border-radius:10px;padding:10px 13px;font-size:14.5px;margin-bottom:12px}
  .bs-slot{min-height:46px;border:2px dashed var(--accent);border-radius:10px;padding:8px;display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-bottom:12px;background:#fdf7f0}
  .bs-fixed{color:var(--muted);font-weight:600;padding:6px 2px}
  .tok{background:#eae2d0;border:1px solid #d8c8a8;border-radius:8px;padding:6px 12px;font-size:14px;cursor:pointer;font-family:inherit}
  .tok:hover{background:#e0d5bd}
  .bs-bank{display:flex;flex-wrap:wrap;gap:7px}
  /* 音频 */
  .audiorow{display:flex;align-items:center;gap:12px;margin:8px 0 14px;flex-wrap:wrap}
  .playbtn{background:var(--blue);color:#fff;border:0;border-radius:10px;padding:9px 16px;font-size:14px;cursor:pointer;font-family:inherit}
  .playbtn:disabled{opacity:.5;cursor:default}
  .accent{font-size:12px;color:var(--muted)}
  .transcript{font-size:13.5px;color:#6f6656;background:#faf7ef;border-radius:8px;padding:10px 12px;margin-top:8px;white-space:pre-wrap;display:none}
  .transcript.show{display:block}
  .linkbtn{font-size:12px;color:var(--muted);cursor:pointer;text-decoration:underline}
  /* 写作 */
  textarea{width:100%;min-height:180px;border:1px solid var(--line);border-radius:10px;padding:12px;font-size:15px;font-family:inherit;line-height:1.6;resize:vertical}
  textarea:focus{outline:none;border-color:var(--accent)}
  .wc{font-size:13px;color:var(--muted);margin-top:6px}
  .wc.low{color:var(--bad)}
  .post{background:#f2f0fb;border-radius:10px;padding:11px 14px;font-size:14px;margin-bottom:10px}
  .post b{color:var(--blue)}
  .bullets{margin:8px 0 0;padding-left:20px;font-size:14px}
  /* 口语录音 */
  .sp-item{border-top:1px dashed var(--line);padding:12px 0}
  .recbtn{background:var(--bad);color:#fff;border:0;border-radius:10px;padding:8px 15px;font-size:13.5px;cursor:pointer;font-family:inherit}
  .recbtn.rec{background:#7a2b22;animation:pulse 1s infinite}
  @keyframes pulse{50%{opacity:.6}}
  .rectime{font-variant-numeric:tabular-nums;color:var(--bad);font-size:13px}
  audio{height:34px;vertical-align:middle}
  /* 导航 */
  .nav{position:fixed;bottom:0;left:0;right:0;background:var(--card);border-top:1px solid var(--line);display:flex;justify-content:center;gap:12px;padding:12px}
  .btn{border:0;border-radius:10px;padding:11px 22px;font-size:15px;cursor:pointer;font-family:inherit}
  .btn.p{background:var(--accent);color:#fff}.btn.p:hover{filter:brightness(1.06)}
  .btn.g{background:#efe8d8;color:#5f574c}.btn.g:hover{background:#e6dcc6}
  .btn:disabled{opacity:.4;cursor:default}
  /* 成绩单 */
  .scorecard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px;margin-top:22px}
  .bandrow{display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid var(--line)}
  .bandrow .nm{width:120px;font-weight:600}
  .bandnum{font-size:26px;font-weight:800;color:var(--accent);width:70px}
  .bandrow .dt{font-size:13px;color:var(--muted)}
  .overall{background:linear-gradient(135deg,#c1662f,#e0913c);color:#fff;border-radius:14px;padding:18px 22px;margin:18px 0;display:flex;align-items:center;gap:20px}
  .overall .big{font-size:44px;font-weight:800;line-height:1}
  .overall .meta{font-size:14px}
  .scoreinput{width:56px;border:1px solid var(--line);border-radius:8px;padding:5px;font-size:15px;text-align:center;font-family:inherit}
  .review{margin-top:8px;font-size:13.5px}
  .review .ri{padding:6px 0;border-bottom:1px dashed var(--line)}
  .review .ok{color:var(--ok)}.review .no{color:var(--bad)}
  .copybtn{background:var(--core);color:#fff;border:0;border-radius:9px;padding:7px 14px;font-size:13px;cursor:pointer;font-family:inherit;margin-top:8px}
  details{margin-top:8px}summary{cursor:pointer;color:var(--muted);font-size:13px}
</style>
</head>
<body>
<div id="app"></div>
<script>
const MOCK = __MOCK_JSON__;
const SECTIONS = __SECTIONS__;
const TYPE_LABELS = __TYPE_LABELS__;
const TYPE_SECTION = __TYPE_SECTION__;
const BAND_READING = __BAND_READING__;
const BAND_LISTEN = __BAND_LISTEN__;
const CEFR = __CEFR__;
const OVERALL120 = __OVERALL120__;
const RUBRICS = __RUBRICS__;
const RKEY = 'toefl-mock:resp:' + MOCK.id;

/* ───────── 工具 ───────── */
const $ = s => document.querySelector(s);
const app = $('#app');
function esc(s){ return (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function norm(s){ return (s||'').toLowerCase().replace(/[.,!?;:'"’]/g,'').replace(/\s+/g,' ').trim(); }
function load(){ try{ return JSON.parse(localStorage.getItem(RKEY))||{}; }catch(e){ return {}; } }
function save(){ localStorage.setItem(RKEY, JSON.stringify(resp)); }
let resp = load();          // 客观/写作作答： key -> value
const audioStore = {};      // 口语录音 blob url： key -> url
const KEYS = ['A','B','C','D','E','F'];

/* ───────── 语音合成（听力，多口音，离线）───────── */
let voices = [];
function loadVoices(){ voices = window.speechSynthesis ? speechSynthesis.getVoices() : []; }
if(window.speechSynthesis){ loadVoices(); speechSynthesis.onvoiceschanged = loadVoices; }
function pickVoice(accent, idx){
  const map = {US:'en-US',UK:'en-GB',AU:'en-AU',NZ:'en-EN'};
  const lang = map[accent]||'en-US';
  let c = voices.filter(v=>v.lang===lang);
  if(!c.length) c = voices.filter(v=>v.lang && v.lang.toLowerCase().startsWith('en'));
  if(!c.length) c = voices;
  return c[idx % (c.length||1)] || null;
}
function speakOne(text, accent, idx, rate){
  return new Promise(res=>{
    if(!window.speechSynthesis){ res(); return; }
    const u = new SpeechSynthesisUtterance(text);
    const v = pickVoice(accent, idx||0); if(v) u.voice = v;
    u.rate = rate||0.95; u.onend = res; u.onerror = res;
    speechSynthesis.speak(u);
  });
}
async function speakSeq(items, accent){ // items: [{text, idx}]
  speechSynthesis.cancel();
  for(const it of items){ await speakOne(it.text, accent, it.idx||0); }
}

/* ───────── 录音（口语，离线）───────── */
let micStream = null, activeRec = null;
async function getMic(){ if(!micStream) micStream = await navigator.mediaDevices.getUserMedia({audio:true}); return micStream; }
function startRec(seconds, onTick, onDone){
  getMic().then(stream=>{
    const mr = new MediaRecorder(stream); const chunks=[];
    mr.ondataavailable = e=>chunks.push(e.data);
    let left = seconds;
    const iv = setInterval(()=>{ left--; onTick(left); if(left<=0){ stop(); } }, 1000);
    function stop(){ clearInterval(iv); if(mr.state!=='inactive') mr.stop(); }
    mr.onstop = ()=>{ const blob = new Blob(chunks,{type:'audio/webm'}); onDone(URL.createObjectURL(blob)); activeRec=null; };
    mr.start(); onTick(left);
    activeRec = { stop };
  }).catch(e=>{ alert('无法录音：请在 Chrome/Edge 打开并允许麦克风权限。\n'+e.message); });
}

/* ───────── 模式 & 区块 ───────── */
// 全部区块（稳定 id，与模式无关）
const ALLBLOCKS = [];
SECTIONS.forEach(sec=>{
  const s = MOCK.sections[sec.key]; if(!s) return;
  (s.tasks||[]).forEach((task,ti)=> ALLBLOCKS.push({ id: sec.key+'-'+ti, section: sec.key, task }));
});
let MODE = null;         // 'full' | 'sec:reading' | 'type:listen_talk'
let blocks = [];         // 当前模式下的区块
let cur = 0;             // 当前区块下标
let secRemain = {};      // 每科剩余秒
let timerIv = null;

function startMode(mode){
  MODE = mode;
  if(mode==='full') blocks = ALLBLOCKS.slice();
  else if(mode.startsWith('sec:')) blocks = ALLBLOCKS.filter(b=>b.section===mode.slice(4));
  else if(mode.startsWith('type:')) blocks = ALLBLOCKS.filter(b=>b.task.type===mode.slice(5));
  cur = 0;
  secRemain = {};
  SECTIONS.forEach(s=> secRemain[s.key] = (MOCK.sections[s.key]?.time_min || s.time_min)*60);
  renderRunner();
}

/* ───────── 开始菜单 ───────── */
function renderMenu(){
  if(timerIv){ clearInterval(timerIv); timerIv=null; }
  const typeChips = Object.keys(TYPE_LABELS).filter(t=> ALLBLOCKS.some(b=>b.task.type===t))
    .map(t=>`<button data-mode="type:${t}">${TYPE_LABELS[t]}</button>`).join('');
  const secChips = SECTIONS.filter(s=>MOCK.sections[s.key]).map(s=>`<button data-mode="sec:${s.key}">${s.name}</button>`).join('');
  app.innerHTML = `<div class="menu">
    <h1>📝 ${esc(MOCK.title)}</h1>
    <div class="sub">新版 TOEFL iBT 仿真 · 阅读→听力→写作→口语 · 1–6 band 估分</div>
    <div class="notice">
      <b>用 Chrome / Edge 打开</b>。听力用<b>浏览器语音合成</b>朗读（离线，多口音）；口语需<b>允许麦克风</b>录音。<br>
      客观题（阅读/听力/连词成句）<b>自动判分并估算 band</b>；写作与口语作答按官方 0–5 量规——一键<b>复制报告贴回给 cc 打分</b>。<br>
      提示：本卷为<b>固定仿真卷</b>（真考的阅读/听力为两模块自适应）。作答自动本地保存。
    </div>
    <button class="bigbtn" data-mode="full">▶ 开始整场模考<small>四科连考 · 计时 · 最后出各科 band + 总分 + CEFR</small></button>
    <h3>按科目练</h3><div class="chips">${secChips}</div>
    <h3>按题型练（新版 9 题型）</h3><div class="chips">${typeChips}</div>
  </div>`;
  app.querySelectorAll('[data-mode]').forEach(b=> b.onclick = ()=> startMode(b.dataset.mode));
}

/* ───────── 运行器骨架 ───────── */
function renderRunner(){
  if(cur >= blocks.length){ renderResults(); return; }
  const b = blocks[cur];
  const sec = SECTIONS.find(s=>s.key===b.section);
  // 计算本模式内该科的进度
  const inSec = blocks.filter(x=>x.section===b.section);
  const posInSec = inSec.indexOf(b)+1;
  app.innerHTML = `
    <header>
      <span class="sec">${sec.name}</span>
      <span class="prog">${posInSec} / ${inSec.length}</span>
      <span class="spacer"></span>
      <span id="timer">--:--</span>
      <span class="exit" id="exit">✕ 退出</span>
    </header>
    <div class="wrap"><div id="blockarea"></div></div>
    <div class="nav">
      <button class="btn g" id="prev">◀ 上一题</button>
      <button class="btn p" id="next">${cur===blocks.length-1?'交卷 · 看成绩':'下一题 ▶'}</button>
    </div>`;
  $('#exit').onclick = ()=>{ if(confirm('退出到菜单？作答已保存。')) renderMenu(); };
  $('#prev').onclick = ()=>{ if(cur>0){ speechSynthesis.cancel(); cur--; renderRunner(); } };
  $('#prev').disabled = cur===0;
  $('#next').onclick = ()=>{ speechSynthesis.cancel(); cur++; renderRunner(); };
  renderBlock(b, $('#blockarea'));
  startTimer(b.section);
}
function startTimer(secKey){
  if(timerIv) clearInterval(timerIv);
  const t = $('#timer');
  function draw(){ const s=secRemain[secKey]; const m=Math.floor(Math.max(0,s)/60), ss=Math.max(0,s)%60;
    t.textContent = (m<10?'0':'')+m+':'+(ss<10?'0':'')+ss; t.classList.toggle('warn', s<=60); }
  draw();
  timerIv = setInterval(()=>{ if(secRemain[secKey]>0){ secRemain[secKey]--; draw(); } }, 1000);
}

/* ───────── 各题型渲染 ───────── */
function renderBlock(b, el){
  const t = b.task.type;
  const head = `<div class="tasklabel">${TYPE_LABELS[t]}</div>`;
  el.innerHTML = `<div class="block">${head}<div id="body"></div></div>`;
  const body = el.querySelector('#body');
  ({ complete_words:cwRender, read_daily:readRender, read_academic:readRender,
     listen_choose:lcRender, listen_conversation:lstRender, listen_announcement:lstRender,
     listen_talk:lstRender, build_sentence:bsRender, write_email:emailRender,
     write_discussion:discRender, listen_repeat:repeatRender, take_interview:interviewRender
   }[t])(b, body);
}

// MCQ 通用
function mcq(key, q, body){
  const sel = resp[key];
  const wrap = document.createElement('div'); wrap.className='qblock';
  wrap.innerHTML = `<div class="qstem">${q.stem}</div><div class="opts">${
    q.options.map((o,i)=>`<div class="opt${sel===i?' sel':''}" data-i="${i}"><span class="k">${KEYS[i]}</span><span>${o}</span></div>`).join('')}</div>`;
  wrap.querySelectorAll('.opt').forEach(op=> op.onclick = ()=>{
    resp[key]=+op.dataset.i; save();
    wrap.querySelectorAll('.opt').forEach(x=>x.classList.remove('sel')); op.classList.add('sel');
  });
  body.appendChild(wrap);
}

// 补全单词：text 中用 [[shown|answer]] 标每个空
// 每个缺失字母渲染成一个虚线小格（格子数 = 缺的字母数，即官方 "mi_ _ _" 提示）
function cwRender(b, body){
  const t = b.task;
  body.innerHTML = `<div class="instr">补出每个词缺失的字母：<b>虚线格子的个数 = 还差几个字母</b>（首句完整，其后每隔一词挖去后半截）。</div><div class="cw" id="cw"></div>`;
  const cw = body.querySelector('#cw');
  const parts = t.text.split(/(\[\[[^\]]*\]\])/);
  let bi = 0;
  parts.forEach(p=>{
    const m = p.match(/^\[\[([^|]*)\|([^\]]*)\]\]$/);
    if(m){
      const key = b.id+':b'+(bi++), n = m[2].length, cur = resp[key]||'';
      let boxes = '';
      for(let j=0;j<n;j++) boxes += `<input class="cwc" maxlength="1" autocomplete="off" spellcheck="false" data-k="${key}" value="${esc(cur[j]||'')}">`;
      const word = document.createElement('span'); word.className='cwword';
      word.innerHTML = `<span class="pre">${esc(m[1])}</span>${boxes}`;
      cw.appendChild(word);
    } else if(p){ cw.appendChild(document.createTextNode(p)); }
  });
  const list = [...cw.querySelectorAll('.cwc')];
  function assemble(key){ let s=''; cw.querySelectorAll('.cwc[data-k="'+key+'"]').forEach(x=>{ s+=x.value; x.classList.toggle('done', !!x.value); }); resp[key]=s; save(); }
  list.forEach((inp,i)=>{
    inp.classList.toggle('done', !!inp.value);
    inp.addEventListener('input', ()=>{ inp.value = inp.value.replace(/[^a-zA-Z]/g,'').slice(-1).toLowerCase(); assemble(inp.dataset.k); if(inp.value && list[i+1]) list[i+1].focus(); });
    inp.addEventListener('keydown', e=>{ if(e.key==='Backspace' && !inp.value && list[i-1]){ list[i-1].focus(); e.preventDefault(); } });
  });
}

// 阅读（生活/学术）
function readRender(b, body){
  const t = b.task;
  const ttl = t.title ? `<div class="ttl">${esc(t.title)}</div>` : (t.genre?`<div class="ttl">［${esc(t.genre)}］</div>`:'');
  body.innerHTML = `<div class="passage">${ttl}${esc(t.text)}</div>`;
  (t.questions||[]).forEach((q,i)=> mcq(b.id+':q'+i, q, body));
}

// 听力：选回应（只听一句）
function lcRender(b, body){
  const t = b.task;
  body.innerHTML = `<div class="instr">听一句话，选出最合适的回应（原文不显示）。</div>
    <div class="audiorow"><button class="playbtn" id="play">▶ 播放</button><span class="accent">口音：${t.accent||'US'}</span>
    <span class="linkbtn" id="show" style="display:none">显示原文</span></div>
    <div class="transcript" id="tr">${esc(t.prompt)}</div>`;
  wirePlay(body, [{text:t.prompt, idx:0}], t.accent, body.querySelector('#play'));
  mcq(b.id+':q0', {stem:'Choose the best response.', options:t.options}, body);
}
// 听力：对话/通知/讲座
function lstRender(b, body){
  const t = b.task;
  const items = t.lines ? t.lines.map(l=>({text:l.text, idx: l.who==='M'?0:1}))
                        : [{text:t.text, idx:0}];
  const trans = t.lines ? t.lines.map(l=>`${l.who==='M'?'M':'W'}: ${l.text}`).join('\n') : t.text;
  body.innerHTML = `<div class="instr">${esc(t.intro||'Listen, then answer.')}</div>
    <div class="audiorow"><button class="playbtn" id="play">▶ 播放音频</button><span class="accent">口音：${t.accent||'US'}</span>
    <span class="linkbtn" id="show">显示原文</span></div>
    <div class="transcript" id="tr">${esc(trans)}</div>`;
  wirePlay(body, items, t.accent, body.querySelector('#play'));
  (t.questions||[]).forEach((q,i)=> mcq(b.id+':q'+i, q, body));
}
function wirePlay(body, items, accent, btn){
  const tr = body.querySelector('#tr'), show = body.querySelector('#show');
  btn.onclick = async ()=>{ btn.disabled=true; const old=btn.textContent; btn.textContent='▶ 播放中…';
    await speakSeq(items, accent); btn.disabled=false; btn.textContent=old; if(show) show.style.display='inline'; };
  if(show) show.onclick = ()=> tr.classList.toggle('show');
}

// 连词成句
function bsRender(b, body){
  const t = b.task; const key = b.id;
  body.innerHTML = `<div class="instr">重排下列词/词组，组成合语法、且能恰当回应上句的句子。</div>
    <div class="bs-prompt">🗣 ${esc(t.prompt)}</div>
    <div class="bs-slot" id="slot"></div>
    <div class="bs-bank" id="bank"></div>
    <div style="margin-top:8px"><span class="linkbtn" id="reset">↺ 清空重排</span></div>`;
  let order = resp[key] ? resp[key].slice() : [];   // token 下标顺序
  const slot = body.querySelector('#slot'), bank = body.querySelector('#bank');
  function draw(){
    slot.innerHTML = (t.before?`<span class="bs-fixed">${esc(t.before)}</span>`:'') +
      order.map(i=>`<button class="tok" data-o="${i}">${esc(t.tokens[i])}</button>`).join('') +
      (t.after?`<span class="bs-fixed">${esc(t.after)}</span>`:'');
    bank.innerHTML = t.tokens.map((tk,i)=> order.includes(i)?'':`<button class="tok" data-b="${i}">${esc(tk)}</button>`).join('');
    slot.querySelectorAll('[data-o]').forEach(x=> x.onclick=()=>{ order=order.filter(i=>i!=+x.dataset.o); resp[key]=order; save(); draw(); });
    bank.querySelectorAll('[data-b]').forEach(x=> x.onclick=()=>{ order.push(+x.dataset.b); resp[key]=order; save(); draw(); });
  }
  body.querySelector('#reset').onclick = ()=>{ order=[]; resp[key]=order; save(); draw(); };
  draw();
}

// 写邮件
function emailRender(b, body){
  const t = b.task; const key=b.id;
  body.innerHTML = `<div class="instr">限时约 ${Math.round((t.time_sec||420)/60)} 分钟。用完整句子写一封邮件，达成下列沟通目的。</div>
    <div class="passage">${esc(t.scenario)}
${t.bullets?('\n在邮件中：'+ t.bullets.map(x=>'\n • '+x).join('')):''}</div>
    <div style="font-size:13px;color:var(--muted);margin-bottom:6px">To: ${esc(t.to||'')} ｜ Subject: ${esc(t.subject||'')}</div>
    <textarea id="ta" placeholder="在此作答…">${esc(resp[key]||'')}</textarea>
    <div class="wc" id="wc"></div>`;
  wireWriting(body, key, 0);
}
// 学术讨论
function discRender(b, body){
  const t = b.task; const key=b.id;
  body.innerHTML = `<div class="instr">限时约 ${Math.round((t.time_sec||600)/60)} 分钟。写出你的立场并论证，回应下面的讨论（有效作答≥${t.min_words||100}词）。</div>
    <div class="post"><b>教授：</b> ${esc(t.professor)}</div>
    <div class="post"><b>学生 A：</b> ${esc(t.student1)}</div>
    <div class="post"><b>学生 B：</b> ${esc(t.student2)}</div>
    <textarea id="ta" placeholder="写出你的观点并论证…">${esc(resp[key]||'')}</textarea>
    <div class="wc" id="wc"></div>`;
  wireWriting(body, key, t.min_words||100);
}
function wireWriting(body, key, minWords){
  const ta = body.querySelector('#ta'), wc = body.querySelector('#wc');
  function count(){ const n = (ta.value.trim().match(/\S+/g)||[]).length; wc.textContent = n+' 词'+(minWords?` / 建议 ≥${minWords}`:''); wc.classList.toggle('low', minWords && n<minWords); }
  ta.oninput = ()=>{ resp[key]=ta.value; save(); count(); }; count();
}

// 跟读
function repeatRender(b, body){
  const t = b.task;
  const secs = i => (i<2?8:(i<5?10:12));
  body.innerHTML = `<div class="instr">${esc(t.scenario)}</div>
    <div style="font-size:13px;color:var(--muted);margin-bottom:6px">逐句：▶ 听一遍 → ⏺ 录音（自动停）→ ▶ 回放。口音：${t.accent||'US'}</div>
    <div id="list"></div>`;
  const list = body.querySelector('#list');
  t.sentences.forEach((s,i)=>{
    const key = b.id+':s'+i;
    const row = document.createElement('div'); row.className='sp-item';
    row.innerHTML = `<div style="font-size:13px;color:var(--muted)">第 ${i+1} 句 · 答题 ${secs(i)} 秒</div>
      <div class="audiorow">
        <button class="playbtn play">▶ 听</button>
        <button class="recbtn rc">⏺ 录音</button>
        <span class="rectime rt"></span>
        <span class="pb"></span>
        <span class="linkbtn sh">显示原句</span>
      </div><div class="transcript tx">${esc(s)}</div>`;
    wireSpeakItem(row, [{text:s,idx:0}], t.accent, key, secs(i));
    list.appendChild(row);
  });
}
// 面试
function interviewRender(b, body){
  const t = b.task;
  body.innerHTML = `<div class="instr">${esc(t.scenario)}</div>
    <div style="font-size:13px;color:var(--muted);margin-bottom:6px">共 ${t.questions.length} 题，每题 45 秒。▶ 听题 → ⏺ 录音（自动停）→ ▶ 回放。口音：${t.accent||'US'}</div>
    <div id="list"></div>`;
  const list = body.querySelector('#list');
  t.questions.forEach((q,i)=>{
    const key = b.id+':q'+i;
    const row = document.createElement('div'); row.className='sp-item';
    row.innerHTML = `<div style="font-size:13px;color:var(--muted)">第 ${i+1} 题 · 45 秒</div>
      <div class="audiorow">
        <button class="playbtn play">▶ 听题</button>
        <button class="recbtn rc">⏺ 录音</button>
        <span class="rectime rt"></span>
        <span class="pb"></span>
        <span class="linkbtn sh">显示题目</span>
      </div><div class="transcript tx">${esc(q)}</div>`;
    wireSpeakItem(row, [{text:q,idx:0}], t.accent, key, 45);
    list.appendChild(row);
  });
}
function wireSpeakItem(row, items, accent, key, secs){
  const play=row.querySelector('.play'), rc=row.querySelector('.rc'), rt=row.querySelector('.rt'),
        pb=row.querySelector('.pb'), sh=row.querySelector('.sh'), tx=row.querySelector('.tx');
  play.onclick = async ()=>{ play.disabled=true; await speakSeq(items, accent); play.disabled=false; };
  sh.onclick = ()=> tx.classList.toggle('show');
  if(audioStore[key]) pb.innerHTML = `<audio controls src="${audioStore[key]}"></audio>`;
  rc.onclick = ()=>{
    if(activeRec){ activeRec.stop(); return; }
    rc.classList.add('rec'); rc.textContent='⏹ 停止';
    startRec(secs, left=>{ rt.textContent = left+'s'; },
      url=>{ audioStore[key]=url; rc.classList.remove('rec'); rc.textContent='⏺ 重录'; rt.textContent='';
             pb.innerHTML = `<audio controls src="${url}"></audio>`; });
  };
}

/* ───────── 判分 & 成绩单 ───────── */
function bandFromRaw(raw, table){ for(const [b,lo,hi] of table){ if(raw>=lo && raw<=hi) return b; } return 1; }
function prodBand(score0to5){ return Math.max(1, Math.min(6, Math.round(score0to5/5*6*2)/2)); }
function cefrOf(band){ for(const [b,l] of CEFR){ if(band>=b) return l; } return 'A1'; }
function round5(x){ return Math.round(x*2)/2; }

function scoreObjective(){
  let r={c:0,t:0}, l={c:0,t:0}, bs={c:0,t:0}; const review={reading:[],listening:[],writing:[]};
  ALLBLOCKS.forEach(b=>{
    const t=b.task, sec=b.section;
    if(t.type==='complete_words'){
      const ans=[...t.text.matchAll(/\[\[([^|]*)\|([^\]]*)\]\]/g)];
      ans.forEach((m,i)=>{ const got=(resp[b.id+':b'+i]||'').toLowerCase().replace(/[^a-z]/g,''); const want=m[2].toLowerCase();
        const ok=got===want; r.c+=ok?1:0; r.t++; review.reading.push({q:'补词 '+(m[1]+'…'), you:got||'—', key:want, ok}); });
    } else if(t.type==='read_daily'||t.type==='read_academic'){
      (t.questions||[]).forEach((q,i)=>{ const got=resp[b.id+':q'+i]; const ok=got===q.answer; r.c+=ok?1:0; r.t++;
        review.reading.push({q:q.stem, you:got!=null?KEYS[got]:'—', key:KEYS[q.answer], ok}); });
    } else if(sec==='listening' && t.questions){
      (t.questions||[]).forEach((q,i)=>{ const got=resp[b.id+':q'+i]; const ok=got===q.answer; l.c+=ok?1:0; l.t++;
        review.listening.push({q:q.stem, you:got!=null?KEYS[got]:'—', key:KEYS[q.answer], ok}); });
    } else if(t.type==='listen_choose'){
      const got=resp[b.id+':q0']; const ok=got===t.answer; l.c+=ok?1:0; l.t++;
      review.listening.push({q:'选回应', you:got!=null?KEYS[got]:'—', key:KEYS[t.answer], ok});
    } else if(t.type==='build_sentence'){
      const order=resp[b.id]||[]; const got=norm((t.before||'')+' '+order.map(i=>t.tokens[i]).join(' ')+' '+(t.after||''));
      const cands=[t.answer,...(t.accept||[])].map(norm); const ok=cands.includes(got);
      bs.c+=ok?1:0; bs.t++; review.writing.push({q:'连词成句', you:order.map(i=>t.tokens[i]).join(' ')||'—', key:t.answer, ok});
    }
  });
  return {r,l,bs,review};
}

function renderResults(){
  if(timerIv){ clearInterval(timerIv); timerIv=null; }
  speechSynthesis.cancel();
  const {r,l,bs,review} = scoreObjective();
  const rBand = r.t? bandFromRaw(Math.round(r.c/r.t*30), BAND_READING):null;
  const lBand = l.t? bandFromRaw(Math.round(l.c/l.t*30), BAND_LISTEN):null;
  // 主观任务清单
  const essays = ALLBLOCKS.filter(b=>b.task.type==='write_email'||b.task.type==='write_discussion');
  const speaks = ALLBLOCKS.filter(b=>b.task.type==='listen_repeat'||b.task.type==='take_interview');

  const revHtml = arr => arr.length? `<details><summary>逐题回顾（${arr.filter(x=>x.ok).length}/${arr.length} 对）</summary><div class="review">${
    arr.map(x=>`<div class="ri"><span class="${x.ok?'ok':'no'}">${x.ok?'✓':'✗'}</span> ${esc(x.q).slice(0,80)}　你:<b>${esc(x.you)}</b>${x.ok?'':' ｜ 答案:<b>'+esc(x.key)+'</b>'}</div>`).join('')}</div></details>` : '';

  app.innerHTML = `<header><span class="sec">成绩单</span><span class="spacer"></span><span class="exit" id="exit">✕ 回菜单</span></header>
  <div class="wrap"><div class="scorecard">
    <div class="overall" id="overall"><div class="big" id="ovband">—</div><div class="meta" id="ovmeta">填入下方写作/口语分后自动计算总分</div></div>

    <div class="bandrow"><span class="nm">阅读 Reading</span><span class="bandnum">${rBand??'—'}</span>
      <span class="dt">客观题 ${r.c}/${r.t} 正确（折 raw≈${r.t?Math.round(r.c/r.t*30):0}/30）　CEFR ${rBand?cefrOf(rBand):'—'}</span></div>
    ${revHtml(review.reading)}
    <div class="bandrow"><span class="nm">听力 Listening</span><span class="bandnum">${lBand??'—'}</span>
      <span class="dt">客观题 ${l.c}/${l.t} 正确（折 raw≈${l.t?Math.round(l.c/l.t*30):0}/30）　CEFR ${lBand?cefrOf(lBand):'—'}</span></div>
    ${revHtml(review.listening)}

    <div class="bandrow"><span class="nm">写作 Writing</span><span class="bandnum" id="wBand">—</span>
      <span class="dt">连词成句 ${bs.c}/${bs.t} 对${essays.length?'　+ 邮件/讨论按官方0–5打分（下方填入）':''}</span></div>
    ${revHtml(review.writing)}
    <div id="essayGrade"></div>

    <div class="bandrow"><span class="nm">口语 Speaking</span><span class="bandnum" id="sBand">—</span>
      <span class="dt">跟读 / 面试 按官方 0–5 打分（下方填入）</span></div>
    <div id="speakGrade"></div>
  </div></div>
  <div class="nav"><button class="btn g" id="menu">← 回菜单</button><button class="btn p" id="recalc">重新计算总分</button></div>`;
  $('#exit').onclick = $('#menu').onclick = renderMenu;

  // 主观任务：报告复制 + 0–5 输入
  const eg = $('#essayGrade');
  essays.forEach(b=>{
    const txt = resp[b.id]||''; const div=document.createElement('div'); div.style.margin='6px 0 14px';
    div.innerHTML = `<div style="font-size:14px;font-weight:600">${TYPE_LABELS[b.task.type]}　cc评分：<input class="scoreinput" id="sc-${b.id}" type="number" min="0" max="5" step="0.5" value="${resp['grade:'+b.id]??''}"> / 5</div>
      <div style="font-size:12.5px;color:var(--muted)">已写 ${(txt.trim().match(/\S+/g)||[]).length} 词</div>
      <button class="copybtn" data-copy="${b.id}">复制评分报告给 cc</button>`;
    eg.appendChild(div);
  });
  const sg = $('#speakGrade');
  speaks.forEach(b=>{
    const div=document.createElement('div'); div.style.margin='6px 0 14px';
    div.innerHTML = `<div style="font-size:14px;font-weight:600">${TYPE_LABELS[b.task.type]}　cc评分：<input class="scoreinput" id="sc-${b.id}" type="number" min="0" max="5" step="0.5" value="${resp['grade:'+b.id]??''}"> / 5</div>
      <button class="copybtn" data-copy="${b.id}">复制口语报告给 cc</button>`;
    sg.appendChild(div);
  });
  app.querySelectorAll('[data-copy]').forEach(btn=> btn.onclick = ()=> copyReport(btn.dataset.copy));

  function recalc(){
    // 收集 0–5
    let ws=[], ss=[];
    if(bs.t) ws.push(prodBand(bs.c/bs.t*5));
    essays.forEach(b=>{ const v=$('#sc-'+b.id).value; resp['grade:'+b.id]=v; if(v!=='') ws.push(prodBand(+v)); });
    speaks.forEach(b=>{ const v=$('#sc-'+b.id).value; resp['grade:'+b.id]=v; if(v!=='') ss.push(prodBand(+v)); });
    save();
    const wBand = ws.length? round5(ws.reduce((a,b)=>a+b,0)/ws.length):null;
    const sBand = ss.length? round5(ss.reduce((a,b)=>a+b,0)/ss.length):null;
    $('#wBand').textContent = wBand??'—'; $('#sBand').textContent = sBand??'—';
    const parts=[rBand,lBand,wBand,sBand].filter(x=>x!=null);
    if(parts.length){ const ov=round5(parts.reduce((a,b)=>a+b,0)/parts.length);
      $('#ovband').textContent=ov;
      $('#ovmeta').innerHTML = `总分 band（四科均值）　CEFR <b>${cefrOf(ov)}</b>　≈ 旧制 ${OVERALL120[String(ov)]||''} /120${parts.length<4?'<br><small>（部分科目未评分，为现有科目均值）</small>':''}`;
    }
  }
  $('#recalc').onclick = recalc;
  app.querySelectorAll('.scoreinput').forEach(i=> i.oninput = recalc);
  recalc();
}

function copyReport(id){
  const b = ALLBLOCKS.find(x=>x.id===id); const t=b.task;
  let txt='';
  if(t.type==='write_email'){
    txt = `【托福写作·Write an Email 评分请求】请依据官方 0–5 量规给我打分(0–5)并给出改进建议。\n\n[情景]\n${t.scenario}\n[要求]\n${(t.bullets||[]).map(x=>'• '+x).join('\n')}\n\n[我的作答]\n${resp[id]||'(空)'}\n\n[评分量规]\n${RUBRICS.write_email}`;
  } else if(t.type==='write_discussion'){
    txt = `【托福写作·Write for an Academic Discussion 评分请求】请依据官方 0–5 量规给我打分(0–5)并给出改进建议。\n\n[教授]\n${t.professor}\n[学生A]\n${t.student1}\n[学生B]\n${t.student2}\n\n[我的作答]\n${resp[id]||'(空)'}\n\n[评分量规]\n${RUBRICS.write_discussion}`;
  } else if(t.type==='listen_repeat'){
    txt = `【托福口语·Listen and Repeat 评分请求】我逐句跟读了下列句子，请依据官方 0–5 量规逐句点评并给总分(0–5)。（若需逐字比对可用『托福口语』的 whisper 转写我的录音）\n\n[原句]\n${t.sentences.map((s,i)=>(i+1)+'. '+s).join('\n')}\n\n[评分量规]\n${RUBRICS.listen_repeat}`;
  } else if(t.type==='take_interview'){
    txt = `【托福口语·Take an Interview 评分请求】面试题如下，请依据官方 0–5 量规点评并给分(0–5)。（可用『托福口语』whisper 转写我的录音后再评）\n\n[情景]\n${t.scenario}\n[题目]\n${t.questions.map((q,i)=>(i+1)+'. '+q).join('\n')}\n\n[评分量规]\n${RUBRICS.take_interview}`;
  }
  navigator.clipboard.writeText(txt).then(()=>{ event.target.textContent='✓ 已复制'; setTimeout(()=>event.target.textContent=event.target.dataset.copy?event.target.textContent:'',1200); })
   .catch(()=> { prompt('复制以下内容贴给 cc：', txt); });
}

/* ───────── 启动 ───────── */
renderMenu();
</script>
</body>
</html>
"""

INDEX = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>托福模考系统</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83}
  *{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6}
  .wrap{max-width:900px;margin:0 auto;padding:40px 22px 80px}
  h1{font-size:28px;margin:0 0 4px}.sub{color:var(--muted);margin-bottom:22px}
  .notice{background:#fff6e8;border:1px solid #f0d9b0;border-left:5px solid var(--accent);border-radius:12px;padding:14px 16px;font-size:14px;margin-bottom:24px}
  .notice b{color:var(--accent)}
  table{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden;font-size:13.5px;margin-bottom:24px;border:1px solid var(--line)}
  th,td{padding:8px 10px;border:1px solid var(--line);text-align:left}th{background:#eef1fb}
  .cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
  a.card{display:block;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;text-decoration:none;color:inherit;box-shadow:0 2px 12px rgba(150,120,70,.06);transition:.15s}
  a.card:hover{transform:translateY(-3px);box-shadow:0 8px 22px rgba(150,120,70,.15);border-color:#d8c8a8}
  a.card h2{font-size:19px;margin:0 0 6px}.card .meta{color:var(--muted);font-size:13px}
  footer{margin-top:30px;color:#a89a86;font-size:12px}
</style></head><body>
<div class="wrap">
  <h1>📝 托福模考系统（新版 iBT）</h1>
  <div class="sub">2026 新版 · 阅读→听力→写作→口语 · 9 大题型 · 1–6 band 估分</div>
  <div class="notice"><b>用 Chrome / Edge 打开</b>。整场连考或单题型专项都行；客观题自动判分估 band，写作/口语按官方 0–5 量规一键复制报告给 cc 打分。</div>
  <table><tr><th>科目</th><th>题型</th><th>官方题数/时间</th></tr>
    <tr><td>阅读</td><td>补全单词 · 生活阅读 · 学术短文</td><td>~50 / ~30min</td></tr>
    <tr><td>听力</td><td>选回应 · 对话 · 通知 · 讲座</td><td>~47 / ~29min</td></tr>
    <tr><td>写作</td><td>连词成句 · 写邮件 · 学术讨论</td><td>12 / ~23min</td></tr>
    <tr><td>口语</td><td>跟读 · 面试</td><td>11 / ~8min</td></tr>
  </table>
  <div class="cards">__CARDS__</div>
  <footer>data/*.json → build.py → mocks/*.html ｜ 共 __COUNT__ 套 ｜ 评分依据官方 Overview Table 2/3</footer>
</div></body></html>
"""

def build():
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    cards = []
    for f in files:
        with open(f, encoding="utf-8") as fp:
            d = json.load(fp)
        page = (PAGE
            .replace("__TITLE__", html.escape(d["title"]))
            .replace("__MOCK_JSON__", json.dumps(d, ensure_ascii=False))
            .replace("__SECTIONS__", json.dumps(SECTIONS, ensure_ascii=False))
            .replace("__TYPE_LABELS__", json.dumps(TYPE_LABELS, ensure_ascii=False))
            .replace("__TYPE_SECTION__", json.dumps(TYPE_SECTION, ensure_ascii=False))
            .replace("__BAND_READING__", json.dumps(BAND_READING))
            .replace("__BAND_LISTEN__", json.dumps(BAND_LISTEN))
            .replace("__CEFR__", json.dumps(CEFR, ensure_ascii=False))
            .replace("__OVERALL120__", json.dumps(OVERALL120, ensure_ascii=False))
            .replace("__RUBRICS__", json.dumps(RUBRICS, ensure_ascii=False)))
        with open(os.path.join(OUT, d["id"] + ".html"), "w", encoding="utf-8") as fp:
            fp.write(page)
        # 统计题量
        secs = d.get("sections", {})
        ntask = sum(len(secs.get(s["key"], {}).get("tasks", [])) for s in SECTIONS)
        cards.append(f'<a class="card" href="mocks/{d["id"]}.html"><h2>{html.escape(d["title"])}</h2>'
                     f'<div class="meta">四科 · {ntask} 个任务 · 整场约 85 分钟</div></a>')
        print("  ✓", d["id"], "—", ntask, "任务")
    idx = INDEX.replace("__CARDS__", "\n".join(cards) or '<div style="color:#8c8072">往 data/ 放 JSON 后运行 build.py</div>').replace("__COUNT__", str(len(files)))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as fp:
        fp.write(idx)
    print(f"完成：{len(files)} 套 → mocks/，已刷新 index.html")

if __name__ == "__main__":
    build()
