// 领域题库：工作与教育
// 万能理由库见 ../reasons.js（12 个：方便/效率/经济/耐用/安全/环保/交流/经验/乐趣/成就/情感/健康）
// 每题答案 = stance(立场) + body(2 个理由，r 标注中文万能理由名) + close(收尾)
window.DOMAIN_work = {
  id:"work", title:"工作与教育", icon:"💼", desc:"职业选择 · 工作生活平衡 · 学习方式 · 教育趋势",
  questions:[
    {
      q:"When choosing a job, which is more important to you: salary or satisfaction? Why?",
      reasons:["成就","情感"],
      answer:{
        stance:"I think satisfaction is more important than salary.",
        body:[
          {r:"成就", en:"A job I enjoy gives me a strong sense of achievement.", ex:"For example, when I finish a hard task and see the result, I feel really proud of myself and want to do even better."},
          {r:"情感", en:"Also, doing work I love makes me happy every day.", ex:"For example, I wake up looking forward to my day, and I do not feel tired or bored even after a long day."}
        ],
        close:"So that's why I would choose satisfaction over salary."
      }
    },
    {
      q:"Some people prefer working from home, while others prefer working in an office. Which do you prefer and why?",
      reasons:["方便","健康"],
      answer:{
        stance:"I prefer working from home.",
        body:[
          {r:"方便", en:"Working from home is very convenient because I do not need to travel to work.", ex:"For example, I save two hours every day on the bus and subway, so I have more time for my work."},
          {r:"健康", en:"Also, working from home is good for my health.", ex:"For example, I can sleep a little longer and eat a home-made lunch, so I feel more relaxed and not so tired."}
        ],
        close:"So that's why I prefer working from home."
      }
    },
    {
      q:"Some students prefer to study alone, while others prefer to study with a group. Which do you prefer and why?",
      reasons:["交流","乐趣"],
      answer:{
        stance:"I prefer to study with a group.",
        body:[
          {r:"交流", en:"Studying with a group helps me talk with others and learn from them.", ex:"For example, when I do not understand a math problem, my classmates can explain it to me in a simple way."},
          {r:"乐趣", en:"Also, studying with friends is more fun and less boring.", ex:"For example, we can take short breaks together and laugh, so I do not feel sleepy after a long time."}
        ],
        close:"So that's why I prefer studying with a group."
      }
    },
    {
      q:"Some people think online classes are better than in-person classes. Do you agree or disagree and why?",
      reasons:["经济","方便"],
      answer:{
        stance:"I agree that online classes are better.",
        body:[
          {r:"经济", en:"Online classes help me save a lot of money.", ex:"For example, I do not need to pay for bus tickets or rent a room near school, so I can use that money to buy more books."},
          {r:"方便", en:"Also, online classes are very convenient.", ex:"For example, I can study at home at any time, and I do not have to wake up early to catch a bus."}
        ],
        close:"So that's why I think online classes are better."
      }
    },
    {
      q:"Do you think college students should learn about AI (artificial intelligence)? Why or why not?",
      reasons:["效率","经验"],
      answer:{
        stance:"Yes, I think college students should learn about AI.",
        body:[
          {r:"效率", en:"Learning AI can help students do their work much faster.", ex:"For example, AI can help me write a report or find information in a few seconds, so I save a lot of time."},
          {r:"经验", en:"Also, learning AI gives students useful experience for the future.", ex:"For example, many companies now want workers who know AI, so this skill will help me get a good job later."}
        ],
        close:"So that's why I think college students should learn AI."
      }
    }
  ]
};
