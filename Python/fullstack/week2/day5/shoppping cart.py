# __author__: wang_chongsheng
# date: 2017/9/14

salary = int(input("请输入你的工资: "))
shop_id = ['1', '2', '3', '4', '5']
shop_list = ['iPhone6s', 'Mac Book', 'coffee', 'Python Book', 'Bicyle']
shop_price = [5800, 9000, 32, 80, 1500]
goods_name = []
goods_price = []

print("以下是商品列表：")
for i in range(5):
    print(shop_id[i] + '. ' + shop_list[i] + '    ' + str(shop_price[i]))

while True:
    shop_select = int(input("请输入商品编号: "))
    price = salary - int(shop_price[shop_select - 1])
    diff = salary - int(sum(goods_price))

    if price < 1:
        print("余额不足，还差", diff)

    else:
        add_goods_name = goods_name.append(shop_list[shop_select - 1])
        add_goods_price = goods_price.append(shop_price[shop_select - 1])
        print("已经添加 %s 到购物车." % shop_list[shop_select - 1])
    keep_going_shopping = input("结束购物？[y/n]")

    if keep_going_shopping == "y" or keep_going_shopping == "Y":
        break
print("你已购买以下商品:")

for j in range(len(goods_name)):
    print(goods_name[j], "    ", goods_price[j])
print("您的余额为: %s\n欢迎下次光临！" % (salary - sum(goods_price)))

