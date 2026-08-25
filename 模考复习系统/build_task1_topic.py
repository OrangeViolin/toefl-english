# -*- coding: utf-8 -*-
"""写作 Task1 连词成句 · 专题突破页（口诀版·自包含）
少术语、多口诀、可背诵。核心口诀 + 3步法 + 3个易错点详解 + 累积错题本（只记错题）。
彩色：@S{谁·主语}蓝 @V{大动词·动作}红 @C{藏着的问/名词小尾巴}紫 @P{被动be+过去分词/固定搭配}橙
新一场模考错题：往 WRONG 对应分组追加（en正确彩注/your你摆成的/point大白话考点/src来源），重跑本脚本。
"""
import os, re, html
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "专题")

def e(s): return html.escape(str(s or ""), quote=True)

def render(text):
    out, i = [], 0
    for m in re.finditer(r'@([SVOCPM])\{([^}]*)\}', text):
        if m.start() > i: out.append(_words(text[i:m.start()]))
        out.append(f'<span class="g g-{m.group(1)} say" data-say="{e(m.group(2))}">{e(m.group(2))}</span>')
        i = m.end()
    if i < len(text): out.append(_words(text[i:]))
    return "".join(out)

def _words(t):
    parts = []
    for tok in re.split(r'(\s+)', t):
        if not tok: continue
        if tok.isspace(): parts.append(tok); continue
        w = re.sub(r"[^A-Za-z'-]", "", tok)
        parts.append(f'<span class="wd" data-say="{e(w)}">{e(tok)}</span>' if w else e(tok))
    return "".join(parts)

def sfull(text): return re.sub(r'@[SVOCPM]\{([^}]*)\}', r'\1', text)

# ============ 口诀总表（这一页的灵魂）============
CHANTS = [
 {"c":"明着问就倒，藏着问不倒","m":"单独一句问话（末尾有问号）→ 把 will/did/is 提到「谁」前面（倒装）；问话藏在 know / ask / wonder 后面 → 不提，跟平常说话一样「谁在前、动作在后」。",
  "eg":["明着问：what @V{will they} serve?","藏着问：I know what @S{they} @V{will} serve."]},
 {"c":"Did 一出手，动词回原形","m":"句子里出现 Did / Does / Do，后面那个动词一律用<b>原形</b>（Did 已经背了「过去/疑问」的锅，后面动词就不用再变）。",
  "eg":["@V{Did you catch} up on it?　（不是 caught / discussed）"]},
 {"c":"能加「被」，就 be + 过去分词","m":"把从句翻成中文，能加个「<b>被</b>」字 → 用 be（is/was/were/been）+ 动词的过去分词。",
  "eg":["被讨论 = @P{was discussed}","被达成 = @P{have been reached}"]},
 {"c":"名词的小尾巴，紧贴不分家","m":"一个名词后面拖着一段补充说明（that… / who… / 我做的…）→ 这段小尾巴<b>紧贴名词</b>，别甩到别处。找整句的「大动词」，它前面一整块就是主语。",
  "eg":["@S{The library @C{that is open 24 hours}} @V{is} the best."]},
 {"c":"看时间词，定时态","m":"yesterday / last → 过去；now / 正在 → 现在(进行)；next / will → 将来；already / yet → 完成（have + 过去分词）。先看时间词，再定动词形态。",
  "eg":["yesterday → went／will → will go／yet → have received"]},
]

# ============ 3 个易错点详解（大白话 + 口诀 + 例）============
HOTS = [
 {"key":"ask","title":"① 明着问 vs 藏着问（要不要把 will/did 提前）","chant":"明着问就倒，藏着问不倒","weak":True,
  "cols":[
   {"t":"明着问（一句话就是个问题·末尾 ?）","f":"→ 倒装：疑问词 + will/did/is + 谁","ex":["what @V{will they} serve?","where @V{did you} go?"],"sp":"help 词提前，谁往后放。"},
   {"t":"藏着问（跟在 know / ask / tell me 后）","f":"→ 不倒：疑问词 + 谁 + 动作","ex":["I know what @S{they} @V{will serve}.","She asked where @S{the class} @V{could go}."],"sp":"藏起来就变乖，恢复平常语序。"}],
  "tip":"⏱ 一眼看：这句话<b>本身是不是个问题</b>（末尾问号）？是→倒装；只是嵌在别的话里→不倒。"},
 {"key":"voice","title":"② 主动 vs 被动（加不加 be + 过去分词）","chant":"能加「被」，就 be + 过去分词","weak":True,
  "cols":[
   {"t":"主动（它自己做动作）","f":"→ 谁 + 动作词","ex":["what resources @S{we} @V{had used}","@S{what} @V{prompted} the change"],"sp":"★ 疑问词自己就是「谁」时，后面直接跟动作（what prompted…）。"},
   {"t":"被动（它被…、动作落它身上）","f":"→ 谁 + be + 过去分词","ex":["what techniques @P{were used}","what goals @P{have been reached}"],"sp":"is/was/were + 过去分词；完成+被动叠加 = have been + 过去分词。"}],
  "tip":"⏱ 翻成中文能加「<b>被</b>」→ 被动。were used = 被用；we had used = 我们用了。"},
 {"key":"tense","title":"③ 时态（动词该用哪个形态）","chant":"Did 一出手，动词回原形　·　看时间词定时态","weak":False,
  "cols":[
   {"t":"有 Did/Does/Do → 动词回原形","f":"","ex":["@V{Did you catch} up?（不是 caught）","@V{Does it resolve} the bugs?"],"sp":"助动词背了时态的锅，主动词就还原。"},
   {"t":"看时间词 → 定时态","f":"","ex":["yesterday → @V{went}","will / next → @V{will be}","yet → @V{have received}"],"sp":"yesterday/last=过去，next/will=将来，yet/already=完成。"}],
  "tip":"⏱ 摆之前先扫一眼句子里的<b>时间词</b>和有没有 <b>Did/have/be</b>，动词形态跟着它们走。"},
]

# ============ 累积错题本（只记错题·按易错点分组·每场往里加）============
WRONG = [
{"grp":"① 明着问 / 藏着问（倒装）","items":[
 {"en":"what type of cuisine @V{will they} serve?","your":"what type of cuisine they will serve","point":"这是明着问（末尾问号）→ 要倒装，will 提到 they 前面。口诀：明着问就倒。","src":"08-21晚 组4·题6"},
 {"en":"She wanted to know where @S{the class} @V{could go} for lunch.","your":"where could the class go","point":"这是藏在 know 后面的问 → 不倒装，恢复「the class + could go」。口诀：藏着问不倒。","src":"08-21晚 组2·题8"},
 {"en":"I'm not sure @C{who the author is}.","your":"who is the author","point":"藏在 I'm not sure 后面的问 → 不倒装：who + the author（谁）+ is（动作），is 放最后。口诀：藏着问不倒。","src":"08-21晨 完整模考·连词成句题8"},
 {"en":"She was curious about @S{what} @V{prompted} the change in the exam schedule.","your":"顺序摆乱","point":"what 自己就是「谁」，后面直接跟动作 prompted，别再加一个主语。","src":"08-21 组2·题1"},
]},
{"grp":"② 主动 / 被动（be+过去分词）","items":[
 {"en":"He wanted to announce what environmental goals @P{have been reached}.","your":"顺序摆乱","point":"目标是「被达成」→ 被动+完成 = have been + reached。口诀：能加「被」就 be+过去分词。","src":"08-21 组2·题7"},
]},
{"grp":"③ 时态（Did+原形 / 完成时）","items":[
 {"en":"@V{Did you catch} up on what @P{was discussed}?","your":"Did you discussed…","point":"Did 后面动词回原形 catch（不是 discussed/caught）；里面「被讨论」用 was discussed。口诀：Did 一出手，动词回原形。","src":"08-21晚 组4·题3"},
 {"en":"@V{Have you installed} all of the necessary software updates?","your":"updates / installed 摆错位","point":"现在完成时的问：Have + 谁 + 过去分词 installed。（have/has + 过去分词 = 完成）","src":"08-21 组2·题2"},
]},
{"grp":"④ 名词的小尾巴（紧贴名词）","items":[
 {"en":"@S{The email @C{I received}} @V{had} the wrong time listed.","your":"The time I received the email had wrong listed","point":"「我收到的」这条小尾巴紧贴 email；大动词 had 前面整块（The email I received）是主语。","src":"08-21 组1·题7"},
 {"en":"@S{The library @C{that is open 24 hours}} @V{is} the most convenient.","your":"顺序摆乱","point":"小尾巴 that is open 24 hours 紧贴 library；大动词 is 前面整块是主语。","src":"08-21 组4·题7"},
 {"en":"@S{The boutique @C{that is downtown}} @V{has} the required clothing items.","your":"顺序摆乱","point":"小尾巴 that is downtown 紧贴 boutique，别甩走。","src":"08-21 组4·题5"},
 {"en":"It was in @S{the magazine @C{that I read at the library}}.","your":"顺序摆乱","point":"小尾巴 that I read 紧贴 magazine。","src":"08-21 组4·题9"},
 {"en":"I'm practicing @S{the piece @C{that my professor suggested}}.","your":"my professor suggested that I'm practicing the piece","point":"主句是「I'm practicing the piece」，「that my professor suggested」是给 piece 加的小尾巴，别把主句摆反。","src":"08-21晚 组3·题1"},
]},
{"grp":"⑤ 固定搭配（背下来直接摆）","items":[
 {"en":"None of the team members have @P{turned} @O{it} @P{in} yet.","your":"turned in it","point":"turn in 遇到代词 it，it 放中间：turn it in。","src":"08-21 组3·题6"},
 {"en":"I have no @P{intention of} going to the seminar.","your":"intention / of / to 摆错","point":"intention OF doing 是固定搭配；going TO the seminar。","src":"08-21 组3·题8"},
]},
]

CHECK = ["先圈出整句的<b>大动词</b>（那个核心动作词）——它是骨架。",
"大动词<b>前面</b>找「谁」；注意「谁」后面可能拖着<b>小尾巴</b>（that…/我做的…），一起当主语，别拆。",
"这句<b>本身是问题吗</b>（末尾?）？是→倒装（will/did 提前）；藏在 know/ask 后→不倒装。",
"能加「<b>被</b>」→ be + 过去分词；有 <b>Did/Does/Do</b> → 后面动词回原形。",
"扫一眼<b>时间词</b>（yesterday/next/yet）定时态。",
"摆完<b>数一下词，全用上、别留空</b>（留空=0分）。"]

def chantcard(x):
    egs = "".join(f'<div class="ceg">{render(g)} <button class="play say" data-say="{e(sfull(g))}">🔊</button></div>' for g in x["eg"])
    return f'<div class="chant"><div class="cc">🔑 {e(x["c"])}</div><div class="cm">{x["m"]}</div>{egs}</div>'

def hotsec(h):
    cols = "".join(
      f'<div class="apbox"><div class="t">{e(c["t"])}</div>{("<div class=f>"+c["f"]+"</div>") if c.get("f") else ""}'
      + "".join(f'<div class="ex">{render(x)} <button class="play say" data-say="{e(sfull(x))}">🔊</button></div>' for x in c["ex"])
      + f'<div class="sp">{c["sp"]}</div></div>' for c in h["cols"])
    badge = '<span class="wkbadge">重点</span>' if h.get("weak") else ""
    return (f'<div class="hotspot" id="h-{h["key"]}"><h3>{e(h["title"])}{badge}</h3>'
            f'<div class="chantline">口诀：<b>{e(h["chant"])}</b></div>'
            f'<div class="apcol">{cols}</div><div class="aptest">{h["tip"]}</div></div>')

def wrongcard(it):
    full = sfull(it["en"])
    src = f'<span class="src">{e(it["src"])}</span>' if it.get("src") else ""
    return (f'<div class="card w" data-mk="{e(full[:40])}"><button class="star">☆</button>{src}'
            f'<div class="en"><button class="play say" data-say="{e(full)}">🔊</button>✓ {render(it["en"])}</div>'
            f'<div class="fix">✗ 你摆成：{e(it["your"])}</div><div class="note">🔑 {it["point"]}</div></div>')

def wronggrp(g):
    return f'<div class="bankgrp"><h3>{e(g["grp"])} <span class="cnt">{len(g["items"])} 题</span></h3><div class="cards">{"".join(wrongcard(i) for i in g["items"])}</div></div>'

nwrong = sum(len(g["items"]) for g in WRONG)
legend = ('<span class="g g-S">谁（主语）</span><span class="g g-V">大动词（动作）</span>'
          '<span class="g g-C">藏着的问 / 名词小尾巴</span><span class="g g-P">被动 be+过去分词 / 固定搭配</span>')

HTML = f'''<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>写作 Task1 连词成句 · 口诀突破</title><style>
:root{{--bg:#f6f3ed;--card:#fffdf9;--ink:#2c2620;--sub:#8a7f70;--accent:#c1662f;--core:#2f8f83;--line:#e7dfd2;--gold:#b8860b;--red:#c0453b;--S:#2f6f8f;--V:#c1662f;--C:#7a5bb0;--P:#b8860b}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.7}}
header{{position:sticky;top:0;z-index:9;background:rgba(246,243,237,.97);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 18px}}
h1{{margin:0 0 5px;font-size:18px}}.diag{{font-size:13px;color:var(--sub);margin-bottom:7px}}.diag b{{color:var(--core)}}
.legend{{display:flex;gap:6px;flex-wrap:wrap;font-size:12px}}
main{{max-width:940px;margin:0 auto;padding:16px 18px 80px}}
h2{{font-size:16.5px;margin:26px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--line)}}
.g{{border-radius:4px;padding:0 4px;font-weight:600;cursor:pointer;color:#fff}}
.g-S{{background:var(--S)}}.g-V{{background:var(--V)}}.g-C{{background:var(--C)}}.g-P{{background:var(--P)}}
.legend .g{{cursor:default}}
.chants{{display:grid;gap:10px}}
.chant{{background:#fff5ec;border:1px solid #f0d3b8;border-left:4px solid var(--accent);border-radius:10px;padding:11px 15px}}
.cc{{font-size:16px;font-weight:800;color:var(--accent)}}
.cm{{font-size:14px;margin:5px 0}}.cm b{{color:var(--accent)}}
.ceg{{font-size:14.5px;margin:4px 0;line-height:1.9}}
.method{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 18px}}
.method ol{{margin:0;padding-left:22px}}.method li{{margin:7px 0;font-size:14.5px}}.method li b{{color:var(--accent)}}
.hotspot{{background:var(--card);border:2px solid var(--line);border-radius:14px;padding:14px 18px;margin:12px 0}}
.hotspot h3{{margin:0 0 6px;font-size:15.5px}}
.wkbadge{{background:var(--accent);color:#fff;font-size:11px;border-radius:5px;padding:1px 8px;margin-left:8px;vertical-align:middle}}
.chantline{{font-size:13.5px;color:var(--sub);margin-bottom:9px}}.chantline b{{color:var(--accent);font-size:14.5px}}
.apcol{{display:grid;grid-template-columns:1fr 1fr;gap:11px}}
@media(max-width:640px){{.apcol{{grid-template-columns:1fr}}}}
.apbox{{background:#fbfaf6;border:1px solid var(--line);border-radius:10px;padding:11px 13px}}
.apbox .t{{font-weight:700;font-size:14px;margin-bottom:3px}}.apbox .f{{font-size:12.5px;color:var(--sub);margin-bottom:6px}}
.apbox .ex{{font-size:15px;margin:5px 0;line-height:1.85}}
.apbox .sp{{font-size:12.5px;color:var(--core);margin-top:7px;border-top:1px dashed var(--line);padding-top:6px}}
.aptest{{background:#fbf4e9;border-radius:9px;padding:9px 13px;margin-top:11px;font-size:13.5px}}.aptest b{{color:var(--accent)}}
.play{{border:none;background:none;cursor:pointer;font-size:13px;opacity:.6;padding:0 3px}}
.wd{{cursor:pointer;border-radius:3px}}.wd:hover{{background:#ffe9cf}}
.bankintro{{font-size:13px;color:var(--sub);margin-bottom:10px;background:#fbf4e9;border-radius:8px;padding:8px 12px}}
.bankgrp{{margin:12px 0}}.bankgrp h3{{font-size:15px;margin:14px 0 8px}}.cnt{{color:var(--sub);font-size:12px;font-weight:400}}
.cards{{display:grid;gap:9px}}
.card{{position:relative;background:#fdf6f4;border:1px solid #ecc7c1;border-radius:11px;padding:11px 44px 10px 13px}}
.card .en{{font-size:15.5px;line-height:1.95}}.card .fix{{font-size:13px;color:var(--red);margin-top:3px}}.card .note{{font-size:13px;color:var(--core);margin-top:4px}}
.card .star{{position:absolute;top:9px;right:10px;border:none;background:none;font-size:15px;color:var(--gold);cursor:pointer}}
.card.done{{background:#eef6f3;border-color:#bfe0d7}}.card.done .star{{color:var(--core)}}
.src{{position:absolute;top:10px;right:32px;font-size:11px;color:var(--sub)}}
.check{{background:#fbf4e9;border:1px solid #ecdcbf;border-radius:12px;padding:12px 16px}}.check ol{{margin:0;padding-left:22px}}.check li{{margin:6px 0;font-size:14px}}.check li b{{color:var(--accent)}}
.tools{{position:fixed;right:14px;bottom:16px;z-index:20}}.tools button{{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:8px 13px;font-size:13px;cursor:pointer;box-shadow:0 2px 8px rgba(150,120,70,.12)}}
</style></head><body>
<header><h1>🧩 写作 Task1 · 连词成句「口诀」突破</h1>
<div class="diag">你练了 8 组，分数在爬——已经刷出 <b>10/10、9/9 两个满分</b>。剩下的错都收进了下面的口诀和错题本，背熟就稳。</div>
<div class="legend">{legend}</div></header>
<main>
<h2>🔑 五句口诀 · 先背这个（全页的灵魂）</h2>
<div class="chants">{"".join(chantcard(c) for c in CHANTS)}</div>

<h2>🎯 摆题 3 步（每次照做）</h2>
<div class="method"><ol>
<li><b>①圈「大动词」</b>：找整句的核心动作词（is/had/wanted/will…），它是骨架。</li>
<li><b>②找「谁」</b>：大动词前面是谁做的；「谁」后面可能拖着<b>小尾巴</b>（that…/我做的…），一起当主语，别拆散。</li>
<li><b>③套口诀摆好</b>：明着问还是藏着问？主动还是被动？什么时态？摆完<b>数词、别留空</b>。</li>
</ol></div>

<h2>📌 三个易错点 · 大白话详解</h2>
{"".join(hotsec(h) for h in HOTS)}

<h2>📕 累积错题本 · {nwrong} 题（只记错题·每场往里加·点彩块看成分·☆标掌握）</h2>
<div class="bankintro">只收你做错的题，对的不记。绿✓=正确摆法，红✗=你当时摆成的，🔑=大白话考点。以后每场模考的错题都累积到这里，越攒越少。</div>
{"".join(wronggrp(g) for g in WRONG)}

<h2>✅ 突破清单 · 每次做题走一遍</h2>
<div class="check"><ol>{"".join(f"<li>{c}</li>" for c in CHECK)}</ol></div>
</main>
<div class="tools"><button id="rate">🐢 语速</button></div>
<script>
const LS="task1topic-mastered";let done=new Set(JSON.parse(localStorage.getItem(LS)||"[]"));
let voices=[],vi=0,rate=.9;
function lv(){{voices=speechSynthesis.getVoices().filter(v=>v.lang.startsWith("en"));const p=voices.findIndex(v=>/Samantha|Ava|Google US|United States/i.test(v.name));if(p>=0)vi=p;}}
lv();if(speechSynthesis.onvoiceschanged!==undefined)speechSynthesis.onvoiceschanged=lv;
function say(t){{if(!t)return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);if(voices[vi])u.voice=voices[vi];u.rate=rate;speechSynthesis.speak(u);}}
document.querySelectorAll(".say,.wd").forEach(el=>el.addEventListener("click",e=>{{e.stopPropagation();say(el.dataset.say);}}));
function paint(){{document.querySelectorAll(".card").forEach(c=>{{const k=c.dataset.mk,on=done.has(k);c.classList.toggle("done",on);c.querySelector(".star").textContent=on?"★":"☆";}});localStorage.setItem(LS,JSON.stringify([...done]));}}
document.querySelectorAll(".card .star").forEach(b=>b.addEventListener("click",e=>{{e.stopPropagation();const c=b.closest(".card"),k=c.dataset.mk;done.has(k)?done.delete(k):done.add(k);paint();}}));
paint();
document.getElementById("rate").onclick=function(){{rate=rate>=1.1?.7:rate+.2;this.textContent="🐢 "+rate.toFixed(1)+"x";say("speed");}};
</script></body></html>'''

os.makedirs(OUT, exist_ok=True)
open(os.path.join(OUT, "写作task1-连词成句专题.html"), "w", encoding="utf-8").write(HTML)
print(f"✅ 写作task1-连词成句专题.html（口诀版）— 5 口诀 · 3 易错点 · 累积错题本 {nwrong} 题")
