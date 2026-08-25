# -*- coding: utf-8 -*-
"""邮件写作专题（自包含）· 照成品练打字 + 保底完整版 + 全文中文翻译
Fish 实测：同一题两次都只打到 ~60 词、最后一个任务被掐掉（打不完）。
核心＝【60词保底完整版】(3任务各1句·请求句绝不省)先打得完，再练进阶版提速。
每封 MODEL：short(保底~60词)+zh / en(进阶~120词)+zh2，均带完整中文翻译，都能载入打字器。
"""
import os, html
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "专题")

def e(s): return html.escape(str(s or ""), quote=True)

MODELS = [
 {"title":"公寓维修 · 致房东", "scene":"空调坏/墙潮 → 描述 + 影响学习 + 请求（你考过·两次都没打完）",
  "short":"Dear Mr. Thompson, I hope you are doing well. I am writing about two problems in my new apartment: the air conditioner is broken, and the wall is damp. These problems make it very hard for me to study at home. I would really appreciate it if you could arrange to fix them as soon as possible. Thank you for your time. Best regards, [Your Name]",
  "zh":"亲爱的Thompson先生，希望您一切都好。我写信是想反映新公寓的两个问题：空调坏了，墙壁潮湿。这些问题让我很难在家学习。如果您能安排尽快修理，我将非常感激。感谢您抽出时间。此致，[你的名字]",
  "en":"Dear Mr. Thompson, I hope you are doing well. I have been living in the apartment for a week now, but I have noticed a few urgent issues that need your attention. Specifically, the air conditioner is not working at all, and there is a significant damp spot on the wall that keeps getting wetter. These problems are making it very difficult for me to focus on my university work. As a student, having a quiet and comfortable place to study is essential for my success. I would really appreciate it if you could make arrangements to have these issues addressed as soon as possible. Thank you very much for your time and assistance. Best regards, [Your Name]",
  "zh2":"亲爱的Thompson先生，希望您一切都好。我已在这套公寓住了一周，但发现了几个亟需您关注的紧急问题。具体来说，空调完全不工作，墙上还有一块明显的潮斑，而且越来越湿。这些问题让我很难专注于大学的学习。作为学生，有一个安静舒适的学习环境对我的学业至关重要。如果您能安排尽快解决这些问题，我将非常感激。非常感谢您的时间和帮助。此致，[你的名字]"},
 {"title":"宿舍网络 · 致宿管", "scene":"网慢常断 → 描述 + 影响网课 + 请求（你考过）",
  "short":"Dear Mr. Evans, I hope you are doing well. I am writing because the Wi-Fi in my dormitory is very slow and often disconnects. This makes it very hard for me to attend my online classes and finish my assignments. I would really appreciate it if you could have it fixed as soon as possible. Thank you for your help. Best regards, [Your Name]",
  "zh":"亲爱的Evans先生，希望您一切都好。我写信是因为宿舍的Wi-Fi很慢、还经常断线。这让我很难上网课和完成作业。如果您能尽快修好，我将非常感激。感谢您的帮助。此致，[你的名字]",
  "en":"Dear Mr. Evans, I hope you are having a productive week. I am writing to bring your attention to the internet connection issues I have been experiencing in my dormitory lately. Over the past few days, the Wi-Fi has become incredibly slow and frequently disconnects without warning. This situation is making it very difficult for me to keep up with my academic responsibilities. For instance, I have been struggling to stay logged into my live online classes, often missing crucial parts of the lectures when the signal drops. I would greatly appreciate it if you could look into this matter and have the connection improved as soon as possible. Thank you for your time and help. Best regards, [Your Name]",
  "zh2":"亲爱的Evans先生，希望您这周过得高效。我写信是想提请您注意我最近在宿舍遇到的网络问题。这几天Wi-Fi变得极慢，还经常毫无预警地断线。这让我很难跟上学业。比如，我一直很难保持登录我的在线直播课，信号一断就常常错过课上的重点。如果您能过问此事、尽快改善网络，我将不胜感激。感谢您的时间和帮助。此致，[你的名字]"},
 {"title":"请求作业延期 · 致教授", "scene":"生病没写完 → 情况 + 原因 + 请求延期",
  "short":"Dear Professor Miller, I hope you are doing well. I am writing to ask for a short extension on the paper due this Friday. I have been sick with a fever for several days, so I could not finish it on time. Could you please give me two more days, until Monday? I would be very grateful for your understanding. Thank you very much. Best regards, [Your Name]",
  "zh":"亲爱的Miller教授，希望您一切都好。我写信是想申请把本周五截止的论文稍微延期。我已经发烧病了好几天，没能按时完成。能否请您多给我两天、延到周一？非常感谢您的理解。此致，[你的名字]",
  "en":"Dear Professor Miller, I hope this email finds you well. I am writing to request a short extension on the research paper that is due this Friday. Unfortunately, I have been ill with a high fever for the past few days and have not been able to concentrate on my work. I have already finished most of the reading, but I would need two more days to write and revise the paper properly. If possible, I would be very grateful if you could extend the deadline to next Monday. I promise to submit high-quality work, and I am happy to provide a doctor's note if you need one. Thank you very much for your understanding and support. Best regards, [Your Name]",
  "zh2":"亲爱的Miller教授，希望您一切都好。我写信是想申请把本周五截止的研究论文延期。很遗憾，过去几天我一直高烧，无法集中精力做功课。我已完成大部分阅读，但还需要两天时间好好撰写和修改论文。如果可以，能把截止日期延到下周一，我将非常感激。我保证提交高质量的作业，如需要我也可以提供医生证明。非常感谢您的理解与支持。此致，[你的名字]"},
 {"title":"图书馆噪音 · 投诉+建议", "scene":"自习区太吵 → 描述 + 影响备考 + 建议设静音区",
  "short":"Dear Library Manager, I hope you are doing well. I am writing because the main study area has become very noisy, as many students talk and take phone calls there. This makes it very hard for me to concentrate on my exams. Could you please create a silent zone where talking is not allowed? I would really appreciate it. Thank you for your time. Best regards, [Your Name]",
  "zh":"亲爱的图书馆管理员，希望您一切都好。我写信是因为主自习区变得很吵，很多学生在那里说话、打电话。这让我很难专心备考。能否请您设一个禁止说话的静音区？我将非常感激。感谢您的时间。此致，[你的名字]",
  "en":"Dear Library Manager, I hope you are doing well. I am writing to share a concern about the noise level in the main study area. Over the past few weeks, it has become very hard to concentrate because many students talk loudly and take phone calls at their desks. As someone who studies there almost every day, I find it difficult to prepare for my exams in such an environment. I would like to suggest creating a designated silent zone on the second floor, where talking is not allowed. I believe this small change would greatly improve the experience for students who need a quiet place to work. Thank you for considering my suggestion. Best regards, [Your Name]",
  "zh2":"亲爱的图书馆管理员，希望您一切都好。我写信是想反映主自习区的噪音问题。过去几周那里很难集中注意力，因为很多学生大声说话、在座位上打电话。作为几乎每天都在那学习的人，我发现在这样的环境里很难备考。我想建议在二楼设立一个专门的静音区、禁止说话。我相信这个小改变能大大改善需要安静环境的同学的体验。感谢您考虑我的建议。此致，[你的名字]"},
 {"title":"组队做小组作业 · 回复同学", "scene":"同学约做 project → 答应 + 分工 + 约时间",
  "short":"Hi Daniel, Thanks for your message about the group project. I would be happy to work with you on the presentation. I think we should choose a topic first and then split the research to save time. Are you free to meet this Thursday afternoon in the library? I will start looking for some sources before then. Looking forward to working together. Best, [Your Name]",
  "zh":"嗨Daniel，谢谢你发消息说小组项目的事。我很乐意和你一起做这个展示。我觉得我们应该先定个主题，然后分工查资料以节省时间。你这周四下午有空在图书馆见面吗？在那之前我会先找一些资料。期待和你合作。此致，[你的名字]",
  "en":"Hi Daniel, Thanks for reaching out about the group project. I would be happy to work with you on the marketing presentation. I think we should first decide on a topic together, and then split the research so that we can save time. I am free to meet this Thursday afternoon in the library, or we could talk over a video call if that works better for you. In the meantime, I will start looking for some useful sources and share them in our group chat. Please let me know which time suits you best. I am looking forward to working together and getting a great grade. Best, [Your Name]",
  "zh2":"嗨Daniel，谢谢你联系我说小组项目的事。我很乐意和你一起做这个市场营销展示。我觉得我们应先一起定一个主题，然后分工查资料，这样能省时间。我这周四下午有空在图书馆见面，或者你方便的话我们也可以视频聊。这期间我会先找一些有用的资料发到群里。请告诉我哪个时间最适合你。期待和你合作、拿个好成绩。此致，[你的名字]"},
 {"title":"请求换宿舍房间 · 致宿舍办公室", "scene":"室友作息差 → 说明 + 已沟通无效 + 请求换房",
  "short":"Dear Housing Office, I hope you are doing well. I am writing to ask for a room change next semester. My roommate often stays up late with the lights and music on, so I cannot sleep or study well. I have talked to him, but nothing has changed. Could you please move me to a quieter room? I would really appreciate it. Best regards, [Your Name]",
  "zh":"亲爱的宿舍办公室，希望您一切都好。我写信是想申请下学期换个房间。我室友经常熬夜、开着灯和音乐，我没法好好睡觉和学习。我已经和他谈过，但没有改变。能否请您把我换到一个更安静的房间？我将非常感激。此致，[你的名字]",
  "en":"Dear Housing Office, I hope you are having a good week. I am writing to request a change of dormitory room for the coming semester. My current roommate keeps very different hours from mine and often stays up late with the lights on and music playing, which makes it hard for me to sleep and study. I have tried to talk with him about it several times, but the situation has not improved. I would really appreciate it if you could move me to a quieter single room, or at least to a room with a roommate who has a similar schedule. Please let me know what options are available. Thank you very much for your help. Best regards, [Your Name]",
  "zh2":"亲爱的宿舍办公室，希望您这周过得愉快。我写信是想申请下学期更换宿舍房间。我目前的室友作息和我很不一样，经常熬夜、开着灯、放着音乐，让我很难睡觉和学习。我已试着和他谈过好几次，但情况没有改善。如果您能把我换到一个更安静的单人间，或至少换到作息相近的室友那里，我将非常感激。请告诉我有哪些可选方案。非常感谢您的帮助。此致，[你的名字]"},
 {"title":"错过课询问内容 · 致教授", "scene":"看病缺课 → 道歉 + 担心跟不上 + 求课件",
  "short":"Dear Professor Chen, I hope you are doing well. I am writing to apologize for missing your lecture yesterday, as I had a medical appointment I could not change. I am worried about falling behind on the topic we covered. Could you please tell me if the slides are online, or what I should read to catch up? Thank you very much. Best regards, [Your Name]",
  "zh":"亲爱的Chen教授，希望您一切都好。我写信是想为昨天缺席您的课道歉，因为我有一个无法改期的医疗预约。我担心跟不上我们讲的内容。能否请您告诉我课件是否在网上，或我该读些什么来补上？非常感谢。此致，[你的名字]",
  "en":"Dear Professor Chen, I hope you are doing well. I am writing to apologize for missing your lecture yesterday. I had a medical appointment that I could not reschedule, so I was unable to attend. I understand that we covered an important topic on data analysis, and I am worried about falling behind. Could you please let me know if the lecture slides are available online, or if there is any reading I should do to catch up? I would also be happy to come to your office hours this week if you have time to explain the key points. Thank you very much for your understanding. Best regards, [Your Name]",
  "zh2":"亲爱的Chen教授，希望您一切都好。我写信是想为昨天缺席您的课道歉。我有一个无法改期的医疗预约，所以没能来上课。我知道我们讲了一个关于数据分析的重要主题，我很担心跟不上。能否请您告诉我课件是否在网上，或有没有我该读的资料来补进度？如果您本周有时间，我也很乐意去您的答疑时间请您讲讲要点。非常感谢您的理解。此致，[你的名字]"},
 {"title":"账号登不上 · 致 IT 部门", "scene":"系统登不上 → 报问题 + 影响交作业 + 请求恢复",
  "short":"Dear IT Support Team, I hope you are doing well. I am writing because I cannot log into the online learning system, even though my password is correct. Because of this, I cannot open my course materials or submit my assignments on time. Could you please help me restore access as soon as possible? Thank you for your time. Best regards, [Your Name]",
  "zh":"亲爱的IT支持团队，希望你们一切都好。我写信是因为我登不上在线学习系统，尽管密码是对的。因此我打不开课程资料，也没法按时交作业。能否请你们帮我尽快恢复登录？感谢你们的时间。此致，[你的名字]",
  "en":"Dear IT Support Team, I hope this message finds you well. I am writing to report a problem with my student account. For the past three days, I have not been able to log into the online learning system, even though I am sure my password is correct. Every time I try, the page shows an error message and then freezes. Because of this, I cannot access my course materials or submit my assignments on time. I would be very grateful if you could look into this issue and help me restore access as soon as possible. Please let me know if you need any more information from me. Thank you for your time and assistance. Best regards, [Your Name]",
  "zh2":"亲爱的IT支持团队，希望这封邮件一切安好地送达。我写信是想报告我学生账号的一个问题。过去三天我一直无法登录在线学习系统，尽管我确定密码是对的。每次尝试，页面都会显示错误信息然后卡住。因此我无法访问课程资料，也没法按时提交作业。如果你们能调查这个问题、帮我尽快恢复登录，我将非常感激。如需我提供更多信息请告诉我。感谢你们的时间和帮助。此致，[你的名字]"},
]

EMAILS = [
 {"title":"公寓维修 · 第2次（63词·漏了请求句 Task3）", "score":"3.6 / 6 · 63 词", "date":"2026-08-22",
  "your":"Dear Mr. Thompson, I hope you are doing well. I am writing to bring your attention to the internet connection issues that I have noticed with the apartment. A few weeks ago, the Wi-Fi in the room has become slow and ofen disconnected, which affect my online studies heavily. For instance, I can not keep logging to online courses. Thank you. Best regards,",
  "missing":"🔴 这次漏了 Task3「请求」！你写到 For instance… 就没时间了，直接 Thank you 收尾，<b>缺了『请你安排维修』那句</b>——AI 判『缺失』。第1次漏影响、这次漏请求＝<b>根本问题是打不完、最后一个任务被掐掉</b>。解法＝用上面 60词保底版，请求句放前面别放最后。",
  "corrections":[
    {"wrong":"ofen","right":"often","why":"拼写：often。"},
    {"wrong":"which affect my online studies","right":"which affects my online studies","why":"which 指 Wi-Fi（单数），动词加 s：affects。"},
    {"wrong":"the Wi-Fi has become slow and ofen disconnected","right":"the Wi-Fi is slow and often disconnects","why":"并列谓语时态要统一；断线反复发生用一般现在时 disconnects。"},
    {"wrong":"I can not keep logging to online courses","right":"I cannot keep logging into online courses","why":"cannot 是一个词；log INTO（登录进）。"},
    {"wrong":"（题目是公寓 AC/墙问题，你写成了 Wi-Fi）","right":"看清题目给的具体问题再写","why":"这题是公寓空调/墙壁问题，别套上一题的网络内容。"}]},
 {"title":"公寓维修 · 第1次（漏了影响 Task2）", "score":"任务完成 3/5", "date":"2026-08-22",
  "your":"Dear Mr. Thompson, I hope you are doing well. I have moved into your apartment for a week, and noticed some issues, such as the airconditionar was broken and the wall was wet. It troubles me a lot. I am looking forward that you can make arrangements to address these issues. Thanks for very much for your time and assitance. Best regards,",
  "missing":"🔴 这次漏了 Task2「对学习的影响」。加上保底版第 3 句：These problems make it very hard for me to study at home.",
  "corrections":[
    {"wrong":"airconditionar","right":"air conditioner","why":"两个词、拼对。"},
    {"wrong":"assitance","right":"assistance","why":"a-ssist-ance。"},
    {"wrong":"Thanks for very much","right":"Thank you very much","why":"Thank you 不加 for。"},
    {"wrong":"I have moved … for a week","right":"I have been living … for a week","why":"move 瞬间动作不能持续一周。"},
    {"wrong":"looking forward that you can make arrangements","right":"look forward to you making arrangements","why":"look forward TO + doing。"}]},
]

FORMULA = [
 {"n":"① 开场（1句）","en":"Dear X, I hope you are doing well. I am writing about …","zh":"称呼 + 问候 + 一句点明来意"},
 {"n":"② 描述问题（1句）","en":"I am writing about two problems: [问题1] and [问题2].","zh":"任务1：把两个问题一句说清"},
 {"n":"③ 影响（1句·别漏）","en":"These problems make it very hard for me to study.","zh":"任务2：一句挂到『学习』——你第1次就漏这句"},
 {"n":"④ 请求（1句·绝不能省）","en":"I would really appreciate it if you could fix them soon.","zh":"任务3：一句请求——你第2次就漏这句。请求句放前面、别拖到最后被掐掉"},
 {"n":"⑤ 收尾（1句）","en":"Thank you for your time. Best regards, [Your Name]","zh":"感谢 + 落款"},
]

COMMON = [
 "🎯 <b>头号铁律：3 个任务一个不能少，尤其『请求句』和『影响句』</b>——你两次各漏一个。宁可每句短，也要 3 个任务全齐。",
 "🧮 <b>你能打 ~60 词就够了</b>：60 词写全 3 任务 = 完整；120 词漏一个任务 = 扣大分。先求完整、再求长。",
 "🔤 <b>拼写</b>：often（不是 ofen）、air conditioner、assistance、connection、cannot（一个词）。",
 "🔗 <b>搭配</b>：log INTO；look forward TO doing；Thank you 不加 for；which/it + 动词加 s（affects/disconnects）。",
 "📖 <b>看清题目</b>：写题目给的那个问题（公寓是空调/墙，别套成网络）。",
]

def modellib():
    out=[]
    for m in MODELS:
        out.append(f'''<div class="ml"><div class="ml-h"><b>{e(m["title"])}</b></div><div class="ml-s">{e(m["scene"])}</div>
<div class="ml-tag">🎯 保底版（~60词·打得完·先练这个）<button class="drill-btn" data-t="{e(m["short"])}">⌨️ 打这封</button> <button class="say drill-say" data-say="{e(m["short"])}">🔊</button></div>
<div class="ml-en short">{e(m["short"])}</div>
<div class="ml-zh">🇨🇳 {e(m["zh"])}</div>
<details class="ml-more"><summary>📈 进阶版（~120词·打字快了再上，含翻译）</summary>
<div class="ml-tag"><button class="drill-btn" data-t="{e(m["en"])}">⌨️ 打这封</button> <button class="say drill-say" data-say="{e(m["en"])}">🔊</button></div>
<div class="ml-en">{e(m["en"])}</div>
<div class="ml-zh">🇨🇳 {e(m["zh2"])}</div></details></div>''')
    return "".join(out)

def emailcards():
    out=[]
    for m in EMAILS:
        corr="".join(f'<div class="corr"><span class="c-x">✗ {e(c["wrong"])}</span><br><span class="c-r">✓ {e(c["right"])}</span><div class="c-w">{e(c["why"])}</div></div>' for c in m["corrections"])
        miss=f'<div class="miss">{m["missing"]}</div>' if m.get("missing") else ""
        out.append(f'''<details class="ecard"><summary><b>{e(m["title"])}</b> <span class="esc">{e(m["score"])}</span></summary>
<div class="ebody"><div class="mh">🎙 你写的</div><div class="ya say" data-say="{e(m["your"])}">{e(m["your"])}</div>{miss}
<div class="mh">🖊 逐处红笔改</div>{corr}</div></details>''')
    return "".join(out)

FORMHTML="".join(f'<div class="fs"><div class="fn">{e(x["n"])}</div><div class="fe say" data-say="{e(x["en"])}">{e(x["en"])}</div><div class="fz">{e(x["zh"])}</div></div>' for x in FORMULA)

HTML=f'''<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>邮件写作专题 · 保底版 + 翻译 + 打字</title><style>
:root{{--bg:#f6f3ed;--card:#fffdf9;--ink:#2c2620;--sub:#8a7f70;--accent:#c1662f;--core:#2f8f83;--line:#e7dfd2;--gold:#b8860b;--red:#c0453b;--green:#2f8f6a}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;line-height:1.65}}
header{{position:sticky;top:0;z-index:9;background:rgba(246,243,237,.97);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:12px 18px}}
h1{{margin:0 0 4px;font-size:18px}}.sub{{font-size:13px;color:var(--sub)}}.sub b{{color:var(--accent)}}
main{{max-width:900px;margin:0 auto;padding:16px 18px 70px}}
h2{{font-size:16.5px;margin:24px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--line)}}
.mh{{font-size:12.5px;color:var(--core);font-weight:700;margin:12px 0 5px}}
.strat{{background:#fff5ec;border:2px solid var(--accent);border-radius:14px;padding:13px 17px;font-size:14px}}.strat b{{color:var(--accent)}}
.formula{{display:grid;gap:7px;margin-top:6px}}
.fs{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 13px}}
.fn{{font-size:12.5px;color:var(--accent);font-weight:700}}.fe{{font-size:14.5px;cursor:pointer;margin:1px 0}}.fe:hover{{color:var(--core)}}.fz{{font-size:12.5px;color:var(--sub)}}
.trainer{{background:var(--card);border:2px solid var(--accent);border-radius:14px;padding:15px 18px}}
.tr-intro{{font-size:13.5px;margin-bottom:10px}}.tr-intro b{{color:var(--accent)}}
.tr-target{{background:#fbfaf6;border:1px solid var(--line);border-radius:10px;padding:12px 14px;font-size:16px;line-height:1.95;min-height:52px;letter-spacing:.2px}}
.tr-target .c-ok{{color:var(--green)}}.tr-target .c-bad{{color:#fff;background:var(--red);border-radius:2px}}.tr-target .c-cur{{background:#ffe08a;border-radius:2px}}
.tr-input{{width:100%;margin-top:9px;border:1px solid var(--line);border-radius:10px;padding:11px 13px;font-size:16px;font-family:inherit;min-height:100px;resize:vertical;background:#fff}}
.tr-stat{{display:flex;gap:16px;flex-wrap:wrap;margin-top:9px;font-size:13.5px}}
.tr-stat b{{font-size:18px;color:var(--accent)}}.tr-stat .best b{{color:var(--core)}}
.tr-bar{{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}}.tr-bar button{{border:1px solid var(--line);background:#fff;border-radius:16px;padding:5px 12px;font-size:12.5px;cursor:pointer}}
.tr-done{{background:#eef6f3;border:1px solid #bfe0d7;border-radius:9px;padding:9px 13px;margin-top:9px;font-size:14px;display:none}}
.drill-btn{{border:1px solid var(--accent);background:#fff5ec;color:var(--accent);border-radius:14px;padding:2px 11px;font-size:12.5px;cursor:pointer;font-weight:600}}
.drill-say{{border:none;background:none;cursor:pointer;font-size:14px}}
.ml{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 15px;margin:10px 0}}
.ml-h b{{font-size:14.5px}}.ml-s{{font-size:12.5px;color:var(--sub);margin:3px 0 8px}}
.ml-tag{{font-size:12.5px;color:var(--accent);font-weight:700;margin:8px 0 4px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.ml-en{{font-size:14.5px;line-height:1.85;background:#fbfaf6;border-radius:9px;padding:10px 13px}}
.ml-en.short{{border:1px solid #cfe3db;background:#f3faf7}}
.ml-zh{{font-size:13px;color:var(--sub);line-height:1.75;margin-top:6px;padding:0 3px}}
.ml-more{{margin-top:8px}}.ml-more>summary{{cursor:pointer;font-size:12.5px;color:var(--sub);font-weight:700}}
.ecard{{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:9px 0;overflow:hidden}}
.ecard>summary{{cursor:pointer;padding:11px 15px;list-style:none;font-size:14px}}.ecard>summary::-webkit-details-marker{{display:none}}
.ecard>summary::before{{content:"▸ ";color:var(--accent)}}.ecard[open]>summary::before{{content:"▾ "}}
.esc{{color:var(--accent);font-weight:700;font-size:12.5px}}
.ebody{{padding:0 15px 14px;border-top:1px solid var(--line)}}
.ya{{background:#fdf4f2;border:1px solid #ecc7c1;border-radius:10px;padding:11px 13px;font-size:14px;font-style:italic;color:#6b4a45;cursor:pointer}}
.miss{{background:#fbf4e9;border:1px solid #ecdcbf;border-radius:9px;padding:9px 13px;margin-top:9px;font-size:13.5px}}
.corr{{margin:7px 0;font-size:13.5px}}.c-x{{color:var(--red);text-decoration:line-through}}.c-r{{color:var(--green);font-weight:600}}.c-w{{font-size:12.5px;color:var(--sub);margin-top:2px}}
.common{{background:#fbf4e9;border:1px solid #ecdcbf;border-radius:12px;padding:12px 16px}}.common div{{margin:6px 0;font-size:13.5px}}.common b{{color:var(--red)}}
.tools{{position:fixed;right:14px;bottom:16px;z-index:20}}.tools button{{border:1px solid var(--line);background:var(--card);border-radius:20px;padding:8px 13px;font-size:13px;cursor:pointer}}
</style></head><body>
<header><h1>📧 邮件写作专题 · 先「打得完」再「打得快」</h1>
<div class="sub">实测：同一题两次都只打到 ~60 词、<b>最后一个任务被掐掉</b>。所以先用 <b>60 词保底完整版</b>（3 任务各一句、请求句绝不省）——写全 &gt; 写长。每封都带<b>中文翻译</b>。</div></header>
<main>
<h2>🎯 核心策略：60 词写全 3 个任务</h2>
<div class="strat">你能打的就 ~60 词，那就<b>把这 60 词用在刀刃上</b>：3 个任务各一句、句句短、请求句和影响句一个都不能少。<b>写完整的 60 词 &gt;&gt; 写不完的漂亮 120 词。</b>下面就是「60 词保底公式」：
<div class="formula">{FORMHTML}</div></div>

<h2>⌨️ 打字速度训练器</h2>
<div class="trainer">
<div class="tr-intro">下面每封都有 <b>🎯保底版(~60词)</b> 和 📈进阶版，都配了中文翻译。<b>先反复打保底版</b>——打到能在时间内打完 3 个任务。实时看 速度+准确率+用时。</div>
<div class="tr-target" id="tgt">👇 到下面点任意 ⌨️ 载入一封来打；先热身：I would really appreciate it if you could fix them soon.</div>
<textarea class="tr-input" id="inp" placeholder="照着上面一字一句地打…（打错标红）" spellcheck="false"></textarea>
<div class="tr-stat"><span>速度 <b id="wpm">0</b> WPM</span><span>准确率 <b id="acc">100</b>%</span><span>用时 <b id="tmr">0</b>s</span><span class="best">这封最佳 <b id="best">—</b> WPM</span></div>
<div class="tr-done" id="done"></div>
<div class="tr-bar"><button data-t="I would really appreciate it if you could fix them soon.">热身：请求句</button><button data-t="These problems make it very hard for me to study.">热身：影响句</button><button id="reset">↺ 重打这封</button></div>
</div>

<h2>📚 成品邮件（{len(MODELS)} 封 · 保底版+进阶版 · 全带中文翻译）</h2>
{modellib()}

<h2>📧 你的真题 + 红笔改</h2>
{emailcards()}

<h2>⚠️ 你的邮件通病</h2>
<div class="common">{"".join(f"<div>{c}</div>" for c in COMMON)}</div>
</main>
<div class="tools"><button id="rate">🐢 语速</button></div>
<script>
let voices=[],vi=0,rate=.95;
function lv(){{voices=speechSynthesis.getVoices().filter(v=>v.lang.startsWith("en"));const p=voices.findIndex(v=>/Samantha|Ava|Google US|United States/i.test(v.name));if(p>=0)vi=p;}}
lv();if(speechSynthesis.onvoiceschanged!==undefined)speechSynthesis.onvoiceschanged=lv;
function say(t){{if(!t)return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);if(voices[vi])u.voice=voices[vi];u.rate=rate;speechSynthesis.speak(u);}}
document.querySelectorAll(".say").forEach(el=>el.onclick=e=>{{e.stopPropagation();say(el.dataset.say);}});
const tgt=document.getElementById("tgt"),inp=document.getElementById("inp"),done=document.getElementById("done");
let target="I would really appreciate it if you could fix them soon.",startT=null,finished=false;
function bestKey(t){{return "email-wpm:"+t.slice(0,34);}}
function loadTarget(t){{target=t;startT=null;finished=false;inp.value="";done.style.display="none";render();inp.focus();
  const b=localStorage.getItem(bestKey(t));document.getElementById("best").textContent=b?b:"—";}}
function esc1(c){{return c==='<'?'&lt;':c==='>'?'&gt;':c==='&'?'&amp;':c;}}
function render(){{const typed=inp.value;let h="";
  for(let i=0;i<target.length;i++){{const c=target[i];const cls=i<typed.length?(typed[i]===c?"c-ok":"c-bad"):(i===typed.length?"c-cur":"");
    h+=cls?`<span class="${{cls}}">${{esc1(c)}}</span>`:esc1(c);}}tgt.innerHTML=h;}}
inp.oninput=()=>{{
  if(!startT&&inp.value.length)startT=Date.now();render();
  const typed=inp.value;let ok=0;for(let i=0;i<typed.length;i++)if(typed[i]===target[i])ok++;
  const secs=startT?(Date.now()-startT)/1000:0;
  const wpm=secs>0?Math.round((ok/5)/(secs/60)):0;const acc=typed.length?Math.round(ok/typed.length*100):100;
  document.getElementById("wpm").textContent=wpm;document.getElementById("acc").textContent=acc;document.getElementById("tmr").textContent=Math.round(secs);
  if(typed===target&&!finished){{finished=true;
    const b=localStorage.getItem(bestKey(target)),nb=(!b||wpm>+b);if(nb)localStorage.setItem(bestKey(target),wpm);
    document.getElementById("best").textContent=localStorage.getItem(bestKey(target));
    const words=target.split(/\\s+/).length;
    done.style.display="block";done.innerHTML=`✅ 打完 ${{words}} 词！速度 <b>${{wpm}} WPM</b> · 准确率 ${{acc}}% · 用时 ${{Math.round(secs)}}s${{nb?" · 🎉新纪录！":""}}<br><span style="font-size:12.5px;color:#8a7f70">保底版 ~60 词，目标＝在考试时间内稳稳打完 3 个任务。多打几遍成肌肉记忆。</span>`;
  }}
}};
document.querySelectorAll(".drill-btn,.tr-bar button[data-t]").forEach(b=>b.onclick=e=>{{e.stopPropagation();if(b.dataset.t){{loadTarget(b.dataset.t);document.querySelector('.trainer').scrollIntoView({{behavior:'smooth',block:'start'}});}}}});
document.getElementById("reset").onclick=()=>loadTarget(target);
document.getElementById("rate").onclick=function(){{rate=rate>=1.1?.7:rate+.2;this.textContent="🐢 "+rate.toFixed(1)+"x";say("speed");}};
render();
</script></body></html>'''

os.makedirs(OUT,exist_ok=True)
open(os.path.join(OUT,"邮件写作专题.html"),"w",encoding="utf-8").write(HTML)
print(f"✅ 邮件写作专题.html — 成品{len(MODELS)}封(保底+进阶·全带中文翻译) + 60词公式 + 真题红笔改{len(EMAILS)}次")
