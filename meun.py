data = {
    "台北":{
        "中正區":{
            "水源里":["羅斯福路4段"],
            "富水里":["永春街"],
            "文盛里":["羅斯福3段"],
        },
        "大同區":{
            "國順里":["延平北路3段"],
            "建明里":["重慶北路一段"],
            "光能里":["民生西路"],
        },
        "信義區":{
            "西村里":["基隆路1段"],
            "正和里":["仁愛路4段"],
            "興隆里":["基隆路1段"],
        },

    },
    "高雄":{
        "左營區":{
            "新下里":["東門路"],
            "新上里":["富國路"],
            "新中里":["至真路"],
        },
        "三民區":{
            "灣中里":["莊敬路"],
            "灣子里":["銀杉街"],
            "本館里":["大裕路"],
        },
        "前鎮區":{
            "興邦里":["翠亨北路"],
            "忠誠里":["光華三路"],
            "瑞竹里":["凱旋四路"],
        },
    }
}

exit_flag = False

while not exit_flag:
    for i in data:
        print(i)
    choice = input("please select city:")
    if choice in data:
        while not exit_flag: 
            for j in data[choice]:
                print("\t", j)
            choice2 = input('please select zone:')
            if choice2 in data[choice]:
                while not exit_flag:
                    for k in data[choice][choice2]:
                        print("\t\t", k)
                    choice3 = input('please select li:')
                    if choice3 in data[choice][choice2]:
                        for road in data[choice][choice2][choice3]:
                            print(road)
                        choice4 = input('最後一層,按b返回')
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
