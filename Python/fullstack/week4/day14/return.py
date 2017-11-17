# __author__: wang_chongsheng
# date: 2017/9/21 0021
# def f():
#     print('ok')
#
#     return (10)  # 作用：1.结束函数，2.返回某个对象
#
#
# a = f()
# print(a)
# print(f())

# def add(*args):
#     # print(args)
#     Sum = 0
#     for i in args:  # args=(1, 2, 3, 4, 5)
#         Sum += i
#     # print(sum)
#     return Sum
#
# a = add(1, 2, 3, 4, 5) #无命名参数
# print(a)

def foo():
    return 1, 'aaa', [1,2,3]


a = foo()  # (1, 'aaa', [1, 2, 3])

print(a)
# 注意点 ：
#     1.执行语句中只要遇到return，就结束并执行返回结果。
#     2.函数里如果不存在return，会默认返回一个None.
#     3.如果return多个对象，那么python会把多个对象封装成一个元组数据返回