# __author__: wang_chongsheng
# date: 2017/9/25 0025

# list,tunple,dict,string:Iterable（可迭代对象）
# 生成器都是迭代器，迭代器不一定是生成器
# l = [1, 2, 3, 5]
# d = iter(l)  # l.__iter__()
# print(d)  # <list_iterator object at 0x0000017AFA524CC0>
#
# # 什么是迭代器？
# # 满足两个条件：1.有iter方法 2.有next方法
#
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))  #报错：StopIteration
# #
# for 循环内部的三件事：
#     1.调用可迭代对象的iter方法，返回一个迭代器对象
#     2.不断调用迭代器对象的next方法
#     3.处理StopIteration
#
# for i in [1, 2, 34]:
#     iter([1, 2, 34])

from collections import Iterator,Iterable

# print(isinstance(2,list))
# l = [1, 2, 3, 5]
# d = iter(l)  # l.__iter__()
# print(d)
# print(isinstance(l,list))
# print(isinstance(l,Iterable)) #判断是否是迭代对象
# print(isinstance(l,Iterator)) #判断是否是迭代器
# print(isinstance(d,Iterator)) #判断是否是迭代器

