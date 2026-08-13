// 领域题库：个人发展与价值观（自信心 · 独立性 · 自律性 · 幸福感来源）
// 理由全部取自 12 个万能理由（见 reasons.js），r 字段填中文名
window.DOMAIN_personal = {
  id:"personal", title:"个人发展与价值观", icon:"🌱", desc:"自信 · 独立 · 自律 · 幸福",
  questions:[
    {
      q:"Do you think traveling helps people become more confident? Why or why not?",
      reasons:["经验","成就"],
      answer:{
        stance:"Yes, I think traveling makes people more confident.",
        body:[
          {r:"经验", en:"First, traveling gives you a lot of real experience in new situations.", ex:"For example, when I traveled to Beijing by myself last year, I had to book a hotel, take the subway, and ask strangers for directions. I made a few mistakes, but I learned how to fix them on my own. That made me feel much stronger."},
          {r:"成就", en:"Second, it gives you a strong sense of achievement.", ex:"For example, I once got lost in a foreign city and could not read the signs. But I used a map and asked local people, and finally found my hotel by myself. When I made it back, I felt really proud."}
        ],
        close:"So that is why I believe traveling builds confidence."
      }
    },
    {
      q:"Do you think playing sports helps people become more self-disciplined? Why or why not?",
      reasons:["健康","乐趣"],
      answer:{
        stance:"Yes, I think sports help people become more self-disciplined.",
        body:[
          {r:"健康", en:"First, sports keep you healthy, and staying healthy needs a regular plan.", ex:"For example, I run every morning at six, so I have to go to bed early and get up on time. I have kept this habit for two years now, even in winter. It was hard at first, but now it is just part of my day."},
          {r:"乐趣", en:"Second, sports are fun, so you want to keep doing them.", ex:"For example, I love playing basketball with my friends every weekend. We have a small team, and I do not want to let them down. So even when I am tired, I still show up and play."}
        ],
        close:"So that is why I think sports teach people self-discipline."
      }
    },
    {
      q:"Do you think having a hobby is necessary for happiness? Why or why not?",
      reasons:["情感","交流"],
      answer:{
        stance:"Yes, I think a hobby is necessary for happiness.",
        body:[
          {r:"情感", en:"First, a hobby makes you feel calm and happy inside.", ex:"For example, after a long and tiring day at school, I like to listen to music or draw. It helps me forget my worries and my body relaxes. When I finish a small drawing, I feel fresh and peaceful again."},
          {r:"交流", en:"Second, a hobby helps you meet people and make friends.", ex:"For example, I joined a running club last year. At first I did not know anyone, but we started talking after each run. Now I have several good friends there, and we eat together every week."}
        ],
        close:"So that is why I believe a hobby is an important part of happiness."
      }
    },
    {
      q:"Do you agree that it is important for young people to be independent? Why or why not?",
      reasons:["效率","经验"],
      answer:{
        stance:"Yes, I think it is very important for young people to be independent.",
        body:[
          {r:"效率", en:"First, when you are independent, you do not wait for others, so you finish things faster.", ex:"For example, when I do my homework, I do not wait for my parents to help me. I work it out myself first. So I usually finish before dinner and still have free time."},
          {r:"经验", en:"Second, being independent gives you valuable experience for life.", ex:"For example, I learned to cook my own meals last summer. At first my rice was too soft and my eggs were burned. But I kept trying, and now I can make a simple dinner by myself. That skill will help me for the rest of my life."}
        ],
        close:"So that is why I think independence is important."
      }
    },
    {
      q:"Do you think people can be happy even if they do not have a lot of money? Why or why not?",
      reasons:["情感","乐趣"],
      answer:{
        stance:"Yes, I think people can be happy without a lot of money.",
        body:[
          {r:"情感", en:"First, happiness mostly comes from love and friendship, not from money.", ex:"For example, I feel happiest when I eat dinner with my family and we talk about our day. That moment costs almost nothing. But it means more to me than any expensive gift."},
          {r:"乐趣", en:"Second, you can still have fun with simple, free things.", ex:"For example, I love taking a walk in the park near my home. I watch the trees and listen to the birds, and it makes me feel good. Reading a book from the library is free too, but I enjoy it very much."}
        ],
        close:"So that is why I believe money is not the key to happiness."
      }
    }
  ]
};
