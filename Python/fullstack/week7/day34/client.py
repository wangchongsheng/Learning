# @Time    : 2017/11/14 0014 17:54
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : client.py

import socket
sk =socket.socket
sk.connect(('127.0.0.1', 8000))

while 1:

    sk.sendall('hello'.encode('utf8'))
    data = sk.recv(1024)
    print(data.decode('utf8'))