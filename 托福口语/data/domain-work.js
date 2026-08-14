// 领域题库：工作与教育
// 万能理由库见 ../reasons.js（12 个：方便/效率/经济/耐用/安全/环保/交流/经验/乐趣/成就/情感/健康）
// 每题 answers = 3 版答案，同一立场同一理由，只分语言难度：
//   A「简单易背」短句简单词 · B「标准」中等 · C「高分丰富」高级词复杂句
window.DOMAIN_work = {
  id:"work", title:"工作与教育", icon:"💼", desc:"职业选择 · 工作生活平衡 · 学习方式 · 教育趋势",
  questions:[
    {
      q:"When choosing a job, which is more important to you: salary or satisfaction? Why?",
      reasons:["成就","情感"],
      answers:[
        {
          label:"简单易背", en:"Easy",
          stance:"I think satisfaction is more important than money.",
          body:[
            {r:"成就", en:"First, a job I like makes me feel proud of my work.", ex:"For example, when I finish something hard, I feel really good about myself."},
            {r:"情感", en:"Second, doing work I enjoy makes me happy every day.", ex:"For example, I am happy to go to work, and I do not feel tired."}
          ],
          close:"So satisfaction is more important to me."
        },
        {
          label:"标准", en:"Standard",
          stance:"I think satisfaction is more important than salary.",
          body:[
            {r:"成就", en:"A job I enjoy gives me a strong sense of achievement, and that pushes me to work harder.", ex:"For example, last month I finished a hard project. When I saw the final result, I felt really proud of myself. That good feeling made me want to do even better next time."},
            {r:"情感", en:"Also, doing work I love makes me happy every day, and money cannot buy that feeling.", ex:"For example, I wake up looking forward to my day, not dreading it. Even after a long day, I do not feel tired or bored. I go home smiling, which means more to me than a big salary."}
          ],
          close:"So that's why I would choose satisfaction over salary."
        },
        {
          label:"高分丰富", en:"Advanced",
          stance:"Personally, I believe job satisfaction outweighs salary in the long run.",
          body:[
            {r:"成就", en:"To begin with, meaningful work cultivates a genuine sense of accomplishment, which in turn fuels my motivation and drive.", ex:"For instance, after spending weeks on a challenging project, seeing the final product come together filled me with immense pride — and that feeling inspired me to raise the bar even higher on the next one."},
            {r:"情感", en:"Beyond that, doing what I genuinely love brings me daily happiness that no paycheck can replace.", ex:"For example, I wake up every morning actually looking forward to the day ahead rather than dreading it. Even after long hours, I go home feeling fulfilled instead of drained."}
          ],
          close:"That's precisely why I would prioritize satisfaction over a higher salary."
        }
      ]
    },
    {
      q:"Some people prefer working from home, while others prefer working in an office. Which do you prefer and why?",
      reasons:["方便","健康"],
      answers:[
        {
          label:"简单易背", en:"Easy",
          stance:"I prefer working from home.",
          body:[
            {r:"方便", en:"First, it is convenient because I do not need to travel to work.", ex:"For example, I save two hours every day, and I can use that time to rest."},
            {r:"健康", en:"Second, it is good for my health.", ex:"For example, I can sleep more and eat a warm lunch at home, so I feel better all day."}
          ],
          close:"So I prefer working from home."
        },
        {
          label:"标准", en:"Standard",
          stance:"I prefer working from home.",
          body:[
            {r:"方便", en:"Working from home is very convenient because I do not need to travel to work.", ex:"For example, I save two hours every day that I used to spend on the bus and subway. Now I can use that time to rest or finish more work, and I never worry about being late."},
            {r:"健康", en:"Also, working from home is good for my health, both body and mind.", ex:"For example, I can sleep a little longer and eat a warm home-made lunch. I do not sit in noisy, crowded trains every morning, so I feel calm and not so tired all day."}
          ],
          close:"So that's why I prefer working from home."
        },
        {
          label:"高分丰富", en:"Advanced",
          stance:"I would definitely choose to work from home.",
          body:[
            {r:"方便", en:"For one thing, working remotely spares me the daily commute, which is both time-consuming and exhausting.", ex:"For example, I reclaim nearly two hours a day that I used to spend squeezed into crowded buses — time I can now invest in deep, focused work or simply in recharging."},
            {r:"健康", en:"For another, staying home does wonders for my physical and mental well-being.", ex:"For instance, I can get extra sleep, prepare a wholesome lunch, and avoid the constant noise and stress of rush-hour traffic, which leaves me calmer and more energetic all day."}
          ],
          close:"For these reasons, working from home is my clear preference."
        }
      ]
    },
    {
      q:"Some students prefer to study alone, while others prefer to study with a group. Which do you prefer and why?",
      reasons:["交流","乐趣"],
      answers:[
        {
          label:"简单易背", en:"Easy",
          stance:"I prefer studying with a group.",
          body:[
            {r:"交流", en:"First, I can talk with my classmates and learn from them.", ex:"For example, when I do not understand a problem, they can explain it to me."},
            {r:"乐趣", en:"Second, studying with friends is more fun.", ex:"For example, we can take breaks and laugh together, so I do not feel bored."}
          ],
          close:"So I like studying with a group."
        },
        {
          label:"标准", en:"Standard",
          stance:"I prefer to study with a group.",
          body:[
            {r:"交流", en:"Studying with a group helps me talk with others and learn from them directly.", ex:"For example, when I do not understand a math problem, my classmates can explain it to me in a simple way. I also share my own ideas, so we all learn faster together."},
            {r:"乐趣", en:"Also, studying with friends is more fun and much less boring.", ex:"For example, we can take short breaks together and tell jokes. When I study for a long time, laughing with my friends keeps me awake and happy, so I do not feel sleepy and I can keep going."}
          ],
          close:"So that's why I prefer studying with a group."
        },
        {
          label:"高分丰富", en:"Advanced",
          stance:"I'm a strong believer in group study.",
          body:[
            {r:"交流", en:"The main advantage is that discussing ideas with classmates deepens my understanding far more than studying alone.", ex:"For instance, when I'm stuck on a difficult math problem, a peer can explain it from a fresh angle — and by articulating my own thoughts in return, I solidify what I've learned."},
            {r:"乐趣", en:"What's more, studying with friends transforms the whole experience from a chore into something genuinely enjoyable.", ex:"For example, sharing short breaks and a few laughs keeps my energy up and my mind sharp, so I can stay focused for much longer without feeling drained."}
          ],
          close:"That's why I'd pick group study over studying alone."
        }
      ]
    },
    {
      q:"Some people think online classes are better than in-person classes. Do you agree or disagree and why?",
      reasons:["经济","方便"],
      answers:[
        {
          label:"简单易背", en:"Easy",
          stance:"I think online classes are better.",
          body:[
            {r:"经济", en:"First, they save me money.", ex:"For example, I do not need to pay for bus tickets or a room near school."},
            {r:"方便", en:"Second, they are convenient because I can study from home.", ex:"For example, I can watch the class any time and replay it if I miss something."}
          ],
          close:"So I think online classes are better."
        },
        {
          label:"标准", en:"Standard",
          stance:"I agree that online classes are better.",
          body:[
            {r:"经济", en:"Online classes help me save a lot of money, which is a big deal for a student.", ex:"For example, I do not need to pay for bus tickets or rent a room near school. I can use that saved money to buy more books, and my family does not have to worry about extra costs."},
            {r:"方便", en:"Also, online classes are very convenient because I can study from anywhere.", ex:"For example, I can watch the class at home at any time and even replay it if I miss something. I do not have to wake up early to catch a bus, so I can learn in a relaxed way."}
          ],
          close:"So that's why I think online classes are better."
        },
        {
          label:"高分丰富", en:"Advanced",
          stance:"In my view, online classes hold a clear edge over traditional in-person ones.",
          body:[
            {r:"经济", en:"For one thing, they are far more economical — a significant advantage for a student on a budget.", ex:"For example, I save on transportation and the cost of renting near campus, which frees up money for books and other essentials while easing the financial burden on my family."},
            {r:"方便", en:"For another, the flexibility is unmatched, since I can learn from virtually anywhere.", ex:"For instance, I can attend a lecture at home, pause and replay it whenever I miss a point, and structure my day without the stress of an early-morning commute."}
          ],
          close:"All things considered, online classes are the better choice for me."
        }
      ]
    },
    {
      q:"Do you think college students should learn about AI (artificial intelligence)? Why or why not?",
      reasons:["效率","经验"],
      answers:[
        {
          label:"简单易背", en:"Easy",
          stance:"Yes, I think college students should learn about AI.",
          body:[
            {r:"效率", en:"First, AI helps students finish their work faster.", ex:"For example, AI can help me write a report in a few minutes, so I save a lot of time."},
            {r:"经验", en:"Second, learning AI gives students useful skills for the future.", ex:"For example, many companies want workers who know AI, so I can get a better job later."}
          ],
          close:"So college students should learn AI."
        },
        {
          label:"标准", en:"Standard",
          stance:"Yes, I think college students should learn about AI.",
          body:[
            {r:"效率", en:"Learning AI can help students do their work much faster and with less effort.", ex:"For example, AI helps me write a report or find information in just a few seconds. This saves me a lot of time, so I can spend that time on other important things."},
            {r:"经验", en:"Also, learning AI gives students useful experience for the future job market.", ex:"For example, many companies now look for workers who know AI, and this skill can make me stand out. If I learn it early in college, I will have a better chance to get a good job later."}
          ],
          close:"So that's why I think college students should learn AI."
        },
        {
          label:"高分丰富", en:"Advanced",
          stance:"Absolutely — I believe every college student should learn about AI.",
          body:[
            {r:"效率", en:"To begin with, AI dramatically boosts productivity, enabling students to accomplish in minutes what used to take hours.", ex:"For example, AI can help me draft a report, locate reliable sources, or summarize a long article in seconds, freeing up valuable time for deeper learning."},
            {r:"经验", en:"Moreover, AI literacy has become an indispensable credential in today's job market, giving students a competitive edge.", ex:"For instance, a growing number of employers actively seek candidates who can work with AI tools, and mastering these skills early gives me a real head start when I graduate."}
          ],
          close:"In short, learning AI is no longer optional — it's essential for college students."
        }
      ]
    }
  ]
};
