// 领域题库：公共生活（城市体验 · 公园 · 通勤 · 购物 · 绿色空间）
// 格式：每道题一个参考答案 = stance + body(2 理由) + close
// 理由从 12 个万能理由里选，r 字段填中文名，见 reasons.js
window.DOMAIN_public = {
  id:"public", title:"公共生活", icon:"🏙", desc:"城市体验 · 公园 · 通勤 · 购物 · 绿色空间",
  questions:[
    {
      q:"Do you prefer living in a big city or a small town? Why?",
      reasons:["方便","交流"],
      answer:{
        stance:"I prefer living in a big city, and I have two main reasons.",
        body:[
          {r:"方便", en:"First, it is very convenient, because everything I need is close by.", ex:"For example, I can walk to a supermarket in five minutes, and there are many restaurants and hospitals near my home. When I need anything, I can get it quickly without traveling far."},
          {r:"交流", en:"Second, living in a big city also helps me meet new people and make friends easily.", ex:"For example, the city has many events and activities, so I can join a club or a sports game on the weekend. I can also talk with people from different places and learn new things from them."}
        ],
        close:"So that is why I would choose to live in a big city."
      }
    },
    {
      q:"Do you think cities should have more parks and green spaces? Why or why not?",
      reasons:["健康","环保"],
      answer:{
        stance:"Yes, I think cities should have more parks and green spaces.",
        body:[
          {r:"健康", en:"First, parks give people a clean and quiet place to relax and exercise.", ex:"For example, I go running in the park near my home every morning, and it makes me feel healthy and energetic. After a long day, I also like to take a walk there to feel relaxed."},
          {r:"环保", en:"Second, more trees and grass make the air cleaner and the city cooler.", ex:"For example, the trees in a park clean the dirty air and give us fresh air to breathe. In summer, green spaces also keep the city from getting too hot."}
        ],
        close:"So I believe more green spaces are very good for a city."
      }
    },
    {
      q:"Do you prefer taking the bus or driving your own car to work? Why?",
      reasons:["经济","效率"],
      answer:{
        stance:"I prefer taking the bus to work.",
        body:[
          {r:"经济", en:"First, taking the bus saves me a lot of money.", ex:"For example, a bus ticket costs only two yuan, but driving a car costs much more for gas and parking. I can save that money for other things I like, and over a month the savings really add up."},
          {r:"效率", en:"Second, I can use my time well while riding the bus.", ex:"For example, I read a book or listen to English on my way to work every day. This way, I study a little bit every morning and feel productive, and when I get off the bus I feel ready for my day."}
        ],
        close:"So the bus is a cheaper and smarter way to go to work."
      }
    },
    {
      q:"Do you prefer shopping in a big mall or online? Why?",
      reasons:["方便","经济"],
      answer:{
        stance:"I prefer shopping online.",
        body:[
          {r:"方便", en:"First, shopping online is very convenient, because I can buy things without leaving my home.", ex:"For example, I can order food, clothes and books with just my phone, and they are delivered right to my door. I can shop at night or on a rainy day, whenever I want, so it saves me a lot of time and energy."},
          {r:"经济", en:"Second, it also helps me save money.", ex:"For example, online shops often have lower prices and big sales, so I can buy the same thing for less. I can also compare prices easily to find the best deal, and this helps my family spend less money."}
        ],
        close:"So I like to shop online more than in a mall."
      }
    },
    {
      q:"Do you think the government should build more public libraries? Why or why not?",
      reasons:["经验","乐趣"],
      answer:{
        stance:"Yes, I think the government should build more public libraries.",
        body:[
          {r:"经验", en:"First, libraries help people learn new things for free.", ex:"For example, I can borrow books about history and science without paying any money. I have learned many new ideas there that I could not find in school, and these books are open to everyone, rich or poor."},
          {r:"乐趣", en:"Second, reading in a quiet library is relaxing and fun.", ex:"For example, I like to spend my weekends reading my favorite stories there. The quiet room makes me feel comfortable, and I always enjoy my time there, so I often bring my friends and we read side by side."}
        ],
        close:"So public libraries are good for everyone, and we should build more of them."
      }
    }
  ]
};
