# __author__: wang_chongsheng
# date: 2017/9/25 0025

# #列表生成式
# def fun(n):
#     return n ** 3
#
#
# a = [fun(x) for x in range(10)] #可对函数进行列表生成
# print(a)
# print(type(a))


# t = ['123', 8]
# a, b = t
# # 相当于
# # a=t[0]
# # b=t[1]
# print(a)
# print(b)


def bar():
    print('ok1')
    count=yield 1
    print(count)

    yield 2

b =bar()
# b.send(None) #第一次send前如果没有next，只能传一个send(None)
next(b)
ret=b.send('eee')
print(ret)