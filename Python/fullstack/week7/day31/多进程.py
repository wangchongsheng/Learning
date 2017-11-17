# @Time    : 2017/11/10 0010 16:36
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 多进程.py

from multiprocessing import Process
import time
def f(name):
    time.sleep(1)
    print('hello',name,time.ctime())

if __name__=='__main__':
    p_list=[]
    for i in range(10):
        p = Process(target=f,args=('123',))
        p_list.append(p)
        p.start()

    for p in p_list:
        p.join()

    print('end')