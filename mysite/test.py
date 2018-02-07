# @Time    : 2018/2/7 0007 11:20
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : test.py\


import  re
ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weew32ttt123/ooo')

print(ret.group())
print(ret.group('id'))
print(ret.group('name'))