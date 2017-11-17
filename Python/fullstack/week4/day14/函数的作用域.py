# __author__: wang_chongsheng
# date: 2017/9/21 0021


# def f():
#     a = 10
# a = f()
# print(a)


# x = int(2.9)  # int built-in 系统变量
#
# g_count = 0  # global,全局变量
#
#
# def outer():
#     o_count = 1  # enclosing 嵌套作用域
#
#     def inner():
#         i_count = 2  # local 局部作用域
#         print(o_count)
#     inner()
# outer()


# count = 10
#
#
# def outer():
#     global count #局部变量不能修改全局变量
#     print(count)
#     count = 5
#     print(count)
#
#
# outer()

# def outer():
#     count = 10
#     def inner():
#         nonlocal count
#         count = 20
#         print(count)
#     inner()
#     print(count)
#
# outer()

# a = 10
# def b():
#     print(a)    #local variable 'a' referenced before assignment
#     a =5
# b()
