// 领域题库：健康（运动习惯 · 饮食健康 · 心理健康）
// 理由全部取自 12 个万能理由（见 reasons.js），r 字段填中文名
window.DOMAIN_health = {
  id:"health", title:"健康", icon:"🏃", desc:"运动习惯 · 饮食健康 · 心理健康",
  questions:[
    {
      q:"What kind of exercise do you like to do? Why?",
      reasons:["健康","乐趣"],
      answer:{
        stance:"I really like jogging in the park near my home.",
        body:[
          {r:"健康", en:"First, jogging keeps my body strong and my heart healthy.", ex:"For example, I jog three times a week, and after that I sleep better at night. I also do not get tired easily during the day, so I can study for a long time."},
          {r:"乐趣", en:"Second, jogging makes me feel relaxed and happy.", ex:"For example, I listen to my favorite music while I run, and I look at the trees and flowers along the way. After each run, I always feel fresh and full of energy, so I look forward to it every time."}
        ],
        close:"So that is why jogging is my favorite kind of exercise."
      }
    },
    {
      q:"Do you think it is important to eat healthy food? Why or why not?",
      reasons:["健康","经济"],
      answer:{
        stance:"Yes, I think eating healthy food is very important, and I try to do it every day.",
        body:[
          {r:"健康", en:"First, healthy food keeps my body strong and stops me from getting sick.", ex:"For example, I eat vegetables and fruit every day, so I rarely catch a cold and I always feel full of energy. I can also think clearly in class."},
          {r:"经济", en:"Second, eating healthy food also helps me save money.", ex:"For example, I cook simple meals with rice and vegetables at home, so I spend much less than buying fast food every day. I can use the extra money to buy books or save it."}
        ],
        close:"So that is why I believe healthy eating matters a lot."
      }
    },
    {
      q:"Do you think going to bed and getting up at the same time every day is important? Why?",
      reasons:["健康","效率"],
      answer:{
        stance:"Yes, I think keeping a regular sleep schedule is very important.",
        body:[
          {r:"健康", en:"First, sleeping at the same time every day keeps my body and my brain healthy.", ex:"For example, when I go to bed at the same time every night, I wake up full of energy. I do not get sick easily, and my head feels clear all day."},
          {r:"效率", en:"Second, a regular routine helps me use my time well during the day.", ex:"For example, when I get up early, I have time to review my English before class. Then I finish my homework faster, and I still have free time to relax."}
        ],
        close:"So that is why I believe a regular routine matters."
      }
    },
    {
      q:"Some people think mental health is just as important as physical health. Do you agree? Why?",
      reasons:["健康","交流"],
      answer:{
        stance:"I agree that mental health is just as important as physical health.",
        body:[
          {r:"健康", en:"First, a healthy mind helps the whole body work well.", ex:"For example, when I feel calm and happy, I sleep better at night. I also have more energy to do my homework and to play sports."},
          {r:"交流", en:"Second, good mental health helps me get along with people around me.", ex:"For example, when I am in a good mood, I talk more with my family and friends, so we become closer. When I am happy, I also smile more, and people like to be with me."}
        ],
        close:"So that is why I think we should take care of our mind as much as our body."
      }
    },
    {
      q:"When you feel stressed, what do you usually do to relax? Why?",
      reasons:["乐趣","交流"],
      answer:{
        stance:"When I feel stressed, I usually go for a walk with my best friend.",
        body:[
          {r:"乐趣", en:"First, walking outside makes me feel relaxed and happy, and it clears my head.", ex:"For example, I look at the trees and the sky, and I breathe in the fresh air. After just a short walk, my worry slowly goes away and I feel calm again."},
          {r:"交流", en:"Second, talking with my friend also helps me feel better.", ex:"For example, I tell her about my problems, and she listens carefully and gives me advice. After we talk, I feel much lighter and I can smile again."}
        ],
        close:"So that is why walking with a friend is my favorite way to relax."
      }
    }
  ]
};
