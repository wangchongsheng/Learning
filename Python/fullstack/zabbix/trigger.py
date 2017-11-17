# __author__: wang_chongsheng
# date: 2017/10/26 0026
# --encoding=utf-8
from pyzabbix import ZabbixAPI


###pyzabbix
class pyzabbixAPI(object):
    def __init__(self):
        self.prioritytostr = {'0': 'ok', '1': '信息', '2': '警告', '3': '严重'}  # 告警级别

    def login(self):
        '''''
        进行认证
        返回 api 接口
        '''
        zapi = ZabbixAPI('http://zabbixdomain.com')
        zapi.login('user', 'pwd')
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
        triggerlist = []
        for t in triggers:
            if int(t['value']) == 1:
                triggerlist.append("[{0}] {1} : {2}({3}) - {4} {5}".format(
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(t['lastchange']))),
                    self.prioritytostr[t['priority']],
                    t['hosts'][0]['host'],
                    self.getHostgroupName(zapi, t['hosts'][0]['host']),
                    t['description'],
                    '(Unack)' if t['unacknowledged'] else ''
                )
                )
        return triggerlist

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