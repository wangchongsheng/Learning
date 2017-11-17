# @Time    : 2017/11/13 0013 11:52
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : test.py


def f():
    print('ok1')
    count =  yield 5
    print('0k2')
    yield 67
print(f()) #<generator object f at 0x000002D1909050A0>

gen = f()
# ret = next(gen)
# print(ret)

gen.send(None)

x = gen.send(100)
print(x)