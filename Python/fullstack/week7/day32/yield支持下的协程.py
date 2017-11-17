# @Time    : 2017/11/13 0013 11:48
# @Author  : "Wang_Chongsheng"

import  time
import  queue

def consumer(name):
    print("----->starting")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" %(name,new_baozi))
def producer():
    r = con.__next__()
    r = con2.__next__()
    n = 0
    # time.sleep(1)
    while n < 5:
        n += 1

        print("\033[32;1m[producer]\033[0m is making baozi %s"%n)

        con.send(n)
        con2.send(n)

if __name__ == '__main__':
    con = consumer('c1')   # 创建一个生成器对象con
    con2 = consumer('c2')  # 创建一个生成器对象con2
    p = producer()         #