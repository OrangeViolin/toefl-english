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
          {r:"经验", en:"Traveling gives you valuable experience dealing with new situations.", ex:"For example, when I travel alone, I have to book hotels, ask for directions, and solve problems all by myself."},
          {r:"成就", en:"It also gives you a strong sense of achievement.", ex:"For example, finding my way in a foreign city makes me feel really proud."}
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
          {r:"健康", en:"Sports keep you healthy, and staying healthy needs a regular plan.", ex:"For example, I run every morning, so I have to get up early and keep this habit day after day."},
          {r:"乐趣", en:"Sports are also fun, so you want to keep doing them.", ex:"For example, I enjoy playing basketball with my friends, so I never want to miss our games."}
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
          {r:"情感", en:"A hobby makes you feel calm and happy inside.", ex:"For example, after a long and tiring day, I listen to music or draw, and I feel relaxed again."},
          {r:"交流", en:"A hobby also helps you meet people and make friends.", ex:"For example, I joined a running club last year, and now I have many good friends to talk with."}
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
          {r:"效率", en:"When you are independent, you do not wait for others, so you finish things faster.", ex:"For example, when I do my homework by myself, I do not wait for my parents to help me."},
          {r:"经验", en:"Being independent also gives you valuable experience.", ex:"For example, when I cook my own meals, I learn how to take care of myself."}
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
          {r:"情感", en:"Happiness mostly comes from love and friendship, not from money.", ex:"For example, I feel very happy when I eat dinner with my family, and this costs almost nothing."},
          {r:"乐趣", en:"You can also have fun with simple, free things.", ex:"For example, I love taking a walk in the park or reading a book at home, and they do not cost any money."}
        ],
        close:"So that is why I believe money is not the key to happiness."
      }
    }
  ]
};
