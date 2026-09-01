# -*- coding: utf-8 -*-
"""背词联动：扫描所有模考 data 的生词 + 句型表达 → 满配汇入背词计划。
用法：python3 sync_vocab.py
1. 生词：各 data 的 vocab[] + wordbank[]（满配词），去重后汇入 wl1-10（主题组）。
2. 句型表达：从 data 的写作范文 / 口语面试范文 / 已提炼 frames 抽高频句型，汇入 wl11「🗣 句型表达」。
"""
import json, os, glob, re

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
BC = os.path.join(HERE, "..", "背词计划", "data", "项目生词.json")

def load_proj():
    return json.load(open(BC, encoding="utf-8"))

def save_proj(d):
    json.dump(d, open(BC, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def san(c):
    if not isinstance(c, dict): return None
    c.setdefault("w", "")
    ss = c.get("senses", []); out = []
    if isinstance(ss, list):
        for s in ss:
            if isinstance(s, str): s = {"gloss": s}
            if isinstance(s, dict): out.append(s)
    c["senses"] = out
    xs = c.get("xex", []); ox = []
    if isinstance(xs, list):
        for x in xs:
            if isinstance(x, dict) and x.get("en"): ox.append(x)
    c["xex"] = ox
    sy = c.get("syn", []); osy = []
    if isinstance(sy, list):
        for s in sy:
            if isinstance(s, str): s = {"w": s}
            if isinstance(s, dict) and s.get("w"): osy.append(s)
    c["syn"] = osy
    rf = c.get("rootfam", []); orf = []
    if isinstance(rf, list):
        for r in rf:
            if not isinstance(r, dict): continue
            ws = r.get("words", []); ow = []
            if isinstance(ws, list):
                for w in ws:
                    if isinstance(w, dict) and w.get("w"): ow.append(w)
            r["words"] = ow; orf.append(r)
    c["rootfam"] = orf
    return c

def topic_of(data_id, task_title=""):
    """按文件名/标题判主题组 wl（1-10）。"""
    s = data_id + " " + task_title
    if "阅读" in data_id:
        return 10  # 阅读填词题/阅读模考 → 阅读填词题组（或按标题细分）
    if "听力" in data_id:
        return 4   # 听力 → 地球海洋/自然科学（保守归通用，再按标题细分见下）
    return 9  # 默认通用学术

def classify_wl(data_id, task_title):
    # 精细主题判断（按任务标题关键词）
    t = task_title.lower()
    if any(k in t for k in ["art", "color", "pigment", "museum", "theatrical", "abstract", "craft", "decalcomania", "conducting"]):
        return 1  # 艺术
    if any(k in t for k in ["ecolog", "keystone", "biodiversity", "pollution", "bird", "migrat", "glacier", "ocean", "hydrolog", "atmospheric", "weather", "renewable", "climate"]):
        return 4  # 地球/海洋/生态
    if any(k in t for k in ["empire", "ancient", "archaeo", "mauryan", "kinship", "prehistoric", "history", "civiliz", "medieval", "roman"]):
        return 3  # 考古历史
    if any(k in t for k in ["microbiome", "sleep", "memory", "dolphin", "dinosaur", "insect", "social structures", "hierarchies", "baiji", "neuroscience", "serotonin", "pathogen"]):
        return 6  # 生物医学
    if any(k in t for k in ["canal", "engineering", "manufacturing", "lean", "turbine", "solar", "wind", "gps", "gis", "tech", "construction", "energy"]):
        return 5  # 材料科技工程
    if any(k in t for k in ["econom", "financial", "money", "purchase", "budget", "commercial", "trade", "marketing", "viral"]):
        return 7  # 经济社会
    if any(k in t for k in ["campus", "college", "course", "syllabus", "student", "dorm", "library", "crumpet", "fitness", "bookstore", "movie night"]):
        return 8  # 校园生活
    return 9  # 通用学术

def sync_words():
    proj = load_proj()
    existing = {w["word"].lower() for w in proj["words"]}
    maxidx = {}
    for w in proj["words"]:
        maxidx[w["wl"]] = max(maxidx.get(w["wl"], 0), w.get("index", 0))

    def to_entry(c, wl, src):
        memory = c.get("core", "")
        if c.get("senses"):
            gl = "；".join(x.get("gloss", "") for x in c["senses"] if x.get("gloss"))
            if gl:
                memory = (memory + " ｜ " + gl) if memory else gl
        e = {"word": c["w"], "pronunciation": c.get("ipa", ""), "definition": c.get("zh", ""),
             "memory": memory, "collocations": "", "examples": "",
             "ety": c.get("ety", ""), "ph": c.get("ph", ""), "tip": c.get("tip", ""),
             "xex": c.get("xex", []), "syn": c.get("syn", []), "ant": c.get("ant", []),
             "nu": c.get("nu", ""), "src_from": src, "wl": wl}
        if c.get("src_sent"):
            e["src_sent"] = c["src_sent"]
        return e

    added = 0
    for f in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        if "scores" not in d:
            continue
        data_id = os.path.basename(f)[:-5]
        for s in d.get("sections", []):
            for t in s.get("tasks", []):
                wl = classify_wl(data_id, t.get("title", ""))
                src = "模考·" + data_id
                for v in t.get("vocab", []):
                    c = san(v)
                    if not c or not c.get("w"): continue
                    lw = c["w"].lower()
                    if lw in existing: continue
                    existing.add(lw)
                    maxidx[wl] = maxidx.get(wl, 0) + 1
                    e = to_entry(c, wl, src)
                    e["index"] = maxidx[wl]; e["id"] = f"PJ{wl:02d}-{maxidx[wl]:03d}"
                    proj["words"].append(e); added += 1
    return proj, added

# ============ 句型表达（wl11）============
# 从写作范文/口语范文里提炼的「高频万能句型」，第一版手工精选（高价值，不自动乱抽）
EXPRESSIONS = {
 "writing": [
  {"word": "I am writing to ask about", "zh": "（邮件开头）我写信想询问…", "xex": [{"en":"I am writing to ask about the class schedule.", "zh":"我写信想询问课程安排。","src":"造句"}]},
  {"word": "I would be very grateful if you could", "zh": "（请求）如果您能…我将非常感激", "xex": [{"en":"I would be very grateful if you could help me.", "zh":"如果您能帮我，我将非常感激。","src":"造句"}]},
  {"word": "Could you please let me know", "zh": "（询问）能否请您告知…", "xex": [{"en":"Could you please let me know how to register?", "zh":"能否请您告知如何注册？","src":"造句"}]},
  {"word": "I am writing to share", "zh": "（邮件开头）我写信想分享…", "xex": [{"en":"I am writing to share some interesting destinations.", "zh":"我写信想分享一些有趣的目的地。","src":"造句"}]},
  {"word": "While I acknowledge", "zh": "（讨论让步）虽然我承认…", "xex": [{"en":"While I acknowledge Paul's point, I believe VR is valuable.", "zh":"虽然我承认 Paul 的观点，但我认为 VR 有价值。","src":"造句"}]},
  {"word": "For instance,", "zh": "（举例）例如，", "xex": [{"en":"For instance, chemistry students could perform experiments in a virtual lab.", "zh":"例如，化学学生可以在虚拟实验室做实验。","src":"造句"}]},
  {"word": "in the long run", "zh": "从长远看", "xex": [{"en":"Investing in VR is beneficial in the long run.", "zh":"从长远看，投资 VR 是有益的。","src":"造句"}]},
  {"word": "take ownership of", "zh": "主导，掌握…的主动权", "xex": [{"en":"Students take ownership of their learning.", "zh":"学生主导自己的学习。","src":"造句"}]},
 ],
 "speaking": [
  {"word": "First off,", "zh": "（面试理由一）首先，", "xex": [{"en":"First off, it helps me build confidence.", "zh":"首先，它帮我建立自信。","src":"造句"}]},
  {"word": "This is because", "zh": "（解释原因）这是因为", "xex": [{"en":"This is because reaching a goal makes me proud.", "zh":"这是因为达成目标让我自豪。","src":"造句"}]},
  {"word": "Besides,", "zh": "（面试理由二）此外，", "xex": [{"en":"Besides, it teaches me a good habit.", "zh":"此外，它教我一个好习惯。","src":"造句"}]},
  {"word": "For example,", "zh": "（举例）例如，", "xex": [{"en":"For example, I set a goal to run every weekend.", "zh":"例如，我定了个每周末跑步的目标。","src":"造句"}]},
  {"word": "Therefore,", "zh": "（收尾）因此，", "xex": [{"en":"Therefore, goals help me grow.", "zh":"因此，目标帮我成长。","src":"造句"}]},
 ],
 "reading": [
  {"word": "not only ... but also", "zh": "（并列递进）不仅…而且", "xex": [{"en":"Kinship not only structured families but also shaped labor.", "zh":"亲缘不仅构建家庭，也塑造劳动分工。","src":"造句"}]},
  {"word": "in contrast", "zh": "相比之下，与此相反", "xex": [{"en":"In contrast, green roofs keep buildings cooler.", "zh":"相比之下，绿屋顶让建筑更凉。","src":"造句"}]},
 ],
 "listening": [
  {"word": "a variety of", "zh": "各种各样的", "xex": [{"en":"Birds use a variety of navigational cues.", "zh":"鸟类使用各种各样的导航线索。","src":"造句"}]},
  {"word": "in particular", "zh": "尤其是，特别是", "xex": [{"en":"Many mammals, in particular primates, show complex behavior.", "zh":"许多哺乳动物，尤其是灵长类，表现出复杂行为。","src":"造句"}]},
 ],
}

def sync_expressions():
    proj, _ = sync_words()  # 先确保词已汇入，再追加句型（proj 已含新词）
    existing = {w["word"].lower() for w in proj["words"]}
    # 确保 wl11 分组存在
    proj.setdefault("wordLists", {})
    proj["wordLists"].setdefault("11", {"name": "🗣 句型表达", "count": 0})
    maxidx = {}
    for w in proj["words"]:
        maxidx[w["wl"]] = max(maxidx.get(w["wl"], 0), w.get("index", 0))

    added = 0
    for mod, items in EXPRESSIONS.items():
        for it in items:
            lw = it["word"].lower()
            if lw in existing: continue
            existing.add(lw)
            maxidx[11] = maxidx.get(11, 0) + 1
            e = {"word": it["word"], "pronunciation": "", "definition": it["zh"],
                 "memory": "", "collocations": "", "examples": "",
                 "ety": "", "ph": "", "tip": "",
                 "xex": it.get("xex", []), "syn": [], "ant": [], "nu": "",
                 "src_from": "句型·" + {"writing":"写作","speaking":"口语","reading":"阅读","listening":"听力"}[mod],
                 "wl": 11, "index": maxidx[11], "id": f"PJ11-{maxidx[11]:03d}"}
            proj["words"].append(e); added += 1
    return proj, added

if __name__ == "__main__":
    proj, added_words = sync_words()
    save_proj(proj)
    proj, added_expr = sync_expressions()
    proj["words"].sort(key=lambda w: (w["wl"], w["index"]))
    from collections import Counter
    cnt = Counter(w["wl"] for w in proj["words"])
    for k, v in proj["wordLists"].items():
        v["count"] = cnt.get(int(k), 0)
    proj["total"] = len(proj["words"])
    save_proj(proj)
    print(f"✅ 生词汇入 {added_words} · 句型表达 {added_expr} · 总 {proj['total']}")
    print("   wl11 句型表达:", cnt.get(11, 0))
