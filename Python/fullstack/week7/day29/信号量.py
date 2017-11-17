# @Time    : 2017/11/7 0007 14:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 信号量.py
import threading,time

class myThread(threading.Thread):
    def run(self):
        if semaptore.acquire():
            print(self.name)
            time.sleep(3)
            semaptore.release()

if __name__ =="__main__":
    semaptore=threading.BoundedSemaphore(5)
    thrs=[]
    for i in range(23):
        thrs.append(myThread())
    for t in thrs:
        t.start()