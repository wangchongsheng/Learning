# @Time    : 2017/11/2 0002 11:23
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : post_server.py
import os

import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8800)
sk.bind(address)
sk.listen(3)
print('waiting......')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
while 1:
    conn, addr = sk.accept()
    while 1:
        data = conn.recv(1024)
        cmd, filename, filesize = str(data, 'utf8').split('|')
        path = os.path.join(BASE_DIR, 'wcs', filename)
        filesize = int(filesize)

        f = open(path, 'ab')

        has_receive = 0
        while has_receive != filesize:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)
        f.close()


sk.close()
