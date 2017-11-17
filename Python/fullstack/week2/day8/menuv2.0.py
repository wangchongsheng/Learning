# __author__: wang_chongsheng
# date: 2017/9/20 0020
#__author__: wang_chongsheng
#date: 2017/9/18 0018

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
            '沙河':{
                '老男孩':{},
            },
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


current_layer = menu    #实现动态循环
# # parent_layer = menu

parent_layers = []  #保存所有父级，最后一个元素永远是父级

while True:
    for key in current_layer:
            print(key)
    choice = input('>>>:').strip()
    if len(choice) == 0 :continue
    if choice in current_layer:
        parent_layers.append(current_layer) #进入下一层之前，把当前层追加到列表中
        #当下一次循环时，取列表最后一个值
        current_layer = current_layer[choice]   #子层赋值
    elif choice == "b":
        if parent_layers: #判断是否为True
            current_layer = parent_layers.pop()
    else:
        print("不存在")

