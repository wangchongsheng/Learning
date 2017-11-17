# __author__: wang_chongsheng
# date: 2017/9/15

goods_list = [
    ('iPhone6s ', 5800),
    ('Mac Book ', 9000),
    ('Coffee   ', 30),
    ('LinuxBook', 50),
    ('Bicyle   ', 1500),
]
shoping_cart = []

salary = input("请输入你的工资: ")

if salary.isdigit():
    salary = int(salary)
    while True:

        #引导用户选择商品
        for i, v in enumerate(goods_list, 1):
            print(i, '>>>', v)

        choice = input("选择购买商品编号[退出：q]: ")

        #验证输入是否合法
        if choice.isdigit():
            choice = int(choice)

            # 判断余额是否充足
            if choice > 0 and choice <= len(goods_list):
                g_item = goods_list[choice - 1]

                if g_item[1] < salary:
                    salary -= g_item[1]
                    shoping_cart.append(g_item)

                else:
                    print('余额不足，还剩%s' % salary)
                print(g_item)

            else:
                print("编码不存在")

        # 退出后并打印商品信息
        elif choice == q:
            print('-----你已购买以下商品-----')
            for i in shoping_cart:
                print(i)
            print("您余额为%s" % salary)
            break