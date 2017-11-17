#coding:utf8
# __author__: wang_chongsheng
# date: 2017/9/19 0019
# import sys
# print(sys.getdefaultencoding())
s = "I'm 特斯拉"
s_to_gbk = s.encode('gbk')
print(s)
print(s_to_gbk.decode("gbk"))
