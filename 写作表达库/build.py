#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
写作表达库 · 渲染器
  data/表达库.json → index.html（自包含，双击即用）
写作专用句型/连接/套话，按功能场景分组。掌握标记绑稳定 id（非位置），带导出/导入备份，进度永不被重建抹掉。
用法：python3 build.py
累积话术：她说「写作表达库加：<表达>」→ 归到对应场景 items[] → 重跑。
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "data")
D = json.load(open(os.path.join(DATA, "表达库.json"), encoding="utf-8"))

PAGE = r"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--blue:#4a5cc7}
  *{box-sizing:border-box}html,body{margin:0}
  body{background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.7;-webkit-font-smoothing:antialiased}
  .wrap{max-width:840px;margin:0 auto;padding:22px 20px 100px}
  h1{font-size:23px;margin:0 0 2px}
  .sub{color:var(--muted);font-size:13px;margin-bottom:12px}
  .bar{position:sticky;top:0;z-index:20;background:var(--bg);padding:10px 0;display:flex;flex-wrap:wrap;gap:7px;align-items:center;border-bottom:1px solid var(--line);margin-bottom:8px}
  .bar button{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:5px 12px;font-size:12.5px;cursor:pointer;color:#5f574c;font-family:inherit}
  .bar button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
  .bar .spacer{flex:1}.count{font-size:12.5px;color:var(--muted)}
  .seg{display:flex;gap:5px;flex-wrap:wrap}
  .scene{margin-top:20px}
  .scene h2{font-size:16px;margin:0 0 8px;color:var(--core)}
  .card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:10px;box-shadow:0 2px 10px rgba(150,120,70,.04)}
  .card.done{opacity:.55}
  .ehead{display:flex;align-items:center;gap:9px;flex-wrap:wrap}
  .en{font-size:17px;font-weight:700;font-family:Georgia,serif}
  .spk{background:var(--blue);color:#fff;border:0;border-radius:8px;padding:3px 10px;font-size:12px;cursor:pointer;font-family:inherit}
  .zh{font-size:14.5px;font-weight:600;margin:5px 0 2px}
  body.recite .zh{filter:blur(6px);cursor:pointer}
  .usage{font-size:12.5px;color:var(--muted);background:#faf7ef;border-radius:7px;padding:5px 9px;margin-top:5px}
  .ex{font-size:13px;margin-top:6px;color:#433d34}
  .ex .exen{font-style:italic}
  .mbtn{border:1px solid var(--line);background:#fff;border-radius:8px;padding:3px 10px;font-size:12px;cursor:pointer;font-family:inherit;color:#5f574c;margin-top:7px}
  .mbtn.on{background:var(--ok);color:#fff;border-color:var(--ok)}
</style></head>
<body>
<div class="wrap">
  <h1>✍️ __TITLE__</h1>
  <div class="sub">__INTRO__</div>
  <div class="bar">
    <div class="seg" id="seg"></div>
    <button id="recite">🙈 背记</button>
    <button id="exp">⬇ 导出备份</button>
    <button id="imp">⬆ 导入</button>
    <input type="file" id="impf" accept="application/json" style="display:none">
    <span class="spacer"></span><span class="count" id="count"></span>
  </div>
  <div id="body"></div>
</div>
<script>
const DATA = __DATA__;
const KEY = 'writeexpr:state';
const $ = s => document.querySelector(s);
const esc = s => (s==null?'':String(s)).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
let mastered = new Set(JSON.parse(localStorage.getItem(KEY)||'[]'));  // 按稳定 id 存
const saveM = ()=> localStorage.setItem(KEY, JSON.stringify([...mastered]));
let recite=false, filter='all';

let voices=[]; const lv=()=>{voices=window.speechSynthesis?speechSynthesis.getVoices():[]};
if(window.speechSynthesis){ lv(); speechSynthesis.onvoiceschanged=lv; }
function say(t){ if(!window.speechSynthesis)return; speechSynthesis.cancel();
  const u=new SpeechSynthesisUtterance(t); u.lang='en-US'; u.rate=0.92;
  const v=voices.find(v=>/en-US/i.test(v.lang)&&/Samantha|Aria|Jenny|Google US|female/i.test(v.name))||voices.find(v=>/en-US/i.test(v.lang)); if(v)u.voice=v;
  speechSynthesis.speak(u); }

const allItems = ()=> DATA.scenes.flatMap(s=>s.items);
function render(){
  const all=allItems();
  $('#count').textContent = `已掌握 ${all.filter(i=>mastered.has(i.id)).length}/${all.length}`;
  const scenes = DATA.scenes.filter(s=> filter==='all' || s.key===filter);
  $('#body').innerHTML = scenes.map(s=>`
    <section class="scene"><h2>${esc(s.name)} <span style="font-size:12px;color:var(--muted)">${s.items.length}</span></h2>
      ${s.items.map(card).join('')}
    </section>`).join('');
  document.querySelectorAll('[data-say]').forEach(b=>b.onclick=()=>say(b.dataset.say));
  document.querySelectorAll('.zh').forEach(el=>el.onclick=()=>{ if(recite) el.style.filter='none'; });
  document.querySelectorAll('[data-m]').forEach(b=>b.onclick=()=>{ const id=b.dataset.m;
    mastered.has(id)?mastered.delete(id):mastered.add(id); saveM();
    const c=b.closest('.card'); const on=mastered.has(id);
    c.classList.toggle('done',on); b.classList.toggle('on',on); b.textContent=on?'✓ 已掌握':'标记已掌握';
    $('#count').textContent=`已掌握 ${allItems().filter(i=>mastered.has(i.id)).length}/${allItems().length}`; });
}
function card(it){
  const done=mastered.has(it.id);
  return `<div class="card ${done?'done':''}">
    <div class="ehead"><span class="en">${esc(it.en)}</span><button class="spk" data-say="${esc(it.en)}">🔊</button></div>
    <div class="zh">${esc(it.zh)}</div>
    ${it.usage?`<div class="usage">🧭 ${esc(it.usage)}</div>`:''}
    ${it.ex?`<div class="ex"><span class="exen">${esc(it.ex.en)}</span><br>${esc(it.ex.zh)} <button class="spk" data-say="${esc(it.ex.en)}">🔊</button></div>`:''}
    <button class="mbtn ${done?'on':''}" data-m="${esc(it.id)}">${done?'✓ 已掌握':'标记已掌握'}</button>
  </div>`;
}
// 场景筛选
$('#seg').innerHTML = `<button data-f="all" class="on">全部</button>`+DATA.scenes.map(s=>`<button data-f="${s.key}">${esc(s.name.replace(/^[①-⑩]\s*/,''))}</button>`).join('');
$('#seg').querySelectorAll('button').forEach(b=>b.onclick=()=>{ filter=b.dataset.f; $('#seg').querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b)); render(); });
$('#recite').onclick=()=>{ recite=!recite; document.body.classList.toggle('recite',recite); $('#recite').classList.toggle('on',recite); if(recite) document.querySelectorAll('.zh').forEach(el=>el.style.filter=''); };
// 导出/导入备份（防标记丢失）
$('#exp').onclick=()=>{ const blob=new Blob([JSON.stringify([...mastered])],{type:'application/json'});
  const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='写作表达库-掌握备份.json'; a.click(); };
$('#imp').onclick=()=>$('#impf').click();
$('#impf').onchange=e=>{ const f=e.target.files[0]; if(!f)return; const r=new FileReader();
  r.onload=()=>{ try{ const arr=JSON.parse(r.result); if(Array.isArray(arr)){ arr.forEach(id=>mastered.add(id)); saveM(); render(); alert('已导入 '+arr.length+' 条掌握标记'); } }catch(_){ alert('文件格式不对'); } };
  r.readAsText(f); };
render();
</script>
</body></html>
"""

def build():
    n = sum(len(s["items"]) for s in D["scenes"])
    html = (PAGE.replace("__TITLE__", D["title"])
                .replace("__INTRO__", D.get("intro", ""))
                .replace("__DATA__", json.dumps(D, ensure_ascii=False)))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(html)
    print(f"完成：{len(D['scenes'])} 场景 · {n} 条表达 → index.html")

if __name__ == "__main__":
    build()
