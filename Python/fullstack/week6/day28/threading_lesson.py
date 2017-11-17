# @Time    : 2017/11/6 0006 11:19
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : threading.py
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  #定义每个线程要运行的函数
        print("runing on number:%s" % self.num)
        time.sleep(3)


if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()
