# __author__: wang_chongsheng
# date: 2017/9/28 0028
# import sys
# import calculate,time #通过搜索路径找到calculate.py后，将calculate.py中的所有代码解释一遍（calculate=calculate.py）


# print(calculate.add(1,2))
#
#
# print(sys.path)
# #搜索路径： sys.path
# print(x) #name 'x' is not defined
# print(calculate.x)

# from calculate import add,sub #从模块调用方法
#
# print(add(1,2)) #3
# print(sub(1,2)) #-1
# print(calculate.x) #name 'calculate' is not defined
# time.sleep(1)
#
# from calculate import * # *调用模块中所有方法（不推荐使用）
#
# def add(x,y):
#     return x+y+2
#
# print(add(1,2))
# print(sub(1,2))

# from calculate import add as plus #改名字
#
# plus(1,2)
#模块是用来组织函数的
# 包(package)，用来组织模块的

# import web.logger
# logger.logger() #name 'logger' is not defined

# from web import logger
# from 包/模块 import 模块/方法
# from  web.web2 import logger
# loggerplogger()
# from 包/模块/方法 import 方法
# from web.web2.logger import logger
# logger()