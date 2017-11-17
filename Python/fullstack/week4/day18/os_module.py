# __author__: wang_chongsheng
# date: 2017/9/26 0026

import os

print(os.getcwd())  # 获取当前工作目录

# os.chdir(r'e:\Learning')#更改目录
print(os.getcwd())

# print(os.curdir) #.
# print(os.pardir) #..

# os.makedirs('a\\b\\c') #当前工作目录中创建文件夹

# os.removedirs('a\\b\\c') #删除文件夹(只能删除空文件夹)

# os.mkdir('dirname')
# os.mkdir('dirname\\a')

# os.rmdir('dirname\\a') # 只删除单级空目录


# a = os.listdir(r'E:\Learning\Python\fullstack\week4\day18')
# print(a)  #列出当前文件夹中的文件

# os.remove('111')  #只能删除文件，不能删除文件夹

# os.rename('a', 'b') #文件或者文件夹重命名

# info = os.stat('.\\a.txt')
#
# print(info.st_size) #文件大小
# print(info) #文件信息

# print(os.sep) #目录分隔符 Windows '\' Linux '/'
# s = os.sep
# print('user%sAdministrator%sPycharm%sfullstack' %(s,s,s))

# print(os.pathsep) #输出分割文件路径的字符串

# print(os.system("dir"))  # 执行shell 命令

# print(os.environ) #输出环境变量信息

# print(os.path.abspath('./b')) #打印目录路径

# a = os.path.split(r'E:\Learning\Python\fullstack\week4\day18')
# print(a)

# a = os.path.dirname(r'E:\Learning\Python\fullstack\week4\day18')
# print(a)   # 打印出当前文件或者文件夹的上级目录
#
# b = os.path.dirname(__file__)
# print(b)
#
# c = os.path.exists(r'E:\Learning\Python\fullstack\week4\day18')
# print(c) #判断路径是否存在，如果存在返回True,不存在返回False

os.path.join() # 多个路径拼接组合


