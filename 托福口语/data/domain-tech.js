// 领域题库：科技（社交媒体 · 人工智能 · 数字设备）
// 格式：每道题一个参考答案 = stance + body(2 理由) + close
// 理由从 12 个万能理由里选，r 字段填中文名，见 reasons.js
window.DOMAIN_tech = {
  id:"tech", title:"科技", icon:"📱", desc:"社交媒体 · 人工智能 · 数字设备",
  questions:[
    {
      q:"Do you prefer to talk with your friends through social media or face to face? Why?",
      reasons:["方便","交流"],
      answer:{
        stance:"I prefer to talk with my friends through social media.",
        body:[
          {r:"方便", en:"First of all, it is very convenient, because I can talk with them anytime and anywhere.", ex:"For example, I can send a quick message to my best friend while I am on the bus or waiting in line for food. Even when I only have one minute, I can still say hello and share a short photo."},
          {r:"交流", en:"Also, it helps me stay close to friends who live far away.", ex:"For example, my old classmate moved to another city last year. We call each other every weekend and talk about our daily life, so we still feel like we see each other often."}
        ],
        close:"So that is why I like talking through social media more than face to face."
      }
    },
    {
      q:"Do you think technology has a good or bad effect on people's mental health? Why?",
      reasons:["健康","情感"],
      answer:{
        stance:"I think technology has a bad effect on people's mental health.",
        body:[
          {r:"健康", en:"First of all, spending too much time on phones and computers is bad for our health.", ex:"For example, I often use my phone late at night to watch short videos. I end up sleeping very late and feel tired the next day. The next morning, I cannot focus well in class."},
          {r:"情感", en:"Also, it makes people feel less connected to each other in real life.", ex:"For example, my family used to chat happily at dinner. But now everyone looks at their own screen and says very little."}
        ],
        close:"So I think technology does more harm than good to our mental health."
      }
    },
    {
      q:"Do you prefer shopping online or shopping in stores? Why?",
      reasons:["经济","方便"],
      answer:{
        stance:"I prefer shopping online to shopping in stores.",
        body:[
          {r:"经济", en:"First of all, it is usually cheaper, because I can compare prices easily.", ex:"For example, last month I wanted to buy a new pair of shoes. I found the same shoes online for half the price, so I saved a lot of money."},
          {r:"方便", en:"Also, it is very convenient, because I can buy things without leaving home. It saves me a lot of time and trouble.", ex:"For example, when it rains or snows, I just order what I need on my phone and wait at home. The package comes to my door in a few days."}
        ],
        close:"So that is why I like shopping online more than going to stores."
      }
    },
    {
      q:"Do you think AI will help people in their work and study, or hurt them? Why?",
      reasons:["效率","经验"],
      answer:{
        stance:"I think AI will help people in their work and study.",
        body:[
          {r:"效率", en:"First of all, AI can help us finish our work much faster.", ex:"For example, I use a translation tool to read English articles every day. It turns hard sentences into Chinese in one second, so it saves me a lot of time."},
          {r:"经验", en:"Also, AI gives us a chance to learn new things more easily.", ex:"For example, when I do not understand a math problem, I ask an AI helper to explain it step by step. It is like having a patient teacher next to me."}
        ],
        close:"So I believe AI will bring more good than bad to our work and study."
      }
    },
    {
      q:"Which piece of technology can you not live without? Why?",
      reasons:["交流","乐趣"],
      answer:{
        stance:"The piece of technology I cannot live without is my smartphone.",
        body:[
          {r:"交流", en:"First of all, my phone helps me stay connected with my family and friends every day.", ex:"For example, I call my mom on my way home to tell her I am safe. I also send messages to my friends to plan where we will meet."},
          {r:"乐趣", en:"Also, it brings me a lot of fun in my free time.", ex:"For example, when I am tired after class, I watch short videos and listen to music on my phone. It helps me relax and feel happy again. Even when I am alone, I never feel bored."}
        ],
        close:"So my smartphone is the one thing I really cannot live without."
      }
    }
  ]
};
