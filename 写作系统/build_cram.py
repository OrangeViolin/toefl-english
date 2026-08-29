# -*- coding: utf-8 -*-
"""写作考前突击：通用模板(打字) + 高频拼写词(拼写测验) → 自包含 HTML"""
import json

# ============ 数据 ============
# 邮件通用模板（填空式万能句 + 2个真题成品）
EMAIL_TEMPLATES = [
 {"name":"邮件万能骨架（填空式·跨题可套）",
  "en":"Dear [Name], I hope you are doing well. I am writing to ask about [topic]. I would like to [goal], so I need some details about [detail 1] and [detail 2]. Could you also let me know [question]? I would really appreciate your help. Best regards, [Your name]",
  "zh":"【万能骨架】Dear [称呼]，希望一切顺利。我写信想询问[话题]。我想[目标]，所以需要[细节1]和[细节2]的信息。能否也告诉我[问题]？非常感谢你的帮助。此致敬礼[你的名字]"},
 {"name":"① 旅行邮件（真题·建议分享）",
  "en":"Dear John, I hope you are doing well. I am writing to share some interesting destinations for our summer trip. After doing some research, I have considered our goals carefully. Italy and England would be the best choices. Italy has a world-famous artistic heritage, and we could attend a fashion show there. We could also visit some famous colleges in England. I would love to hear your opinion and any other ideas. Best regards, Cindy",
  "zh":"旅行邮件：分享研究的目的地(意大利艺术+时尚秀、英国大学) → 询问意见。学 world-famous artistic heritage / I would love to hear your opinion"},
 {"name":"② 健身邮件（真题·询问信息）",
  "en":"Dear Ms. Carter, I hope you are having a wonderful week. I am writing because I am very interested in joining the fitness class next semester. My primary goal is to get in better shape and tone my body. Could you please provide more details about the class schedule and activities? I also want to know if this class is suitable for beginners. Additionally, how can I complete the registration process? I would be very grateful for your help. Best regards, Cindy",
  "zh":"健身邮件：表达兴趣+具体目标(get in better shape and tone my body) → 问课程/适合度/注册。学 complete the registration process / I would be very grateful"},
]

# 学术讨论通用模板（万能骨架 + 2个真题成品）
DISCUSSION_TEMPLATES = [
 {"name":"讨论万能骨架（填空式·跨题可套）",
  "en":"While I acknowledge [Name]'s point about [对方观点], I believe [主题] plays a significant role by [核心论点]. For example, [具体例子]. This approach does more than [表面作用]; it [深层价值]. Ultimately, [总结]. Therefore, [呼应结论].",
  "zh":"【万能骨架】虽然我承认[对方]关于[对方观点]的看法，但我认为[主题]通过[核心论点]起到重要作用。例如[具体例子]。这种方式不只是[表面]，它[深层]。最终[总结]。因此[结论]"},
 {"name":"① VR 教育（真题）",
  "en":"While I acknowledge Paul's point that VR is expensive, I believe it plays a significant role by offering immersive learning experiences. For example, chemistry students could perform dangerous experiments in a virtual lab without physical risks. This approach does more than teach theory; it lets students solve real-world problems. Ultimately, widespread use will bring costs down. Therefore, investing in VR is a beneficial long-term commitment.",
  "zh":"VR 教育：承认成本高→转折沉浸体验→化学虚拟实验例子→动手解决问题→成本会降→长期投资值得"},
 {"name":"② 公共艺术（真题）",
  "en":"While I acknowledge Student B's point about social programs, I believe public art plays a significant role by acting as a visual storyteller. For example, a series of historical murals can connect residents to their shared roots. This approach does more than decorate; it reminds people of their common values. Ultimately, public art weaves different community efforts into one story. Therefore, it strongly shapes community identity.",
  "zh":"公共艺术：承认社交项目→转折视觉讲故事→历史壁画例子→不只是装饰→串联社区→塑造认同"},
]

# 高频拼写易错词（拼写测验）
SPELL_WORDS = [
 {"w":"interesting","ipa":"/ˈɪntrəstɪŋ/","zh":"有趣的"},
 {"w":"fashion","ipa":"/ˈfæʃn/","zh":"时尚"},
 {"w":"college","ipa":"/ˈkɑːlɪdʒ/","zh":"大学，学院"},
 {"w":"destination","ipa":"/ˌdestɪˈneɪʃn/","zh":"目的地"},
 {"w":"opinion","ipa":"/əˈpɪnjən/","zh":"意见，看法"},
 {"w":"appreciate","ipa":"/əˈpriːʃieɪt/","zh":"感激，欣赏"},
 {"w":"could","ipa":"/kʊd/","zh":"能（can 过去式）"},
 {"w":"detail","ipa":"/ˈdiːteɪl/","zh":"细节"},
 {"w":"substantial","ipa":"/səbˈstænʃl/","zh":"重大的，实质的"},
 {"w":"community","ipa":"/kəˈmjuːnəti/","zh":"社区"},
 {"w":"museum","ipa":"/mjuˈziːəm/","zh":"博物馆"},
 {"w":"beneficial","ipa":"/ˌbenɪˈfɪʃl/","zh":"有益的"},
 {"w":"knowledge","ipa":"/ˈnɑːlɪdʒ/","zh":"知识（不可数）"},
 {"w":"convenient","ipa":"/kənˈviːniənt/","zh":"方便的"},
 {"w":"schedule","ipa":"/ˈskedʒuːl/","zh":"时间表，日程"},
 {"w":"equipment","ipa":"/ɪˈkwɪpmənt/","zh":"设备（不可数）"},
 {"w":"registration","ipa":"/ˌredʒɪˈstreɪʃn/","zh":"注册"},
 {"w":"experience","ipa":"/ɪkˈspɪriəns/","zh":"经验，体验"},
 {"w":"immediately","ipa":"/ɪˈmiːdiətli/","zh":"立即"},
 {"w":"grateful","ipa":"/ˈɡreɪtfl/","zh":"感激的"},
]

data = {
 "emails": EMAIL_TEMPLATES,
 "discussions": DISCUSSION_TEMPLATES,
 "words": SPELL_WORDS,
}
datajson = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

HTML = r'''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>写作考前突击 · 通用模板打字 + 高频词拼写</title><style>
:root{--bg:#f6f3ed;--card:#fffdf8;--ink:#2f2a24;--muted:#8c8072;--line:#e5dccb;--accent:#c1662f;--core:#2f8f83;--ok:#2f8f5b;--bad:#c0453a}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Helvetica Neue",sans-serif;line-height:1.7}
.wrap{max-width:820px;margin:0 auto;padding:0 18px 90px}
header{position:sticky;top:0;z-index:9;background:rgba(246,243,237,.97);border-bottom:1px solid var(--line);padding:12px 18px}
header h1{font-size:18px;margin:0}
header .sub{font-size:12.5px;color:var(--muted);margin-top:2px}
h2{font-size:16px;margin:30px 0 8px;color:var(--core);border-bottom:2px solid var(--line);padding-bottom:6px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:15px 17px;margin:12px 0}
.card h3{font-size:14.5px;margin:0 0 8px;color:var(--accent)}
.zh{color:var(--muted);font-size:13px;margin-bottom:8px}
.en{font-family:Georgia,serif;font-size:16px;line-height:1.9;background:#fbfaf6;border:1px solid var(--line);border-radius:8px;padding:10px 13px;white-space:pre-wrap}
button{cursor:pointer;font-family:inherit;border:1px solid var(--line);background:var(--card);border-radius:18px;padding:5px 13px;font-size:13px;color:#5f574c}
button.on,button.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
.trainer{margin:14px 0}
textarea{width:100%;min-height:70px;border:1px solid var(--line);border-radius:10px;padding:10px 12px;font-size:16px;font-family:Georgia,serif;background:var(--card);margin-top:8px}
.tr-target{font-size:18px;line-height:1.9;background:#fbfaf6;border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-family:Georgia,serif;min-height:30px;white-space:pre-wrap}
.c-ok{color:#1d7a44}.c-bad{color:#fff;background:#c0453a}.c-cur{background:#ffe9cf;border-bottom:2px solid var(--accent)}
.tr-stat{display:flex;gap:16px;font-size:13px;color:var(--muted);margin-top:8px;flex-wrap:wrap}
.tr-stat b{color:var(--ink)}
.tr-done{background:#e8f4ec;border:1px solid #bfdfc7;border-radius:8px;padding:8px 12px;margin-top:8px;font-size:13px;display:none}
.wgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}
.wcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.wcard .wzh{font-size:15px;font-weight:600}
.wcard .wipa{font-size:12px;color:var(--muted)}
.wcard input{width:100%;border:1px solid var(--line);border-radius:8px;padding:7px 9px;font-size:15px;margin-top:8px;font-family:Georgia,serif}
.wcard input.ok{border-color:var(--ok);background:#eef7f0}
.wcard input.bad{border-color:var(--bad);background:#fdeeea}
.wcard .ans{font-size:12.5px;margin-top:5px;display:none}
.wcard .ans.show{display:block;color:var(--accent)}
.spell-stat{font-size:13px;color:var(--muted);margin:8px 0}
.tools{position:fixed;bottom:18px;right:18px}
</style></head><body>
<header><h1>✍️ 写作考前突击</h1><div class="sub">通用模板打字 + 高频词拼写 · 考前把打字速度和拼写练成肌肉记忆</div></header>
<div class="wrap">

<h2>一、考前建议（写作 · 4 条）</h2>
<div class="card">
<b>1. 拼写是最大的坑，回读 30 秒能救一半。</b>两场作文的错全是 interesting/fashion/college/substantial/museum 这类，回读一遍就能抓出大半。下面是 20 个高频易错词，考前拼到全对。<br>
<b>2. 邮件套万能骨架，3 个任务各一句写全。</b>你打字只能打 ~60 词，那就把 60 词用在刀刃上：任务 1/2/3 各一句、句句短、请求句不省。<b>写全 &gt; 写长。</b><br>
<b>3. 学术讨论套万能骨架：先承认对方 → 转折 → 举 1 个具体例子 → 总结。</b>AI 两场都点你「例子不够具体」——把「博物馆」换成一个具体的 mural/sculpture，论证立刻深一档。<br>
<b>4. 写完作文，一定留 1 分钟回读。</b>抓拼写 + 抓 run-on（逗号连两个完整句）。
</div>

<h2>二、通用模板 · ⌨️ 打字练习</h2>
<div class="trainer">
<div class="tr-intro" style="font-size:13px;color:var(--muted)">点下方「⌨️ 打这封」载入，照着打，实时看速度+准确率。目标是<b>打完不再纠结拼写</b>。</div>
<div class="tr-target" id="tgt">👇 点下面任意「⌨️ 打这封」开始</div>
<textarea id="inp" placeholder="照着上面一字一句地打…（打错标红）" spellcheck="false"></textarea>
<div class="tr-stat"><span>速度 <b id="wpm">0</b> WPM</span><span>准确率 <b id="acc">100</b>%</span><span>用时 <b id="tmr">0</b>s</span></div>
<div class="tr-done" id="done"></div>
</div>

<h3>📧 邮件模板</h3>
<div id="emails"></div>

<h3>💬 学术讨论模板</h3>
<div id="discussions"></div>

<h2>三、高频拼写词 · ✍️ 拼写测验</h2>
<div class="spell-stat">看中文+音标，拼出英文。拼对变绿，拼错变红（点「看答案」）。目标 20 个全对。</div>
<div class="wgrid" id="wgrid"></div>

</div>
<div class="tools"><button id="rate">🐢 语速</button></div>
<script>
const DATA=__DATA__;
// TTS
let voices=[],vi=0,rate=.95;
function lv(){voices=speechSynthesis.getVoices().filter(v=>v.lang.startsWith("en"));const p=voices.findIndex(v=>/Samantha|Ava|Google US|United States/i.test(v.name));if(p>=0)vi=p;}
lv();if(speechSynthesis.onvoiceschanged!==undefined)speechSynthesis.onvoiceschanged=lv;
function say(t){if(!t)return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);if(voices[vi])u.voice=voices[vi];u.rate=rate;speechSynthesis.speak(u);}
function esc(s){return (s==null?'':''+s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function esc1(c){return c==='<'?'&lt;':c==='>'?'&gt;':c==='&'?'&amp;':c;}

// 打字器
const tgt=document.getElementById("tgt"),inp=document.getElementById("inp"),done=document.getElementById("done");
let target="",startT=null,finished=false;
function loadTarget(t){target=t;startT=null;finished=false;inp.value="";done.style.display="none";render();inp.focus();}
function render(){const typed=inp.value;let h="";
  for(let i=0;i<target.length;i++){const c=target[i];const cls=i<typed.length?(typed[i]===c?"c-ok":"c-bad"):(i===typed.length?"c-cur":"");
    h+=cls?'<span class="'+cls+'">'+esc1(c)+'</span>':esc1(c);}tgt.innerHTML=h;}
inp.oninput=function(){
  if(!startT&&inp.value.length)startT=Date.now();render();
  const typed=inp.value;let ok=0;for(let i=0;i<typed.length;i++)if(typed[i]===target[i])ok++;
  const secs=startT?(Date.now()-startT)/1000:0;
  const wpm=secs>0?Math.round((ok/5)/(secs/60)):0;const acc=typed.length?Math.round(ok/typed.length*100):100;
  document.getElementById("wpm").textContent=wpm;document.getElementById("acc").textContent=acc;document.getElementById("tmr").textContent=Math.round(secs);
  if(typed===target&&!finished){finished=true;const words=target.split(/\s+/).length;
    done.style.display="block";done.innerHTML='✅ 打完 '+words+' 词！速度 <b>'+wpm+' WPM</b> · 准确率 '+acc+'% · 用时 '+Math.round(secs)+'s<br><span style="font-size:12.5px;color:#8a7f70">多打几遍成肌肉记忆，考前就不纠结拼写了。</span>';}
};

// 渲染模板卡片
function tplCard(t){return '<div class="card"><h3>'+esc(t.name)+'</h3><div class="zh">'+esc(t.zh)+'</div><div class="en">'+esc(t.en)+'</div><div style="margin-top:8px"><button class="drill" data-t="'+esc(t.en).replace(/"/g,'&quot;')+'">⌨️ 打这封</button> <button class="say" data-say="'+esc(t.en).replace(/"/g,'&quot;')+'">🔊 朗读</button></div></div>';}
document.getElementById("emails").innerHTML=DATA.emails.map(tplCard).join('');
document.getElementById("discussions").innerHTML=DATA.discussions.map(tplCard).join('');
document.querySelectorAll(".drill").forEach(b=>b.onclick=()=>{loadTarget(b.dataset.t);document.querySelector('.trainer').scrollIntoView({behavior:'smooth',block:'start'});});
document.querySelectorAll(".say").forEach(el=>el.onclick=e=>{e.stopPropagation();say(el.dataset.say);});

// 拼写测验
const wg=document.getElementById("wgrid");
wg.innerHTML=DATA.words.map((w,i)=>'<div class="wcard" data-i="'+i+'"><div class="wzh">'+esc(w.zh)+'</div><div class="wipa">'+esc(w.ipa)+' <button class="say" data-say="'+esc(w.w)+'">🔊</button></div><input placeholder="拼出来…" spellcheck="false" autocomplete="off"><div class="ans">✓ '+esc(w.w)+'</div></div>').join('');
document.querySelectorAll(".wcard").forEach(card=>{
  const i=+card.dataset.i, w=DATA.words[i], inp2=card.querySelector("input"), ans=card.querySelector(".ans");
  inp2.oninput=()=>{
    const v=inp2.value.trim();
    if(v.toLowerCase()===w.w.toLowerCase()){inp2.classList.add("ok");inp2.classList.remove("bad");}
    else if(v){inp2.classList.add("bad");inp2.classList.remove("ok");}
    else{inp2.classList.remove("ok","bad");}
  };
  inp2.onkeydown=e=>{if(e.key==="Enter"){ans.classList.toggle("show");}};
  card.querySelector(".ans").onclick=()=>ans.classList.toggle("show");
});
// 拼写卡里的 say 也要绑定（上面 querySelectorAll(".say") 已覆盖，但动态渲染的 wcard 里的 say 需要重新绑定）
document.querySelectorAll(".wcard .say").forEach(el=>el.onclick=e=>{e.stopPropagation();say(el.dataset.say);});

document.getElementById("rate").onclick=function(){rate=rate>=1.1?0.7:rate+0.2;this.textContent="🐢 "+rate.toFixed(1)+"x";say("speed");};
render();
</script></body></html>'''

html = HTML.replace("__DATA__", datajson)
open("写作考前突击.html","w",encoding="utf-8").write(html)
print("✅ 写作考前突击.html — 邮件模板",len(EMAIL_TEMPLATES),"· 讨论模板",len(DISCUSSION_TEMPLATES),"· 拼写词",len(SPELL_WORDS))
