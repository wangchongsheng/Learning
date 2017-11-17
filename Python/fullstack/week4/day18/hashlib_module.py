# __author__: wang_chongsheng
# date: 2017/9/26 0026

import hashlib

# # 1.MD5
#
# m = hashlib.md5()
# print(m)
#
# m.update('hello world'.encode('utf8'))
#
# #16进制
# print(m.hexdigest()) #5eb63bbbe01eeed093cb22bb8f5acdc3
#
# m.update('Alice'.encode('utf8')) #进行拼接 再次转换
# print(m.hexdigest())
#
#
# m2=hashlib.md5()
#
# m2.update("hello worldAlice".encode('utf8'))
# print(m2.hexdigest())

# 2.sha

s = hashlib.sha256()  #算法越复杂，效率越低
s.update('hello word'.encode('utf8'))

print(s.hexdigest())