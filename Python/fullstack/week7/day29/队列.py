# @Time    : 2017/11/8 0008 10:20
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 队列.py

#多线程利器queue

import queue

#存放数据的个数
d =queue.Queue(3)


d.put('Alice',0)
d.put('Lucy')
d.put('Luci')


#FIFO(first in，first out)
print(d.get())
print(d.get())
print(d.get())
print(d.get(0))

#队列模式
#   FIFO
#   LIFO