// 听力复述题库 · 10 场景 × 21 句（7 短 + 7 中 + 7 长）
// 由 data/_build_lr.py 从 data/lr-parts/*.json 组装，勿手改本文件
// 每句: {en, zh, lv(简单/中等/困难), tier(short/medium/long), chunks[], skeleton[]}
window.LR_SCENES = [
 {
  "id": "zoo",
  "name": "🦒 动物园",
  "en": "Zoo",
  "desc": "欢迎语·喂食时间·参观规则·导览路线·动物馆区·闭园·门票·纪念品店",
  "items": [
   {
    "en": "Welcome to the city zoo.",
    "zh": "欢迎来到城市动物园。",
    "lv": "简单",
    "chunks": [
     "Welcome to",
     "the city zoo."
    ],
    "skeleton": [
     "欢迎来到",
     "城市动物园。"
    ],
    "tier": "short"
   },
   {
    "en": "The penguins are being fed now.",
    "zh": "企鹅现在正在喂食。",
    "lv": "简单",
    "chunks": [
     "The penguins",
     "are being fed now."
    ],
    "skeleton": [
     "企鹅",
     "正在被喂食。"
    ],
    "tier": "short"
   },
   {
    "en": "Please do not feed the animals.",
    "zh": "请不要给动物喂食。",
    "lv": "简单",
    "chunks": [
     "Please do not",
     "feed the animals."
    ],
    "skeleton": [
     "请不要",
     "喂动物。"
    ],
    "tier": "short"
   },
   {
    "en": "The reptile house is straight ahead.",
    "zh": "爬行动物馆就在正前方。",
    "lv": "简单",
    "chunks": [
     "The reptile house",
     "is straight ahead."
    ],
    "skeleton": [
     "爬行动物馆",
     "在正前方。"
    ],
    "tier": "short"
   },
   {
    "en": "Flash photography is not allowed here.",
    "zh": "这里不允许使用闪光灯拍照。",
    "lv": "简单",
    "chunks": [
     "Flash photography",
     "is not allowed here."
    ],
    "skeleton": [
     "闪光灯拍照",
     "这里不允许。"
    ],
    "tier": "short"
   },
   {
    "en": "The zoo closes at six tonight.",
    "zh": "动物园今晚六点闭园。",
    "lv": "简单",
    "chunks": [
     "The zoo closes",
     "at six tonight."
    ],
    "skeleton": [
     "动物园闭园",
     "今晚六点。"
    ],
    "tier": "short"
   },
   {
    "en": "Tickets are sold at the entrance.",
    "zh": "门票在入口处出售。",
    "lv": "简单",
    "chunks": [
     "Tickets are sold",
     "at the entrance."
    ],
    "skeleton": [
     "门票出售",
     "在入口处。"
    ],
    "tier": "short"
   },
   {
    "en": "Please do not feed the animals by hand.",
    "zh": "请不要用手给动物喂食。",
    "lv": "中等",
    "chunks": [
     "Please do not feed",
     "the animals",
     "by hand."
    ],
    "skeleton": [
     "请不要喂",
     "动物",
     "用手。"
    ],
    "tier": "medium"
   },
   {
    "en": "The reptile house is just past the café.",
    "zh": "爬行动物馆就在咖啡馆过去一点。",
    "lv": "中等",
    "chunks": [
     "The reptile house",
     "is just past",
     "the café."
    ],
    "skeleton": [
     "爬行动物馆",
     "就在过了",
     "咖啡馆。"
    ],
    "tier": "medium"
   },
   {
    "en": "The guided tour starts near the main gate.",
    "zh": "导览团在正门附近出发。",
    "lv": "中等",
    "chunks": [
     "The guided tour",
     "starts near",
     "the main gate."
    ],
    "skeleton": [
     "导览团",
     "出发地点靠近",
     "正门。"
    ],
    "tier": "medium"
   },
   {
    "en": "The elephants are fed twice on most afternoons.",
    "zh": "大象在大多数下午都喂食两次。",
    "lv": "中等",
    "chunks": [
     "The elephants",
     "are fed twice",
     "on most afternoons."
    ],
    "skeleton": [
     "大象",
     "被喂食两次",
     "在多数下午。"
    ],
    "tier": "medium"
   },
   {
    "en": "The gift shop stays open until closing time.",
    "zh": "纪念品店一直营业到闭园时间。",
    "lv": "中等",
    "chunks": [
     "The gift shop",
     "stays open",
     "until closing time."
    ],
    "skeleton": [
     "纪念品店",
     "保持营业",
     "直到闭园时间。"
    ],
    "tier": "medium"
   },
   {
    "en": "Please keep your ticket for re-entry to the zoo.",
    "zh": "请保管好门票以便重新进入动物园。",
    "lv": "中等",
    "chunks": [
     "Please keep your ticket",
     "for re-entry",
     "to the zoo."
    ],
    "skeleton": [
     "请保管好门票",
     "以便重新入园",
     "进动物园。"
    ],
    "tier": "medium"
   },
   {
    "en": "The bird aviary is closed for cleaning this morning.",
    "zh": "鸟舍今天上午因清洁关闭。",
    "lv": "中等",
    "chunks": [
     "The bird aviary",
     "is closed for cleaning",
     "this morning."
    ],
    "skeleton": [
     "鸟舍",
     "因清洁关闭",
     "今天上午。"
    ],
    "tier": "medium"
   },
   {
    "en": "If you arrive before noon, you can watch the sea lions being trained.",
    "zh": "如果中午前到达，你可以观看海狮训练。",
    "lv": "困难",
    "chunks": [
     "If you arrive before noon,",
     "you can watch",
     "the sea lions",
     "being trained."
    ],
    "skeleton": [
     "如果中午前到达，",
     "你可以观看",
     "海狮",
     "被训练。"
    ],
    "tier": "long"
   },
   {
    "en": "The tigers, which arrived last spring, are in the enclosure on your left.",
    "zh": "去年春天到来的老虎，就在你左边的围栏里。",
    "lv": "困难",
    "chunks": [
     "The tigers,",
     "which arrived last spring,",
     "are in the enclosure",
     "on your left."
    ],
    "skeleton": [
     "老虎，",
     "去年春天到来的，",
     "在围栏里",
     "你的左边。"
    ],
    "tier": "long"
   },
   {
    "en": "If it starts to rain, the outdoor animal shows will be moved indoors soon.",
    "zh": "如果开始下雨，户外的动物表演将很快移到室内。",
    "lv": "困难",
    "chunks": [
     "If it starts to rain,",
     "the outdoor animal shows",
     "will be moved indoors soon."
    ],
    "skeleton": [
     "如果开始下雨，",
     "户外动物表演",
     "将很快移到室内。"
    ],
    "tier": "long"
   },
   {
    "en": "Visitors who bring young children can borrow the free strollers near the main entrance.",
    "zh": "带小孩的游客可以在正门附近借用免费的婴儿车。",
    "lv": "困难",
    "chunks": [
     "Visitors who bring young children",
     "can borrow the free strollers",
     "near the main entrance."
    ],
    "skeleton": [
     "带小孩的游客",
     "可以借用免费婴儿车",
     "在正门附近。"
    ],
    "tier": "long"
   },
   {
    "en": "Because the panda is resting, please stay quiet when you pass its habitat.",
    "zh": "因为熊猫在休息，经过它的场馆时请保持安静。",
    "lv": "困难",
    "chunks": [
     "Because the panda is resting,",
     "please stay quiet",
     "when you pass its habitat."
    ],
    "skeleton": [
     "因为熊猫在休息，",
     "请保持安静",
     "经过它的场馆时。"
    ],
    "tier": "long"
   },
   {
    "en": "When the zoo closes, an announcement that guides you to the exit will play.",
    "zh": "闭园时，会播放一则引导你前往出口的广播。",
    "lv": "困难",
    "chunks": [
     "When the zoo closes,",
     "an announcement",
     "that guides you to the exit",
     "will play."
    ],
    "skeleton": [
     "闭园时，",
     "一则广播",
     "引导你前往出口的",
     "会播放。"
    ],
    "tier": "long"
   },
   {
    "en": "The souvenirs that we sell in the gift shop are made by local artists nearby.",
    "zh": "我们纪念品店里出售的纪念品由附近的本地艺术家制作。",
    "lv": "困难",
    "chunks": [
     "The souvenirs",
     "that we sell in the gift shop",
     "are made by local artists",
     "nearby."
    ],
    "skeleton": [
     "纪念品",
     "我们纪念品店出售的",
     "由本地艺术家制作",
     "附近的。"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "gym",
  "name": "🏋️ 健身房",
  "en": "Gym",
  "desc": "签到·器械·更衣室·团课·预约·安全·会员卡·私教·营业时间·擦拭",
  "items": [
   {
    "en": "Please sign in at the desk.",
    "zh": "请在前台签到。",
    "lv": "简单",
    "chunks": [
     "Please sign in",
     "at the desk"
    ],
    "skeleton": [
     "请签到",
     "在前台"
    ],
    "tier": "short"
   },
   {
    "en": "Wipe down each machine after use.",
    "zh": "用完后请擦拭每台器械。",
    "lv": "简单",
    "chunks": [
     "Wipe down",
     "each machine",
     "after use"
    ],
    "skeleton": [
     "擦拭",
     "每台器械",
     "用完后"
    ],
    "tier": "short"
   },
   {
    "en": "Bring a towel and a bottle.",
    "zh": "请带一条毛巾和一个水瓶。",
    "lv": "简单",
    "chunks": [
     "Bring a towel",
     "and a bottle"
    ],
    "skeleton": [
     "带毛巾",
     "和水瓶"
    ],
    "tier": "short"
   },
   {
    "en": "The locker rooms are down the hall.",
    "zh": "更衣室在走廊尽头。",
    "lv": "简单",
    "chunks": [
     "The locker rooms",
     "are down the hall"
    ],
    "skeleton": [
     "更衣室",
     "在走廊尽头"
    ],
    "tier": "short"
   },
   {
    "en": "Free classes run every evening.",
    "zh": "每天晚上都有免费团课。",
    "lv": "简单",
    "chunks": [
     "Free classes",
     "run every evening"
    ],
    "skeleton": [
     "免费团课",
     "每晚开设"
    ],
    "tier": "short"
   },
   {
    "en": "Show your card to the staff.",
    "zh": "请向工作人员出示会员卡。",
    "lv": "简单",
    "chunks": [
     "Show your card",
     "to the staff"
    ],
    "skeleton": [
     "出示会员卡",
     "给工作人员"
    ],
    "tier": "short"
   },
   {
    "en": "The gym closes at ten.",
    "zh": "健身房十点关门。",
    "lv": "简单",
    "chunks": [
     "The gym",
     "closes at ten"
    ],
    "skeleton": [
     "健身房",
     "十点关门"
    ],
    "tier": "short"
   },
   {
    "en": "Please rack the weights neatly after every set.",
    "zh": "每组练完请把杠铃片整齐归位。",
    "lv": "中等",
    "chunks": [
     "Please rack the weights",
     "neatly",
     "after every set"
    ],
    "skeleton": [
     "请归位杠铃片",
     "整齐地",
     "每组练完后"
    ],
    "tier": "medium"
   },
   {
    "en": "You can book a private trainer at the front desk.",
    "zh": "你可以在前台预约私人教练。",
    "lv": "中等",
    "chunks": [
     "You can book",
     "a private trainer",
     "at the front desk"
    ],
    "skeleton": [
     "你可预约",
     "私人教练",
     "在前台"
    ],
    "tier": "medium"
   },
   {
    "en": "Group classes are posted on the board outside.",
    "zh": "团课时间表贴在外面的公告板上。",
    "lv": "中等",
    "chunks": [
     "Group classes",
     "are posted",
     "on the board outside"
    ],
    "skeleton": [
     "团课",
     "被张贴",
     "在外面公告板"
    ],
    "tier": "medium"
   },
   {
    "en": "Please return the dumbbells to their proper rack.",
    "zh": "请把哑铃放回正确的架子上。",
    "lv": "中等",
    "chunks": [
     "Please return",
     "the dumbbells",
     "to their proper rack"
    ],
    "skeleton": [
     "请放回",
     "哑铃",
     "到正确架子"
    ],
    "tier": "medium"
   },
   {
    "en": "Your membership card lets you in at any hour.",
    "zh": "你的会员卡可以随时刷卡进入。",
    "lv": "中等",
    "chunks": [
     "Your membership card",
     "lets you in",
     "at any hour"
    ],
    "skeleton": [
     "你的会员卡",
     "可让你进入",
     "在任何时候"
    ],
    "tier": "medium"
   },
   {
    "en": "Lockers are free, but bring your own lock.",
    "zh": "储物柜免费，但请自带锁。",
    "lv": "中等",
    "chunks": [
     "Lockers are free",
     "but bring",
     "your own lock"
    ],
    "skeleton": [
     "储物柜免费",
     "但请带",
     "你自己的锁"
    ],
    "tier": "medium"
   },
   {
    "en": "The pool reopens at six on weekday mornings.",
    "zh": "泳池工作日早上六点重新开放。",
    "lv": "中等",
    "chunks": [
     "The pool reopens",
     "at six",
     "on weekday mornings"
    ],
    "skeleton": [
     "泳池重开",
     "六点",
     "工作日早晨"
    ],
    "tier": "medium"
   },
   {
    "en": "If you are new here, a trainer can show you how the equipment works.",
    "zh": "如果你是新来的，教练可以教你器械怎么用。",
    "lv": "困难",
    "chunks": [
     "If you are new here",
     "a trainer can show you",
     "how the equipment works"
    ],
    "skeleton": [
     "如果你是新来的",
     "教练可教你",
     "器械怎么用"
    ],
    "tier": "long"
   },
   {
    "en": "Members who reserve a court online will always get priority during our busy hours.",
    "zh": "在线预约场地的会员在高峰时段始终享有优先权。",
    "lv": "困难",
    "chunks": [
     "Members who reserve a court online",
     "will always get priority",
     "during our busy hours"
    ],
    "skeleton": [
     "在线预约场地的会员",
     "将始终获优先权",
     "在我们高峰时段"
    ],
    "tier": "long"
   },
   {
    "en": "When a machine breaks down, please tell a staff member at the desk right away.",
    "zh": "当器械出故障时，请立刻到前台告诉工作人员。",
    "lv": "困难",
    "chunks": [
     "When a machine breaks down",
     "please tell a staff member at the desk",
     "right away"
    ],
    "skeleton": [
     "当器械故障",
     "请到前台告诉工作人员",
     "立刻"
    ],
    "tier": "long"
   },
   {
    "en": "If you feel dizzy or short of breath, stop and sit down immediately.",
    "zh": "如果你感到头晕或喘不上气，请立刻停下坐好。",
    "lv": "困难",
    "chunks": [
     "If you feel dizzy or short of breath",
     "stop and sit down",
     "immediately"
    ],
    "skeleton": [
     "如果你头晕或气短",
     "停下坐好",
     "立刻"
    ],
    "tier": "long"
   },
   {
    "en": "Classes that fill up quickly usually require you to sign up a day early.",
    "zh": "很快满员的团课通常需要你提前一天报名。",
    "lv": "困难",
    "chunks": [
     "Classes that fill up quickly",
     "usually require you",
     "to sign up a day early"
    ],
    "skeleton": [
     "很快满员的团课",
     "通常要求你",
     "提前一天报名"
    ],
    "tier": "long"
   },
   {
    "en": "Because the treadmills are limited, please keep your workout under thirty minutes at peak times.",
    "zh": "由于跑步机数量有限，高峰时段请把锻炼控制在三十分钟内。",
    "lv": "困难",
    "chunks": [
     "Because the treadmills are limited",
     "please keep your workout under thirty minutes",
     "at peak times"
    ],
    "skeleton": [
     "因跑步机有限",
     "请控制锻炼在三十分钟内",
     "高峰时段"
    ],
    "tier": "long"
   },
   {
    "en": "If your card expires this month, you can renew it at the desk today.",
    "zh": "如果你的会员卡本月到期，今天就可以在前台续费。",
    "lv": "困难",
    "chunks": [
     "If your card expires this month",
     "you can renew it",
     "at the desk today"
    ],
    "skeleton": [
     "如果卡本月到期",
     "你可续费",
     "今天在前台"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "orientation",
  "name": "🎓 迎新·咨询台",
  "en": "University Orientation / Info Booth",
  "desc": "迎新·领资料·校园导览·学生证·选课·答疑·宿舍·社团·校园卡·答疑志愿者",
  "items": [
   {
    "en": "Welcome to our new student orientation.",
    "zh": "欢迎参加我们的新生迎新。",
    "lv": "简单",
    "chunks": [
     "Welcome to",
     "our new student orientation"
    ],
    "skeleton": [
     "欢迎",
     "我们的新生迎新"
    ],
    "tier": "short"
   },
   {
    "en": "Pick up your orientation packet here.",
    "zh": "在这里领取你的迎新资料包。",
    "lv": "简单",
    "chunks": [
     "Pick up",
     "your orientation packet",
     "here"
    ],
    "skeleton": [
     "领取",
     "迎新资料包",
     "在这里"
    ],
    "tier": "short"
   },
   {
    "en": "Campus tours begin at the library.",
    "zh": "校园导览从图书馆出发。",
    "lv": "简单",
    "chunks": [
     "Campus tours begin",
     "at the library"
    ],
    "skeleton": [
     "校园导览开始",
     "在图书馆"
    ],
    "tier": "short"
   },
   {
    "en": "Your student ID is ready now.",
    "zh": "你的学生证现在已办好了。",
    "lv": "简单",
    "chunks": [
     "Your student ID",
     "is ready now"
    ],
    "skeleton": [
     "你的学生证",
     "现在已办好"
    ],
    "tier": "short"
   },
   {
    "en": "The housing office is right next door.",
    "zh": "宿舍办公室就在隔壁。",
    "lv": "简单",
    "chunks": [
     "The housing office",
     "is right next door"
    ],
    "skeleton": [
     "宿舍办公室",
     "就在隔壁"
    ],
    "tier": "short"
   },
   {
    "en": "Please sign in at the arrival desk.",
    "zh": "请在报到咨询台签到。",
    "lv": "简单",
    "chunks": [
     "Please sign in",
     "at the arrival desk"
    ],
    "skeleton": [
     "请签到",
     "在报到咨询台"
    ],
    "tier": "short"
   },
   {
    "en": "The student club fair begins at noon.",
    "zh": "学生社团招新中午开始。",
    "lv": "简单",
    "chunks": [
     "The student club fair",
     "begins at noon"
    ],
    "skeleton": [
     "学生社团招新",
     "中午开始"
    ],
    "tier": "short"
   },
   {
    "en": "Ask any volunteer in a blue shirt for help.",
    "zh": "有问题请找任何穿蓝衬衫的志愿者。",
    "lv": "中等",
    "chunks": [
     "Ask any volunteer",
     "in a blue shirt",
     "for help"
    ],
    "skeleton": [
     "找任何志愿者",
     "穿蓝衬衫的",
     "求助"
    ],
    "tier": "medium"
   },
   {
    "en": "Your campus card also works at the dining hall.",
    "zh": "你的校园卡在食堂也能用。",
    "lv": "中等",
    "chunks": [
     "Your campus card",
     "also works",
     "at the dining hall"
    ],
    "skeleton": [
     "你的校园卡",
     "也能用",
     "在食堂"
    ],
    "tier": "medium"
   },
   {
    "en": "Advisors are available all week to answer your questions.",
    "zh": "本周整周都有顾问解答你的问题。",
    "lv": "中等",
    "chunks": [
     "Advisors are available",
     "all week",
     "to answer your questions"
    ],
    "skeleton": [
     "顾问可预约",
     "整周",
     "解答你的问题"
    ],
    "tier": "medium"
   },
   {
    "en": "You can add your ID photo online later.",
    "zh": "你之后可以在线上传证件照。",
    "lv": "中等",
    "chunks": [
     "You can add",
     "your ID photo online",
     "later"
    ],
    "skeleton": [
     "你可上传",
     "证件照在线",
     "之后"
    ],
    "tier": "medium"
   },
   {
    "en": "Grab a campus map before you leave here.",
    "zh": "离开这里之前拿一张校园地图。",
    "lv": "中等",
    "chunks": [
     "Grab a campus map",
     "before you leave",
     "here"
    ],
    "skeleton": [
     "拿张校园地图",
     "在离开前",
     "这里"
    ],
    "tier": "medium"
   },
   {
    "en": "The bookstore offers a discount during orientation week.",
    "zh": "迎新周期间书店提供折扣。",
    "lv": "中等",
    "chunks": [
     "The bookstore offers a discount",
     "during orientation week"
    ],
    "skeleton": [
     "书店提供折扣",
     "迎新周期间"
    ],
    "tier": "medium"
   },
   {
    "en": "Parking permits are sold at the security office.",
    "zh": "停车证在保卫处出售。",
    "lv": "中等",
    "chunks": [
     "Parking permits",
     "are sold",
     "at the security office"
    ],
    "skeleton": [
     "停车证",
     "被出售",
     "在保卫处"
    ],
    "tier": "medium"
   },
   {
    "en": "If you have not chosen your classes, an advisor is available all week.",
    "zh": "如果你还没选课，本周整周都有顾问可以帮你。",
    "lv": "困难",
    "chunks": [
     "If you have not chosen your classes",
     "an advisor is available",
     "all week"
    ],
    "skeleton": [
     "如果你还没选课",
     "有顾问可预约",
     "整周"
    ],
    "tier": "long"
   },
   {
    "en": "Students who live on campus should collect their room keys before five o'clock.",
    "zh": "住校的学生应在五点前领取宿舍钥匙。",
    "lv": "困难",
    "chunks": [
     "Students who live on campus",
     "should collect their room keys",
     "before five o'clock"
    ],
    "skeleton": [
     "住校的学生",
     "应领宿舍钥匙",
     "五点前"
    ],
    "tier": "long"
   },
   {
    "en": "When you finish the campus tour, come back here to pick up your ID.",
    "zh": "参观完校园后，回到这里领取你的学生证。",
    "lv": "困难",
    "chunks": [
     "When you finish the campus tour",
     "come back here",
     "to pick up your ID"
    ],
    "skeleton": [
     "导览结束后",
     "回到这里",
     "领学生证"
    ],
    "tier": "long"
   },
   {
    "en": "The welcome packet includes a small course guide that lists every open elective.",
    "zh": "迎新资料包里有一本简明课程手册，列出所有开放的选修课。",
    "lv": "困难",
    "chunks": [
     "The welcome packet includes a small course guide",
     "that lists",
     "every open elective"
    ],
    "skeleton": [
     "资料包含简明课程手册",
     "它列出",
     "每门开放选修"
    ],
    "tier": "long"
   },
   {
    "en": "If your card does not scan, the help desk can reset it in minutes.",
    "zh": "如果你的卡刷不出来，服务台几分钟就能重置。",
    "lv": "困难",
    "chunks": [
     "If your card does not scan",
     "the help desk can reset it",
     "in minutes"
    ],
    "skeleton": [
     "如果卡刷不出",
     "服务台可重置",
     "几分钟内"
    ],
    "tier": "long"
   },
   {
    "en": "Any student who joins a club today will get a free tote bag.",
    "zh": "今天加入社团的学生都能领到一个免费帆布袋。",
    "lv": "困难",
    "chunks": [
     "Any student who joins a club today",
     "will get",
     "a free tote bag"
    ],
    "skeleton": [
     "今天加社团的学生",
     "将得到",
     "免费帆布袋"
    ],
    "tier": "long"
   },
   {
    "en": "Because the lines get long after lunch, please pick up your keys early.",
    "zh": "由于午餐后排队会很长，请早点来领钥匙。",
    "lv": "困难",
    "chunks": [
     "Because the lines get long after lunch",
     "please pick up your keys",
     "early"
    ],
    "skeleton": [
     "午餐后队伍长",
     "请领你的钥匙",
     "早点"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "library",
  "name": "📚 图书馆",
  "en": "Library",
  "desc": "开放时间·借阅·罚款·安静区·预约·数据库·打印·续借·馆际互借",
  "items": [
   {
    "en": "The library opens at eight.",
    "zh": "图书馆八点开门。",
    "lv": "简单",
    "chunks": [
     "The library",
     "opens at eight"
    ],
    "skeleton": [
     "图书馆",
     "八点开门"
    ],
    "tier": "short"
   },
   {
    "en": "Please return your books on time.",
    "zh": "请按时归还图书。",
    "lv": "简单",
    "chunks": [
     "Please return",
     "your books",
     "on time"
    ],
    "skeleton": [
     "请归还",
     "你的书",
     "按时"
    ],
    "tier": "short"
   },
   {
    "en": "You can borrow up to ten books.",
    "zh": "你最多可以借十本书。",
    "lv": "简单",
    "chunks": [
     "You can borrow",
     "up to ten books"
    ],
    "skeleton": [
     "你可以借",
     "最多十本书"
    ],
    "tier": "short"
   },
   {
    "en": "The quiet rooms are upstairs.",
    "zh": "安静自习室在楼上。",
    "lv": "简单",
    "chunks": [
     "The quiet rooms",
     "are upstairs"
    ],
    "skeleton": [
     "安静自习室",
     "在楼上"
    ],
    "tier": "short"
   },
   {
    "en": "Printing costs ten cents a page.",
    "zh": "打印每页一角钱。",
    "lv": "简单",
    "chunks": [
     "Printing costs",
     "ten cents",
     "a page"
    ],
    "skeleton": [
     "打印花费",
     "一角钱",
     "每页"
    ],
    "tier": "short"
   },
   {
    "en": "You may renew books online.",
    "zh": "你可以在线续借图书。",
    "lv": "简单",
    "chunks": [
     "You may renew",
     "books online"
    ],
    "skeleton": [
     "你可续借",
     "在线图书"
    ],
    "tier": "short"
   },
   {
    "en": "Please keep your voice down.",
    "zh": "请小声说话。",
    "lv": "简单",
    "chunks": [
     "Please keep",
     "your voice down"
    ],
    "skeleton": [
     "请保持",
     "小声"
    ],
    "tier": "short"
   },
   {
    "en": "Late returns are charged a small daily fine.",
    "zh": "逾期归还每天收取少量罚金。",
    "lv": "中等",
    "chunks": [
     "Late returns",
     "are charged",
     "a small daily fine"
    ],
    "skeleton": [
     "逾期归还",
     "被收取",
     "每日少量罚金"
    ],
    "tier": "medium"
   },
   {
    "en": "The quiet study rooms are on the third floor.",
    "zh": "安静自习室在三楼。",
    "lv": "中等",
    "chunks": [
     "The quiet study rooms",
     "are on the third floor"
    ],
    "skeleton": [
     "安静自习室",
     "在三楼"
    ],
    "tier": "medium"
   },
   {
    "en": "You can reserve a group room at the front desk.",
    "zh": "你可以在前台预约小组研讨室。",
    "lv": "中等",
    "chunks": [
     "You can reserve",
     "a group room",
     "at the front desk"
    ],
    "skeleton": [
     "你可预约",
     "小组研讨室",
     "在前台"
    ],
    "tier": "medium"
   },
   {
    "en": "Our online databases are free for all students.",
    "zh": "我们的在线数据库对全体学生免费。",
    "lv": "中等",
    "chunks": [
     "Our online databases",
     "are free",
     "for all students"
    ],
    "skeleton": [
     "在线数据库",
     "免费",
     "对全体学生"
    ],
    "tier": "medium"
   },
   {
    "en": "Please log in with your student ID first.",
    "zh": "请先用你的学生证登录。",
    "lv": "中等",
    "chunks": [
     "Please log in",
     "with your student ID",
     "first"
    ],
    "skeleton": [
     "请登录",
     "用学生证",
     "先"
    ],
    "tier": "medium"
   },
   {
    "en": "Food and drinks are not allowed near the computers.",
    "zh": "电脑区附近禁止携带食物和饮料。",
    "lv": "中等",
    "chunks": [
     "Food and drinks",
     "are not allowed",
     "near the computers"
    ],
    "skeleton": [
     "食物和饮料",
     "不被允许",
     "在电脑区附近"
    ],
    "tier": "medium"
   },
   {
    "en": "Each book can be renewed twice before the deadline.",
    "zh": "每本书在到期前可续借两次。",
    "lv": "中等",
    "chunks": [
     "Each book",
     "can be renewed twice",
     "before the deadline"
    ],
    "skeleton": [
     "每本书",
     "可续借两次",
     "在到期前"
    ],
    "tier": "medium"
   },
   {
    "en": "If a book is checked out, you can place a hold and we will email you.",
    "zh": "如果书已被借走，你可以预约，我们会邮件通知你。",
    "lv": "困难",
    "chunks": [
     "If a book is checked out",
     "you can place a hold",
     "and we will email you"
    ],
    "skeleton": [
     "如果书被借走",
     "你可预约",
     "我们会邮件通知"
    ],
    "tier": "long"
   },
   {
    "en": "Reference books, which cannot leave the building, must be used at the tables here.",
    "zh": "参考书不能带出楼外，必须在这里的桌子上使用。",
    "lv": "困难",
    "chunks": [
     "Reference books",
     "which cannot leave the building",
     "must be used at the tables here"
    ],
    "skeleton": [
     "参考书",
     "不能带出楼",
     "须在此桌上使用"
    ],
    "tier": "long"
   },
   {
    "en": "When you return a book late, the fine grows by a dime each day.",
    "zh": "当你逾期还书时，罚金每天增加一角钱。",
    "lv": "困难",
    "chunks": [
     "When you return a book late",
     "the fine grows",
     "by a dime each day"
    ],
    "skeleton": [
     "当你逾期还书",
     "罚金增长",
     "每天一角"
    ],
    "tier": "long"
   },
   {
    "en": "If we don't own the title, we can request a copy through interlibrary loan.",
    "zh": "如果我们没有这本书，可以通过馆际互借调取一册。",
    "lv": "困难",
    "chunks": [
     "If we don't own the title",
     "we can request a copy",
     "through interlibrary loan"
    ],
    "skeleton": [
     "如果没有这本书",
     "我们可申请一册",
     "通过馆际互借"
    ],
    "tier": "long"
   },
   {
    "en": "Students who need to print in color should use the machine by the entrance.",
    "zh": "需要彩色打印的学生应使用入口旁的那台机器。",
    "lv": "困难",
    "chunks": [
     "Students who need to print in color",
     "should use the machine",
     "by the entrance"
    ],
    "skeleton": [
     "需彩印的学生",
     "应用那台机器",
     "在入口旁"
    ],
    "tier": "long"
   },
   {
    "en": "Because the database is busy, you may lose access when too many people log in.",
    "zh": "由于数据库繁忙，登录人数过多时你可能会掉线。",
    "lv": "困难",
    "chunks": [
     "Because the database is busy",
     "you may lose access",
     "when too many people log in"
    ],
    "skeleton": [
     "因数据库繁忙",
     "你可能掉线",
     "当登录人太多"
    ],
    "tier": "long"
   },
   {
    "en": "During the final exam week, the reading room stays open until midnight so students can study.",
    "zh": "期末考试周期间，阅览室开放至午夜，方便学生学习。",
    "lv": "困难",
    "chunks": [
     "During the final exam week",
     "the reading room stays open until midnight",
     "so students can study"
    ],
    "skeleton": [
     "期末考试周期间",
     "阅览室开放至午夜",
     "方便学生学习"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "hotel",
  "name": "🏨 酒店前台",
  "en": "Hotel Front Desk",
  "desc": "入住·早餐·房间·钥匙·退房·预订·停车·Wi-Fi·叫醒·行李",
  "items": [
   {
    "en": "Welcome. May I have your name?",
    "zh": "欢迎光临，请问您贵姓？",
    "lv": "简单",
    "chunks": [
     "Welcome.",
     "May I have",
     "your name?"
    ],
    "skeleton": [
     "欢迎",
     "请问",
     "您的名字"
    ],
    "tier": "short"
   },
   {
    "en": "Check-in begins at three o'clock.",
    "zh": "办理入住从三点开始。",
    "lv": "简单",
    "chunks": [
     "Check-in begins",
     "at three o'clock."
    ],
    "skeleton": [
     "入住开始",
     "三点整"
    ],
    "tier": "short"
   },
   {
    "en": "Your room is on the fifth floor.",
    "zh": "您的房间在五楼。",
    "lv": "简单",
    "chunks": [
     "Your room is",
     "on the fifth floor."
    ],
    "skeleton": [
     "您的房间",
     "在五楼"
    ],
    "tier": "short"
   },
   {
    "en": "The elevator is behind you.",
    "zh": "电梯就在您身后。",
    "lv": "简单",
    "chunks": [
     "The elevator is",
     "behind you."
    ],
    "skeleton": [
     "电梯",
     "在您身后"
    ],
    "tier": "short"
   },
   {
    "en": "Here are your two room keys.",
    "zh": "这是您的两张房卡。",
    "lv": "简单",
    "chunks": [
     "Here are",
     "your two room keys."
    ],
    "skeleton": [
     "这是",
     "您的两张房卡"
    ],
    "tier": "short"
   },
   {
    "en": "Please sign here for me.",
    "zh": "请在这里签个字。",
    "lv": "简单",
    "chunks": [
     "Please sign",
     "here for me."
    ],
    "skeleton": [
     "请签字",
     "在这里"
    ],
    "tier": "short"
   },
   {
    "en": "Checkout is by eleven tomorrow.",
    "zh": "退房时间是明天十一点前。",
    "lv": "简单",
    "chunks": [
     "Checkout is",
     "by eleven tomorrow."
    ],
    "skeleton": [
     "退房",
     "明天十一点前"
    ],
    "tier": "short"
   },
   {
    "en": "Breakfast is served in the lobby until ten.",
    "zh": "早餐在大堂供应，到十点为止。",
    "lv": "中等",
    "chunks": [
     "Breakfast is served",
     "in the lobby",
     "until ten."
    ],
    "skeleton": [
     "早餐供应",
     "在大堂",
     "到十点"
    ],
    "tier": "medium"
   },
   {
    "en": "Your room is on the fifth floor, facing the garden.",
    "zh": "您的房间在五楼，面朝花园。",
    "lv": "中等",
    "chunks": [
     "Your room is",
     "on the fifth floor,",
     "facing the garden."
    ],
    "skeleton": [
     "您的房间",
     "在五楼",
     "面朝花园"
    ],
    "tier": "medium"
   },
   {
    "en": "The Wi-Fi password is printed on your key card.",
    "zh": "Wi-Fi 密码印在您的房卡上。",
    "lv": "中等",
    "chunks": [
     "The Wi-Fi password",
     "is printed",
     "on your key card."
    ],
    "skeleton": [
     "Wi-Fi 密码",
     "印着",
     "在房卡上"
    ],
    "tier": "medium"
   },
   {
    "en": "We can store your luggage behind the front desk.",
    "zh": "我们可以把行李存在前台后面。",
    "lv": "中等",
    "chunks": [
     "We can store",
     "your luggage",
     "behind the front desk."
    ],
    "skeleton": [
     "我们可存",
     "您的行李",
     "前台后面"
    ],
    "tier": "medium"
   },
   {
    "en": "May I have a card for the deposit?",
    "zh": "可以给我一张卡用作押金吗？",
    "lv": "中等",
    "chunks": [
     "May I have a card",
     "for the deposit?"
    ],
    "skeleton": [
     "可给张卡吗",
     "用作押金"
    ],
    "tier": "medium"
   },
   {
    "en": "I've set a wake-up call for six thirty.",
    "zh": "我已为您设好六点半的叫醒服务。",
    "lv": "中等",
    "chunks": [
     "I've set",
     "a wake-up call",
     "for six thirty."
    ],
    "skeleton": [
     "我已设",
     "叫醒服务",
     "六点半"
    ],
    "tier": "medium"
   },
   {
    "en": "Parking is available in the garage across the street.",
    "zh": "停车可以停在街对面的车库。",
    "lv": "中等",
    "chunks": [
     "Parking is available",
     "in the garage",
     "across the street."
    ],
    "skeleton": [
     "有停车位",
     "在车库",
     "街对面"
    ],
    "tier": "medium"
   },
   {
    "en": "Please leave your key at the front desk whenever you go out for the day.",
    "zh": "只要您外出一整天，请把钥匙留在前台。",
    "lv": "困难",
    "chunks": [
     "Please leave your key",
     "at the front desk",
     "whenever you go out for the day."
    ],
    "skeleton": [
     "请留钥匙",
     "在前台",
     "只要您外出一天"
    ],
    "tier": "long"
   },
   {
    "en": "If you need a late checkout, please let us know the night before.",
    "zh": "如果您需要延迟退房，请提前一晚告诉我们。",
    "lv": "困难",
    "chunks": [
     "If you need a late checkout,",
     "please let us know",
     "the night before."
    ],
    "skeleton": [
     "若需延退",
     "请告诉我们",
     "提前一晚"
    ],
    "tier": "long"
   },
   {
    "en": "Guests who booked online will find their parking included in the room rate.",
    "zh": "网上预订的客人会发现停车费已含在房价里。",
    "lv": "困难",
    "chunks": [
     "Guests who booked online",
     "will find their parking",
     "included in the room rate."
    ],
    "skeleton": [
     "网订的客人",
     "会发现停车",
     "已含在房价"
    ],
    "tier": "long"
   },
   {
    "en": "If your room isn't ready yet, we can hold your bags until noon.",
    "zh": "如果您的房间还没准备好，我们可以帮您存包到中午。",
    "lv": "困难",
    "chunks": [
     "If your room isn't ready yet,",
     "we can hold your bags",
     "until noon."
    ],
    "skeleton": [
     "若房未备好",
     "可帮存包",
     "到中午"
    ],
    "tier": "long"
   },
   {
    "en": "When you check out in the morning, please return both room keys to the front desk.",
    "zh": "早上退房时，请把两张房卡都交回前台。",
    "lv": "困难",
    "chunks": [
     "When you check out in the morning,",
     "please return both room keys",
     "to the front desk."
    ],
    "skeleton": [
     "早上退房时",
     "请交回两张房卡",
     "到前台"
    ],
    "tier": "long"
   },
   {
    "en": "The suite that overlooks the harbor costs about forty dollars more for each night.",
    "zh": "俯瞰港口的那间套房，每晚大约要多收四十美元。",
    "lv": "困难",
    "chunks": [
     "The suite that overlooks the harbor",
     "costs about forty dollars more",
     "for each night."
    ],
    "skeleton": [
     "俯瞰港口的套房",
     "多收约四十美元",
     "每一晚"
    ],
    "tier": "long"
   },
   {
    "en": "Because the rooftop pool is being cleaned today, it will not reopen before Friday morning.",
    "zh": "因为屋顶泳池今天在清洁，它周五上午前不会重新开放。",
    "lv": "困难",
    "chunks": [
     "Because the rooftop pool is being cleaned today,",
     "it will not reopen",
     "before Friday morning."
    ],
    "skeleton": [
     "因屋顶泳池今天清洁",
     "不会重开",
     "周五上午前"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "nature",
  "name": "🌿 自然保护区",
  "en": "Nature Reserve",
  "desc": "欢迎·步道·保护规则·观鸟·野生动物·天气·防火·垃圾·向导·季节关闭",
  "items": [
   {
    "en": "Welcome to the nature reserve.",
    "zh": "欢迎来到自然保护区。",
    "lv": "简单",
    "chunks": [
     "Welcome to",
     "the nature reserve"
    ],
    "skeleton": [
     "欢迎来到",
     "自然保护区"
    ],
    "tier": "short"
   },
   {
    "en": "Please stay on the marked trails.",
    "zh": "请走标记好的步道。",
    "lv": "简单",
    "chunks": [
     "Please stay",
     "on the marked trails"
    ],
    "skeleton": [
     "请待在",
     "标记步道上"
    ],
    "tier": "short"
   },
   {
    "en": "Do not pick the wild flowers.",
    "zh": "不要采摘野花。",
    "lv": "简单",
    "chunks": [
     "Do not pick",
     "the wild flowers"
    ],
    "skeleton": [
     "不要采",
     "野花"
    ],
    "tier": "short"
   },
   {
    "en": "The bird tower is near the lake.",
    "zh": "观鸟塔就在湖边。",
    "lv": "简单",
    "chunks": [
     "The bird tower",
     "is near the lake"
    ],
    "skeleton": [
     "观鸟塔",
     "在湖边"
    ],
    "tier": "short"
   },
   {
    "en": "Carry out all your trash.",
    "zh": "把你所有的垃圾带走。",
    "lv": "简单",
    "chunks": [
     "Carry out",
     "all your trash"
    ],
    "skeleton": [
     "带走",
     "所有垃圾"
    ],
    "tier": "short"
   },
   {
    "en": "Open fires are strictly forbidden here.",
    "zh": "这里严禁明火。",
    "lv": "简单",
    "chunks": [
     "Open fires",
     "are strictly forbidden here"
    ],
    "skeleton": [
     "明火",
     "此处严禁"
    ],
    "tier": "short"
   },
   {
    "en": "Guided tours start every hour.",
    "zh": "导览每小时一场。",
    "lv": "简单",
    "chunks": [
     "Guided tours",
     "start every hour"
    ],
    "skeleton": [
     "导览",
     "每小时开始"
    ],
    "tier": "short"
   },
   {
    "en": "The visitor center closes at five in winter.",
    "zh": "冬季游客中心五点关门。",
    "lv": "中等",
    "chunks": [
     "The visitor center",
     "closes at five",
     "in winter"
    ],
    "skeleton": [
     "游客中心",
     "五点关门",
     "冬季"
    ],
    "tier": "medium"
   },
   {
    "en": "Please keep your dog on a leash at all times.",
    "zh": "请全程给你的狗系上牵引绳。",
    "lv": "中等",
    "chunks": [
     "Please keep your dog",
     "on a leash",
     "at all times"
    ],
    "skeleton": [
     "请让你的狗",
     "系着绳",
     "全程"
    ],
    "tier": "medium"
   },
   {
    "en": "The main trail loops back to the parking lot.",
    "zh": "主步道绕一圈回到停车场。",
    "lv": "中等",
    "chunks": [
     "The main trail",
     "loops back",
     "to the parking lot"
    ],
    "skeleton": [
     "主步道",
     "绕回",
     "停车场"
    ],
    "tier": "medium"
   },
   {
    "en": "You can rent binoculars at the front gate.",
    "zh": "你可以在大门口租借望远镜。",
    "lv": "中等",
    "chunks": [
     "You can rent binoculars",
     "at the front gate"
    ],
    "skeleton": [
     "你可租望远镜",
     "在大门口"
    ],
    "tier": "medium"
   },
   {
    "en": "Please do not feed any of the wild animals.",
    "zh": "请不要投喂任何野生动物。",
    "lv": "中等",
    "chunks": [
     "Please do not feed",
     "any of the wild animals"
    ],
    "skeleton": [
     "请勿投喂",
     "任何野生动物"
    ],
    "tier": "medium"
   },
   {
    "en": "Sudden storms can roll in over the mountains.",
    "zh": "暴风雨可能从山那边突然袭来。",
    "lv": "中等",
    "chunks": [
     "Sudden storms",
     "can roll in",
     "over the mountains"
    ],
    "skeleton": [
     "暴风雨",
     "可能袭来",
     "越过山"
    ],
    "tier": "medium"
   },
   {
    "en": "Toss your matches into the metal fire bins.",
    "zh": "把火柴扔进金属防火桶里。",
    "lv": "中等",
    "chunks": [
     "Toss your matches",
     "into the metal",
     "fire bins"
    ],
    "skeleton": [
     "扔火柴",
     "进金属",
     "防火桶"
    ],
    "tier": "medium"
   },
   {
    "en": "If you spot a deer on the path, please keep your distance and stay quiet.",
    "zh": "如果你在小路上看到鹿，请保持距离并保持安静。",
    "lv": "困难",
    "chunks": [
     "If you spot a deer on the path",
     "please keep your distance",
     "and stay quiet"
    ],
    "skeleton": [
     "若你在小路上看到鹿",
     "请保持距离",
     "并保持安静"
    ],
    "tier": "long"
   },
   {
    "en": "The wetland area, which floods each spring, is closed to all visitors until May.",
    "zh": "每年春天泛滥的湿地区域，五月前对所有游客关闭。",
    "lv": "困难",
    "chunks": [
     "The wetland area",
     "which floods each spring",
     "is closed to all visitors",
     "until May"
    ],
    "skeleton": [
     "湿地区域",
     "每春泛滥",
     "对所有游客关闭",
     "直到五月"
    ],
    "tier": "long"
   },
   {
    "en": "Hikers who wander off the trail can easily disturb the birds nesting in the reeds.",
    "zh": "偏离步道的徒步者很容易惊扰在芦苇丛中筑巢的鸟。",
    "lv": "困难",
    "chunks": [
     "Hikers who wander off the trail",
     "can easily disturb",
     "the birds nesting in the reeds"
    ],
    "skeleton": [
     "偏离步道的徒步者",
     "很容易惊扰",
     "在芦苇中筑巢的鸟"
    ],
    "tier": "long"
   },
   {
    "en": "Because the ground is dry, we ask that no one light a fire.",
    "zh": "由于地面干燥，我们请求任何人都不要生火。",
    "lv": "困难",
    "chunks": [
     "Because the ground is dry",
     "we ask that no one",
     "light a fire"
    ],
    "skeleton": [
     "因地面干燥",
     "我们请求无人",
     "生火"
    ],
    "tier": "long"
   },
   {
    "en": "When the north trail is icy, our guides will lead you along the river instead.",
    "zh": "当北步道结冰时，向导会改带你沿河而行。",
    "lv": "困难",
    "chunks": [
     "When the north trail is icy",
     "our guides will lead you",
     "along the river instead"
    ],
    "skeleton": [
     "当北步道结冰",
     "向导会带你",
     "改沿河走"
    ],
    "tier": "long"
   },
   {
    "en": "The green bins that sit along the path are meant only for recyclable bottles and cans.",
    "zh": "沿路摆放的绿色垃圾桶只用于可回收的瓶子和易拉罐。",
    "lv": "困难",
    "chunks": [
     "The green bins that sit along the path",
     "are meant only",
     "for recyclable bottles and cans"
    ],
    "skeleton": [
     "沿路的绿色垃圾桶",
     "只用于",
     "可回收瓶子和罐子"
    ],
    "tier": "long"
   },
   {
    "en": "If a bear approaches, back away slowly and do not turn to run.",
    "zh": "如果熊靠近，请慢慢后退，不要转身逃跑。",
    "lv": "困难",
    "chunks": [
     "If a bear approaches",
     "back away slowly",
     "and do not turn to run"
    ],
    "skeleton": [
     "若熊靠近",
     "慢慢后退",
     "别转身逃"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "registrar",
  "name": "🏛 教务处",
  "en": "Registrar's Office",
  "desc": "取号·填表·门户登录·盖章·邮寄·选课·成绩单·退课·截止日期·官方件",
  "items": [
   {
    "en": "Please take a number and wait.",
    "zh": "请取号后等候。",
    "lv": "简单",
    "chunks": [
     "Please take a number",
     "and wait"
    ],
    "skeleton": [
     "请取号",
     "并等候"
    ],
    "tier": "short"
   },
   {
    "en": "Fill out the transcript form.",
    "zh": "请填写成绩单申请表。",
    "lv": "简单",
    "chunks": [
     "Fill out",
     "the transcript form"
    ],
    "skeleton": [
     "填写",
     "成绩单表"
    ],
    "tier": "short"
   },
   {
    "en": "The office opens at nine.",
    "zh": "教务处九点开门。",
    "lv": "简单",
    "chunks": [
     "The office",
     "opens at nine"
    ],
    "skeleton": [
     "教务处",
     "九点开门"
    ],
    "tier": "short"
   },
   {
    "en": "Log into the portal now.",
    "zh": "现在登录门户网站。",
    "lv": "简单",
    "chunks": [
     "Log into",
     "the portal now"
    ],
    "skeleton": [
     "登录",
     "门户网站"
    ],
    "tier": "short"
   },
   {
    "en": "We will stamp your transcript.",
    "zh": "我们会给成绩单盖章。",
    "lv": "简单",
    "chunks": [
     "We will stamp",
     "your transcript"
    ],
    "skeleton": [
     "我们盖章",
     "你的成绩单"
    ],
    "tier": "short"
   },
   {
    "en": "Course changes close on Friday.",
    "zh": "选课变更周五截止。",
    "lv": "简单",
    "chunks": [
     "Course changes",
     "close on Friday"
    ],
    "skeleton": [
     "选课变更",
     "周五截止"
    ],
    "tier": "short"
   },
   {
    "en": "Sign the form in ink.",
    "zh": "请用签字笔签名。",
    "lv": "简单",
    "chunks": [
     "Sign the form",
     "in ink"
    ],
    "skeleton": [
     "签署表格",
     "用签字笔"
    ],
    "tier": "short"
   },
   {
    "en": "Log into the portal to check your records.",
    "zh": "登录门户网站查看你的档案。",
    "lv": "中等",
    "chunks": [
     "Log into the portal",
     "to check your records"
    ],
    "skeleton": [
     "登录门户",
     "查看你的档案"
    ],
    "tier": "medium"
   },
   {
    "en": "We will stamp your transcript with our official seal.",
    "zh": "我们会给成绩单加盖官方印章。",
    "lv": "中等",
    "chunks": [
     "We will stamp your transcript",
     "with our official seal"
    ],
    "skeleton": [
     "盖章成绩单",
     "用官方印章"
    ],
    "tier": "medium"
   },
   {
    "en": "Your transcript will be mailed to your chosen schools.",
    "zh": "你的成绩单将寄往你选择的学校。",
    "lv": "中等",
    "chunks": [
     "Your transcript",
     "will be mailed",
     "to your chosen schools"
    ],
    "skeleton": [
     "你的成绩单",
     "将被寄出",
     "到你选的学校"
    ],
    "tier": "medium"
   },
   {
    "en": "Please take a number from the machine by the door.",
    "zh": "请在门旁的机器上取号。",
    "lv": "中等",
    "chunks": [
     "Please take a number",
     "from the machine",
     "by the door"
    ],
    "skeleton": [
     "请取号",
     "从机器上",
     "在门旁"
    ],
    "tier": "medium"
   },
   {
    "en": "The deadline to add classes is next Monday.",
    "zh": "加课的截止日期是下周一。",
    "lv": "中等",
    "chunks": [
     "The deadline to add classes",
     "is next Monday"
    ],
    "skeleton": [
     "加课截止日",
     "是下周一"
    ],
    "tier": "medium"
   },
   {
    "en": "Official copies cost five dollars for each page.",
    "zh": "官方件每页收费五美元。",
    "lv": "中等",
    "chunks": [
     "Official copies",
     "cost five dollars",
     "for each page"
    ],
    "skeleton": [
     "官方件",
     "收费五美元",
     "每页"
    ],
    "tier": "medium"
   },
   {
    "en": "Please bring a photo ID to pick up documents.",
    "zh": "领取文件请携带带照片的证件。",
    "lv": "中等",
    "chunks": [
     "Please bring a photo ID",
     "to pick up documents"
    ],
    "skeleton": [
     "请带证件",
     "来领取文件"
    ],
    "tier": "medium"
   },
   {
    "en": "If you need an unofficial copy, which you can keep for yourself, check this box.",
    "zh": "如果你需要一份可自留的非官方副本，请勾选此框。",
    "lv": "困难",
    "chunks": [
     "If you need an unofficial copy",
     "which you can keep for yourself",
     "check this box"
    ],
    "skeleton": [
     "如需非官方副本",
     "可自己留存",
     "勾选此框"
    ],
    "tier": "long"
   },
   {
    "en": "Please email the office right away to fix issues such as missing courses.",
    "zh": "如遇缺课等问题，请立即邮件联系教务处处理。",
    "lv": "困难",
    "chunks": [
     "Please email the office right away",
     "to fix issues",
     "such as missing courses"
    ],
    "skeleton": [
     "请立即邮件教务处",
     "解决问题",
     "如缺课"
    ],
    "tier": "long"
   },
   {
    "en": "If you drop a course after the deadline, a withdrawal mark stays on your record.",
    "zh": "如果你在截止日期后退课，退课标记会留在你的档案上。",
    "lv": "困难",
    "chunks": [
     "If you drop a course after the deadline",
     "a withdrawal mark",
     "stays on your record"
    ],
    "skeleton": [
     "若截止后退课",
     "退课标记",
     "留在你档案上"
    ],
    "tier": "long"
   },
   {
    "en": "Students who register late must pay a small extra fee before they can enroll.",
    "zh": "逾期注册的学生须先缴一笔少量附加费才能选课。",
    "lv": "困难",
    "chunks": [
     "Students who register late",
     "must pay a small extra fee",
     "before they can enroll"
    ],
    "skeleton": [
     "逾期注册的学生",
     "须缴少量附加费",
     "才能选课"
    ],
    "tier": "long"
   },
   {
    "en": "When your form is complete, drop it in the box that is near the window.",
    "zh": "表格填好后，把它投进靠窗的那个箱子里。",
    "lv": "困难",
    "chunks": [
     "When your form is complete",
     "drop it in the box",
     "that is near the window"
    ],
    "skeleton": [
     "表格填好后",
     "投进箱子里",
     "靠窗那个"
    ],
    "tier": "long"
   },
   {
    "en": "Because grades post at midnight, you should check the portal on Monday morning.",
    "zh": "由于成绩午夜发布，你应在周一早上查看门户网站。",
    "lv": "困难",
    "chunks": [
     "Because grades post at midnight",
     "you should check the portal",
     "on Monday morning"
    ],
    "skeleton": [
     "因成绩午夜发布",
     "你应查门户",
     "在周一早上"
    ],
    "tier": "long"
   },
   {
    "en": "Any request that arrives after Friday will not be processed until the following week.",
    "zh": "周五之后收到的任何申请要到下一周才会处理。",
    "lv": "困难",
    "chunks": [
     "Any request that arrives after Friday",
     "will not be processed",
     "until the following week"
    ],
    "skeleton": [
     "周五后到的申请",
     "不会被处理",
     "直到下一周"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "museum",
  "name": "🖼 博物馆·画廊",
  "en": "Museum / Gallery",
  "desc": "票务·参观规则·寄存·展区·导览·语音导览·特展·摄影·闭馆·会员",
  "items": [
   {
    "en": "The museum is free on Sundays.",
    "zh": "博物馆周日免费。",
    "lv": "简单",
    "chunks": [
     "The museum",
     "is free",
     "on Sundays"
    ],
    "skeleton": [
     "博物馆",
     "免费",
     "周日"
    ],
    "tier": "short"
   },
   {
    "en": "Please do not touch the paintings.",
    "zh": "请勿触摸画作。",
    "lv": "简单",
    "chunks": [
     "Please do not touch",
     "the paintings"
    ],
    "skeleton": [
     "请勿触摸",
     "画作"
    ],
    "tier": "short"
   },
   {
    "en": "Tickets are sold at the entrance.",
    "zh": "门票在入口处出售。",
    "lv": "简单",
    "chunks": [
     "Tickets are sold",
     "at the entrance"
    ],
    "skeleton": [
     "门票出售",
     "在入口"
    ],
    "tier": "short"
   },
   {
    "en": "The gift shop closes at six.",
    "zh": "礼品店六点关门。",
    "lv": "简单",
    "chunks": [
     "The gift shop",
     "closes at six"
    ],
    "skeleton": [
     "礼品店",
     "六点关门"
    ],
    "tier": "short"
   },
   {
    "en": "Photography is allowed without flash.",
    "zh": "允许拍照，但不能用闪光灯。",
    "lv": "简单",
    "chunks": [
     "Photography is allowed",
     "without flash"
    ],
    "skeleton": [
     "允许拍照",
     "不用闪光灯"
    ],
    "tier": "short"
   },
   {
    "en": "Please keep your ticket with you.",
    "zh": "请随身保管好门票。",
    "lv": "简单",
    "chunks": [
     "Please keep",
     "your ticket",
     "with you"
    ],
    "skeleton": [
     "请保管",
     "你的门票",
     "随身"
    ],
    "tier": "short"
   },
   {
    "en": "The east wing is closed today.",
    "zh": "东翼展厅今天关闭。",
    "lv": "简单",
    "chunks": [
     "The east wing",
     "is closed today"
    ],
    "skeleton": [
     "东翼展厅",
     "今天关闭"
    ],
    "tier": "short"
   },
   {
    "en": "Large bags must be left at the entrance.",
    "zh": "大件行李必须寄存在入口处。",
    "lv": "中等",
    "chunks": [
     "Large bags",
     "must be left",
     "at the entrance"
    ],
    "skeleton": [
     "大件行李",
     "必须寄存",
     "在入口"
    ],
    "tier": "medium"
   },
   {
    "en": "The modern art gallery is on the second floor.",
    "zh": "现代艺术展厅在二楼。",
    "lv": "中等",
    "chunks": [
     "The modern art gallery",
     "is on the second floor"
    ],
    "skeleton": [
     "现代艺术展厅",
     "在二楼"
    ],
    "tier": "medium"
   },
   {
    "en": "Guided tours start every hour near the front desk.",
    "zh": "导览每小时在服务台附近开始。",
    "lv": "中等",
    "chunks": [
     "Guided tours start",
     "every hour",
     "near the front desk"
    ],
    "skeleton": [
     "导览开始",
     "每小时",
     "在服务台附近"
    ],
    "tier": "medium"
   },
   {
    "en": "The special exhibition upstairs requires a separate ticket.",
    "zh": "楼上的特展需要另外购票。",
    "lv": "中等",
    "chunks": [
     "The special exhibition upstairs",
     "requires",
     "a separate ticket"
    ],
    "skeleton": [
     "楼上的特展",
     "需要",
     "另外购票"
    ],
    "tier": "medium"
   },
   {
    "en": "You can store your coat in the lockers downstairs.",
    "zh": "你可以把外套存在楼下的储物柜里。",
    "lv": "中等",
    "chunks": [
     "You can store your coat",
     "in the lockers",
     "downstairs"
    ],
    "skeleton": [
     "你可存外套",
     "在储物柜",
     "楼下"
    ],
    "tier": "medium"
   },
   {
    "en": "Members enter for free through the side door.",
    "zh": "会员可从侧门免费入场。",
    "lv": "中等",
    "chunks": [
     "Members enter for free",
     "through the side door"
    ],
    "skeleton": [
     "会员免费入场",
     "从侧门"
    ],
    "tier": "medium"
   },
   {
    "en": "The audio guide is available in five languages.",
    "zh": "语音导览提供五种语言。",
    "lv": "中等",
    "chunks": [
     "The audio guide",
     "is available",
     "in five languages"
    ],
    "skeleton": [
     "语音导览",
     "可提供",
     "五种语言"
    ],
    "tier": "medium"
   },
   {
    "en": "If you want an audio guide, you can rent one at the ticket counter.",
    "zh": "如果你想要语音导览，可以在售票台租一个。",
    "lv": "困难",
    "chunks": [
     "If you want an audio guide",
     "you can rent one",
     "at the ticket counter"
    ],
    "skeleton": [
     "如果你想要语音导览",
     "你可租一个",
     "在售票台"
    ],
    "tier": "long"
   },
   {
    "en": "The sculptures, which were donated last year, are displayed in the east wing.",
    "zh": "这些去年捐赠的雕塑陈列在东翼展厅。",
    "lv": "困难",
    "chunks": [
     "The sculptures",
     "which were donated last year",
     "are displayed in the east wing"
    ],
    "skeleton": [
     "这些雕塑",
     "去年被捐赠",
     "陈列在东翼"
    ],
    "tier": "long"
   },
   {
    "en": "When the museum closes, a bell rings so visitors can find the exit.",
    "zh": "闭馆时会响铃，方便参观者找到出口。",
    "lv": "困难",
    "chunks": [
     "When the museum closes",
     "a bell rings",
     "so visitors can find the exit"
    ],
    "skeleton": [
     "闭馆时",
     "会响铃",
     "方便游客找出口"
    ],
    "tier": "long"
   },
   {
    "en": "If you become a member, you can visit every special exhibition for free.",
    "zh": "如果你成为会员，就能免费参观每一场特展。",
    "lv": "困难",
    "chunks": [
     "If you become a member",
     "you can visit every special exhibition",
     "for free"
    ],
    "skeleton": [
     "如果你成为会员",
     "可参观每场特展",
     "免费"
    ],
    "tier": "long"
   },
   {
    "en": "Visitors who bring large backpacks must check them at the coat room first.",
    "zh": "携带大背包的参观者须先在寄存处存放。",
    "lv": "困难",
    "chunks": [
     "Visitors who bring large backpacks",
     "must check them",
     "at the coat room first"
    ],
    "skeleton": [
     "带大背包的游客",
     "须寄存它们",
     "先在寄存处"
    ],
    "tier": "long"
   },
   {
    "en": "Because the special show is popular, please book your time slot online in advance.",
    "zh": "由于特展很受欢迎，请提前在网上预约入场时段。",
    "lv": "困难",
    "chunks": [
     "Because the special show is popular",
     "please book your time slot",
     "online in advance"
    ],
    "skeleton": [
     "因特展受欢迎",
     "请预约入场时段",
     "提前网上"
    ],
    "tier": "long"
   },
   {
    "en": "The photographs that hang in the main hall may not be touched or moved.",
    "zh": "挂在主展厅的这些照片不得触摸或移动。",
    "lv": "困难",
    "chunks": [
     "The photographs",
     "that hang in the main hall",
     "may not be touched or moved"
    ],
    "skeleton": [
     "这些照片",
     "挂在主展厅",
     "不得触摸或移动"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "carrental",
  "name": "🚗 租车行",
  "en": "Car Rental Agency",
  "desc": "驾照核验·满油归还·保险费率·还车地点·加驾司机·延误费·车型升级·油费·导航租借·车况检查",
  "items": [
   {
    "en": "Please show your driver's license.",
    "zh": "请出示您的驾照。",
    "lv": "简单",
    "chunks": [
     "Please show",
     "your driver's license."
    ],
    "skeleton": [
     "请出示",
     "您的驾照。"
    ],
    "tier": "short"
   },
   {
    "en": "The car must be returned full.",
    "zh": "还车时油箱必须加满。",
    "lv": "简单",
    "chunks": [
     "The car",
     "must be returned full."
    ],
    "skeleton": [
     "这辆车",
     "必须加满油归还。"
    ],
    "tier": "short"
   },
   {
    "en": "Insurance is included in the rate.",
    "zh": "保险已含在租金里。",
    "lv": "简单",
    "chunks": [
     "Insurance is included",
     "in the rate."
    ],
    "skeleton": [
     "保险已包含",
     "在租金里。"
    ],
    "tier": "short"
   },
   {
    "en": "Please check the car for damage.",
    "zh": "请检查车辆是否有损伤。",
    "lv": "简单",
    "chunks": [
     "Please check the car",
     "for damage."
    ],
    "skeleton": [
     "请检查车辆",
     "有无损伤。"
    ],
    "tier": "short"
   },
   {
    "en": "A navigation device costs extra.",
    "zh": "导航设备需另收费。",
    "lv": "简单",
    "chunks": [
     "A navigation device",
     "costs extra."
    ],
    "skeleton": [
     "导航设备",
     "需额外收费。"
    ],
    "tier": "short"
   },
   {
    "en": "We offer compact and full-size cars.",
    "zh": "我们提供紧凑型和全尺寸车。",
    "lv": "简单",
    "chunks": [
     "We offer",
     "compact and full-size cars."
    ],
    "skeleton": [
     "我们提供",
     "紧凑型和全尺寸车。"
    ],
    "tier": "short"
   },
   {
    "en": "Sign here to confirm the pickup.",
    "zh": "请在此签字确认取车。",
    "lv": "简单",
    "chunks": [
     "Sign here",
     "to confirm the pickup."
    ],
    "skeleton": [
     "在此签字",
     "确认取车。"
    ],
    "tier": "short"
   },
   {
    "en": "Please return the vehicle to this lot by noon.",
    "zh": "请在中午前把车还到这个停车场。",
    "lv": "中等",
    "chunks": [
     "Please return the vehicle",
     "to this lot",
     "by noon."
    ],
    "skeleton": [
     "请归还车辆",
     "到这个停车场",
     "中午之前。"
    ],
    "tier": "medium"
   },
   {
    "en": "A second driver can be added for a small fee.",
    "zh": "加一名司机只需付一笔小费用。",
    "lv": "中等",
    "chunks": [
     "A second driver",
     "can be added",
     "for a small fee."
    ],
    "skeleton": [
     "第二名司机",
     "可以添加",
     "只需一笔小费用。"
    ],
    "tier": "medium"
   },
   {
    "en": "Insurance is included in the daily rate automatically.",
    "zh": "保险自动含在每日租金中。",
    "lv": "中等",
    "chunks": [
     "Insurance is included",
     "in the daily rate",
     "automatically."
    ],
    "skeleton": [
     "保险已包含",
     "在每日租金里",
     "自动含入。"
    ],
    "tier": "medium"
   },
   {
    "en": "The fuel tank should be full at return.",
    "zh": "还车时油箱应当是满的。",
    "lv": "中等",
    "chunks": [
     "The fuel tank",
     "should be full",
     "at return."
    ],
    "skeleton": [
     "油箱",
     "应当是满的",
     "还车时。"
    ],
    "tier": "medium"
   },
   {
    "en": "You can pick up your car after ten o'clock.",
    "zh": "十点以后您就能取车了。",
    "lv": "中等",
    "chunks": [
     "You can pick up your car",
     "after ten o'clock."
    ],
    "skeleton": [
     "您可以取车",
     "十点以后。"
    ],
    "tier": "medium"
   },
   {
    "en": "Please report any scratches to the front desk immediately.",
    "zh": "有任何划痕请立即向前台报告。",
    "lv": "中等",
    "chunks": [
     "Please report any scratches",
     "to the front desk",
     "immediately."
    ],
    "skeleton": [
     "请报告任何划痕",
     "向前台",
     "立即。"
    ],
    "tier": "medium"
   },
   {
    "en": "The daily rate covers unlimited miles within the state.",
    "zh": "每日租金包含州内不限里程。",
    "lv": "中等",
    "chunks": [
     "The daily rate covers",
     "unlimited miles",
     "within the state."
    ],
    "skeleton": [
     "每日租金涵盖",
     "不限里程",
     "州内。"
    ],
    "tier": "medium"
   },
   {
    "en": "If you return the car after noon, an extra day will be charged to your card.",
    "zh": "如果您中午之后才还车，会向您的卡多收一天的费用。",
    "lv": "困难",
    "chunks": [
     "If you return the car after noon,",
     "an extra day",
     "will be charged to your card."
    ],
    "skeleton": [
     "如果您中午之后还车，",
     "额外一天",
     "将从您卡上收取。"
    ],
    "tier": "long"
   },
   {
    "en": "Customers who booked a compact car may be upgraded when none are left.",
    "zh": "预订了紧凑型车的顾客，若没车了可能会被升级。",
    "lv": "困难",
    "chunks": [
     "Customers who booked a compact car",
     "may be upgraded",
     "when none are left."
    ],
    "skeleton": [
     "预订了紧凑型车的顾客",
     "可能被升级",
     "当没车剩下时。"
    ],
    "tier": "long"
   },
   {
    "en": "If the tank is not full, we will charge you for the fuel.",
    "zh": "如果油箱没加满，我们会向您收取油费。",
    "lv": "困难",
    "chunks": [
     "If the tank is not full,",
     "we will charge you",
     "for the fuel."
    ],
    "skeleton": [
     "如果油箱没加满，",
     "我们会向您收费",
     "关于油费。"
    ],
    "tier": "long"
   },
   {
    "en": "Drivers who are under twenty-five must pay a young-driver surcharge at the front desk.",
    "zh": "二十五岁以下的司机必须在前台支付一笔年轻司机附加费。",
    "lv": "困难",
    "chunks": [
     "Drivers who are under twenty-five",
     "must pay a young-driver surcharge",
     "at the front desk."
    ],
    "skeleton": [
     "二十五岁以下的司机",
     "必须支付年轻司机附加费",
     "在前台。"
    ],
    "tier": "long"
   },
   {
    "en": "Because the lot is closed at night, please use the after-hours drop box.",
    "zh": "由于停车场夜间关闭，请使用非营业时间还车箱。",
    "lv": "困难",
    "chunks": [
     "Because the lot is closed at night,",
     "please use",
     "the after-hours drop box."
    ],
    "skeleton": [
     "因为停车场夜间关闭，",
     "请使用",
     "非营业时间还车箱。"
    ],
    "tier": "long"
   },
   {
    "en": "When you pick up the car, please inspect the tires and the mirrors carefully.",
    "zh": "取车时，请仔细检查轮胎和后视镜。",
    "lv": "困难",
    "chunks": [
     "When you pick up the car,",
     "please inspect the tires",
     "and the mirrors carefully."
    ],
    "skeleton": [
     "取车时，",
     "请检查轮胎",
     "和后视镜，要仔细。"
    ],
    "tier": "long"
   },
   {
    "en": "The insurance plan that we offer will cover most repairs after an accident.",
    "zh": "我们提供的保险方案能覆盖事故后的大部分维修。",
    "lv": "困难",
    "chunks": [
     "The insurance plan that we offer",
     "will cover most repairs",
     "after an accident."
    ],
    "skeleton": [
     "我们提供的保险方案",
     "将覆盖大部分维修",
     "事故之后。"
    ],
    "tier": "long"
   }
  ]
 },
 {
  "id": "community",
  "name": "🏢 社区中心",
  "en": "Community Centre",
  "desc": "开放时间·会员卡·泳池·课程报名·陪同规定·订场·活动·押金·志愿者·收费",
  "items": [
   {
    "en": "The community centre opens at ten.",
    "zh": "社区中心十点开门。",
    "lv": "简单",
    "chunks": [
     "The community centre",
     "opens at ten"
    ],
    "skeleton": [
     "社区中心",
     "十点开门"
    ],
    "tier": "short"
   },
   {
    "en": "Please register for a membership card.",
    "zh": "请办理一张会员卡。",
    "lv": "简单",
    "chunks": [
     "Please register",
     "for a membership card"
    ],
    "skeleton": [
     "请办理",
     "会员卡"
    ],
    "tier": "short"
   },
   {
    "en": "The swimming pool reopens tomorrow morning.",
    "zh": "泳池明天早上重新开放。",
    "lv": "简单",
    "chunks": [
     "The swimming pool reopens",
     "tomorrow morning"
    ],
    "skeleton": [
     "泳池重开",
     "明天早上"
    ],
    "tier": "short"
   },
   {
    "en": "Please register at the reception desk.",
    "zh": "请到接待台登记。",
    "lv": "简单",
    "chunks": [
     "Please register",
     "at the reception desk"
    ],
    "skeleton": [
     "请登记",
     "在接待台"
    ],
    "tier": "short"
   },
   {
    "en": "The yoga class begins at seven.",
    "zh": "瑜伽课七点开始。",
    "lv": "简单",
    "chunks": [
     "The yoga class",
     "begins at seven"
    ],
    "skeleton": [
     "瑜伽课",
     "七点开始"
    ],
    "tier": "short"
   },
   {
    "en": "Please pay the deposit in advance.",
    "zh": "请提前支付押金。",
    "lv": "简单",
    "chunks": [
     "Please pay the deposit",
     "in advance"
    ],
    "skeleton": [
     "请付押金",
     "提前"
    ],
    "tier": "short"
   },
   {
    "en": "We welcome volunteers every weekend.",
    "zh": "我们每个周末都欢迎志愿者。",
    "lv": "简单",
    "chunks": [
     "We welcome volunteers",
     "every weekend"
    ],
    "skeleton": [
     "欢迎志愿者",
     "每个周末"
    ],
    "tier": "short"
   },
   {
    "en": "The swimming pool is closed on Mondays for regular maintenance.",
    "zh": "泳池每周一关闭做常规维护。",
    "lv": "中等",
    "chunks": [
     "The swimming pool is closed",
     "on Mondays",
     "for regular maintenance"
    ],
    "skeleton": [
     "泳池关闭",
     "每周一",
     "做常规维护"
    ],
    "tier": "medium"
   },
   {
    "en": "Sign up for the evening cooking class at the reception desk.",
    "zh": "请到接待台报名晚间烹饪课。",
    "lv": "中等",
    "chunks": [
     "Sign up for",
     "the evening cooking class",
     "at the reception desk"
    ],
    "skeleton": [
     "报名",
     "晚间烹饪课",
     "在接待台"
    ],
    "tier": "medium"
   },
   {
    "en": "Children under six must be accompanied by an adult.",
    "zh": "六岁以下儿童必须有成人陪同。",
    "lv": "中等",
    "chunks": [
     "Children under six",
     "must be accompanied",
     "by an adult"
    ],
    "skeleton": [
     "六岁以下儿童",
     "必须被陪同",
     "由成人"
    ],
    "tier": "medium"
   },
   {
    "en": "You can reserve the main hall online after ten tomorrow.",
    "zh": "明天十点后你可以在线预订主厅。",
    "lv": "中等",
    "chunks": [
     "You can reserve the main hall",
     "online",
     "after ten tomorrow"
    ],
    "skeleton": [
     "你可预订主厅",
     "在线",
     "明天十点后"
    ],
    "tier": "medium"
   },
   {
    "en": "Your membership includes free access to every class.",
    "zh": "你的会员资格包含每门课程的免费使用权。",
    "lv": "中等",
    "chunks": [
     "Your membership includes",
     "free access",
     "to every class"
    ],
    "skeleton": [
     "会员包含",
     "免费使用",
     "每门课程"
    ],
    "tier": "medium"
   },
   {
    "en": "The deposit will be refunded within seven business days.",
    "zh": "押金将在七个工作日内退还。",
    "lv": "中等",
    "chunks": [
     "The deposit will be refunded",
     "within seven business days"
    ],
    "skeleton": [
     "押金将退还",
     "七个工作日内"
    ],
    "tier": "medium"
   },
   {
    "en": "The weekend craft activity is completely free for members.",
    "zh": "周末的手工活动对会员完全免费。",
    "lv": "中等",
    "chunks": [
     "The weekend craft activity",
     "is completely free",
     "for members"
    ],
    "skeleton": [
     "周末手工活动",
     "完全免费",
     "对会员"
    ],
    "tier": "medium"
   },
   {
    "en": "If you want to reserve the main hall, please pay a refundable deposit in advance.",
    "zh": "如果你想预订主厅，请提前支付一笔可退押金。",
    "lv": "困难",
    "chunks": [
     "If you want to reserve the main hall",
     "please pay a refundable deposit",
     "in advance"
    ],
    "skeleton": [
     "如果你想订主厅",
     "请付可退押金",
     "提前"
    ],
    "tier": "long"
   },
   {
    "en": "Volunteers who help at our events will receive free entry to every class.",
    "zh": "在活动中帮忙的志愿者将获得每门课程的免费入场资格。",
    "lv": "困难",
    "chunks": [
     "Volunteers who help at our events",
     "will receive free entry",
     "to every class"
    ],
    "skeleton": [
     "活动帮忙的志愿者",
     "将获免费入场",
     "每门课程"
    ],
    "tier": "long"
   },
   {
    "en": "If you are not a member yet, you can still join today's afternoon guided tour.",
    "zh": "如果你还不是会员，仍然可以参加今天下午的导览。",
    "lv": "困难",
    "chunks": [
     "If you are not a member yet",
     "you can still join",
     "today's afternoon guided tour"
    ],
    "skeleton": [
     "如果你还不是会员",
     "你仍可参加",
     "今天下午的导览"
    ],
    "tier": "long"
   },
   {
    "en": "When the swimming pool gets crowded, please limit your session to one single hour.",
    "zh": "当泳池拥挤时，请把游泳时段控制在一小时以内。",
    "lv": "困难",
    "chunks": [
     "When the swimming pool gets crowded",
     "please limit your session",
     "to one single hour"
    ],
    "skeleton": [
     "当泳池拥挤时",
     "请限制你的时段",
     "在一小时以内"
    ],
    "tier": "long"
   },
   {
    "en": "The weekend cooking class that fills up fast usually needs an early reservation.",
    "zh": "很快满员的周末烹饪课通常需要提前预约。",
    "lv": "困难",
    "chunks": [
     "The weekend cooking class that fills up fast",
     "usually needs",
     "an early reservation"
    ],
    "skeleton": [
     "很快满员的周末烹饪课",
     "通常需要",
     "提前预约"
    ],
    "tier": "long"
   },
   {
    "en": "Because the main hall is very popular this month, please reserve your preferred date early.",
    "zh": "由于本月主厅非常抢手，请尽早预订你心仪的日期。",
    "lv": "困难",
    "chunks": [
     "Because the main hall is very popular this month",
     "please reserve your preferred date",
     "early"
    ],
    "skeleton": [
     "因本月主厅抢手",
     "请预订心仪日期",
     "尽早"
    ],
    "tier": "long"
   },
   {
    "en": "If your membership expires this month, you can renew it at the reception desk today.",
    "zh": "如果你的会员卡本月到期，今天就可以在接待台续费。",
    "lv": "困难",
    "chunks": [
     "If your membership expires this month",
     "you can renew it",
     "at the reception desk today"
    ],
    "skeleton": [
     "如果会员本月到期",
     "你可续费",
     "今天在接待台"
    ],
    "tier": "long"
   }
  ]
 }
];
