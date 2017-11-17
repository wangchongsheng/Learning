# @Time    : 2017/11/3 0003 10:52
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : lesson_threading.py

'''
import time
import threading

begin=time.time()

def foo(n):
    print('foo%s'%n)
    time.sleep(1)
    print('end foo')

def bar(n):
    print('bar%s'%n)
    time.sleep(2)
    print('end bar')

# foo()
# bar()

t1=threading.Thread(target=foo,args=(1,))

t2=threading.Thread(target=bar,args=(2,))
t1.start()
t2.start()
print('....in the main.....')
end = time.time()
print(end-begin)
'''

import  time
import threading

begin = time.time()
def add(n):
    Sum = 0
    for i in range(n):
        Sum+=i
    print(Sum)

# add(10000000)
# add(20000000)
# end =time.time()
# print(end-begin)
t1 = threading.Thread(target=add,args=(10000000,))
t1.start()

t2 = threading.Thread(target=add,args=( 20000000,))
t2.start()

t1.join()
t2.join()

end =time.time()
print(end-begin)