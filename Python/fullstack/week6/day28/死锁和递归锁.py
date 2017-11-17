# @Time    : 2017/11/6 0006 16:19
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 死锁和递归锁.py

import threading, time
'''

class myThread(threading.Thread):
    def doA(self):
        lock.acquire()
        print(self.name, 'gotlockA', time.ctime())
        time.sleep(3)
        lock.acquire()
        print(self.name, 'gotlockB', time.ctime())
        lock.release()
        lock.release()

    def doB(self):
        lock.acquire()
        print(self.name, 'gotlockB', time.ctime())
        time.sleep(2)
        lock.acquire()
        print(self.name, 'gotlockA', time.ctime())
        lock.release()
        lock.release()

    def run(self):
        self.doA()
        self.doB()


if __name__ == '__main__':
    lock = threading.RLock()
    threads = []
    for i in range(5):
        threads.append(myThread())

    for t in threads:
        t.start()
    for t in threads:
        t.join()
'''

class Account:
    def __init__(self, id, money):
        self.id = id
        self.balance = money

    def withdraw(self, num):
        r.acquire()
        self.balance -= num
        r.release()
    def repay(self, num):
        r.acquire()
        self.balance += num
        r.release()

def transer(_from, to, count):
    r.acquire()
    _from.withdraw(count)
    to.repay(count)
    r.release()

r=threading.RLock()
a1 = Account('Alice', 100)
a2 = Account('Lucy', 200000)
t1 = threading.Thread(target = transer, args = (a1, a2, 100,r))
t2 = threading.Thread(target = transer, args = (a2, a1, 200,r))

t1.start()
t2.start()
