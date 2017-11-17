# __author__: wang_chongsheng
# date: 2017/9/25 0025
import time


# # 功能函数加参数
# def show_time(f):   #装饰器函数
#     def inner(*a, **b):
#         start = time.time()
#         f(*a, **b)
#         end = time.time()
#         print('speed %s' % (end - start))
#
#     return inner
#
#
# @show_time  # add = show_time(add)
# def add(*a, **b):       #功能函数
#     sums = 0
#     for i in a:
#         sums += i
#     print(sums)
#     time.sleep(1)
#
#
# add(1, 2, 3, 4, 10)


# 装饰器函数加参数
def logger(flag=''):
    def show_time(f):  # 装饰器函数
        def inner(*a, **b):
            start = time.time()
            f(*a, **b)
            end = time.time()
            print('speed %s' % (end - start))
            if flag == 'true':
                print('日志记录 ')

        return inner

    return show_time


@logger('true')
def add(*a, **b):  # 功能函数
    sums = 0
    for i in a:
        sums += i
    print(sums)
    time.sleep(1)


add(1, 2, 3, 4, 5)


@logger()
def bar():
    print('bar...')
    time.sleep(2)


bar()
# add(1, 2, 3, 4, 10)
