# __author__: wang_chongsheng
# date: 2017/9/19 0019

# 能调用方法的一定是列表
#
# li = [1,2,3]
# li.append(int('5'))
# print(li)
# 打开-操作-关闭
#
# file = open('TestFile','a',encoding='utf8')
# #data = file.read(5)
# #print(data)
# file.write('\nHello,world\n')
# file.write('Alice')
#
# file.close()

# file = open('TestFile', 'r', encoding='utf8')
#
# # print(file.read(5))
# # print(file.read(10))
# # print(file.readline())
# # print(file.readline())
# # print(file.readlines())
#
# data = file.readlines()
# file.close()
# number = 0
# for i in data:
#     # number += 1
#     # if number == 3:
#     #     i = ''.join([i.strip(), '1212'])
#     print(i.strip())


# f = open('TestFile', 'w', encoding='utf8')
# f.write('Hello,world\n')
# f.write('Alice\n')

# n = 0
# for i in f.readlines():
#     n += 1
#     if n == 6:
#         i = ','.join([i.strip(), '121we'])
#     print(i.strip())
# f.close()

# data = f.readlines()
# f.close()
# n = 0
# for i in data:
#     n += 1
#     if n == 6:
#         i = ','.join([i.strip(), '121we'])
#     print(i.strip())
#
# 这是最好的
# n = 0
# for i in f:  # for内部将f对象做成一个迭代器，用一行取一行。
#     n += 1
#     if n ==6:
#         i = ''.join([i.strip(),'12qw'])
#     print(i.strip())
# print(f.tell())
# print(f.read(2))
# print(f.tell())
#
# f.seek(0)
# print(f.read(4))
# print(f.tell())

# import  sys,time
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.1)

# f = open('TestFile', 'a+', encoding='utf8')

# print(f.isatty())
# f.truncate(5)
# # f.write('Hello,world')
# # f.truncate(5)
# print(f.tell())
# print(f.readline())
# f.write('Csking')
# print(f.tell())
# f.seek(0)
# print(f.readline())

# f.close()

# f = open('TestFile', 'r+', encoding='utf8')

# 终极问题
# n = 0
# for line in f:
#     n += 1
#     if n == 3:
#         # line=''.join([line.strip(),'Alice'])
#         f.write('Alice')

# 文件替换
# f_read = open('TestFile', 'r', encoding='utf8')
# f_write = open('TestFile2', 'w', encoding='utf8')
#
# n = 0
# for line in f_read:
#     n +=1
#     if n == 5:
#         # line='hello,Alice\n'
#         line = ''.join([line,'Hello,Alice\n'])
#     f_write.write(line)

# with
# f = open('TestFilE','r')
# with open('TestFile','r') as f:
#     print(f.read())
#     f.readline()
#
# print('Hello')

# with 同时管理多个文件
# with open('TestFile','r') as f_read,open('TestFile1','w') as f_write:
#     for line in f_read:
#         f_write.write(line)

# 打印系统保留标识符
# from keyword import kwlist
# print(kwlist)
# for i in kwlist:
#     print(i)

b = repr("he is happy \n Yes")
print(b)