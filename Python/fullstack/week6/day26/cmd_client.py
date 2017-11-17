# @Time    : 2017/11/1 0001 16:14
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : cmd_client.py
import socket

sk = socket.socket()
print(sk)

address = ('127.0.0.1', 8800)
sk.connect(address)

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    sk.sendall(bytes(111)) # 发送十六进制数据
    print(result_len)
    data = bytes()
    while len(data) != result_len:

        recv = sk.recv(1024)
        data += recv

    print(str(data,'gbk'))

sk.close()
