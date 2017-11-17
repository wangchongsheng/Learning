# @Time    : 2017/11/3 0003 15:22
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : threading_test.py

import threading
from time import ctime,sleep
import time
def music(func):
    for i in range(2):
        print("Begin listening to %s. %s" %(func,ctime()))
        sleep(2)
        print("end listenting %s" %ctime())

def move(func):
    for i in range(2):
        print("Begin watching at the %s! %s" %(func,ctime()))
        sleep(3)
        print("end listening %s"%ctime())
threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=music,args=('阿甘正传',))
threads.append(t2)

if __name__ ==  '__main__':
    for t in threads:
        t.setDaemon(True)  #守护进程
        t.start()

    print(threading.current_thread())

    print(threading.active_count())
    print("all over %s"%ctime)

