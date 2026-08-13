// 自定义面试情景库（Take an Interview）
// 用户每次给题目 → 在这里追加一个对象 → 页面自动出现该套模考
// 每套 = 1 个情景开场白 + 4 个问题，覆盖两个信息模块：
//   ① 个人经历与感受的描述   ② 社会议题的观点表达与论证
window.INTERVIEWS = [
  {
    id: "fashion",
    title: "服装选择与时尚观念",
    scenario: "研究访谈 · 服装与时尚",
    intro: "Thank you for speaking with me today. I'm conducting a study about people's clothing choices and opinions about fashion.",
    questions: [
      { text: "First, do you try to wear fashionable clothes? Why or why not?", module: "① 个人经历与感受" },
      { text: "Can you describe a piece of clothing that is especially meaningful to you, and tell me why?", module: "① 个人经历与感受" },
      { text: "How much do you think the way a person dresses affects the way others treat them?", module: "①→② 过渡" },
      { text: "Some people argue that the fashion industry encourages people to buy too much and harms the environment. What is your opinion?", module: "② 社会议题观点论证" }
    ]
  }
];
