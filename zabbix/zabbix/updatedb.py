import json
from urllib.request import Request, urlopen
from  urllib.error import URLError
from zabbix.wsgi import *
from moniter.models import Zabbix_moniter


class get_hostinfo:
    # 先定义API要用的基本信息
    def __init__(self):
        self.url = 'http://120.27.232.133:20000/zabbix/api_jsonrpc.php'
        self.header = {'Content-Type': 'application/json'}
        self.authID = self.login()

    # 登录的json请求，返回认证ID
    def login(self):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": "Admin",  # zabbix的管理员账号
                    "password": "zabbix"  # zabbix的管理员密码
                },
                "id": 0
            }).encode('utf-8')
        request = Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urlopen(request)
        except URLError as e:
            print('Auth Failed', e.errno)
        else:
            response = json.loads(result.read().decode('utf-8'))
            result.close()
            authID = response['result']
            return authID

            # 取数据的json请求基本格式，下面都要用到

    def get_data(self, data, param=""):
        request = Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server could not fulfill the request.')
                print('Error code: ', e.code)
            return 0
        else:
            response = json.loads(result.read().decode('utf-8'))
            result.close()
            return response

            # 取得指定hostgroup的hostid一览

    def get_hostids(self, groupid):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    "output": "hostid",
                    "groupids": groupid
                },
                "auth": self.authID,
                "id": 2
            }).encode('utf-8')
        res = self.get_data(data)['result']
        hostids = []
        for i in range(len(res)):
            hostids.append(res[i]['hostid'])
        return hostids

    # 根据hostid一览取得所有host的数据
    def get_info(self, groupid, method, info, parm=""):
        hostinfos = []
        infos = self.get_hostids(groupid)
        for i in infos:
            data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": method,
                    "params": {
                        "output": "extend",
                        "hostids": i,
                        "search": {
                            "key_": parm
                        },
                    },
                    "auth": self.authID,
                    "id": 2
                },).encode('utf-8')
            res = self.get_data(data)['result']
            hostinfos.append(res[0][info]) if len(res) != 0 else hostinfos.append("0")
        return hostinfos

    def update_sqlite(self, name, ipaddr, ping, disk):
        global zabbix_moniter
        zabbix_moniter, create = Zabbix_moniter.objects.update_or_create(
            ip=ipaddr, defaults={
                "name": name, 'ping': int(ping), 'disk': float(disk)
            })


def main():
    # 登录
    zbx = get_hostinfo()
    zbx.login()

    names = zbx.get_info("24", "host.get", "name")

    ips = zbx.get_info("24", "hostinterface.get", "ip")

    pings = zbx.get_info("24", "item.get", "lastvalue", "icmpping")

    disk = zbx.get_info("24", "item.get", "lastvalue", "hrStorageUsage2")
    for a, b, c, d in zip(names, ips, pings, disk):
        print(a,b,c,d)


if __name__ == '__main__':
    main()
