# @Time    : 2017/11/1 0001 16:14
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : cmd_server.py

# 远程执行命令
import subprocess

import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8800)
sk.bind(address)
sk.listen(3)
print('waiting......')

while 1:
    conn, addr = sk.accept()
    print(addr)
    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            break
        if not data: break
        print('......', str(data, 'utf8'))

        obj = subprocess.Popen(str(data, 'utf8'), shell=True, stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        result_len = bytes(str(len(cmd_result)), 'utf8')
        conn.sendall(result_len) #粘包现象，这条语句执行的时候紧接着执行下一跳命令
         # import time
        # time.sleep(1)
        conn.recv(1024)  #解决粘包现象
        conn.sendall(cmd_result)

sk.close()
