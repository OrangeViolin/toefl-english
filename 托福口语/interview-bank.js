// 面试真题库（Take an Interview） —— 面试问答.html 读取本文件渲染
// 一个「真题」= 一个 item，可含 1 道或多道题（真考一场 = 4 题）。
// 每道题 question 结构：
//   q          题目原文
//   outline    思路表格：观点 / 原因一(+展开bullets) / 原因二(+展开bullets)
//   model      范文，按 8 句骨架逐句：{mk:引导词, role:结构名, en:句子, optional:是否可省}
//   words      范文词数
//   frames     常见「框架表达」拆解：{t:表达, zh:中文用法}
//   vocab      有用「单词/搭配」拆解：{w:词, ipa:音标, zh:中文}
window.INTERVIEW_BANK = [
  {
    id: "financial-planning",
    title: "理财规划 Financial Planning",
    topic: "生活观点",
    questions: [
      {
        q: "Do you think detailed financial planning is important? Why or why not?",
        outline: [
          { role: "观点",   text: "detailed financial planning is very important" },
          { role: "原因一", text: "make more money" },
          { role: "展开",   bullets: ["choose better investments", "stocks with higher returns", "a more stable financial future"] },
          { role: "原因二", text: "avoid risks" },
          { role: "展开",   bullets: ["balance my investments", "safer + higher-return options", "adjust my plan & stay safe"] }
        ],
        model: [
          { mk: "Well,",          role: "观点",     en: "honestly, I think detailed financial planning is really important." },
          { mk: "First off,",     role: "原因一",   en: "it helps me make more money." },
          { mk: "This is because", role: "展开·为什么", en: "careful planning lets me pick better investments, like stocks with higher returns." },
          { mk: "So,",            role: "小结",     en: "over time, I build a more stable financial future." },
          { mk: "Besides,",       role: "原因二",   en: "it also helps me avoid risks." },
          { mk: "This is because", role: "展开·为什么", en: "I can balance my investments — for example, mixing safer options with higher-return ones." },
          { mk: "So,",            role: "小结",     en: "I can adjust my plan anytime and stay safe." },
          { mk: "Therefore,",     role: "收尾·可省", en: "detailed planning is really worth it.", optional: true }
        ],
        words: 76,
        frames: [
          { t: "Well, honestly, I think…",  zh: "开场表态：先亮观点" },
          { t: "First off, … / Besides, …", zh: "引出第一个 / 第二个理由" },
          { t: "This is because …",          zh: "给理由（告诉考官「为什么」）" },
          { t: "like / for example, …",      zh: "举个具体例子" },
          { t: "So, … / Therefore, …",       zh: "小结 / 收尾" }
        ],
        vocab: [
          { w: "financial planning", ipa: "/faɪˈnænʃl ˈplænɪŋ/", zh: "财务规划" },
          { w: "investment",         ipa: "/ɪnˈvestmənt/",       zh: "投资" },
          { w: "returns",            ipa: "/rɪˈtɜːrnz/",         zh: "回报，收益" },
          { w: "stable",             ipa: "/ˈsteɪbl/",           zh: "稳定的" },
          { w: "avoid risks",        ipa: "/əˈvɔɪd rɪsks/",      zh: "规避风险" },
          { w: "balance my investments", ipa: "",                zh: "平衡我的投资" }
        ]
      }
    ]
  }
];
