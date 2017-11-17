# __author__: wang_chongsheng
# date: 2017/9/26 0026

import time

# print(help(time))
# print(time.time()) #1506392191.09246 ：*****时间戳，当前时间，以秒显示 表示时间的一种方式

# time.sleep(3)     # *****时间暂停
# print(time.clock()) #计算CPU执行的时间



# print(time.gmtime())#结构化时间：time.struct_time(tm_year=2017, tm_mon=9, tm_mday=26, tm_hour=2, tm_min=31, tm_sec=17, tm_wday=1, tm_yday=269, tm_isdst=0)
# print(time.localtime())#***** 本地时间：time.struct_time(tm_year=2017, tm_mon=9, tm_mday=26, tm_hour=10, tm_min=33, tm_sec=29, tm_wday=1, tm_yday=269, tm_isdst=0)


# print(help(time.strftime))
# struct_time = time.localtime()
# print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time)) #******字符串时间


# print(time.strptime('2017-09-26 10:42:27','%Y-%m-%d %H:%M:%S'))
# # *****把当前字符串时间转换成元组结构化时间
#
# a = time.strptime('2017-09-26 10:42:27','%Y-%m-%d %H:%M:%S')
# print(a.tm_year)  #单独打印年月日
# print(a.tm_mon)
# print(a.tm_mday)

# print(time.ctime()) #固定格式的本地时间
# print(time.ctime(3600))

# print(time.mktime(time.localtime()))
#将本地时间转换为时间戳


# 时间戳，结构化时间，格式化时间


import datetime

print(datetime.datetime.now( ))

