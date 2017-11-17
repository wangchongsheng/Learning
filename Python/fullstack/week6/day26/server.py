# @Time    : 2017/10/27 0027 16:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : server.py

import socket

# family, type
sk = socket.socket()

print(sk)
address = ('127.0.0.1', 8000)
# 绑定地址
sk.bind(address)
# 设置排队的数量
sk.listen(3)
print('waiting.....')
conn, addr = sk.accept()
# conn时客户端的sock对象

# print(conn)
# print(addr)

# inp = input('>>>')
# conn.send(bytes(inp,'utf8'))

# data = conn.recv(1024)
# print(data)
while 1:
    conn, addr = sk.accept()
    print(addr)

    while 1:
        try:
            data = conn.recv(1024)
        except Exception:
            break

        if not data: break
        inp = input('>>>')
        conn.send(bytes(inp, 'utf8'))

        data = conn.recv(1024)
        print(data)

# 关闭当前链接
conn.close()
#关闭服务器所有链接
sk.close()
