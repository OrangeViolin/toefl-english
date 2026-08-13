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
          {r:"成就", en:"A job I enjoy gives me a strong sense of achievement, and that pushes me to work harder.", ex:"For example, last month I finished a hard project. When I saw the final result, I felt really proud of myself. That good feeling made me want to do even better next time."},
          {r:"情感", en:"Also, doing work I love makes me happy every day, and money cannot buy that feeling.", ex:"For example, I wake up looking forward to my day, not dreading it. Even after a long day, I do not feel tired or bored. I go home smiling, which means more to me than a big salary."}
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
          {r:"方便", en:"Working from home is very convenient because I do not need to travel to work.", ex:"For example, I save two hours every day that I used to spend on the bus and subway. Now I can use that time to rest or finish more work, and I never worry about being late."},
          {r:"健康", en:"Also, working from home is good for my health, both body and mind.", ex:"For example, I can sleep a little longer and eat a warm home-made lunch. I do not sit in noisy, crowded trains every morning, so I feel calm and not so tired all day."}
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
          {r:"交流", en:"Studying with a group helps me talk with others and learn from them directly.", ex:"For example, when I do not understand a math problem, my classmates can explain it to me in a simple way. I also share my own ideas, so we all learn faster together."},
          {r:"乐趣", en:"Also, studying with friends is more fun and much less boring.", ex:"For example, we can take short breaks together and tell jokes. When I study for a long time, laughing with my friends keeps me awake and happy, so I do not feel sleepy and I can keep going."}
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
          {r:"经济", en:"Online classes help me save a lot of money, which is a big deal for a student.", ex:"For example, I do not need to pay for bus tickets or rent a room near school. I can use that saved money to buy more books, and my family does not have to worry about extra costs."},
          {r:"方便", en:"Also, online classes are very convenient because I can study from anywhere.", ex:"For example, I can watch the class at home at any time and even replay it if I miss something. I do not have to wake up early to catch a bus, so I can learn in a relaxed way."}
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
          {r:"效率", en:"Learning AI can help students do their work much faster and with less effort.", ex:"For example, AI helps me write a report or find information in just a few seconds. This saves me a lot of time, so I can spend that time on other important things."},
          {r:"经验", en:"Also, learning AI gives students useful experience for the future job market.", ex:"For example, many companies now look for workers who know AI, and this skill can make me stand out. If I learn it early in college, I will have a better chance to get a good job later."}
        ],
        close:"So that's why I think college students should learn AI."
      }
    }
  ]
};
