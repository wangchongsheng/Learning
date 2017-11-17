# __author__: wang_chongsheng
# date: 2017/9/25 0025

# 生成器
# s = (x * 2 for x in range(5))

# print(s)  # <generator object <genexpr> at 0x00000236B0D550A0>
# # 生成器生成的只是一个对象，并不是值
#
# print(next(s))  # s.__next__()  in py2: s.next()
#
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))  # StopIteration

# 生成器就是一个可迭代对象（Iterable）

# for i in s:   #调用next
#     print(i)

# 生成器的两种创建方式：
#     1.(x * 2 for x in range(5))
#     2.yield

# def foo():
#     print('ok')
#     yield 1
#
#     print('ok2')
#     yield 2
#
#     return None

# g=foo()
# print(g) #<generator object foo at 0x000001E1EE1F50A0>
#
# next(g)
# next(g)

# for i in foo(): #for循环遍历可迭代对象
#     print(i)

# 什么事可迭代对象(对象拥有iter方法的成为可迭代对象)
# l = [1,2,3]
# l.__iter__()
#
# t=(1,2,3)
# t.__iter__()
#
# d={'name':'123'}
# d.__iter__()

# for i in [1,2,3]:
#     print(i)

# 0 1 1 2 3 5 8 13 21

def fib(max):
    n, before, after = 0, 0, 1
    while n < max:
        # print(after)
        yield before

        before, after = after, before + after
        n = n + 1


g = fib(8)
print(g) #<generator object fib at 0x00000273999A50A0>