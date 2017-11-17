# @Time    : 2017/11/13 0013 14:49
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : gevent下的协程.py


from greenlet import  greenlet
def test1():
    print(12)
    gr1.switch()
    print(34)
def test2():
    print(56)
    gr2.switch()
    print(78)
gr1 = greenlet(test1)
print(gr1.switch())
gr2 = greenlet(test2)
print(gr2.switch())