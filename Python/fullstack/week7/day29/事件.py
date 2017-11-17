# @Time    : 2017/11/7 0007 15:19
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 事件.py
import threading,time
class Boss(threading.Thread):
    def run(self):
        print("BOSS：今天加班到22:00")
        event.isSet() or event.set()
        time.sleep(5)
        print("BOSS:<22:00>可以下班了")
        event.isSet() or event.set()

class Worker(threading.Thread):
    def run(self):
        event.wait()
        print('Worker：哎。。。。')
        time.sleep(1)
        event.clear()
        event.wait()
        print('Worker:ohyeah!')

if __name__=='__main__':
    event=threading.Event()
    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    for t in threads:
        t.start()
    for t in threads:
        t.join()