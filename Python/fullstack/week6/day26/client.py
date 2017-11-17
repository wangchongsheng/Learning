# @Time    : 2017/10/27 0027 16:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : client.py

import socket

## family type
sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8000)
sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))
sk.close()