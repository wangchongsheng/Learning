
# @Time    : 2017/11/6 0006 11:41
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 同步锁.py

import threading
import time
from time import sleep

def addNum():
    global num  #在每个线程中都获取这个全局变量
    lock.acquire()
    temp=num
    # print('--get num:',num)
    time.sleep(0.1)
    num = temp-1  #对公共变量进行-1操作
    # sleep(5)
    lock.release()

num = 100  #设定一个共享变量

thread_list = []
lock = threading.Lock()

for i in range(100):
    t =threading.Thread(target=addNum())
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()

print('final num:',num)