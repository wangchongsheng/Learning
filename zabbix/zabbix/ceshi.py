from pyzabbix import ZabbixAPI

import time


class Zapi():
    def __init__(self):
        self.zapi = ZabbixAPI("http://120.27.232.133:20000/zabbix")
        self.zapi.login('Admin', 'zabbix')
        # print(self.zapi.api_version())

    def host_info(self):
        host_list=[]
        for host in self.zapi.host.get(output="extend"):
            # print(host['hostid'])
            ret = host_list.append(host['hostid'])

        return host_list

    def group_list(self):
        data = self.zapi.hostgroup.get(
            output=["groupid", "name"],
        )
        for group in data:
            print("Group ID:", group['groupid'],'\t\t',"GroupName:", group['name'])

    def group_host_list(self,groupid):
        data = self.zapi.host.get(
            output=["hostid", "name"],
            groupids=groupid,
        )
        for host in data:
            print("Host ID:", host['hostid'],'\t\t',"HostName:", host['name'])

    def get_items(self):
        data = self.zapi.item.get(
            output=["itemids", "key_"],
            hostids='10117',
        )
        for items in data:
            print("Item ID:", items['itemid'],'\t\t',"Key:", items['key_'])
    def get_items_history(self):
        data = self.zapi.history.get(
            output="extend",
            history=3,
            itemids="24515",
            limit=10,
        )
        Format = '%Y-%m-%d %H:%M:%S'
        # time_value=
        for values in data:
            dtime=values['clock']
            dt = time.localtime(int(dtime))
            dt2=time.strftime('%Y-%m-%d %H:%M:%S', dt)
            print("Time:",dt2,'\t\t',"Item ID:",values['itemid'],'\t','Ns:',values['ns'],'\t',"Values:",values['value'])
'''
    def update_sqlite(self, name, ipaddr, ping, disk):
        global zabbix_moniter
        zabbix_moniter, create = Zabbix_moniter.objects.update_or_create(
            ip=ipaddr, defaults={
                "name": name, 'ping': int(ping)
            })
'''
def main():
    obj = Zapi()
    # obj.group_list()
    # obj.group_host_list(10)
    # obj.get_items()
    # obj.get_items_history()
    ret = obj.host_info()
    print(ret)

if __name__ == '__main__':
    main()
