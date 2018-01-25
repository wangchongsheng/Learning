from django.shortcuts import render

#!/usr/bin/env python
# Version = 3.5.2
# __auth__ = '无名小妖'
import time
from zabbix_client import ZabbixServerProxy

ZABBIX_URL = 'http://120.27.232.133:20000/zabbix'
ZABBIX_USERNAME = "Admin"
ZABBIX_PASSWORD = "zabbix"


class Zabbix:
    def __init__(self):
        self.zb = ZabbixServerProxy(ZABBIX_URL)
        self.zb.user.login(user=ZABBIX_USERNAME, password=ZABBIX_PASSWORD)

    def get_hostgroup(self):
        """
        查询组所有组获取组id和name
        :return: groupid和name
        """
        data = {
            "output": ['groupid', 'name']  # "output": "extend",   查看所有字段
        }
        ret = self.zb.hostgroup.get(**data)
        return ret

    def get_hostid(self, groupids=None):
        """
        通过组id获取相关组内的所有主机
        :param groupids: None表示获取所有组的主机，可以通过列表，元组等传入多个组id
        :return: "hostid"和"name"
        """
        data = {
            "output": ["hostid", "name"],
            "groupids": groupids
        }
        ret = self.zb.host.get(**data)
        return ret

    def item_get(self, hostids=None):
        """
        通过获取的hostid查找相关监控想itemid
        :param hostids: None表示获取所有主机的item，可以通过列表，元组等传入多个itemid
        :return: "itemids", "key_"
        """
        data = {
            "output": ["itemids", "key_"],
            "hostids": hostids,
        }

        ret = self.zb.item.get(**data)
        return ret

    def history_get(self, itemid, i, limit=10):
        """
        通过itemid 获取相关监控项的历史数据
        :param itemid:
        :param i: 0 - numeric float; 1 - character; 2 - log; 3 - numeric unsigned; 4 - text.
        :param limit: 获取数据的数量
        :return:
        """
        data = {"output": "extend",
                "history": i,
                "itemids": [itemid],
                "limit": limit
                }
        ret = self.zb.history.get(**data)
        return ret

    def add_zabbix_host(self, hostname="test_zabbix", ip="192.168.10.100", groupid="2"):
        """
        添加主机并且指定到组（传入主机名，IP地址和组ID）
        :param hostname:
        :param ip:
        :param groupid:
        :return:
        """
        data = {
            "host": hostname,
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": groupid
                }
            ]
        }
        ret = self.zb.host.create(data)
        return ret

    def get_template(self):
        """
        查看现有模板
        :return:
        """
        datalist = []
        datadict = {}
        data = {
            "output": ["templateid", "name"]
        }
        ret = self.zb.template.get(data)
        for i in ret:
            datadict[i['name']] = i['templateid']
            datalist.append(datadict)
        return datalist

    def link_template(self, hostid=10156, templateids=10001):
        """
        关联主机到模板
        :param hostid:
        :param templateids:
        :return:
        """
        data = {
            "hostid": hostid,
            "templates": templateids
        }

        ret = self.zb.host.update(data)
        return ret

    def create_maintenance(self, name="test", hostids=10156, time=2):
        """
        添加维护周期
        :param name:
        :param hostids:
        :param time:
        :return:
        """
        data = {
            "name": name,
            "active_since": 1458142800,
            "active_till": 1489678800,
            "hostids": [
                hostids
            ],
            "timeperiods": [
                {
                    "timeperiod_type": 0,
                    "period": 3600
                }
            ]
        }
        ret = self.zb.maintenance.create(data)
        self.host_status(10130, 1)
        return ret

    def get_maintenance(self):
        """
        获取维护周期
        :return:
        """
        data = {
            "output": "extend",
            "selectGroups": "extend",
            "selectTimeperiods": "extend"
        }
        ret = self.zb.maintenance.get(data)
        return ret

    #
    # def del_maintenance(self, maintenanceids):
    #     """
    #     获取维护周期之后，通过传入maintenanceid删除维护周期
    #     :param maintenanceids:
    #     :return:
    #     """
    #     return self.zb.maintenance.delete(maintenanceids)

    def host_status(self, hostid, status):
        """
        添加维护周期时候需要吧zabbix_host设置成非监控状态
        :param hostid:
        :param status:
        :return:
        """
        data = {
            "hostid": hostid,
            "status": status
        }
        return self.zb.host.update(data)

        # def host_del(self, hostids=10155):
        #     """
        #     通过hostids删除主机id,顺带也删除模板
        #     :param hostids:
        #     :return:
        #     """
        #     return self.zb.host.delete(hostids)

'''
if __name__ == "__main__":
    zabbix_server = Zabbix()
    zabbix_list=[]
    for i in zabbix_server.get_hostgroup():
        if i['groupid'] in ["1","2","5","6","7"]:
            pass
        else:
            zabbix_list.append("-------------------------------------------")
            zabbix_list.append("{0}{1}  {2}{3}".format("GroupID:",i["groupid"],"NodeName:",i['name']))
            for Host in zabbix_server.get_hostid(i["groupid"]):
                zabbix_list.append("{0}{1}  {2}{3}".format("HostID:",Host['hostid'],"HostName:",Host['name']))
    print(zabbix_list)
            # print(zabbix_server.item_get())
            # data = zabbix_server.history_get("24889",0)
            # print(zabbix_server.add_zabbix_host())
            # print(zabbix_server.get_template())
            # print(data[0]['Template OS Linux'])
            # print(zabbix_server.link_template())
            # print(zabbix_server.create_maintenance())
            # print(zabbix_server.host_del(10155))
            # print(zabbix_server.get_maintenance())
            # print(zabbix_server.del_maintenance(15)))
'''
def zabbix(request):
    zabbix_server = Zabbix()
    NodeInfo = []
    HostInfo = []
    item = []
    for i in zabbix_server.get_hostgroup():
        if i['groupid'] in ["1", "2", "5", "6", "7"]:
            pass
        else:
            # NodeInfo.append("-------------------------------------------")
            # NodeInfo.append("{0}{1}  {2}{3}".format("GroupID:", i["groupid"], "NodeName:", i['name']))
            NodeInfo.append(i['name'])
            for Host in zabbix_server.get_hostid(i["groupid"]):
                # HostInfo.append("{0}{1}  {2}{3}".format("HostID:", Host['hostid'], "HostName:", Host['name']))
                HostInfo.append(Host['name'])
                # for moniter in zabbix_server.get_template():
                    # if "10001" in moniter:
                    # item.append(moniter)
    dic = zabbix_server.get_template()[0]
    for Item in dic:
        if Item in ['Template OS Linux', 'Template App MySQL']:
            # item.append(dic[Item])
            item.append(dic[Item])
        else:
            pass
        for ItemID in item:
            ret = zabbix_server.history_get(ItemID, 3)
    # item.append(zabbix_server.get_template()[0])
                # for moniter in zabbix_server.history_get():
                #     item.append(moniter)

    return render(request,'index.html',{'NodeInfo':NodeInfo,'HostInfo':HostInfo,'item':item})

