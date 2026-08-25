// 面试真题库（Take an Interview） —— 面试问答.html 读取本文件渲染
// 一个「真题」= 一个 item，可含 1 道或多道题（真考一场 = 4 题）。
// ⚠️ 工作流（Fish 2026-08-20）：cc 不自撰，润色考拉考拉系统给的范文 → 极简大白话 + ~80词。
// 每题给两个版本供练习：① 单理由 5 步 Well→First off→This is because→Like→So；② 两理由(再加 Also+一段)。
// 双版本字段：outline/model/words = 单理由；outline2/model2/words2 = 两理由（面试问答.html 两块都渲染）。
// 每道题 question 结构：
//   q       题目原文
//   outline 思路：观点 / 理由(唯一) / 展开(bullets：为什么 + 一个例子)
//   model   范文 5 句：{mk:引导词, role:结构名, en:句子}
//   words   范文词数(目标 ≤70)
//   frames  框架表达：{t:表达, zh:用法}   vocab 单词/搭配：{w, ipa, zh}
window.INTERVIEW_BANK = [
  {
    "id": "financial-planning",
    "title": "理财规划 Financial Planning",
    "topic": "生活观点",
    "questions": [
      {
        "q": "Do you think detailed financial planning is important? Why or why not?",
        "outline": [
          {
            "role": "观点",
            "text": "Yes, it really matters"
          },
          {
            "role": "理由（唯一）",
            "text": "It helps me spend and save money way more wisely"
          },
          {
            "role": "展开",
            "bullets": [
              "When I see where my money goes, I stop wasting it",
              "I can cut the useless stuff and grow my savings",
              "例子：Tracking a coffee habit saved me real money"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I think detailed financial planning really matters."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it helps me spend and save my money way more wisely."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "once I write everything down, I can clearly see where my money goes and cut the useless stuff."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "last year I tracked my daily coffee, realized I was overspending, and saved a lot."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "a clear plan just keeps me in control."
          }
        ],
        "words": 68,
        "frames": [
          {
            "t": "Well, honestly, I think…",
            "zh": "表态"
          },
          {
            "t": "First off,…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like,…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So,…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "financial planning",
            "ipa": "/faɪˈnænʃəl ˈplænɪŋ/",
            "zh": "财务规划"
          },
          {
            "w": "wisely",
            "ipa": "/ˈwaɪzli/",
            "zh": "明智地"
          },
          {
            "w": "cut the useless stuff",
            "ipa": "/kʌt ðə ˈjuːsləs stʌf/",
            "zh": "砍掉没用的开销"
          },
          {
            "w": "overspend",
            "ipa": "/ˌoʊvərˈspend/",
            "zh": "超额花费"
          },
          {
            "w": "in control",
            "ipa": "/ɪn kənˈtroʊl/",
            "zh": "掌控之中"
          }
        ]
      }
    ]
  },
  {
    "id": "mock-home-office-2026-08-20",
    "title": "本场模考 · 在家 vs 办公室（每题①单理由/②两理由）",
    "topic": "工作/生活观点 · 4题一套",
    "questions": [
      {
        "q": "Tell me about your current work or study routine. Do you mostly do your tasks at home or in an office or classroom?",
        "outline": [
          {
            "role": "观点",
            "text": "I mostly do my tasks at home."
          },
          {
            "role": "理由（唯一）",
            "text": "It saves me a lot of time and energy."
          },
          {
            "role": "展开",
            "bullets": [
              "I don't have a two-hour commute anymore",
              "I use that time to rest or start work early",
              "例子：I sleep a bit more and feel less tired"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I do most of my work and study at home these days."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "the main reason is that it saves me a lot of time and energy."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "I used to spend two hours a day on a crowded bus, and it was really tiring."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "now I use that extra time to sleep a bit more or start my work early."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "staying at home makes my whole day easier and more efficient."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "I prefer doing my tasks at home."
          },
          {
            "role": "理由一",
            "text": "It saves time and energy (no commute)."
          },
          {
            "role": "展开",
            "bullets": [
              "No two-hour bus ride every day",
              "I use that time to rest or start early"
            ]
          },
          {
            "role": "理由二",
            "text": "I love the freedom to control my own space."
          },
          {
            "role": "展开",
            "bullets": [
              "I can set the noise and the temperature",
              "so I feel comfortable and focus better"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I really prefer doing my work and study at home."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "it saves me a lot of time and energy, because I don't have to commute two hours every day."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "now I use that time to rest or start my tasks early."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "I really like the freedom I have at home."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "I can control my own space, like the noise and the temperature, so I focus better."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "for me, working at home is more comfortable and more efficient."
          }
        ],
        "frames": [
          {
            "t": "I do most of my … at home",
            "zh": "我大部分……都在家做"
          },
          {
            "t": "the main reason is that it saves me …",
            "zh": "主要原因是它帮我省了……"
          },
          {
            "t": "This is because I used to …",
            "zh": "这是因为我以前……"
          },
          {
            "t": "Like, now I use that time to …",
            "zh": "比如，现在我用那段时间去……"
          },
          {
            "t": "Also, I like the freedom to …（两理由版）",
            "zh": "另外，我喜欢……的自由"
          }
        ],
        "vocab": [
          {
            "w": "commute",
            "ipa": "/kəˈmjuːt/",
            "zh": "通勤"
          },
          {
            "w": "energy",
            "ipa": "/ˈenərdʒi/",
            "zh": "精力"
          },
          {
            "w": "tiring",
            "ipa": "/ˈtaɪərɪŋ/",
            "zh": "累人的"
          },
          {
            "w": "efficient",
            "ipa": "/ɪˈfɪʃnt/",
            "zh": "高效的"
          },
          {
            "w": "freedom",
            "ipa": "/ˈfriːdəm/",
            "zh": "自由"
          }
        ],
        "words": 79,
        "words2": 87
      },
      {
        "q": "Do you prefer working from home or going to a specific place like an office? Why?",
        "outline": [
          {
            "role": "观点",
            "text": "I prefer working from home."
          },
          {
            "role": "理由（唯一）",
            "text": "It saves me about two hours of commuting every day."
          },
          {
            "role": "展开",
            "bullets": [
              "No crowded bus, so I feel less tired and stressed",
              "I use that time to sleep or eat a good breakfast",
              "例子：I start work with much more energy"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I'd much rather work from home than go to an office."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "the main reason is that I save about two hours of commuting every day."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "I don't have to sit on a crowded bus, so I feel less tired and stressed."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I use that time to sleep more or eat a good breakfast, so I start work with more energy."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "working from home is just the better and more relaxing choice for me."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "I prefer working from home."
          },
          {
            "role": "理由一",
            "text": "It saves about two hours of commuting."
          },
          {
            "role": "展开",
            "bullets": [
              "No crowded bus every morning",
              "I use that time to sleep or make breakfast"
            ]
          },
          {
            "role": "理由二",
            "text": "A comfortable place keeps me relaxed all day."
          },
          {
            "role": "展开",
            "bullets": [
              "I can control everything around me",
              "I never feel rushed"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I'd rather work from home."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I save about two hours every day, because I don't have to commute on a crowded bus."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I use that time to sleep more or make a healthy breakfast, so I feel fresh."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "being in a comfortable place keeps me relaxed all day."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "at home I can control everything around me, and I never feel rushed."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "working from home is more efficient and less stressful for me."
          }
        ],
        "frames": [
          {
            "t": "I'd much rather … than …",
            "zh": "我宁愿……而不是……"
          },
          {
            "t": "the main reason is that I save …",
            "zh": "主要原因是我省下了……"
          },
          {
            "t": "so I feel less tired and stressed",
            "zh": "所以我没那么累、没那么有压力"
          },
          {
            "t": "Like, I use that time to …",
            "zh": "比如，我用那段时间去……"
          },
          {
            "t": "Also, being in a comfortable place …（两理由版）",
            "zh": "另外，待在舒服的地方……"
          }
        ],
        "vocab": [
          {
            "w": "commute",
            "ipa": "/kəˈmjuːt/",
            "zh": "通勤"
          },
          {
            "w": "crowded",
            "ipa": "/ˈkraʊdɪd/",
            "zh": "拥挤的"
          },
          {
            "w": "stressed",
            "ipa": "/strest/",
            "zh": "有压力的"
          },
          {
            "w": "energy",
            "ipa": "/ˈenərdʒi/",
            "zh": "精力"
          },
          {
            "w": "comfortable",
            "ipa": "/ˈkʌmftəbl/",
            "zh": "舒适的"
          }
        ],
        "words": 82,
        "words2": 82
      },
      {
        "q": "Do you think office work helps people feel less lonely? Why or why not?",
        "outline": [
          {
            "role": "观点",
            "text": "Yes, office work helps people feel less lonely."
          },
          {
            "role": "理由（唯一）",
            "text": "You can chat with your coworkers face to face all day."
          },
          {
            "role": "展开",
            "bullets": [
              "Quick, easy talks make you feel connected",
              "They break up the boring parts of work",
              "例子：you laugh with a coworker while making coffee"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I agree that working in an office helps people feel less lonely."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "the main reason is that you can chat with your coworkers face to face all day."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "these quick, easy talks break up the boring parts of work and make you feel connected."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "you might meet a coworker while making coffee and laugh about your weekend for a few minutes."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "being around people at the office really makes you feel less alone."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "Yes, office work helps people feel less lonely."
          },
          {
            "role": "理由一",
            "text": "You can chat face to face all day."
          },
          {
            "role": "展开",
            "bullets": [
              "Quick talks break up the boring parts of work",
              "例子：laugh with a coworker while making coffee"
            ]
          },
          {
            "role": "理由二",
            "text": "Having lunch with your team makes a big difference."
          },
          {
            "role": "展开",
            "bullets": [
              "Instead of eating alone, you share a meal",
              "So you feel like part of a group"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I think working in an office helps people feel less lonely."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "you can chat with coworkers face to face all day, which breaks up the boring parts of work."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "you might run into someone while making coffee and laugh together for a few minutes."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "having lunch with your team makes a big difference."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "instead of eating alone, you sit together and share a meal, so you feel like part of a group."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "the office really helps you make friends and feel happy."
          }
        ],
        "frames": [
          {
            "t": "I agree that … helps people feel less lonely",
            "zh": "我同意……让人不那么孤单"
          },
          {
            "t": "chat with your coworkers face to face",
            "zh": "和同事面对面聊天"
          },
          {
            "t": "break up the boring parts of work",
            "zh": "打破工作里沉闷的部分"
          },
          {
            "t": "Like, you might meet a coworker while …",
            "zh": "比如你可能在……的时候遇到同事"
          },
          {
            "t": "Also, having lunch with your team …（两理由版）",
            "zh": "另外，和团队一起吃午饭……"
          }
        ],
        "vocab": [
          {
            "w": "coworker",
            "ipa": "/ˈkoʊwɜːrkər/",
            "zh": "同事"
          },
          {
            "w": "face to face",
            "ipa": "/ˌfeɪs tə ˈfeɪs/",
            "zh": "面对面地"
          },
          {
            "w": "lonely",
            "ipa": "/ˈloʊnli/",
            "zh": "孤独的"
          },
          {
            "w": "chat",
            "ipa": "/tʃæt/",
            "zh": "闲聊"
          },
          {
            "w": "group",
            "ipa": "/ɡruːp/",
            "zh": "群体，团队"
          }
        ],
        "words": 82,
        "words2": 92
      },
      {
        "q": "Some people think employees are more productive at home. Others say they work harder in an office where managers can see them. Which view do you agree with? Why or why not?",
        "outline": [
          {
            "role": "观点",
            "text": "I think people are more productive at home."
          },
          {
            "role": "理由（唯一）",
            "text": "They don't have a long, tiring commute every morning."
          },
          {
            "role": "展开",
            "bullets": [
              "A crowded subway drains your energy before you start",
              "At home you can rest or eat a good breakfast",
              "例子：you begin work feeling fresh and ready"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I think people are more productive when they work from home."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "the main reason is that they don't have a long, tiring commute every morning."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "sitting on a crowded subway for two hours drains your energy before you even start."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when you stay home, you can rest or have a good breakfast, so you begin work feeling fresh."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "working from home really helps people focus and get more done."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "I think people work better at home."
          },
          {
            "role": "理由一",
            "text": "They don't have a long, tiring commute."
          },
          {
            "role": "展开",
            "bullets": [
              "No two hours on a crowded subway",
              "They rest or eat a good breakfast, so they feel fresh"
            ]
          },
          {
            "role": "理由二",
            "text": "A quiet home is better than a noisy office."
          },
          {
            "role": "展开",
            "bullets": [
              "Even if no one is watching, they focus more",
              "They feel calm and comfortable"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I believe people work better at home."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "they don't have a long, tiring commute, so they start the day with more energy."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "instead of two hours on a crowded subway, they can rest or eat a healthy breakfast."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "a quiet home is often better than a noisy office."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "even if no one is watching, people focus more when they feel calm and comfortable."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "working from home actually helps people get more done."
          }
        ],
        "frames": [
          {
            "t": "people are more productive when they …",
            "zh": "人们在……时更高效"
          },
          {
            "t": "the main reason is that they don't have …",
            "zh": "主要原因是他们不用……"
          },
          {
            "t": "drains your energy before you even start",
            "zh": "还没开始就把精力耗光了"
          },
          {
            "t": "Like, when you stay home, you can …",
            "zh": "比如，待在家你就能……"
          },
          {
            "t": "Also, a quiet home is better than a noisy office（两理由版）",
            "zh": "另外，安静的家比吵闹的办公室好"
          }
        ],
        "vocab": [
          {
            "w": "productive",
            "ipa": "/prəˈdʌktɪv/",
            "zh": "高效的"
          },
          {
            "w": "commute",
            "ipa": "/kəˈmjuːt/",
            "zh": "通勤"
          },
          {
            "w": "drain",
            "ipa": "/dreɪn/",
            "zh": "耗尽"
          },
          {
            "w": "fresh",
            "ipa": "/freʃ/",
            "zh": "精神饱满的"
          },
          {
            "w": "focus",
            "ipa": "/ˈfoʊkəs/",
            "zh": "专注"
          }
        ],
        "words": 78,
        "words2": 82
      }
    ]
  },
  {
    "id": "starter-pack",
    "title": "高频面试练习 · 启动 6 题",
    "topic": "综合高频（个人+社会）",
    "questions": [
      {
        "q": "Do you prefer studying alone or studying with a group? Why?",
        "outline": [
          {
            "role": "观点",
            "text": "I prefer studying alone"
          },
          {
            "role": "理由（唯一）",
            "text": "I can fully focus and go at my own pace"
          },
          {
            "role": "展开",
            "bullets": [
              "No distractions, so my mind stays on one thing",
              "I can slow down on hard parts and skip what I know",
              "例子：I mastered a tough math chapter in one quiet night"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I definitely prefer studying alone."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it lets me fully focus and move at my own pace."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "nobody's distracting me, so I slow down on hard parts and skip what I know."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "last week I finally cracked a tough math chapter in one quiet night."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "studying alone just works way better for me."
          }
        ],
        "words": 61,
        "frames": [
          {
            "t": "Well, honestly, I think…",
            "zh": "表态"
          },
          {
            "t": "First off,…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like,…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So,…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "fully focus",
            "ipa": "/ˈfʊli ˈfoʊkəs/",
            "zh": "完全专注"
          },
          {
            "w": "at my own pace",
            "ipa": "/æt maɪ oʊn peɪs/",
            "zh": "按自己的节奏"
          },
          {
            "w": "distracting",
            "ipa": "/dɪˈstræktɪŋ/",
            "zh": "使分心的"
          },
          {
            "w": "tricky",
            "ipa": "/ˈtrɪki/",
            "zh": "棘手的"
          },
          {
            "w": "crack a chapter",
            "ipa": "/kræk ə ˈtʃæptər/",
            "zh": "攻克一章"
          }
        ]
      },
      {
        "q": "Describe a skill you have learned recently and explain why it is useful to you.",
        "outline": [
          {
            "role": "观点",
            "text": "recently picked up basic cooking"
          },
          {
            "role": "理由（唯一）",
            "text": "it saves me a lot of money"
          },
          {
            "role": "展开",
            "bullets": [
              "eating out every day is expensive",
              "home-cooked meals cost far less",
              "例子：cooking my own lunch cut my weekly food bill in half"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, the skill I picked up recently is basic cooking."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "the main reason it's useful is it saves me a lot of money."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "eating out every day really adds up, while cooking at home costs way less."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "once I made my own lunch, my weekly food bill dropped by half."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that's why learning to cook is so useful."
          }
        ],
        "words": 66,
        "frames": [
          {
            "t": "Well, honestly, the skill I picked up recently is…",
            "zh": "表态+点出技能"
          },
          {
            "t": "First off, the main reason it's useful is…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like, once I started…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So, that's why…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "pick up (a skill)",
            "ipa": "/pɪk ʌp/",
            "zh": "（无意中）学会、掌握"
          },
          {
            "w": "basic cooking",
            "ipa": "/ˈbeɪsɪk ˈkʊkɪŋ/",
            "zh": "基础烹饪"
          },
          {
            "w": "add up",
            "ipa": "/æd ʌp/",
            "zh": "（费用）越攒越多"
          },
          {
            "w": "food bill",
            "ipa": "/fuːd bɪl/",
            "zh": "伙食开销"
          },
          {
            "w": "drop by half",
            "ipa": "/drɒp baɪ hɑːf/",
            "zh": "减少一半"
          }
        ]
      },
      {
        "q": "Some people say smartphones make people less social. Do you agree? Why or why not?",
        "outline": [
          {
            "role": "观点",
            "text": "I totally agree smartphones make us less social"
          },
          {
            "role": "理由（唯一）",
            "text": "people keep staring down at their phones and ignore the real people around them"
          },
          {
            "role": "展开",
            "bullets": [
              "screens are so addictive that we forget who's beside us",
              "we miss real conversations and eye contact",
              "例子：at dinner everyone scrolls instead of talking"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I totally agree that smartphones make people less social."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "people keep staring down at their phones and ignore the people around them."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "screens are so addictive that we forget who's right next to us."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "at dinner, my friends and I all scroll instead of talking to each other."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "yeah, phones really do pull us apart in person."
          }
        ],
        "words": 66,
        "frames": [
          {
            "t": "Well, honestly, I totally agree that…",
            "zh": "表态"
          },
          {
            "t": "First off,…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like,…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So,…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "less social",
            "ipa": "/les ˈsoʊʃəl/",
            "zh": "更不合群、更少社交"
          },
          {
            "w": "stare down at",
            "ipa": "/ster daʊn æt/",
            "zh": "低头盯着看"
          },
          {
            "w": "ignore",
            "ipa": "/ɪɡˈnɔːr/",
            "zh": "忽略、不理会"
          },
          {
            "w": "addictive",
            "ipa": "/əˈdɪktɪv/",
            "zh": "让人上瘾的"
          },
          {
            "w": "scroll",
            "ipa": "/skroʊl/",
            "zh": "刷、滑动屏幕"
          }
        ]
      },
      {
        "q": "Do you think students should be required to take physical education (PE) classes? Why or why not?",
        "outline": [
          {
            "role": "观点",
            "text": "Yes, PE should be required"
          },
          {
            "role": "理由（唯一）",
            "text": "It keeps students physically healthy"
          },
          {
            "role": "展开",
            "bullets": [
              "Students sit almost all day in class",
              "Regular movement fights that and builds fitness",
              "例子：One PE session finally gets them running and active"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I think students should be required to take PE classes."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it keeps them physically healthy."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "we sit at a desk all day, and our bodies need real movement to stay fit."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "after six hours of sitting, one PE class finally gets me running and energized."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "a required PE class keeps everyone healthy."
          }
        ],
        "words": 61,
        "frames": [
          {
            "t": "Well, honestly, I think…",
            "zh": "表态"
          },
          {
            "t": "First off,…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like,…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So,…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "physical education (PE)",
            "ipa": "/ˈfɪzɪkl ˌedʒuˈkeɪʃn/",
            "zh": "体育课"
          },
          {
            "w": "physically healthy",
            "ipa": "/ˈfɪzɪkli ˈhelθi/",
            "zh": "身体健康"
          },
          {
            "w": "sit at a desk",
            "ipa": "/sɪt æt ə desk/",
            "zh": "坐在书桌前"
          },
          {
            "w": "stay fit",
            "ipa": "/steɪ fɪt/",
            "zh": "保持健康强壮"
          },
          {
            "w": "energized",
            "ipa": "/ˈenərdʒaɪzd/",
            "zh": "充满活力的"
          }
        ]
      },
      {
        "q": "Do you prefer shopping online or shopping in physical stores? Why?",
        "outline": [
          {
            "role": "观点",
            "text": "I definitely prefer shopping online"
          },
          {
            "role": "理由（唯一）",
            "text": "it's way more convenient and saves me a ton of time"
          },
          {
            "role": "展开",
            "bullets": [
              "I can browse and buy anything from my phone anytime",
              "I don't have to travel, park, or wait in long lines",
              "例子：last week I ordered groceries in bed and they arrived next morning"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I'd go with shopping online any day."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it's just so much more convenient and saves me a ton of time."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "I can buy almost anything from my phone, without traveling or waiting in long lines."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "last week I ordered groceries in bed, and they arrived the next morning."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "online shopping just fits my busy life way better."
          }
        ],
        "words": 66,
        "frames": [
          {
            "t": "Well, honestly, I'd go with…",
            "zh": "表态"
          },
          {
            "t": "First off,…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like,…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So,…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "convenient",
            "ipa": "/kənˈviːniənt/",
            "zh": "方便的"
          },
          {
            "w": "save time",
            "ipa": "/seɪv taɪm/",
            "zh": "省时间"
          },
          {
            "w": "browse",
            "ipa": "/braʊz/",
            "zh": "浏览（商品）"
          },
          {
            "w": "wait in long lines",
            "ipa": "/weɪt ɪn lɔːŋ laɪnz/",
            "zh": "排长队"
          },
          {
            "w": "show up",
            "ipa": "/ʃoʊ ʌp/",
            "zh": "出现；送达"
          }
        ]
      },
      {
        "q": "Some people argue that social media does more harm than good. What is your opinion?",
        "outline": [
          {
            "role": "观点",
            "text": "I think it does more harm than good"
          },
          {
            "role": "理由（唯一）",
            "text": "It hurts our mental health"
          },
          {
            "role": "展开",
            "bullets": [
              "We constantly compare our real lives to others' highlights",
              "This comparison quietly makes us anxious and unhappy",
              "例子：a friend felt worthless after scrolling perfect posts"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "honestly, I think social media does way more harm than good."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it really hurts our mental health."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "we keep comparing our real lives to everyone else's perfect posts, so we feel anxious."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "a friend of mine felt worthless after scrolling through people's perfect vacations for hours."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "to me, that harm to our minds outweighs the fun."
          }
        ],
        "words": 64,
        "frames": [
          {
            "t": "Well, honestly, I think…",
            "zh": "表态"
          },
          {
            "t": "First off,…",
            "zh": "给出唯一理由"
          },
          {
            "t": "This is because…",
            "zh": "解释为什么"
          },
          {
            "t": "Like,…",
            "zh": "举一个具体例子"
          },
          {
            "t": "So,…",
            "zh": "小结回扣观点"
          }
        ],
        "vocab": [
          {
            "w": "do more harm than good",
            "ipa": "/duː mɔːr hɑːrm ðæn ɡʊd/",
            "zh": "弊大于利"
          },
          {
            "w": "mental health",
            "ipa": "/ˈmentl helθ/",
            "zh": "心理健康"
          },
          {
            "w": "compare … to …",
            "ipa": "/kəmˈper tuː/",
            "zh": "把……和……比较"
          },
          {
            "w": "anxious",
            "ipa": "/ˈæŋkʃəs/",
            "zh": "焦虑的"
          },
          {
            "w": "worthless",
            "ipa": "/ˈwɜːrθləs/",
            "zh": "一文不值的"
          }
        ]
      }
    ]
  },
  {
    "id": "mock-sport-0820",
    "title": "口语模考·运动（2题·①单②两）",
    "topic": "口语模考 8/20",
    "questions": [
      {
        "q": "If you were able to, what sport that you do not currently play would you like to be really good at? Why that particular sport?",
        "outline": [
          {
            "role": "观点",
            "text": "想擅长游泳"
          },
          {
            "role": "理由（唯一）",
            "text": "游泳既放松又对健康好"
          },
          {
            "role": "展开",
            "bullets": [
              "在水里很放松，压力都没了",
              "对身体健康很好",
              "下班后想游一会儿"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "if I could be really good at any sport, I would pick swimming."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "swimming is both super relaxing and really good for my health."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "when I'm in the water, my whole body feels calm and all my stress just goes away."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "after a long day at work, I love to jump in the pool and swim a few rounds."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that's why I really want to be great at swimming."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "想擅长游泳"
          },
          {
            "role": "理由一",
            "text": "能放松减压"
          },
          {
            "role": "展开",
            "bullets": [
              "在水里心情很平静"
            ]
          },
          {
            "role": "理由二",
            "text": "对全身健康好"
          },
          {
            "role": "展开",
            "bullets": [
              "用到全身，越来越强壮"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "if I could, I would love to be really good at swimming."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "swimming helps me relax and let go of my stress."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when I'm in the water, my mind feels calm and I forget all my worries."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "it's really good for my whole body."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "swimming uses every part of my body, so I get stronger and healthier."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that's why swimming is the sport I want to master."
          }
        ],
        "frames": [
          {
            "t": "if I could be really good at any sport, I would pick ___.",
            "zh": "如果我能擅长任何一项运动，我会选 ___。"
          },
          {
            "t": "___ is both super relaxing and really good for my health.",
            "zh": "___ 既放松又对健康很好。"
          },
          {
            "t": "when I'm ___, my whole body feels calm.",
            "zh": "当我 ___ 时，全身都很平静。"
          },
          {
            "t": "after a long day at work, I love to ___.",
            "zh": "忙了一天后，我喜欢 ___。"
          },
          {
            "t": "that's why I really want to be great at ___.",
            "zh": "这就是我很想擅长 ___ 的原因。"
          }
        ],
        "vocab": [
          {
            "w": "swimming",
            "ipa": "/ˈswɪmɪŋ/",
            "zh": "游泳"
          },
          {
            "w": "relaxing",
            "ipa": "/rɪˈlæksɪŋ/",
            "zh": "放松的"
          },
          {
            "w": "stress",
            "ipa": "/stres/",
            "zh": "压力"
          },
          {
            "w": "calm",
            "ipa": "/kɑːm/",
            "zh": "平静的"
          },
          {
            "w": "healthy",
            "ipa": "/ˈhelθi/",
            "zh": "健康的"
          }
        ],
        "words": 77,
        "words2": 76
      },
      {
        "q": "Some people believe that children should not participate in contact sports like rugby or hockey because they could get hurt, while others believe that these sports teach awareness and teamwork. What do you think, and why?",
        "outline": [
          {
            "role": "观点",
            "text": "孩子应该玩这类接触性运动，好处大于风险"
          },
          {
            "role": "理由（唯一）",
            "text": "这些运动能教会他们团队合作"
          },
          {
            "role": "展开",
            "bullets": [
              "在球场上要跟队友一起配合",
              "学会传球、互相帮忙",
              "这些技能长大后也用得上"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think children should play these sports."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "sports like rugby teach kids how to work as a team."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "on the field, they have to play with their teammates and help each other."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "my little brother plays hockey, and now he shares things and works well with other kids."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "I think the good side is much bigger than the small risk of getting hurt."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "孩子应该玩这类运动"
          },
          {
            "role": "理由一",
            "text": "能学会团队合作"
          },
          {
            "role": "展开",
            "bullets": [
              "要和队友一起配合、互相帮忙"
            ]
          },
          {
            "role": "理由二",
            "text": "会变得更勇敢、更自信"
          },
          {
            "role": "展开",
            "bullets": [
              "敢去尝试难的事，不怕犯错"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think children should play sports like rugby or hockey."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "these sports teach kids how to work as a team."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "they have to play with their teammates and help each other to win."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "playing these sports makes kids braver and more confident."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "they learn to try hard things and are not afraid of making mistakes."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "I think the good side is much bigger than the small risk."
          }
        ],
        "frames": [
          {
            "t": "I think children should play these sports.",
            "zh": "我觉得孩子应该玩这些运动。"
          },
          {
            "t": "these sports teach kids how to work as a team.",
            "zh": "这些运动能教会孩子怎么团队合作。"
          },
          {
            "t": "they have to help each other.",
            "zh": "他们必须互相帮忙。"
          },
          {
            "t": "playing these sports makes kids braver and more confident.",
            "zh": "玩这些运动让孩子更勇敢、更自信。"
          },
          {
            "t": "the good side is much bigger than the small risk.",
            "zh": "好处远远大于那点小风险。"
          }
        ],
        "vocab": [
          {
            "w": "teammate",
            "ipa": "/ˈtiːmmeɪt/",
            "zh": "队友"
          },
          {
            "w": "teamwork",
            "ipa": "/ˈtiːmwɜːrk/",
            "zh": "团队合作"
          },
          {
            "w": "confident",
            "ipa": "/ˈkɑːnfɪdənt/",
            "zh": "自信的"
          },
          {
            "w": "brave",
            "ipa": "/breɪv/",
            "zh": "勇敢的"
          },
          {
            "w": "risk",
            "ipa": "/rɪsk/",
            "zh": "风险"
          }
        ],
        "words": 71,
        "words2": 76
      }
    ]
  },
  {
    "id": "mock-energy-0820",
    "title": "口语模考·可再生能源（2题·①单②两）",
    "topic": "口语模考 8/20",
    "questions": [
      {
        "q": "What initiatives could your community take to promote renewable energy or energy conservation?",
        "outline": [
          {
            "role": "观点",
            "text": "社区可以做很多事来推广清洁能源"
          },
          {
            "role": "理由（唯一）",
            "text": "在楼顶装太阳能板"
          },
          {
            "role": "展开",
            "bullets": [
              "屋顶白晒着，装了就能发电",
              "阳光免费，太阳能板能省电费",
              "住户用上干净能源"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think my community can do a lot to promote clean energy."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "we could put solar panels on the roofs of our buildings."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "the roofs are just sitting there in the sun all day."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "sunlight is free, so the panels can make power and cut our electricity bills."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "putting solar panels on the roofs is a really smart move for us."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "社区可以从两方面着手"
          },
          {
            "role": "理由一",
            "text": "在楼顶装太阳能板"
          },
          {
            "role": "展开",
            "bullets": [
              "屋顶晒着阳光，装了就能发电省钱"
            ]
          },
          {
            "role": "理由二",
            "text": "办活动教大家日常省电"
          },
          {
            "role": "展开",
            "bullets": [
              "很多人不知道随手关灯能省很多"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think my community can work on two things."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "we could put solar panels on the roofs of our buildings."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "the roofs get lots of sun, so the panels can make power and save money."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "we could hold events to teach people how to save energy every day."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "many people don't know that turning off lights really helps."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "with solar panels and these events, we can save a lot of energy."
          }
        ],
        "frames": [
          {
            "t": "I think my community can do a lot to ___.",
            "zh": "我觉得我的社区能做很多事来……"
          },
          {
            "t": "We could put ___ on the roofs of our buildings.",
            "zh": "我们可以在楼顶装……"
          },
          {
            "t": "the roofs are just sitting there in the sun.",
            "zh": "屋顶就那么晒着阳光。"
          },
          {
            "t": "We could hold events to teach people how to ___.",
            "zh": "我们可以办活动教大家怎么……"
          },
          {
            "t": "we can save a lot of energy.",
            "zh": "我们能省很多能源。"
          }
        ],
        "vocab": [
          {
            "w": "solar panel",
            "ipa": "/ˈsoʊlər ˈpænl/",
            "zh": "太阳能板"
          },
          {
            "w": "roof",
            "ipa": "/ruːf/",
            "zh": "屋顶"
          },
          {
            "w": "electricity",
            "ipa": "/ɪˌlekˈtrɪsəti/",
            "zh": "电"
          },
          {
            "w": "save",
            "ipa": "/seɪv/",
            "zh": "节省"
          },
          {
            "w": "energy",
            "ipa": "/ˈenərdʒi/",
            "zh": "能源"
          }
        ],
        "words": 69,
        "words2": 80
      },
      {
        "q": "Do the benefits of renewable energy outweigh the costs? Why or why not?",
        "outline": [
          {
            "role": "观点",
            "text": "利大于弊，很值得"
          },
          {
            "role": "理由（唯一）",
            "text": "空气更干净，对健康好"
          },
          {
            "role": "展开",
            "bullets": [
              "太阳能风能不烧煤，不排脏气体",
              "城市空气变好，天更蓝",
              "呼吸道毛病少了"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I really think the benefits of renewable energy are worth it."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it gives us much cleaner air, which is great for our health."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "solar and wind power don't burn coal, so they don't put dirty gases into the sky."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "in my city the air got a lot better, and fewer people have breathing problems now."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "for me, cleaner air and better health make it totally worth the cost."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "利大于弊，很值得"
          },
          {
            "role": "理由一",
            "text": "空气更干净，对健康好"
          },
          {
            "role": "展开",
            "bullets": [
              "不烧煤，城市天更蓝，呼吸道病少"
            ]
          },
          {
            "role": "理由二",
            "text": "长期能省钱"
          },
          {
            "role": "展开",
            "bullets": [
              "太阳风是免费的，用久了电费更便宜"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think the benefits of renewable energy are really worth it."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "it gives us cleaner air, which is good for our health."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when we stop burning coal, the sky gets bluer and fewer people get sick."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "it can save us money in the long run."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "sun and wind are free, so once it's set up, the power gets cheaper."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "better health and lower bills make it a really good deal."
          }
        ],
        "frames": [
          {
            "t": "I really think ___ is worth it.",
            "zh": "我真的觉得……很值得。"
          },
          {
            "t": "it gives us ___, which is good for ___.",
            "zh": "它带来……，这对……有好处。"
          },
          {
            "t": "they don't burn coal, so ___.",
            "zh": "它们不烧煤，所以……。"
          },
          {
            "t": "it can save us money in the long run.",
            "zh": "从长远看它能帮我们省钱。"
          },
          {
            "t": "___ make it a really good deal.",
            "zh": "……让它非常划算。"
          }
        ],
        "vocab": [
          {
            "w": "renewable",
            "ipa": "/rɪˈnuːəbl/",
            "zh": "可再生的"
          },
          {
            "w": "clean",
            "ipa": "/kliːn/",
            "zh": "干净的"
          },
          {
            "w": "health",
            "ipa": "/helθ/",
            "zh": "健康"
          },
          {
            "w": "coal",
            "ipa": "/koʊl/",
            "zh": "煤"
          },
          {
            "w": "cheaper",
            "ipa": "/ˈtʃiːpər/",
            "zh": "更便宜的"
          }
        ],
        "words": 76,
        "words2": 79
      }
    ]
  },
  {
    "id": "mock-social-0820",
    "title": "口语模考·社交聚会（3题·①单②两）",
    "topic": "口语模考 8/20",
    "questions": [
      {
        "q": "Can you describe a memorable social gathering that you attended recently? What made it especially memorable?",
        "outline": [
          {
            "role": "观点",
            "text": "最近去了最好的朋友的生日聚会"
          },
          {
            "role": "理由（唯一）",
            "text": "和最好的朋友在一起，非常开心"
          },
          {
            "role": "展开",
            "bullets": [
              "她请了我们几个亲近的朋友",
              "我们一起吃蛋糕、聊天、大笑",
              "整个晚上都感觉很温暖"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "the most memorable one was my best friend's birthday party last week."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it was so special just because I got to spend time with my best friend."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "we are really close, and being with her always makes me happy."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "she invited a few close friends, and we ate cake, talked, and laughed a lot together."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that warm night is something I will always remember."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "最近去了最好的朋友的生日聚会"
          },
          {
            "role": "理由一",
            "text": "和最好的朋友在一起，很开心"
          },
          {
            "role": "展开",
            "bullets": [
              "她请了几个亲近的朋友，一起吃蛋糕大笑"
            ]
          },
          {
            "role": "理由二",
            "text": "一起玩游戏，聊到很晚，很难忘"
          },
          {
            "role": "展开",
            "bullets": [
              "那种放松又开心的感觉让我一直记得"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "the most memorable one was my best friend's birthday party last week."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "it was special because I got to spend time with my best friend."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "she invited a few close friends, and we ate cake and laughed a lot."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "we played some fun games and talked until very late that night."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "we were all so relaxed and happy, so the time just flew by."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that lovely night is something I will never forget."
          }
        ],
        "frames": [
          {
            "t": "The most memorable one was ___.",
            "zh": "最难忘的一次是……"
          },
          {
            "t": "it was special because ___.",
            "zh": "它特别是因为……"
          },
          {
            "t": "we ate cake, talked, and laughed a lot.",
            "zh": "我们一起吃蛋糕、聊天、大笑。"
          },
          {
            "t": "we played games and talked until very late.",
            "zh": "我们玩游戏，聊到很晚。"
          },
          {
            "t": "that night is something I will never forget.",
            "zh": "那个夜晚我永远不会忘记。"
          }
        ],
        "vocab": [
          {
            "w": "memorable",
            "ipa": "/ˈmemərəbl/",
            "zh": "难忘的"
          },
          {
            "w": "gathering",
            "ipa": "/ˈɡæðərɪŋ/",
            "zh": "聚会"
          },
          {
            "w": "invite",
            "ipa": "/ɪnˈvaɪt/",
            "zh": "邀请"
          },
          {
            "w": "relaxed",
            "ipa": "/rɪˈlækst/",
            "zh": "放松的"
          },
          {
            "w": "forget",
            "ipa": "/fərˈɡet/",
            "zh": "忘记"
          }
        ],
        "words": 72,
        "words2": 82
      },
      {
        "q": "How do you usually prepare for a social gathering? What do you pay the most attention to when getting ready?",
        "outline": [
          {
            "role": "观点",
            "text": "准备时我最在意会见到谁"
          },
          {
            "role": "理由（唯一）",
            "text": "知道有谁能帮我准备话题、少尴尬"
          },
          {
            "role": "展开",
            "bullets": [
              "先问朋友谁会来",
              "想几个大家都爱聊的事",
              "一到场就能自然开口"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "when I get ready for a party, the thing I care about most is who will be there."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "I always try to find out who is coming before I go."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "knowing the people helps me think of good things to talk about."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I text a friend and ask, and then I plan a few topics in my head."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "when I get there, I can start a chat easily and feel less shy."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "我主要做两件事"
          },
          {
            "role": "理由一",
            "text": "先想清楚会见到谁"
          },
          {
            "role": "展开",
            "bullets": [
              "提前问谁会来，好想话题"
            ]
          },
          {
            "role": "理由二",
            "text": "准备点吃的或小礼物"
          },
          {
            "role": "展开",
            "bullets": [
              "带点东西大家都开心，气氛更好"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "before a gathering, I usually do two simple things to get ready."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I think about who will be there, because that matters the most to me."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I ask a friend who is coming, so I can plan a few topics."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "I bring some snacks or a small gift with me."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "a little gift makes people happy and warms up the mood."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "with these two things ready, I always feel calm and enjoy the party more."
          }
        ],
        "frames": [
          {
            "t": "the thing I care about most is ___.",
            "zh": "我最在意的是……"
          },
          {
            "t": "before I go, I try to find out ___.",
            "zh": "去之前我会先弄清……"
          },
          {
            "t": "I plan a few topics in my head.",
            "zh": "我在脑子里想好几个话题。"
          },
          {
            "t": "I usually do two simple things.",
            "zh": "我一般做两件简单的事。"
          },
          {
            "t": "it warms up the mood.",
            "zh": "它能暖场／让气氛更好。"
          }
        ],
        "vocab": [
          {
            "w": "gathering",
            "ipa": "/ˈɡæðərɪŋ/",
            "zh": "聚会"
          },
          {
            "w": "topic",
            "ipa": "/ˈtɒpɪk/",
            "zh": "话题"
          },
          {
            "w": "snack",
            "ipa": "/snæk/",
            "zh": "零食"
          },
          {
            "w": "gift",
            "ipa": "/ɡɪft/",
            "zh": "礼物"
          },
          {
            "w": "mood",
            "ipa": "/muːd/",
            "zh": "气氛；心情"
          }
        ],
        "words": 80,
        "words2": 84
      },
      {
        "q": "Some people believe that social gatherings are important opportunities for building and maintaining professional connections. Do you agree or disagree? Why?",
        "outline": [
          {
            "role": "观点",
            "text": "同意，社交聚会很适合建立工作人脉"
          },
          {
            "role": "理由（唯一）",
            "text": "能当面认识很多新的人"
          },
          {
            "role": "展开",
            "bullets": [
              "在网上聊很难真的记住一个人",
              "面对面聊天更放松更真实",
              "以后要帮忙时更容易开口"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I totally agree that social gatherings are a great way to build work connections."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "you can meet a lot of new people face to face at these events."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "talking online just feels cold, and it's hard to really remember someone."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "at a party, you chat, you laugh, and you feel more real to each other."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "later, when you need help, it's much easier to reach out."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "同意，对工作人脉很重要"
          },
          {
            "role": "理由一",
            "text": "能当面认识新朋友和人脉"
          },
          {
            "role": "展开",
            "bullets": [
              "面对面聊天让人更容易记住你"
            ]
          },
          {
            "role": "理由二",
            "text": "能从这些人身上学到新东西"
          },
          {
            "role": "展开",
            "bullets": [
              "大家会分享经验和想法"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I agree with this. Social gatherings really help with work connections."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "you get to meet new friends and useful people in person."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "talking face to face makes it much easier for them to remember you."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "you can learn new things from all these people."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "they often share their own ideas and work experience."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "going to these events is really good for me, and that's why I agree."
          }
        ],
        "frames": [
          {
            "t": "I totally agree that ___.",
            "zh": "我完全同意……"
          },
          {
            "t": "you can meet a lot of new people.",
            "zh": "你能认识很多新的人。"
          },
          {
            "t": "talking face to face.",
            "zh": "面对面聊天。"
          },
          {
            "t": "when you need help, it's easier to reach out.",
            "zh": "当你需要帮助时，更容易开口求助。"
          },
          {
            "t": "you can learn new things from them.",
            "zh": "你能从他们身上学到新东西。"
          }
        ],
        "vocab": [
          {
            "w": "gathering",
            "ipa": "/ˈɡæðərɪŋ/",
            "zh": "聚会"
          },
          {
            "w": "connection",
            "ipa": "/kəˈnekʃn/",
            "zh": "人脉；联系"
          },
          {
            "w": "face to face",
            "ipa": "/ˌfeɪs tə ˈfeɪs/",
            "zh": "面对面"
          },
          {
            "w": "reach out",
            "ipa": "/ˌriːtʃ ˈaʊt/",
            "zh": "联系；求助"
          },
          {
            "w": "share",
            "ipa": "/ʃer/",
            "zh": "分享"
          }
        ],
        "words": 74,
        "words2": 76
      }
    ]
  },
  {
    "id": "mock-hobby-0820",
    "title": "口语模考·爱好（3题·①单②两）",
    "topic": "口语模考 8/20",
    "questions": [
      {
        "q": "What role do you think friends, family, or online communities play in encouraging someone to start a hobby?",
        "outline": [
          {
            "role": "观点",
            "text": "我觉得网上社群作用最大"
          },
          {
            "role": "理由（唯一）",
            "text": "网上能帮你发现新爱好，还能跟别人学"
          },
          {
            "role": "展开",
            "bullets": [
              "网上有各种各样的人分享",
              "你能看到很多新东西",
              "还能免费学到怎么做"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think online communities help the most when you want to start a new hobby."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "online you can find lots of new things and learn from other people."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "so many people share what they do online every single day."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I found drawing on a video app, and people showed me how to start for free."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that's why I think online communities really help a lot."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "我觉得网上社群作用最大"
          },
          {
            "role": "理由一",
            "text": "网上能发现很多新东西"
          },
          {
            "role": "展开",
            "bullets": [
              "我在视频里看到画画就想试"
            ]
          },
          {
            "role": "理由二",
            "text": "能找到同好，一起学、坚持下去"
          },
          {
            "role": "展开",
            "bullets": [
              "大家互相帮忙，你就不想放弃"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think online communities matter the most for starting a new hobby."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "online you can find many new things you never knew about."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I saw people drawing in short videos, and I really wanted to try it too."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "you can find people who like the same thing and learn together."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "when everyone helps each other, you don't want to give up."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that's why online communities help so much."
          }
        ],
        "frames": [
          {
            "t": "I think ___ help the most when you want to start a new hobby.",
            "zh": "我觉得想开始新爱好时，___帮助最大。"
          },
          {
            "t": "online you can find lots of new things.",
            "zh": "网上你能发现很多新东西。"
          },
          {
            "t": "so many people share what they do online.",
            "zh": "很多人在网上分享他们做的事。"
          },
          {
            "t": "you can find people who like the same thing.",
            "zh": "你能找到喜欢同样东西的人。"
          },
          {
            "t": "when everyone helps each other, you don't want to give up.",
            "zh": "大家互相帮忙，你就不想放弃。"
          }
        ],
        "vocab": [
          {
            "w": "community",
            "ipa": "/kəˈmjuːnəti/",
            "zh": "社群，群体"
          },
          {
            "w": "hobby",
            "ipa": "/ˈhɒbi/",
            "zh": "爱好"
          },
          {
            "w": "share",
            "ipa": "/ʃer/",
            "zh": "分享"
          },
          {
            "w": "together",
            "ipa": "/təˈɡeðər/",
            "zh": "一起"
          },
          {
            "w": "give up",
            "ipa": "/ɡɪv ʌp/",
            "zh": "放弃"
          }
        ],
        "words": 73,
        "words2": 77
      },
      {
        "q": "Many people begin hobbies but eventually stop doing them. What do you think causes people to give up their hobbies?",
        "outline": [
          {
            "role": "观点",
            "text": "我觉得主要是因为没时间"
          },
          {
            "role": "理由（唯一）",
            "text": "工作和学习让人太忙"
          },
          {
            "role": "展开",
            "bullets": [
              "白天忙完就很累",
              "没精力做爱好",
              "慢慢就放弃了"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think most people give up their hobbies because they don't have enough time."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "work and school keep people really busy every day."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "after a long day, they feel tired and have no energy left for fun."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I used to draw a lot, but my job got busy, so I just stopped little by little."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "I think being too busy is the main reason people give up their hobbies."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "我觉得主要有两个原因"
          },
          {
            "role": "理由一",
            "text": "没时间，太忙了"
          },
          {
            "role": "展开",
            "bullets": [
              "工作学习占满了时间"
            ]
          },
          {
            "role": "理由二",
            "text": "爱好要花钱"
          },
          {
            "role": "展开",
            "bullets": [
              "有些爱好花费很高，负担不起"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I think there are two main reasons people give up their hobbies."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "most people just don't have enough time because they are so busy."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "work and school take up almost all of their day."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "some hobbies cost a lot of money to keep doing."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "things like tennis or photography need money for gear and lessons."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "being too busy and spending too much money make people stop."
          }
        ],
        "frames": [
          {
            "t": "I think most people ___ because ___.",
            "zh": "我觉得大多数人……因为……"
          },
          {
            "t": "work and school keep people really busy.",
            "zh": "工作和学习让人很忙。"
          },
          {
            "t": "they have no energy left for ___.",
            "zh": "他们没精力做……"
          },
          {
            "t": "some hobbies cost a lot of money.",
            "zh": "有些爱好很花钱。"
          },
          {
            "t": "___ make people stop.",
            "zh": "……让人放弃。"
          }
        ],
        "vocab": [
          {
            "w": "busy",
            "ipa": "/ˈbɪzi/",
            "zh": "忙的"
          },
          {
            "w": "energy",
            "ipa": "/ˈenərdʒi/",
            "zh": "精力"
          },
          {
            "w": "tired",
            "ipa": "/ˈtaɪərd/",
            "zh": "累的"
          },
          {
            "w": "reason",
            "ipa": "/ˈriːzən/",
            "zh": "原因"
          },
          {
            "w": "gear",
            "ipa": "/ɡɪr/",
            "zh": "装备"
          }
        ],
        "words": 77,
        "words2": 75
      },
      {
        "q": "Some people believe spending time on hobbies is important for maintaining a healthy lifestyle, while others think hobbies are not necessary if people are busy with work or school. What is your opinion?",
        "outline": [
          {
            "role": "观点",
            "text": "我觉得爱好很重要，就算忙也该留时间"
          },
          {
            "role": "理由（唯一）",
            "text": "爱好能帮你放松、减轻压力"
          },
          {
            "role": "展开",
            "bullets": [
              "工作学习一天很累",
              "做喜欢的事能让脑子休息",
              "压力小了身体也更健康"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I really think hobbies are important, even when we are busy with work or school."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "having a hobby can help you relax and feel less stressed."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "after a long day, your mind is tired and needs a real break."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I love drawing, and when I draw for an hour, all my stress just goes away."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "in my opinion, we should always keep some time for our hobbies."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "我觉得爱好很重要，就算忙也该留时间"
          },
          {
            "role": "理由一",
            "text": "爱好能放松减压，心情更好"
          },
          {
            "role": "展开",
            "bullets": [
              "画画一小时，压力就没了"
            ]
          },
          {
            "role": "理由二",
            "text": "爱好能学新技能、认识新朋友"
          },
          {
            "role": "展开",
            "bullets": [
              "打篮球又健身又交到朋友"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I really think hobbies are important, even when we are busy."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "a hobby helps you relax and puts you in a better mood."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when I draw for an hour, all my stress just goes away."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "hobbies help you learn new skills and meet new friends."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "you often join a group and do things with other people."
          },
          {
            "mk": "So,",
            "role": "小结",
            "en": "that's why I always keep some time for my hobbies."
          }
        ],
        "frames": [
          {
            "t": "I really think ___, even when we are busy.",
            "zh": "我真觉得……，就算忙也一样。"
          },
          {
            "t": "having a hobby can help you relax.",
            "zh": "有个爱好能帮你放松。"
          },
          {
            "t": "your mind is tired and needs a real break.",
            "zh": "你的脑子很累，需要真正休息一下。"
          },
          {
            "t": "when I ___, all my stress just goes away.",
            "zh": "当我……时，压力全都没了。"
          },
          {
            "t": "we should always keep some time for ___.",
            "zh": "我们该一直留点时间给……。"
          }
        ],
        "vocab": [
          {
            "w": "hobby",
            "ipa": "/ˈhɑːbi/",
            "zh": "爱好"
          },
          {
            "w": "relax",
            "ipa": "/rɪˈlæks/",
            "zh": "放松"
          },
          {
            "w": "stressed",
            "ipa": "/strest/",
            "zh": "有压力的"
          },
          {
            "w": "mood",
            "ipa": "/muːd/",
            "zh": "心情"
          },
          {
            "w": "skill",
            "ipa": "/skɪl/",
            "zh": "技能"
          }
        ],
        "words": 75,
        "words2": 75
      }
    ]
  },
  {
    "id": "mock-goal-0820",
    "title": "口语模考·目标与成就（4题·①单②两③高级）",
    "topic": "口语模考 8/20",
    "questions": [
      {
        "q": "Think of a time, recent or not, when you had something you wanted to achieve. What was it?",
        "outline": [
          {
            "role": "观点",
            "text": "我想学好英语，通过一个重要的英语考试"
          },
          {
            "role": "理由（唯一）",
            "text": "因为我想出国学习，英语是关键"
          },
          {
            "role": "展开",
            "bullets": [
              "好的英语能让我进好学校",
              "能听懂课、交到朋友",
              "这个考试是我出国的第一步"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "there was one big goal I really wanted to reach — passing a high-level English exam."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "I want this because I hope to study abroad one day."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "good English is the key to getting into a good school."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I dream of studying business at a school like NYU."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "once my English is strong, I can follow lectures there and make friends."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "this test is my first big step, and I work hard for it every day."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "我想学好英语、通过一个重要的英语考试"
          },
          {
            "role": "理由一",
            "text": "为了有一天出国学习"
          },
          {
            "role": "展开",
            "bullets": [
              "好英语能进好学校",
              "能听懂课、交到朋友"
            ]
          },
          {
            "role": "理由二",
            "text": "为了以后找更好的工作"
          },
          {
            "role": "展开",
            "bullets": [
              "好英语带来更多机会、打开职场大门"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "there was one big goal I wanted — passing a high-level English exam."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I want it because I hope to study abroad."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "good English helps me get into a good school."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I dream of studying business at NYU."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I can follow the lectures there and make friends."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "I want a better job in the future."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "good English opens doors at big companies."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I hope to be a marketing manager at Google."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I can work with international teams every day."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "this test means a lot to me."
          }
        ],
        "frames": [
          {
            "t": "There was one thing I really wanted to do. I wanted to ___.",
            "zh": "有一件我很想做的事。我想要……"
          },
          {
            "t": "I wanted this because I hope to ___.",
            "zh": "我想要这个，是因为我希望……"
          },
          {
            "t": "Good ___ is the key. It can help me ___.",
            "zh": "好的……是关键。它能帮我……"
          },
          {
            "t": "If my ___ is good, I can ___.",
            "zh": "如果我的……好，我就能……"
          },
          {
            "t": "Passing this test is my first big step to ___.",
            "zh": "通过这个考试是我……的第一大步。"
          },
          {
            "t": "⬆️进阶 I aspire to pursue a master's degree abroad",
            "zh": "我立志出国读硕士（aspire to pursue＝渴望追求，比 want 高级）"
          },
          {
            "t": "⬆️进阶 strong English skills are essential for academic success",
            "zh": "扎实的英语是学术成功的关键"
          },
          {
            "t": "⬆️进阶 I can fully engage in lectures and discussions",
            "zh": "我能全身心投入课堂和讨论（engage in＝投入参与）"
          },
          {
            "t": "⬆️进阶 fluency will create career opportunities",
            "zh": "流利的英语会创造职业机会"
          },
          {
            "t": "⬆️进阶 global companies highly value strong communication",
            "zh": "跨国公司高度重视强沟通力"
          },
          {
            "t": "⬆️进阶 I need to collaborate effectively with global teams",
            "zh": "我需要与全球团队高效协作（collaborate effectively）"
          },
          {
            "t": "⬆️进阶 I could study international marketing techniques and actively participate",
            "zh": "我可以学国际营销技巧、积极参与（actively participate）"
          },
          {
            "t": "⬆️进阶 I could lead worldwide brand campaigns",
            "zh": "我可以主导全球品牌活动（worldwide brand campaigns）"
          },
          {
            "t": "⬆️进阶 I'm fully committed to this goal",
            "zh": "我全力投入这个目标（fully committed to，收尾有力）"
          }
        ],
        "vocab": [
          {
            "w": "achieve",
            "ipa": "/əˈtʃiːv/",
            "zh": "实现，达成"
          },
          {
            "w": "abroad",
            "ipa": "/əˈbrɔːd/",
            "zh": "到国外"
          },
          {
            "w": "pass",
            "ipa": "/pæs/",
            "zh": "通过（考试）"
          },
          {
            "w": "chance",
            "ipa": "/tʃæns/",
            "zh": "机会"
          },
          {
            "w": "step",
            "ipa": "/step/",
            "zh": "步骤，一步"
          },
          {
            "w": "a strong command of",
            "ipa": "/ə strɔːŋ kəˈmɑːnd əv/",
            "zh": "对…的扎实掌握"
          },
          {
            "w": "essential",
            "ipa": "/ɪˈsenʃl/",
            "zh": "必不可少的"
          },
          {
            "w": "fluent",
            "ipa": "/ˈfluːənt/",
            "zh": "流利的"
          },
          {
            "w": "ultimate dream",
            "ipa": "/ˈʌltɪmət driːm/",
            "zh": "终极梦想"
          },
          {
            "w": "proficiency",
            "ipa": "/prəˈfɪʃnsi/",
            "zh": "熟练，精通（English proficiency exam＝英语水平考试）"
          },
          {
            "w": "a strong command of English",
            "ipa": "/ə strɔːŋ kəˈmɑːnd/",
            "zh": "对英语的熟练掌握"
          },
          {
            "w": "marketing manager",
            "ipa": "/ˈmɑːrkɪtɪŋ ˈmænɪdʒər/",
            "zh": "市场经理（具体职位名）"
          },
          {
            "w": "aspire to",
            "ipa": "/əˈspaɪər tə/",
            "zh": "立志/渴望做（aspire to pursue＝立志追求）"
          },
          {
            "w": "pursue",
            "ipa": "/pərˈsuː/",
            "zh": "追求，攻读（pursue a master's＝读硕士）"
          },
          {
            "w": "engage in",
            "ipa": "/ɪnˈɡeɪdʒ ɪn/",
            "zh": "投入，参与"
          },
          {
            "w": "collaborate",
            "ipa": "/kəˈlæbəreɪt/",
            "zh": "协作，合作"
          },
          {
            "w": "effectively",
            "ipa": "/ɪˈfektɪvli/",
            "zh": "有效地，高效地"
          }
        ],
        "words": 85,
        "words2": 101,
        "model3": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "one goal I've worked toward recently is passing an advanced English exam."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I aspire to pursue a master's degree abroad."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "strong English skills are essential for academic success."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I hope to study business at a top school like NYU."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I can fully engage in lectures and discussions there."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "fluency will create career opportunities."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "global companies highly value strong communication."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I aim to be a marketing manager at an international firm."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I need to collaborate effectively with global teams."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "this exam is so important to me."
          }
        ],
        "outline3": [
          {
            "role": "观点",
            "text": "想通过一个高水平英语考试、拿到好分数"
          },
          {
            "role": "理由一",
            "text": "终极梦想是出国读硕士"
          },
          {
            "role": "展开",
            "bullets": [
              "扎实的英语能力对听懂复杂讲座、参与小组讨论至关重要"
            ]
          },
          {
            "role": "理由二",
            "text": "流利的英语能为未来职业打开很多大门"
          },
          {
            "role": "展开",
            "bullets": [
              "跨国公司看重能和国际团队有效沟通的人"
            ]
          }
        ],
        "words3": 100,
        "model4": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "I want to pass an advanced English exam."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "it will help me pursue a master's in business abroad."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "top universities like NYU require strong English."
          },
          {
            "mk": "For example,",
            "role": "举例+深入",
            "en": "I could study international marketing techniques and actively participate."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "it will advance my career."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "global companies need strong communicators."
          },
          {
            "mk": "For instance,",
            "role": "举例+深入",
            "en": "I could lead worldwide brand campaigns, so I'll have more global opportunities."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "I'm fully committed to this goal."
          }
        ],
        "words4": 77
      },
      {
        "q": "In general, how do you handle difficulties or obstacles that come up while working toward what you want to achieve?",
        "outline": [
          {
            "role": "观点",
            "text": "遇到困难先保持冷静，然后想办法解决"
          },
          {
            "role": "理由（唯一）",
            "text": "向懂的人请教（朋友或老师）"
          },
          {
            "role": "展开",
            "bullets": [
              "他们做过，能给更快的办法",
              "比如卡在难题上就问老师",
              "一问就通，继续往前走"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "when I run into difficulties, I always try to ask someone for help."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "I turn to a friend or a teacher who knows more than me."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "they have been through it before and can guide me."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when I was stuck on a hard problem, I asked my teacher."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "one quick tip from her saved me hours and I moved on fast."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "asking for help always keeps me going."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "我有两个简单办法应对困难"
          },
          {
            "role": "理由一",
            "text": "向朋友或老师请教怎么做"
          },
          {
            "role": "展开",
            "bullets": [
              "卡住时一个小提示就省很多时间"
            ]
          },
          {
            "role": "理由二",
            "text": "把大目标拆成小步、做个计划"
          },
          {
            "role": "展开",
            "bullets": [
              "小步很轻松，就不会放弃"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "when I face difficulties, I use two simple ways to deal with them."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I ask someone with more experience."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "one good tip can save me lots of time."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "once I was stuck and asked my teacher."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "she showed me a faster way and I finished quickly."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "I break the big goal into small steps."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "small steps feel easy, so I don't give up."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I make a short to-do list each morning."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I finish one thing at a time and keep going."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "these two ways always keep me moving."
          }
        ],
        "frames": [
          {
            "t": "I always try to stay calm when things get hard.",
            "zh": "事情变难时我总是尽量保持冷静。"
          },
          {
            "t": "I ask someone who knows more than me.",
            "zh": "我会请教比我懂的人。"
          },
          {
            "t": "They can show me a faster way.",
            "zh": "他们能给我一个更快的办法。"
          },
          {
            "t": "I break the big goal into small steps.",
            "zh": "我把大目标拆成小步。"
          },
          {
            "t": "These two things keep me going.",
            "zh": "这两件事让我坚持下去。"
          },
          {
            "t": "⬆️进阶 When I face tough obstacles, I usually rely on two simple strategies.",
            "zh": "遇到困难时，我通常靠两个简单策略（高级开头）"
          },
          {
            "t": "⬆️进阶 I reach out to a mentor or a friend who has more experience.",
            "zh": "我会向更有经验的前辈或朋友请教"
          },
          {
            "t": "⬆️进阶 Their perspective often reveals a solution I would never have found on my own.",
            "zh": "他们的视角常给我一个自己想不到的办法"
          },
          {
            "t": "⬆️进阶 I break my large goals into tiny, manageable steps.",
            "zh": "我把大目标拆成小而可控的步骤"
          },
          {
            "t": "⬆️进阶 This approach keeps my momentum until I reach the finish line.",
            "zh": "这个方法让我保持势头，直到抵达终点"
          },
          {
            "t": "⬆️进阶 break the preparation tasks into small pieces",
            "zh": "把备考任务拆成小块（明确指代，别用模糊的 cut them down）"
          },
          {
            "t": "⬆️进阶 I seek advice from someone with more experience",
            "zh": "我向更有经验的人请教（比 ask a teacher 高级）"
          },
          {
            "t": "a five-minute explanation from my teacher saved me hours",
            "zh": "老师五分钟的讲解帮我省了好几小时（具体到时长，细节到位）"
          }
        ],
        "vocab": [
          {
            "w": "calm",
            "ipa": "/kɑːm/",
            "zh": "冷静的"
          },
          {
            "w": "stuck",
            "ipa": "/stʌk/",
            "zh": "卡住的"
          },
          {
            "w": "tip",
            "ipa": "/tɪp/",
            "zh": "小提示"
          },
          {
            "w": "step",
            "ipa": "/step/",
            "zh": "步骤"
          },
          {
            "w": "plan",
            "ipa": "/plæn/",
            "zh": "计划"
          },
          {
            "w": "obstacle",
            "ipa": "/ˈɒbstəkl/",
            "zh": "障碍，困难"
          },
          {
            "w": "mentor",
            "ipa": "/ˈmentɔːr/",
            "zh": "导师，前辈"
          },
          {
            "w": "perspective",
            "ipa": "/pərˈspektɪv/",
            "zh": "视角，看法"
          },
          {
            "w": "manageable",
            "ipa": "/ˈmænɪdʒəbl/",
            "zh": "可管理的、能应付的"
          },
          {
            "w": "momentum",
            "ipa": "/məˈmentəm/",
            "zh": "势头，冲劲"
          }
        ],
        "words": 77,
        "words2": 103,
        "model3": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "when I face obstacles, I rely on two strategies."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I reach out to a mentor with experience."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "their advice reveals a solution I would miss."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when preparing for TOEFL, I asked my tutor for tips."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "she found my weak spots and I improved fast."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "I break big goals into small, manageable steps."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "one step at a time keeps me calm."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I set a daily target of twenty new words."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "steady progress adds up and keeps me motivated."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "these strategies keep my momentum to the finish line."
          }
        ],
        "outline3": [
          {
            "role": "观点",
            "text": "面对目标上的困难，我靠两个简单策略"
          },
          {
            "role": "理由一",
            "text": "向更有经验的前辈或朋友请教"
          },
          {
            "role": "展开",
            "bullets": [
              "他们的视角常给我一个自己想不到的办法"
            ]
          },
          {
            "role": "理由二",
            "text": "把大而吓人的目标拆成小而可控的步骤、做计划"
          },
          {
            "role": "展开",
            "bullets": [
              "一次只专注一小步，就不会想放弃"
            ]
          }
        ],
        "words3": 101,
        "model4": [
          {
            "mk": "Well,",
            "role": "观点",
            "en": "I usually have two simple ways to deal with hard times and problems."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "I seek advice from someone with more experience, like a teacher or mentor."
          },
          {
            "mk": "For instance,",
            "role": "举例一",
            "en": "when I'm struggling with a complex grammar rule, a five-minute explanation from my teacher saved me hours."
          },
          {
            "mk": "Also,",
            "role": "理由二",
            "en": "I break the big goal into small steps and make a clear plan."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "tiny steps always feel easy, so I will never really want to give up."
          },
          {
            "mk": "For example,",
            "role": "举例二",
            "en": "when I'm preparing for my English test, I break the preparation task into small pieces."
          },
          {
            "mk": "",
            "role": "收尾",
            "en": "These tips really helped me a lot."
          }
        ],
        "words4": 103,
        "score": "5.8"
      },
      {
        "q": "In your opinion, how important is goal setting for personal growth?",
        "outline": [
          {
            "role": "观点",
            "text": "非常重要"
          },
          {
            "role": "理由（唯一）",
            "text": "有目标就有方向，不会迷茫"
          },
          {
            "role": "展开",
            "bullets": [
              "知道自己想去哪里",
              "每天做事更有重点",
              "不会浪费时间乱转"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "I think setting goals is really important for personal growth."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "a goal gives you a clear direction in life."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "you always know what to do next."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "when I set a goal to get fit, I made a simple weekly plan."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I ran a little every weekend and slowly became much healthier."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "a clear goal helps you grow step by step."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "非常重要"
          },
          {
            "role": "理由一",
            "text": "给你清晰的方向，知道往哪走"
          },
          {
            "role": "展开",
            "bullets": [
              "知道该做什么，不迷茫"
            ]
          },
          {
            "role": "理由二",
            "text": "给你动力，更容易坚持下去"
          },
          {
            "role": "展开",
            "bullets": [
              "有目标就更想努力，不容易放弃"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "I believe setting goals is very important for personal growth."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "a goal gives you a clear direction."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "you know exactly what to do each day."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I set a goal to get fit and run every weekend."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I stopped wasting time and built a good habit."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "a goal gives you motivation to keep going."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "you try harder when you really want something."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "before exams, my goal pushes me to study late."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I don't give up even when it gets hard."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "goals help you become a better person."
          }
        ],
        "frames": [
          {
            "t": "I think ___ is really important for ___.",
            "zh": "我觉得___对___很重要。"
          },
          {
            "t": "When you have a goal, you have a clear direction.",
            "zh": "当你有目标，你就有清晰的方向。"
          },
          {
            "t": "A goal tells you where you want to go.",
            "zh": "目标告诉你想去哪里。"
          },
          {
            "t": "A goal gives you motivation to keep going.",
            "zh": "目标给你坚持下去的动力。"
          },
          {
            "t": "Goals push me forward and help me grow.",
            "zh": "目标推着我前进，帮我成长。"
          },
          {
            "t": "⬆️进阶 Setting clear goals is essential for personal growth.",
            "zh": "设定明确目标对个人成长至关重要"
          },
          {
            "t": "⬆️进阶 A goal gives you a real sense of direction.",
            "zh": "目标给你真正的方向感"
          },
          {
            "t": "⬆️进阶 For example, when I decided to get fit, I set a goal to …",
            "zh": "具体例子模板：我决定…时，定下了…目标"
          },
          {
            "t": "⬆️进阶 When you have a clear vision, you are less likely to give up after a setback.",
            "zh": "有清晰愿景，就不易因挫折放弃"
          },
          {
            "t": "⬆️进阶 A goal is like a roadmap that guides you toward a better version of yourself.",
            "zh": "目标像一张路线图，引导你成为更好的自己"
          }
        ],
        "vocab": [
          {
            "w": "goal",
            "ipa": "/ɡoʊl/",
            "zh": "目标"
          },
          {
            "w": "direction",
            "ipa": "/dəˈrekʃn/",
            "zh": "方向"
          },
          {
            "w": "motivation",
            "ipa": "/ˌmoʊtɪˈveɪʃn/",
            "zh": "动力"
          },
          {
            "w": "focused",
            "ipa": "/ˈfoʊkəst/",
            "zh": "专注的"
          },
          {
            "w": "lost",
            "ipa": "/lɔːst/",
            "zh": "迷茫的"
          },
          {
            "w": "essential",
            "ipa": "/ɪˈsenʃl/",
            "zh": "必不可少的"
          },
          {
            "w": "a sense of direction",
            "ipa": "/ə sens əv dəˈrekʃn/",
            "zh": "方向感"
          },
          {
            "w": "setback",
            "ipa": "/ˈsetbæk/",
            "zh": "挫折"
          },
          {
            "w": "vision",
            "ipa": "/ˈvɪʒn/",
            "zh": "愿景，清晰的目标"
          },
          {
            "w": "roadmap",
            "ipa": "/ˈroʊdmæp/",
            "zh": "路线图，规划"
          }
        ],
        "words": 69,
        "words2": 101,
        "model3": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "I strongly believe goal setting is essential for personal growth."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "a goal gives you a real sense of direction."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "it keeps you from drifting aimlessly."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "I set a goal to run 5 kilometers each weekend."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I stayed focused and slowly built a healthy routine."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "goals give you motivation to push through hard times."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "a clear vision stops you from quitting."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "my goal to pass TOEFL keeps me studying every night."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "I keep improving instead of giving up."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "a goal is like a roadmap that guides your growth."
          }
        ],
        "outline3": [
          {
            "role": "观点",
            "text": "设定明确目标对个人成长至关重要"
          },
          {
            "role": "理由一",
            "text": "给你真正的方向感，不会漫无目的地混日子"
          },
          {
            "role": "展开",
            "bullets": [
              "具体例子：为健身定下每周跑5公里 → 更容易专注"
            ]
          },
          {
            "role": "理由二",
            "text": "在遇到困难时给你坚持下去的动力"
          },
          {
            "role": "展开",
            "bullets": [
              "有清晰愿景，就不会因一点小挫折放弃"
            ]
          }
        ],
        "words3": 102
      },
      {
        "q": "Do you think children should be taught to set personal goals from an early age? Why or why not?",
        "my": "I think children should be taught how to set personal goals at an early age because it's very important skills that can help almost everything about their school work, job, and even the sports they like. If you teach children that way, they can be more confident. So, such as they want to go to a better school, they prepare it earlier, and they will be much more confident.",
        "score": "3.6",
        "outline": [
          {
            "role": "观点",
            "text": "应该，孩子该从小学会定目标"
          },
          {
            "role": "理由（唯一）",
            "text": "帮他们建立自信、有方向"
          },
          {
            "role": "展开",
            "bullets": [
              "有小目标去努力，达成时很自豪",
              "例子：小表妹定每周读一本书，现在很有成就感"
            ]
          }
        ],
        "model": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "yes, I think children should learn to set goals from a young age."
          },
          {
            "mk": "First off,",
            "role": "理由",
            "en": "it helps them build confidence."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "reaching a small goal makes them feel proud."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "my little cousin set a goal to read one book every week."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "every time she finishes one, she feels happy and more sure of herself."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "setting goals early makes children more confident and independent."
          }
        ],
        "outline2": [
          {
            "role": "观点",
            "text": "应该，孩子该从小学会定目标"
          },
          {
            "role": "理由一",
            "text": "帮他们建立自信"
          },
          {
            "role": "展开",
            "bullets": [
              "定个小目标(如每周读一本书)，达成就很自豪"
            ]
          },
          {
            "role": "理由二",
            "text": "养成一个对未来有用的好习惯"
          },
          {
            "role": "展开",
            "bullets": [
              "会规划、朝目标努力，以后读书工作都更好"
            ]
          }
        ],
        "model2": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "yes, I think children should learn to set goals early."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "it helps them build confidence."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "reaching a small goal makes them feel proud."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "my cousin set a goal to read one book a week."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "each time she finishes one, she believes in herself more."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "it teaches them a good habit for the future."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "they learn to plan and work toward a target."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "a child who plans homework early does better in school."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "they become more organized and ready for life."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "learning this early makes children confident and prepared."
          }
        ],
        "outline3": [
          {
            "role": "观点",
            "text": "绝对应该，孩子该从小被教会定目标"
          },
          {
            "role": "理由一",
            "text": "建立自信、带来成就感"
          },
          {
            "role": "展开",
            "bullets": [
              "达成小目标让他们自豪、有动力"
            ]
          },
          {
            "role": "理由二",
            "text": "从小养成受益终身的好习惯"
          },
          {
            "role": "展开",
            "bullets": [
              "会提前规划、有自律，读书和未来职业都更好"
            ]
          }
        ],
        "model3": [
          {
            "mk": "Well,",
            "role": "切题",
            "en": "I believe children should be taught to set goals early."
          },
          {
            "mk": "First off,",
            "role": "理由一",
            "en": "it builds confidence and gives them a sense of achievement."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "reaching a small goal makes them proud."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "my cousin set a goal to read one book each week."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "finishing each one made her proud and eager to learn."
          },
          {
            "mk": "Besides,",
            "role": "理由二",
            "en": "it instills a habit that benefits them for life."
          },
          {
            "mk": "This is because",
            "role": "为什么",
            "en": "kids who plan ahead grow disciplined."
          },
          {
            "mk": "Like,",
            "role": "举例",
            "en": "a child who sets study goals does better at school."
          },
          {
            "mk": "So,",
            "role": "深入细节",
            "en": "they become well-prepared for their future careers."
          },
          {
            "mk": "Therefore,",
            "role": "收尾",
            "en": "teaching goals early helps children become capable adults."
          }
        ],
        "frames": [
          {
            "t": "children should learn to set their own goals from a young age",
            "zh": "孩子该从小学会给自己定目标"
          },
          {
            "t": "it helps them build confidence",
            "zh": "这能帮他们建立自信"
          },
          {
            "t": "⬆️进阶 it builds their confidence and gives them a real sense of achievement",
            "zh": "建立自信、带来真正的成就感"
          },
          {
            "t": "⬆️进阶 it instills a valuable habit that will benefit them for the rest of their lives",
            "zh": "养成受益终身的好习惯"
          },
          {
            "t": "⬆️进阶 kids who learn to plan ahead and stay disciplined do far better later",
            "zh": "会提前规划、有自律的孩子以后更出色"
          }
        ],
        "vocab": [
          {
            "w": "confidence",
            "ipa": "/ˈkɑːnfɪdəns/",
            "zh": "自信"
          },
          {
            "w": "a sense of achievement",
            "ipa": "/ə sens əv əˈtʃiːvmənt/",
            "zh": "成就感"
          },
          {
            "w": "instill a habit",
            "ipa": "/ɪnˈstɪl ə ˈhæbɪt/",
            "zh": "灌输/养成一个习惯"
          },
          {
            "w": "disciplined",
            "ipa": "/ˈdɪsəplɪnd/",
            "zh": "自律的"
          },
          {
            "w": "well-prepared",
            "ipa": "/ˌwel prɪˈperd/",
            "zh": "准备充分的"
          }
        ],
        "words": 69,
        "words2": 103,
        "words3": 103
      }
    ]
  }
];
