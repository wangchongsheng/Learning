# @Time    : 2017/11/2 0002 11:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : post_client.py

import socket
import os

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8800)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    inp = input('>>>').strip()  # post \123.png

    # 路径分割
    cmd, path = inp.split('|')

    # 路径拼接
    path = os.path.join(BASE_DIR, path)

    # 获取文件名
    filename = os.path.basename(path)
    # 读取文件大小
    file_size = os.stat(path).st_size

    file_info = 'post|%s|%s' % (filename, file_size)

    sk.sendall(bytes(file_info, 'utf8'))

    # rb 以bytes的方式读取
    f = open(path, 'rb')

    has_sent = 0
    while has_sent != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_sent += len(data)
    f.close()
    print('upload done')