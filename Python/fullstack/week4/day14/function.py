# __author__: wang_chongsheng
# date: 2017/9/21 0021

# define
# def test():
#     # print('ok')
#     for i in range(10):
#         print(i)
#
# # test()
# test() #调用一定记得加括号

# def add(x, y):
#     print(x + y)
#
# add(9,2)
# add(5,8)

# def test(index):
#     print('function %s' % index)
#
#
# test('aaa')
# def add(x, y): #参数按顺序对应
#     print(x)
#     print(y)
#
#
# add(9, 2)
import time


def loger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('log', 'a') as f:
        f.write('%s end anction%s\n' %(time_current,n))


def action1(n):
    print('start action1...')
    loger(n)


def action2(n):
    print('start action2...')
    loger(n)


def action3(n):
    print('start action3...')
    loger(n)


action1(1)
action2(2)
action3(3)

