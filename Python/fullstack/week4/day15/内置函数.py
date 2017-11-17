# __author__: wang_chongsheng
# date: 2017/9/22 0022
# 重要内置函数
# 1.filter
# str = ['a', 'b', 'c', 'd']
#
#
# def fun1(s):
#     if s != 'a':
#         return s
#
#
# ret = filter(fun1, str)
# # print(ret)  # <filter object at 0x000001591355B470>
# print(list(ret))  # ret 是一个迭代器对象

# 2.map
# str = ['e', 'c', 'd']
#
#
# def fun2(s):
#     return s + 'Alice'
#
#
# ret = map(fun2, str)    #注意filter与map的区别
# print(ret)  #map object的迭代器
# print(list(ret))

# 3.reduce
# from functools import reduce
#
# def add1(x,y):
#     return x+y
#
# print(reduce(add1,range(1,101)))#reduce的结果就是一个值

# 4.lambda

def add(a, b):
    return a + b

a = add(lambda a, b: a + b)
print(a)
