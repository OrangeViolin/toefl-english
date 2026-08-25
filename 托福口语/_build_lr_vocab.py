# -*- coding: utf-8 -*-
"""Listen and Repeat · 场景词 & 常见表达 积累页
data/lr-vocab.json → 跟读场景词与表达.html（自包含·点读·掌握标记·背记模式）
每来新一场跟读真题，就往 lr-vocab.json 的 scenes[].words / expressions[] 追加，再跑本脚本。
"""
import json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "lr-vocab.json")
OUT = os.path.join(HERE, "跟读场景词与表达.html")

def e(s): return html.escape(str(s), quote=True)

def main():
    d = json.load(open(DATA, encoding="utf-8"))
    nword = sum(len(s["words"]) for s in d["scenes"])
    nexpr = len(d["expressions"])

    # 场景词卡片
    scene_html = []
    for s in d["scenes"]:
        cards = "".join(
            f'''<div class="card" data-key="{e(w["w"])}" data-zh="{e(w["zh"])}">
      <button class="star" title="标记掌握">☆</button>
      <div class="w say" data-say="{e(w["w"].replace(" (v.)",""))}">{e(w["w"])}</div>
      <div class="ipa">{e(w.get("ipa",""))}</div>
      <div class="zh">{e(w["zh"])}</div>
    </div>''' for w in s["words"])
        scene_html.append(f'''<section class="scene" data-scene="{e(s["key"])}">
    <h2>{e(s["label"])} <span class="n">{len(s["words"])}</span></h2>
    <div class="grid">{cards}</div>
  </section>''')
    scene_html = "\n".join(scene_html)

    # 常见表达卡片
    expr_cards = "".join(
        f'''<div class="ecard" data-key="{e(x["en"])}" data-zh="{e(x["zh"])}">
      <button class="star" title="标记掌握">☆</button>
      <div class="en say" data-say="{e(x.get("eg", x["en"]))}">{e(x["en"])}</div>
      <div class="zh">{e(x["zh"])}</div>
      <div class="eg say" data-say="{e(x.get("eg",""))}">🔊 {e(x.get("eg",""))}</div>
    </div>''' for x in d["expressions"])

    page = f'''<!DOCTYPE html>
<html lang="zh"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d["title"])}</title>
<style>
:root{{--bg:#f6f3ed;--card:#fffdf9;--ink:#2c2620;--sub:#8a7f70;--accent:#c1662f;--core:#2f8f83;--line:#e7dfd2;--gold:#d9a441}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.5}}
header{{position:sticky;top:0;z-index:9;background:rgba(246,243,237,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:14px 18px}}
h1{{margin:0 0 3px;font-size:19px}}
.sub{{color:var(--sub);font-size:12.5px;margin-bottom:9px}}
.bar{{display:flex;gap:8px;flex-wrap:wrap;align-items:center}}
.btn{{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:20px;padding:6px 13px;font-size:13px;cursor:pointer}}
.btn.on{{background:var(--core);color:#fff;border-color:var(--core)}}
.btn.amber.on{{background:var(--accent);border-color:var(--accent)}}
.prog{{margin-left:auto;font-size:13px;color:var(--sub)}}
.prog b{{color:var(--accent)}}
main{{max-width:920px;margin:0 auto;padding:16px 18px 60px}}
h2{{font-size:15.5px;margin:22px 0 10px;padding-bottom:5px;border-bottom:2px solid var(--line)}}
h2 .n{{color:var(--sub);font-size:12px;font-weight:400}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}}
.card{{position:relative;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 12px 11px}}
.card .w{{font-size:16px;font-weight:700;cursor:pointer;padding-right:20px}}
.card .w:hover{{color:var(--accent)}}
.ipa{{color:var(--core);font-size:12.5px;margin:2px 0}}
.zh{{color:var(--sub);font-size:13px}}
.star{{position:absolute;top:8px;right:9px;border:none;background:none;font-size:17px;color:var(--gold);cursor:pointer;line-height:1;padding:0}}
.card.done{{background:#eef6f3;border-color:#bfe0d7}}
.card.done .star{{color:var(--core)}}
.elist{{display:grid;gap:10px}}
.ecard{{position:relative;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 40px 11px 14px}}
.ecard .en{{font-size:15.5px;font-weight:700;cursor:pointer}}
.ecard .en:hover{{color:var(--accent)}}
.ecard .zh{{font-size:13px;margin:2px 0}}
.ecard .eg{{font-size:12.5px;color:var(--core);cursor:pointer;margin-top:3px}}
.ecard.done{{background:#eef6f3;border-color:#bfe0d7}}
.ecard.done .star{{color:var(--core)}}
body.recite .zh{{filter:blur(5px);cursor:pointer}}
body.recite .zh.show{{filter:none}}
.hint{{color:var(--sub);font-size:12px;margin:6px 0 0}}
</style></head>
<body>
<header>
  <h1>🎧 {e(d["title"])}</h1>
  <div class="sub">{e(d["subtitle"])}　·　场景词 <b>{nword}</b> · 常见表达 <b>{nexpr}</b></div>
  <div class="bar">
    <button class="btn" id="voice">🔊 朗读</button>
    <button class="btn amber" id="recite">🙈 背记模式</button>
    <button class="btn" id="onlyleft">只看未掌握</button>
    <button class="btn" id="reset">↺ 清掌握</button>
    <span class="prog">掌握 <b id="pdone">0</b> / <span id="ptot">{nword+nexpr}</span></span>
  </div>
  <div class="hint">点词/句 → 朗读；点右上 ☆ → 标掌握；背记模式下点中文可显形。掌握进度存本地。</div>
</header>
<main>
{scene_html}
  <section class="scene" data-scene="expr">
    <h2>🗣 常见表达 · 跟读高频句型 <span class="n">{nexpr}</span></h2>
    <div class="elist">{expr_cards}</div>
  </section>
</main>
<script>
const LS="lrvocab-mastered-v1";
let done=new Set(JSON.parse(localStorage.getItem(LS)||"[]"));
// TTS
let voices=[],vi=0;
function loadV(){{voices=speechSynthesis.getVoices().filter(v=>v.lang.startsWith("en"));
  const pref=voices.findIndex(v=>/Samantha|Ava|Google US|United States/i.test(v.name));if(pref>=0)vi=pref;}}
loadV();if(speechSynthesis.onvoiceschanged!==undefined)speechSynthesis.onvoiceschanged=loadV;
function say(t){{if(!t)return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);
  if(voices[vi])u.voice=voices[vi];u.rate=.92;speechSynthesis.speak(u);}}
document.querySelectorAll(".say").forEach(el=>el.addEventListener("click",e=>{{
  if(document.body.classList.contains("recite")&&el.classList.contains("zh"))return;
  say(el.dataset.say);}}));
// 掌握标记
function key(c){{return c.dataset.key;}}
function paint(){{let n=0;
  document.querySelectorAll(".card,.ecard").forEach(c=>{{
    const k=key(c),on=done.has(k);c.classList.toggle("done",on);
    c.querySelector(".star").textContent=on?"★":"☆";if(on)n++;
    c.style.display=(document.body.classList.contains("onlyleft")&&on)?"none":"";
  }});
  document.getElementById("pdone").textContent=n;
  localStorage.setItem(LS,JSON.stringify([...done]));}}
document.querySelectorAll(".card,.ecard").forEach(c=>{{
  c.querySelector(".star").addEventListener("click",e=>{{e.stopPropagation();
    const k=key(c);done.has(k)?done.delete(k):done.add(k);paint();}});}});
// 背记模式：点中文显形
document.querySelectorAll(".zh").forEach(z=>z.addEventListener("click",()=>{{
  if(document.body.classList.contains("recite"))z.classList.toggle("show");}}));
// 按钮
document.getElementById("recite").onclick=function(){{document.body.classList.toggle("recite");
  this.classList.toggle("on");document.querySelectorAll(".zh.show").forEach(z=>z.classList.remove("show"));}};
document.getElementById("onlyleft").onclick=function(){{document.body.classList.toggle("onlyleft");
  this.classList.toggle("on");paint();}};
document.getElementById("reset").onclick=function(){{if(confirm("清空所有掌握标记？")){{done.clear();paint();}}}};
document.getElementById("voice").onclick=function(){{
  if(voices.length){{vi=(vi+1)%voices.length;say("This is voice "+(vi+1));this.textContent="🔊 "+voices[vi].name.split(" ")[0];}}}};
paint();
</script>
</body></html>'''
    open(OUT, "w", encoding="utf-8").write(page)
    print(f"✅ 跟读场景词与表达.html — 场景词 {nword} · 常见表达 {nexpr}（{len(d['scenes'])} 个场景）")

if __name__ == "__main__":
    main()
