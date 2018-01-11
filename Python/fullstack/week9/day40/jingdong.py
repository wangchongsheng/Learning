# @Time    : 2017/12/27 22:04
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : jingdong.py
# @Software: PyCharm
import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 333))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        print (buf.decode("utf8"))
        # connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n"))
        with open('lesoon1.html', 'rb') as f:
            data = f.read()
        connection.sendall(data)
        connection.close()


if __name__ == "__main__":
    main()
