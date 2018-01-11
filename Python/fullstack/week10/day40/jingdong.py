# @Time    : 2018/1/11 0011 14:10
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : jingdong.py

import socket

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8888))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
        buf = connection.recv(1024)
        print(buf.decode('utf8'))
        connection.sendall(bytes("HTTP/1.1 201 ok\r\n\r\n","utf8"))
        with open('lesoon1.html','rb') as f:
            data = f.read()
        connection.sendall(data)
        connection.close()

if __name__ == '__main__':
    main()