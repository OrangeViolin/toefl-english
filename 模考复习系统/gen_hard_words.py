# -*- coding: utf-8 -*-
"""生成 hard_words.json：六级/托福「稍难」词形集合（含屈折），供 build_review.py 重点划线高亮。

数据源：绿皮书(green-book.json) + BEAT(beat-vocab.json) + 项目生词满配词(项目生词.json 里有 ety 的)
排除：四级以下基础词白名单(BASIC)
展开：常见屈折形式(复数/三单/过去式/现在分词/比较级)
用法：python3 gen_hard_words.py   （改完词库后重跑，再 rebuild 各复盘页）
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
BC = os.path.join(HERE, "..", "背词计划", "data")

# 四级以下基础词白名单（这些词不算「稍难」，不划线）
BASIC = set("""the a an is are was were be been being have has had do does did will would can could may might shall should must
i you he she it we they me him her us them my your his its our their this that these those
who whom whose which what when where why how all another any both each few more most other some such no nor not only
and but or so yet for nor of in to on at by with from about into over under above below between among through during before after
up down out off on again then once here there now just very too also well
one two three four five first second last next able about above across after again against almost along already also always among
amount animal another answer any around ask away back bad because become before begin behind best better between big body book
both boy bring brother build business but buy call came can car care carry case cause certain change child city class close come
company could country course day different do does done door down during each early earth east end enough even ever every example
eye face fact family far father feel few find first five follow food foot for form four free friend from full game get girl
give go good government great group grow half hand happen hard have head hear help here her high him home house how however
hundred idea important include information just keep kind know land large last late later learn leave left less let life light like
line little live long look lot low made main make man many may mean men might mile million mind miss money month more morning
most mother move much must name near need never new next night no north not note nothing now number off often old once one only
open or order other our out over own page paper part pay people person place plan play point put question quite read real right
river road room run said same say school sea second see seem sentence set several she should show side since small so some
something sometimes soon south speak state still story student study such take talk teach tell ten than that the their them then
there these they thing think third this those though thought three through time to today together too took top toward town tree
try turn two under until up us use used very want war water way we week well went were west what when where which while white
who whole why will wind with without woman word work world would write year yes yet you young
become became begins began bring brought build built buy bought come coming cost cut doing done drew draw drawn drink drove eat
ate eaten fall fell fallen feel felt find found fly flew flown forget forgot get got gotten give gave given go goes going gone
grow grew grown hear heard hold held keep kept know knew known lead led leave left let lie lay lain lose lost make made meet
met pay paid put read read run ran say said see saw seen sell sold send sent show showed shown sit sat sleep slept speak
spoke spoken spend spent stand stood swim swam take taken teach taught tell told think thought throw threw thrown understand
understood wear wore worn win won write wrote written
dutch english america american europe european netherlands indonesia italian french german chinese japanese""".split())


def infl(w):
    out = {w}
    if w.endswith("e"):
        out |= {w + "s", w + "d", w[:-1] + "ing"}
    else:
        out |= {w + "s", w + "ed", w + "ing"}
    if w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou":
        out.add(w[:-1] + "ies")
        out.add(w[:-1] + "ied")
    return out


def main():
    hard = set()
    for fn, key in [("green-book.json", "words"), ("beat-vocab.json", "words"), ("项目生词.json", "words")]:
        try:
            d = json.load(open(os.path.join(BC, fn), encoding="utf-8"))
        except Exception as e:
            print("⚠️ 跳过", fn, e)
            continue
        for w in d.get(key, []):
            if not isinstance(w, dict):
                continue
            word = w.get("word") or w.get("w")
            if not word:
                continue
            # 项目生词只收满配实词(有 ety)
            if fn == "项目生词.json" and not w.get("ety"):
                continue
            hard.add(word.lower())

    hard -= BASIC

    expanded = set(hard)
    for w in list(hard):
        expanded |= infl(w)

    out = os.path.join(HERE, "hard_words.json")
    json.dump(sorted(expanded), open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"✅ 生成 {out}\n   原形 {len(hard)} 词 · 含屈折 {len(expanded)} 词")


if __name__ == "__main__":
    main()
