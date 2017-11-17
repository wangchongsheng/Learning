# @Time    : 2017/11/10 0010 10:18
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : service.py

import socket,socketserver

REQUEST_CODE = {
    '1001':'cmd info',
    '1002':'cmd ack',
    '2001':'post info',
    '2002':'ACK(可以开始上传)',
    '2003':'文件已经存在',
    '2004':'续传',
    '2005':'不续传',
    '3001':'get info',
    '3002':'get ack',
    '4001':'未授权',
    '4002':'授权成功',
    '4003':'授权失败',
}

class Server(object):
    pass
class MultiServerHangdler(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes("欢迎登陆",'utf-8'))
        obj = Action(conn)
        while True:
            client_bytes = conn.recv(1024)
            if not client_bytes:
                break
            client_str = str(client_bytes,encoding='utf-8')
            if obj.has_login:
                o = client_str.split('|',1)
                if len(o) > 0:
                    func = getattr(obj,o[0])
                    func(client_str)
                else:
                    conn.sendall('输入格式错误','utf-8')
            else:
                obj.login(client_str)

        conn.close()

class MultiServer(object):
    def __init__(self):
        server = socketserver.ThreadingTCPServer((setting.BIND_HOST,setting.BIND_PORT),MultiServerHangdler)
        server.serve_forever()
class Action(object):
    def __init__(self,conn):
        self.conn = conn
        self.has_login = False
        self.username = None
        self.home = None
        self.current_dir = None
    def login(selforigin):
        pass
