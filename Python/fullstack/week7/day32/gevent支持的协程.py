# @Time    : 2017/11/13 0013 14:56
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : gevent支持的协程.py
# import gevent
# import time
# def foo():
#     print('Running in foo',time.ctime())
#     gevent.sleep(1)
#     print('Explicit context switch to foo again',time.ctime())
#
# def bar():
#     print('Running in bar',time.ctime())
#     gevent.sleep(0)
#     print('Implicit context switch to bar again',time.ctime())
#
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
# ])

#爬虫小程序
import urllib
import time
from gevent import monkey
import gevent
from urllib.request import urlopen
monkey.patch_all()
def f(url):
    print('GET: %s'% url)
    resp = urlopen(url)
    data = resp.read()

    with open('xiaohua.html','wb') as f:
        f.write(data)
    print('%d bytes received from %s.'%(len(data),url))
# l = ['https://www.python.org/','https://www.yahoo.com/','https://github.com/']
start = time.time()
# for url in l:
#     f(url)
gevent.joinall([
    # gevent.spawn(f,'https://www.python.org/'),
    # gevent.spawn(f,'https://www.yahoo.com/'),
    # gevent.spawn(f,'https://github.com/'),
    gevent.spawn(f,'http://blog.csking.cn/'),
    # gevent.spawn(f,'http://www.symbolics.com/'),

])

print(time.time()-start)