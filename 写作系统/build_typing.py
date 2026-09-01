#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""英语打字练习页生成器：极简界面 + 离线拼写纠错(系统词典) + WPM 测速。"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------- 拼写词典 ----------
words = set()
DICT_PATH = "/usr/share/dict/web2"
if os.path.exists(DICT_PATH):
    with open(DICT_PATH, encoding="utf-8", errors="ignore") as f:
        for line in f:
            w = line.strip().lower()
            if w and w.isalpha() and 2 <= len(w) <= 28:
                words.add(w)

def add_json_words(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
        for x in d.get("words", []):
            w = (x.get("word") or x.get("w") or "").strip().lower()
            if w.isalpha() and 2 <= len(w) <= 28:
                words.add(w)
    except Exception:
        pass

BDIR = os.path.join(ROOT, "..", "背词计划", "data")
for fn in ("green-book.json", "beat-vocab.json", "项目生词.json", "lecture-lex.json", "subject-vocab.json"):
    add_json_words(os.path.join(BDIR, fn))

# 现代高频词（web2 是旧词典，补常用现代词，减少误报）
_modern = ("internet email website online smartphone laptop wifi google youtube facebook twitter app blog "
           "download upload software hardware keyboard mouse screen password account login logout selfie "
           "spellcheck autocorrect podcast netflix instagram tiktok zoom emoji gif meme vlog hashtag").split()
words.update(_modern)

WORDLIST = "\n".join(sorted(words))
WORDLIST_JS = "`" + WORDLIST.replace("\\", "").replace("`", "") + "`"   # 反引号包裹成 JS 字符串字面量

# ---------- 页面模板 ----------
HTML = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>英语打字练习</title>
<style>
  :root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--ok:#2f8f5b;--bad:#c0453a}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
  .wrap{max-width:780px;margin:0 auto;padding:32px 20px 80px}
  header{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:16px}
  h1{font-size:24px;margin:0}
  .stat{font-size:14px;color:var(--muted)}
  .stat b{color:var(--ink);font-size:16px;font-variant-numeric:tabular-nums}
  textarea{width:100%;min-height:280px;resize:vertical;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;font-size:17px;line-height:1.7;font-family:"SF Mono",Menlo,Consolas,"PingFang SC",monospace;color:var(--ink);outline:none}
  textarea:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(193,102,47,.08)}
  .btns{display:flex;gap:10px;margin:14px 0 6px}
  button{border:0;border-radius:10px;padding:10px 18px;font-size:14px;cursor:pointer;font-family:inherit}
  .btn-end{background:var(--accent);color:#fff;font-weight:600}
  .btn-reset{background:var(--card);color:var(--ink);border:1px solid var(--line)}
  .result{display:none;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;margin-top:10px}
  .result.show{display:block}
  .result .big{font-size:22px;font-weight:700;font-variant-numeric:tabular-nums}
  .result .row{display:flex;gap:26px;flex-wrap:wrap;margin:6px 0 10px}
  .result .row>div{font-size:14px;color:var(--muted)}
  .result .row b{color:var(--ink);font-size:20px;font-variant-numeric:tabular-nums}
  .verdict{font-size:14px;font-weight:600;padding:10px 14px;border-radius:10px}
  .verdict.pass{background:#e8f5ec;color:var(--ok)}
  .verdict.fail{background:#fdeeee;color:var(--bad)}
  .hint{font-size:12.5px;color:var(--muted);margin-top:4px}
  .spell{margin-top:16px}
  .spell h3{margin:0 0 8px;font-size:14px;color:var(--muted);font-weight:600}
  .bad-row{display:inline-flex;align-items:center;gap:8px;background:var(--card);border:1px solid var(--line);border-radius:9px;padding:5px 10px;margin:0 6px 6px 0;font-size:14px}
  .bad-word{color:var(--bad);font-weight:600;text-decoration:line-through;text-decoration-color:rgba(192,69,58,.5)}
  .bad-arrow{color:var(--muted)}
  .bad-sug{color:var(--ok);font-weight:700;cursor:pointer;border-bottom:1px dashed var(--ok)}
  .bad-sug:hover{background:#e8f5ec}
  .bad-ign{color:var(--muted);font-size:12px;cursor:pointer;margin-left:2px}
  .bad-ign:hover{color:var(--ink)}
  .empty{color:var(--muted);font-size:13px}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>⌨️ 英语打字练习</h1>
    <div class="stat">⏱ <b id="clock">00:00</b> &nbsp;·&nbsp; 📝 <b id="wc">0</b> 词</div>
  </header>

  <textarea id="box" placeholder="在这里直接打字（英文），开始输入即自动计时。打完点「结束」看速度。" spellcheck="false" autocomplete="off" autocapitalize="off" autocorrect="off"></textarea>

  <div class="btns">
    <button class="btn-end" id="end">结束 · 出结果</button>
    <button class="btn-reset" id="reset">重来</button>
  </div>
  <div class="hint">拼错会实时标出并给出正确拼写（点绿色建议词可直接替换；点「忽略」不再提示该词）。</div>

  <div class="result" id="result">
    <div class="row">
      <div>总词数<b id="r_words">0</b></div>
      <div>用时<b id="r_time">0:00</b></div>
      <div>速度<b id="r_wpm">0</b> WPM</div>
    </div>
    <div class="verdict" id="verdict"></div>
    <div class="hint" id="r_note"></div>
  </div>

  <div class="spell" id="spell">
    <h3>🔍 拼写提示</h3>
    <div id="spell-list"><span class="empty">暂无拼错</span></div>
  </div>
</div>

<script>
const WORDLIST = __WORDLIST__;
const BYFIRST = {};
(()=>{ for(const w of WORDLIST.split('\n')){ if(!w) continue; const k=w[0], L=w.length;
  (BYFIRST[k] || (BYFIRST[k]={})); (BYFIRST[k][L] || (BYFIRST[k][L]=new Set())).add(w); } })();

const box = document.getElementById('box');
const clockEl = document.getElementById('clock'), wcEl = document.getElementById('wc');
const spellList = document.getElementById('spell-list');
const ignored = new Set();   // 本次会话里用户点「忽略」的词

let startTime = null, timerId = null, ended = false;

function spelled(w){ const b=BYFIRST[w[0]]; return !!(b && b[w.length] && b[w.length].has(w)); }
function lev(a,b){ if(a===b) return 0; const m=a.length,n=b.length; if(Math.abs(m-n)>2) return 99;
  // Damerau–Levenshtein：相邻字母换位算 1 步（recieve→receive 这类最常见打字错）
  const d=[]; for(let i=0;i<=m;i++){ d[i]=[i]; } for(let j=0;j<=n;j++) d[0][j]=j;
  for(let i=1;i<=m;i++){ for(let j=1;j<=n;j++){
    const c=a[i-1]===b[j-1]?0:1;
    d[i][j]=Math.min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+c);
    if(i>1 && j>1 && a[i-1]===b[j-2] && a[i-2]===b[j-1]) d[i][j]=Math.min(d[i][j], d[i-2][j-2]+1);
  } }
  return d[m][n]; }
function transposeHit(w){ for(let i=0;i<w.length-1;i++){ const t=w.slice(0,i)+w[i+1]+w[i]+w.slice(i+2); if(t!==w && spelled(t)) return t; } return null; }  // recieve→receive
function suggest(w){ const b=BYFIRST[w[0]]; if(!b) return []; const th=transposeHit(w);
  if(th){ const rest=cand0(w).filter(x=>x!==th); return [th].concat(rest).slice(0,3); }
  return cand0(w); }
function cand0(w){ const b=BYFIRST[w[0]]; if(!b) return []; const cand=[];
  for(let L=Math.max(1,w.length-2); L<=w.length+2; L++){ const s=b[L]; if(!s) continue;
    for(const c of s){ const d=lev(w,c); if(d>0 && d<=2) cand.push([c,d]); } }
  cand.sort((x,y)=> x[1]-y[1] || (pref(w,y[0])-pref(w,x[0])) || (x[0]<y[0]?-1:1));
  return cand.slice(0,3).map(x=>x[0]); }
function pref(a,c){ let n=0; while(n<a.length && n<c.length && a[n]===c[n]) n++; return n; }

function wordCount(){ const t=box.value; const m=t.match(/[A-Za-z]+(?:[''-][A-Za-z]+)*/g)||[]; return m.length; }

function fmtClock(sec){ const m=Math.floor(sec/60), s=Math.floor(sec%60); return m+':'+String(s).padStart(2,'0'); }

function startTimer(){ if(startTime) return; startTime=Date.now(); timerId=setInterval(()=>{
  clockEl.textContent=fmtClock((Date.now()-startTime)/1000); }, 500); }

function checkSpell(){
  const text = box.value;
  const tokens = text.match(/[A-Za-z]+(?:[''-][A-Za-z]+)*/g) || [];
  const seen = new Map();
  for(const tok of tokens){
    const lower = tok.toLowerCase().replace(/^'+|'+$/g,'');
    if(lower.length<2 || spelled(lower) || ignored.has(lower)) continue;
    if(!seen.has(lower)) seen.set(lower,{orig:tok, sugs:suggest(lower)});
  }
  if(seen.size===0){ spellList.innerHTML='<span class="empty">暂无拼错 ✓</span>'; return; }
  spellList.innerHTML='';
  for(const [lower,o] of seen){
    const row=document.createElement('div'); row.className='bad-row';
    const bw=document.createElement('span'); bw.className='bad-word'; bw.textContent=o.orig; row.appendChild(bw);
    const ar=document.createElement('span'); ar.className='bad-arrow'; ar.textContent='→'; row.appendChild(ar);
    const sugs=o.sugs.length? o.sugs : ['（无相近建议）'];
    sugs.forEach(s=>{ const a=document.createElement('span'); a.className='bad-sug'; a.textContent=s; a.title='点击替换'; a.onclick=()=>replaceWord(o.orig,s); row.appendChild(a); });
    const ig=document.createElement('span'); ig.className='bad-ign'; ig.textContent='忽略'; ig.title='不再提示这个词';
    ig.onclick=()=>{ ignored.add(lower); checkSpell(); }; row.appendChild(ig);
    spellList.appendChild(row);
  }
}
function replaceWord(orig,good){
  const keepCase = s=> orig && orig[0]===orig[0].toUpperCase() ? s[0].toUpperCase()+s.slice(1) : s;
  box.value = box.value.replace(new RegExp('\\b'+orig.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\b'), keepCase(good));
  checkSpell();
}
let deb=null;
box.addEventListener('input', ()=>{ startTimer(); wcEl.textContent=wordCount(); clearTimeout(deb); deb=setTimeout(checkSpell,400); });

function endTest(){
  if(ended) return; ended=true;
  if(timerId) clearInterval(timerId);
  const sec = startTime ? (Date.now()-startTime)/1000 : 0;
  const wc = wordCount();
  const mins = sec/60;
  const wpm = mins>0 ? Math.round(wc/mins) : 0;
  document.getElementById('r_words').textContent = wc;
  document.getElementById('r_time').textContent = fmtClock(sec);
  document.getElementById('r_wpm').textContent = wpm;
  const v=document.getElementById('verdict');
  const targetWpm=20;   // 10分钟200词 = 20 WPM（预留思考时间，手速要更快）
  if(wpm>=targetWpm){ v.className='verdict pass'; v.textContent='✓ 达标：已达到你的目标打字速度（10 分钟 ≥ 200 词，即 ≥ '+targetWpm+' WPM）。'; }
  else { v.className='verdict fail'; v.textContent='✗ 未达标：你的目标是 10 分钟 ≥ 200 词（≥ '+targetWpm+' WPM），当前 '+wpm+' WPM。'; }
  document.getElementById('r_note').textContent = '按此速度，10 分钟可打约 '+(wpm*10)+' 词。';
  document.getElementById('result').classList.add('show');
}
function resetAll(){
  ended=false; startTime=null; if(timerId) clearInterval(timerId); timerId=null;
  box.value=''; wcEl.textContent='0'; clockEl.textContent='00:00';
  spellList.innerHTML='<span class="empty">暂无拼错</span>';
  document.getElementById('result').classList.remove('show');
  ignored.clear(); box.focus();
}
document.getElementById('end').onclick=endTest;
document.getElementById('reset').onclick=resetAll;
box.focus();
</script>
</body>
</html>
"""

html = HTML.replace("__WORDLIST__", WORDLIST_JS)
out = os.path.join(ROOT, "打字练习.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("生成 打字练习.html · 词典 %d 词 · %.2f MB" % (len(words), os.path.getsize(out)/1024/1024))
