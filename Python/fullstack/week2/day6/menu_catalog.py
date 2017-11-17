# __author__: wang_chongsheng
# date: 2017/9/15 0015
menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                'CICC': {},
                'HP': {},
                '渣打银行': {},
                'CCTV': {},
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {},
            },
            '三里屯': {
                '优衣库': {},
                'Apple': {},
            },
        },
        '昌平': {
            '天通苑': {
                "链家": {},
                "我爱我家": {},
            },
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                'Sohu': {},
                'Sogo': {},
                '快手': {},
            },
            '中关村': {
                'Youku': {},
                'Iqiyi': {},
                '汽车之家': {},
                '新东方': {},
                '腾讯': {},
            },
        },
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                'CICC': {},
                '高盛': {},
                '摩根': {},
            },
            '外滩': {},
        },
        '闵行': {},
        '静安': {},
    },
    '山东': {
        '济南': {},
        '青岛': {
            '青岛啤酒': {}
        },
    },
}

back_flag = False
exit_falg = False
while not back_flag and not exit_falg:
    for key in menu:
        print(key)
    choice = input("1>>:").strip()
    if choice == "q":
        exit_flag = True

    if choice in menu:
        while not back_flag and not exit_falg:
            for key2 in menu[choice]:
                print(key2)
            choice2 = input('2>>:').strip()
            if choice2 == "b":
                back_flag = True
            if choice2 == "q":
                exit_flag = True

            if choice2 in menu[choice]:
                while not back_flag and not exit_falg:
                    for key3 in menu[choice][choice2]:
                        print(key3)
                    choice3 = input('3>>:').strip()
                    if choice3 == "b":
                        back_flag = True
                    if choice3 == "q":
                        exit_flag = True

                    if choice3 in menu[choice][choice2]:
                        while not back_flag and not exit_falg:
                            for key4 in menu[choice][choice2][choice3]:
                                print(key4)
                            choice4 = input('4>>:').strip()
                            print("last level")
                            if choice4 == "b":
                                back_flag = True
                            if choice4 == "q":
                                exit_flag = True
                        else:
                            back_flag = False
                else:
                    back_flag = False
        else:
            back_flag = False
