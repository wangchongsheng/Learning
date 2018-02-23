from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
from pyzabbix import ZabbixAPI
import time


###pyzabbix
class pyzabbixAPI(object):
    def __init__(self):
        self.prioritytostr = {'0': 'ok', '1': '信息', '2': '警告', '3': '故障','4':'严重','5':'灾难'}  # 告警级别
    def login(self):
        '''''
        进行认证
        返回 api 接口
        '''
        zapi = ZabbixAPI('http://120.27.232.133:20000/zabbix')
        zapi.login('Admin', 'shengyan777.com')
        return zapi

    def getCurIssue(self, zapi):
        '''''
        获取所有最近有问题的trigger
        返回trigger的信息列表： ['trigger1','trigger2',......]
        '''
        triggers = zapi.trigger.get(
            only_true=1,
            skipDependent=1,
            monitored=1,
            active=1,
            output='extend',
            expandDescription=1,
            selectHosts=['host'],
        )

        # 获取未确认的trigger
        unack_triggers = zapi.trigger.get(
            only_true=1,
            skipDependent=1,
            monitored=1,
            active=1,
            output='extend',
            expandDescription=1,
            selectHosts=['host'],
            withLastEventUnacknowledged=1,
        )
        unack_trigger_ids = [t['triggerid'] for t in unack_triggers]
        for t in triggers:
            t['unacknowledged'] = True if t['triggerid'] in unack_trigger_ids else False

            # 每个trigger信息格式 ：[时间] 级别：ip - 详情 是否确认
        hostlist = []
        triggerlist = []
        timelist =[]

        for t in triggers:
            if int(t['value']) == 1:
                # triggerlist.append("[{0}] {1} : {2}({3}) - {4} {5}".format(
                timelist.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(t['lastchange']))))
                hostlist.append(t['hosts'][0]['host'])
                triggerlist.append("({0})-{1}".format(
                    # time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(t['lastchange']))),
                    self.prioritytostr[t['priority']],
                    # self.getHostgroupName(zapi, t['hosts'][0]['host']),
                    t['description'],
                    # '(Unack)' if t['unacknowledged'] else ''
                )
                )
        return hostlist,triggerlist,timelist

    def getHostgroupName(self, zapi, hostname):
        '''''
        通过hostname(即ip)获取host所在的监控组名
        返回由组名组成的字符串
        '''
        groups = zapi.host.get(
            search={"name": hostname},
            selectGroups=['name'],
            output=['groups']
        )[0]['groups']
        groupname = [group['name'] for group in groups]
        return ' '.join(groupname)

def zabbix(request):
    # return  HttpResponse(main())
    papi = pyzabbixAPI()
    zapi = papi.login()
    Host = papi.getCurIssue(zapi)[0][::-1]
    target = papi.getCurIssue(zapi)[1][::-1] #列表倒序
    Time = papi.getCurIssue(zapi)[2][::-1]
    # return render(request,'index.html',{'Host':Host,'target':target,"Time":Time})
    return render(request,'index.html',locals())