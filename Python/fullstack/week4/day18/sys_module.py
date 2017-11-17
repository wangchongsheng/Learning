# __author__: wang_chongsheng
# date: 2017/9/26 0026

#python 解释器进行交互

import sys
# print(sys.argv) #命令行参数
#
# def post():
#     print('ok')
#
# def dowload():
#     pass
#
# if sys.argv[1] == 'post':
#     post()
#
# elif sys.argv[1] == 'download':
#     dowload()

# sys.exit(n) #退出程序，正常退出sys.exit(0)

# print(sys.path)  #返回搜寻模块的路径

# print(sys.platform) #返回操作系统名称

import  os
if sys.platform =='win32':
    os.system('dir')
else:
    os.system('ls')