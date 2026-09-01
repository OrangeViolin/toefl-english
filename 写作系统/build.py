#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
托福写作专项系统 · 渲染器
  data/build-sentence.json + email.json + discussion.json  →  index.html（自包含，双击即开）
用法：  python3 build.py
理念：复用模考系统的题型 schema / 配色 / 官方 0–5 量规；补上「更多造句填空题 + 邮件/讨论模板脚手架 + 写作专注刷练」。
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")

def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)

BS = load("build-sentence.json")
EMAIL = load("email.json")
DISC = load("discussion.json")

# 官方 0–5 量规（与模考系统一致，供复制报告给 cc）
RUBRICS = {
 "email": "Write an Email（0–5）\n5 完全成功：有效清晰、语言驾驭稳定；论述有效支撑沟通目的；句式多样用词精准地道；社交惯例(礼貌/语域/请求措辞)得体；几乎无错。\n4 大体成功：基本有效易懂；论述较充分；句式多样得体；社交惯例大体到位；少量词法/语法错。\n3 部分成功：基本完成但语言局限使部分信息不清；论述部分支撑；句式词汇中等；结构/词形/习语/社交惯例有明显错。\n2 大体不成功：尝试但大体无效；论述有限或跑题；范围窄；错误累积。\n1 不成功：近乎不可懂；几无论述；电报式；严重频繁出错。\n0：空白/离题/非英文/照抄/乱敲。",
 "discussion": "Write for an Academic Discussion（0–5）\n5 完全成功：贴题清楚的讨论贡献、语言稳定；解释/举例/细节充分相关；句式多样用词地道；几乎无错。\n4 大体成功：相关易懂；解释举例较充分；句式多样得体；少量错。\n3 部分成功：大体相关可懂；例证有缺失/不清/不相关；词法句法习语有明显错。\n2 大体不成功：尝试贡献但语言局限使观点难懂；论述差或部分相关；范围有限；错误累积。\n1 不成功：贡献无效；几无连贯观点；极受限；严重频繁错。\n0：空白/离题/非英文/照抄/乱敲。",
}

PAGE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>托福写作专项系统</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--bad:#c0453a;--blue:#4a5cc7}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
  .wrap{max-width:860px;margin:0 auto;padding:0 20px 100px}
  header{position:sticky;top:0;z-index:20;background:var(--card);border-bottom:1px solid var(--line);display:flex;align-items:center;gap:14px;padding:10px 20px}
  header .sec{font-weight:700;font-size:15px}
  header .prog{font-size:13px;color:var(--muted)}
  header .spacer{flex:1}
  #timer{font-variant-numeric:tabular-nums;font-size:15px;background:#efe7d6;border-radius:8px;padding:4px 10px;color:#6f6552}
  #timer.warn{background:#f4dcd6;color:var(--bad)}
  .exit{font-size:13px;color:var(--muted);cursor:pointer}
  .menu{padding:40px 20px 60px;max-width:860px;margin:0 auto}
  .menu h1{font-size:26px;margin:0 0 4px}
  .menu .sub{color:var(--muted);margin-bottom:18px}
  .notice{background:#fff6e8;border:1px solid #f0d9b0;border-left:5px solid var(--accent);border-radius:12px;padding:13px 15px;font-size:13.5px;margin-bottom:22px}
  .notice b{color:var(--accent)}
  .bigbtn{display:block;width:100%;text-align:left;background:var(--accent);color:#fff;border:0;border-radius:16px;padding:18px 22px;font-size:18px;font-weight:700;cursor:pointer;font-family:inherit;margin-bottom:14px}
  .bigbtn small{display:block;font-weight:400;font-size:13px;opacity:.92;margin-top:3px}
  .bigbtn.b2{background:#3f7d74}.bigbtn.b3{background:var(--blue)}.bigbtn.b4{background:#8a6d3b}
  .block{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px;margin-top:22px;box-shadow:0 2px 12px rgba(150,120,70,.05)}
  .tasklabel{display:inline-block;font-size:12px;color:#fff;background:var(--core);padding:2px 10px;border-radius:20px;margin-bottom:12px}
  .lv{display:inline-block;font-size:11px;color:var(--muted);border:1px solid var(--line);border-radius:20px;padding:1px 8px;margin-left:6px}
  .instr{font-size:14px;color:var(--muted);margin-bottom:12px}
  /* 连词成句 */
  .bs-prompt{background:#eef1fb;border-radius:10px;padding:10px 13px;font-size:14.5px;margin-bottom:12px}
  .bs-slot{min-height:46px;border:2px dashed var(--accent);border-radius:10px;padding:8px;display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-bottom:12px;background:#fdf7f0}
  .bs-bank{display:flex;flex-wrap:wrap;gap:7px;margin-bottom:6px}
  .tok{background:#eae2d0;border:1px solid #d8c8a8;border-radius:8px;padding:6px 12px;font-size:14px;cursor:pointer;font-family:inherit}
  .tok:hover{background:#e0d5bd}
  .verdict{margin-top:12px;font-size:14.5px;padding:12px 14px;border-radius:10px;display:none}
  .verdict.show{display:block}
  .verdict.ok{background:#eaf6ee;border:1px solid #bfe3cb}
  .verdict.no{background:#fbecea;border:1px solid #f0c9c2}
  .verdict .ans{font-weight:700;margin-top:4px}
  .verdict .note{font-size:13px;color:#6f6656;margin-top:6px}
  /* 写作 */
  .tmpl{border:1px solid #cfe0dc;background:#eef6f4;border-radius:12px;margin-bottom:14px;overflow:hidden}
  .tmpl summary{cursor:pointer;padding:11px 15px;font-weight:600;color:#2c6a60;font-size:14px;list-style:none}
  .tmpl summary::-webkit-details-marker{display:none}
  .tmpl summary::before{content:"📋 ";}
  .ref{border:1px solid #e5cdbb;background:#fffaf4;border-radius:12px;margin-top:14px;overflow:hidden}
  .ref>summary{cursor:pointer;padding:11px 15px;font-weight:600;color:var(--accent);font-size:14px;list-style:none}
  .ref>summary::-webkit-details-marker{display:none}
  .ref>summary::before{content:"📖 ";}
  .rin{padding:0 16px 14px}
  .rlabel{font-weight:700;color:var(--core);font-size:13px;margin:10px 0 4px}
  .model{background:#faf7ef;border:1px solid #efe6d4;border-radius:10px;padding:12px 14px;margin:8px 0;white-space:pre-wrap;line-height:1.75;font-size:14px}
  .mlabel{font-weight:700;color:#8a5a2e;font-size:12.5px;margin-bottom:6px}
  .sbb{font-weight:600;font-size:13px;color:#5f574c;margin:9px 0 2px}
  .sopt{font-size:13.5px;color:#433d34;padding:2px 0}
  .cn-tbl{width:100%;border-collapse:collapse;font-size:13px;margin:6px 0}
  .cn-tbl th,.cn-tbl td{border:1px solid #e0d7c7;padding:5px 8px;text-align:left;vertical-align:top}
  .cn-tbl th{background:#eef1fb;font-weight:600}
  .cn-n{white-space:nowrap;color:var(--muted)}
  .cn-p{color:var(--blue);font-style:italic}
  .cn-sample{margin-top:10px;background:#faf7ef;border:1px solid #efe6d4;border-radius:8px;padding:10px 12px}
  .cn-slabel{font-weight:700;color:var(--core);font-size:13px;margin-bottom:6px}
  .cn-sl{font-size:13.5px;margin:5px 0;line-height:1.55}
  .cn-sn{display:inline-block;font-size:11px;color:#fff;background:#b9ad95;border-radius:8px;padding:1px 7px;margin-right:5px}
  .tmpl .tin{padding:0 16px 14px;font-size:13.5px}
  .tmpl .frame div{padding:3px 0;border-bottom:1px dashed #d3e5e0}
  .tmpl .phr{margin-top:10px}
  .tmpl .phr span{display:inline-block;background:#fff;border:1px solid #d3e5e0;border-radius:8px;padding:3px 9px;margin:3px 4px 0 0;font-size:12.5px;color:#3a6b63}
  .tmpl .tips{margin-top:10px;color:#8a5a2e;background:#fff6e8;border-radius:8px;padding:8px 11px;font-size:12.5px}
  .passage{background:#faf7ef;border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:15px;white-space:pre-wrap;margin-bottom:12px}
  .post{background:#f2f0fb;border-radius:10px;padding:11px 14px;font-size:14px;margin-bottom:10px}
  .post b{color:var(--blue)}
  .meta{font-size:13px;color:var(--muted);margin-bottom:6px}
  textarea{width:100%;min-height:220px;border:1px solid var(--line);border-radius:10px;padding:12px;font-size:15px;font-family:inherit;line-height:1.6;resize:vertical}
  textarea:focus{outline:none;border-color:var(--accent)}
  .wc{font-size:13px;color:var(--muted);margin-top:6px}
  .wc.low{color:var(--bad)}
  .chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px}
  .chips button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:6px 13px;font-size:13px;cursor:pointer;color:#5f574c;font-family:inherit}
  .chips button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
  .row{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin:10px 0}
  .btn{border:0;border-radius:10px;padding:10px 18px;font-size:14.5px;cursor:pointer;font-family:inherit}
  .btn.p{background:var(--accent);color:#fff}.btn.g{background:#efe8d8;color:#5f574c}
  .btn.t{background:var(--core);color:#fff}
  .btn:disabled{opacity:.45;cursor:default}
  .nav{position:fixed;bottom:0;left:0;right:0;background:var(--card);border-top:1px solid var(--line);display:flex;justify-content:center;gap:12px;padding:12px}
</style>
</head>
<body>
<div id="app"></div>
<script>
const BS = __BS__, EMAIL = __EMAIL__, DISC = __DISC__, RUBRICS = __RUBRICS__;
const $ = s => document.querySelector(s);
const app = $('#app');
const esc = s => (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const norm = s => (s||'').toLowerCase().replace(/[.,!?;:'"’]/g,'').replace(/\s+/g,' ').trim();
const wcount = s => (s.trim().match(/\S+/g)||[]).length;
const store = { get:(k,d)=>{try{return JSON.parse(localStorage.getItem('toefl-writing:'+k))??d}catch(e){return d}}, set:(k,v)=>localStorage.setItem('toefl-writing:'+k,JSON.stringify(v)) };
let timerIv=null;
function stopTimer(){ if(timerIv){clearInterval(timerIv); timerIv=null;} }

/* ───────── 菜单 ───────── */
function menu(){
  stopTimer();
  app.innerHTML = `<div class="menu">
    <h1>✍️ 托福写作专项系统</h1>
    <div class="sub">新版 iBT 写作三题型 · 造句填空自动判分 · 邮件/讨论带模板 + 一键复制报告给 cc 打分</div>
    <div class="notice"><b>写作占总分 1/4。</b> 造句填空(10题×1分)+邮件(5分)+学术讨论(5分)=20 原始分。造句填空是稳拿分区，两篇作文靠<b>模板+切题+一个具体例子</b>就能到 band 4。</div>
    <button class="bigbtn" onclick="bsStart()">🧩 连词成句 Build a Sentence<small>${BS.items.length} 题 · 重排词块成句 · 自动对错 + 语法点</small></button>
    <button class="bigbtn b2" onclick="writeStart('email')">✉️ 写邮件 Write an Email<small>${EMAIL.items.length} 个情景 · 7 分钟 · 带万能框架 + 高频句</small></button>
    <button class="bigbtn b3" onclick="writeStart('disc')">💬 学术讨论 Write for an Academic Discussion<small>${DISC.items.length} 个话题 · 10 分钟 · ≥100 词 · 带立场论证框架</small></button>
    <a class="bigbtn b4" href="./打字练习.html" style="text-decoration:none">⌨️ 打字练习<small>极简打字框 · 拼错纠错 · WPM 测速（对标 10 分钟 100 词）</small></a>
  </div>`;
}

/* ───────── 连词成句 ───────── */
let bsi=0;
function bsStart(){ bsi = store.get('bs-pos',0); if(bsi>=BS.items.length) bsi=0; bsRender(); }
function bsRender(){
  stopTimer();
  const it = BS.items[bsi];
  const done = store.get('bs-done',{});
  const nDone = Object.values(done).filter(Boolean).length;
  app.innerHTML = `<header><span class="sec">连词成句</span><span class="prog">第 ${bsi+1}/${BS.items.length} 题 · 已做对 ${nDone}</span><span class="spacer"></span><span class="exit" onclick="menu()">✕ 退出</span></header>
  <div class="wrap"><div class="block">
    <div class="tasklabel">Build a Sentence</div><span class="lv">${it.level}</span>
    <div class="instr">${esc(BS.intro)}</div>
    <div class="bs-prompt">🗣 ${esc(it.prompt)}</div>
    <div class="bs-slot" id="slot"></div>
    <div class="bs-bank" id="bank"></div>
    <div><span class="exit" id="reset">↺ 清空重排</span></div>
    <div class="verdict" id="vd"></div>
  </div></div>
  <div class="nav">
    <button class="btn g" id="prev">◀ 上一题</button>
    <button class="btn t" id="check">✓ 对答案</button>
    <button class="btn p" id="next">${bsi===BS.items.length-1?'回菜单':'下一题 ▶'}</button>
  </div>`;
  let order = store.get('bs-order:'+bsi, []);
  const slot=$('#slot'), bank=$('#bank');
  function draw(){
    slot.innerHTML = order.map(i=>`<button class="tok" data-o="${i}">${esc(it.tokens[i])}</button>`).join('') || '<span style="color:#b3a78f;font-size:13px">点下面的词块，按顺序排到这里</span>';
    bank.innerHTML = it.tokens.map((tk,i)=> order.includes(i)?'':`<button class="tok" data-b="${i}">${esc(tk)}</button>`).join('');
    slot.querySelectorAll('[data-o]').forEach(x=>x.onclick=()=>{order=order.filter(i=>i!=+x.dataset.o);persist();draw();});
    bank.querySelectorAll('[data-b]').forEach(x=>x.onclick=()=>{order.push(+x.dataset.b);persist();draw();});
  }
  function persist(){ store.set('bs-order:'+bsi, order); }
  $('#reset').onclick=()=>{order=[];persist();draw();$('#vd').classList.remove('show');};
  $('#check').onclick=()=>{
    const got = norm(order.map(i=>it.tokens[i]).join(' '));
    const cands = [it.answer, ...(it.accept||[])].map(norm);
    const ok = cands.includes(got);
    const done = store.get('bs-done',{}); done[bsi]=ok; store.set('bs-done',done);
    const vd=$('#vd'); vd.className='verdict show '+(ok?'ok':'no');
    vd.innerHTML = (ok?'✅ 正确！':'❌ 语序/语法不对')+`<div class="ans">✔︎ ${esc(it.answer)}</div>`+(it.note?`<div class="note">📎 ${esc(it.note)}</div>`:'');
  };
  $('#prev').onclick=()=>{ if(bsi>0){bsi--;store.set('bs-pos',bsi);bsRender();} };
  $('#prev').disabled=bsi===0;
  $('#next').onclick=()=>{ if(bsi===BS.items.length-1){menu();} else {bsi++;store.set('bs-pos',bsi);bsRender();} };
  draw();
}

/* ───────── 写作（邮件 / 讨论）───────── */
function writeStart(kind){ writeRender(kind, store.get(kind+'-pick',0)); }
function tmplHtml(t){
  return `<details class="tmpl" open><summary>${esc(t.name)}</summary><div class="tin">
    <div class="frame">${t.frame.map(f=>`<div>${esc(f)}</div>`).join('')}</div>
    <div class="phr">${t.phrases.map(p=>`<span>${esc(p)}</span>`).join('')}</div>
    ${t.tips?`<div class="tips">💡 ${esc(t.tips)}</div>`:''}
  </div></details>`;
}
function concessionHtml(D){
  const c = D.concession; if(!c) return '';
  const rows = c.rows.map(r=>`<tr><td class="cn-n">${esc(r.n)}</td><td>${esc(r.outline)}</td><td class="cn-p">${esc(r.pattern)}</td></tr>`).join('');
  const sample = c.sample ? `<div class="cn-sample"><div class="cn-slabel">${esc(c.sample.topic)}</div>`+
      c.sample.lines.map(l=>`<div class="cn-sl"><span class="cn-sn">${esc(l.n)}</span>${esc(l.en)}</div>`).join('')+`</div>` : '';
  return `<details class="tmpl" open><summary>${esc(c.name)}</summary><div class="tin">
    ${c.note?`<div class="tips" style="margin-bottom:8px">💡 ${esc(c.note)}</div>`:''}
    <table class="cn-tbl"><thead><tr><th>句</th><th>提纲</th><th>句式开头</th></tr></thead><tbody>${rows}</tbody></table>
    ${sample}
  </div></details>`;
}
function refHtml(it){
  if(!it.models && !it.bySentence) return '';
  const models=(it.models||[]).map(m=>`<div class="model"><div class="mlabel">${esc(m.label)}</div>${esc(m.text)}</div>`).join('');
  const sb=(it.bySentence||[]).map(b=>`<div class="sbb">${esc(b.bullet)}</div>`+b.options.map(o=>`<div class="sopt">· ${esc(o)}</div>`).join('')).join('');
  return `<details class="ref"><summary>参考范文 &amp; 例句（先自己写，再对照）</summary><div class="rin">`+
    (models?`<div class="rlabel">范文</div>${models}`:'')+
    (sb?`<div class="rlabel">分点参考例句（每点挑一句套用）</div>${sb}`:'')+
    `</div></details>`;
}
function writeRender(kind, idx){
  stopTimer();
  const D = kind==='email'?EMAIL:DISC;
  const it = D.items[idx];
  store.set(kind+'-pick', idx);
  const secs = it.time_sec||(kind==='email'?420:600);
  const key = kind+'-draft:'+idx;
  const chips = D.items.map((_,i)=>`<button class="${i===idx?'on':''}" data-i="${i}">${kind==='email'?'情景':'话题'} ${i+1}</button>`).join('');
  const scene = kind==='email'
    ? `<div class="meta">To: ${esc(it.to)} ｜ Subject: ${esc(it.subject)} ｜ 限时 ${Math.round(secs/60)} 分钟</div>
       <div class="passage">${esc(it.scenario)}\n\n在邮件中：${it.bullets.map(b=>'\n • '+esc(b)).join('')}</div>`
    : `<div class="meta">限时 ${Math.round(secs/60)} 分钟 · 有效作答 ≥${it.min_words||100} 词</div>
       <div class="post"><b>教授：</b> ${esc(it.professor)}</div>
       <div class="post"><b>学生 A：</b> ${esc(it.student1)}</div>
       <div class="post"><b>学生 B：</b> ${esc(it.student2)}</div>`;
  app.innerHTML = `<header><span class="sec">${kind==='email'?'写邮件':'学术讨论'}</span><span class="spacer"></span>
      <span id="timer">${String(Math.floor(secs/60)).padStart(2,'0')}:00</span>
      <span class="exit" onclick="menu()" style="margin-left:12px">✕ 退出</span></header>
  <div class="wrap"><div class="block">
    <div class="tasklabel">${kind==='email'?'Write an Email':'Write for an Academic Discussion'}</div>
    <div class="instr">${esc(D.intro)}</div>
    <div class="chips" id="chips">${chips}</div>
    ${tmplHtml(D.template)}
    ${scene}
    <textarea id="ta" placeholder="在此作答…">${esc(store.get(key,''))}</textarea>
    <div class="wc" id="wc"></div>
    <div class="row">
      <button class="btn g" id="tstart">▶ 开始限时</button>
      <button class="btn t" id="copy">复制报告给 cc 打分</button>
    </div>
    ${refHtml(it)}
  </div></div>
  <div class="nav"><button class="btn g" onclick="menu()">← 回菜单</button></div>`;
  $('#chips').querySelectorAll('button').forEach(b=>b.onclick=()=>writeRender(kind,+b.dataset.i));
  const ta=$('#ta'), wc=$('#wc');
  const minW = kind==='disc'?(it.min_words||100):0;
  function cnt(){ const n=wcount(ta.value); wc.textContent=n+' 词'+(minW?` / 建议 ≥${minW}`:''); wc.classList.toggle('low', minW&&n<minW); }
  ta.oninput=()=>{ store.set(key, ta.value); cnt(); }; cnt();
  // 计时
  let left=secs; const tEl=$('#timer');
  function tdraw(){ const m=Math.floor(Math.max(0,left)/60),s=Math.max(0,left)%60; tEl.textContent=String(m).padStart(2,'0')+':'+String(s).padStart(2,'0'); tEl.classList.toggle('warn',left<=60); }
  $('#tstart').onclick=()=>{ stopTimer(); left=secs; tdraw(); $('#tstart').disabled=true; $('#tstart').textContent='计时中…';
    timerIv=setInterval(()=>{ left--; tdraw(); if(left<=0){ stopTimer(); tEl.textContent='时间到'; ta.blur(); } },1000); };
  // 复制报告
  $('#copy').onclick=()=>{
    let txt;
    if(kind==='email'){
      txt=`【托福写作·Write an Email 评分请求】请依据官方 0–5 量规给我打分并给改进建议。\n\n[情景]\n${it.scenario}\n[要求]\n${it.bullets.map(b=>'• '+b).join('\n')}\n\n[我的作答 · ${wcount(ta.value)}词]\n${ta.value||'(空)'}\n\n[评分量规]\n${RUBRICS.email}`;
    } else {
      txt=`【托福写作·Write for an Academic Discussion 评分请求】请依据官方 0–5 量规给我打分并给改进建议。\n\n[教授]\n${it.professor}\n[学生A]\n${it.student1}\n[学生B]\n${it.student2}\n\n[我的作答 · ${wcount(ta.value)}词]\n${ta.value||'(空)'}\n\n[评分量规]\n${RUBRICS.discussion}`;
    }
    navigator.clipboard.writeText(txt).then(()=>{$('#copy').textContent='✓ 已复制，贴回给 cc';setTimeout(()=>$('#copy').textContent='复制报告给 cc 打分',1600);})
      .catch(()=>prompt('复制以下内容贴给 cc：',txt));
  };
}

menu();
</script>
</body>
</html>
"""

def build():
    page = (PAGE
        .replace("__BS__", json.dumps(BS, ensure_ascii=False))
        .replace("__EMAIL__", json.dumps(EMAIL, ensure_ascii=False))
        .replace("__DISC__", json.dumps(DISC, ensure_ascii=False))
        .replace("__RUBRICS__", json.dumps(RUBRICS, ensure_ascii=False)))
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("完成：写作系统 → index.html")
    print(f"  连词成句 {len(BS['items'])} 题 · 邮件 {len(EMAIL['items'])} 情景 · 学术讨论 {len(DISC['items'])} 话题")

if __name__ == "__main__":
    build()
