# __author__: wang_chongsheng
# date: 2017/9/22 0022

# #闭包
# def outer():
#     x=10
#     def inner(): #条件1：inner就是内部函数
#         print(x) #条件2：外部环境的一个变量
#     return inner    #结论：内部函数inner就是一个闭包
#
# outer()()
# # inner()#局部变量，全局变量无法调用
#
# f =outer()
# f()
import time


# 遵守开放封闭原则
def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('speed %s' % (end - start))

    return inner


@show_time  # foo = show_time(foo)
def foo():
    print('foo...')
    time.sleep(2)


@show_time  # bar = show_time(bar)
def bar():
    print('bar...')
    time.sleep(2)


# foo()
# show_time(foo)

# foo()  # 执行inner函数
foo()
bar()
