# @Time    : 2017/11/14 0014 15:29
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : IOtest.py

import socket
sk = socket.socket()
bind = sk.bind(('127.0.0.1',8000))
sk.listen(3)

sk.setblocking(False)
import  time

while 1:
    try:
        conn,addr=sk.accept()
        print(addr)

        data = conn.recv(1024)
        print(data.decode('utf8'))
        conn.sendall(data)
    except Exception as e:
        print('error:',e)
        time.sleep(3)