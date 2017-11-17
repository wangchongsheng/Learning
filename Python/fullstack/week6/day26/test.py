# @Time    : 2017/11/2 0002 10:46
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : test.py

#python3 的两种数据类型： str  bytes
#
# str:unidoe
# bytes:十六进制字符

s ='Hello老王'

print(type(s))  #<class 'str'>

        #规则
# str ------------> bytes 编码

b = bytes(s,'utf8')
print(b) #b'Hello\xe8\x80\x81\xe7\x8e\x8b' #utf8规则下的bytes类型
print(type(b))  #<class 'bytes'>

#encoding编码
b2 = s.encode('utf8')
print(b2) #b'Hello\xe8\x80\x81\xe7\x8e\x8b'

b3 = s.encode('gbk')
print('gbk编码下的bytes数据',b3) #b'Hello\xc0\xcf\xcd\xf5'


#bytes --->str 解码
# s1 = str(b2,'gbk')
# print(s1)#Hello鑰佺帇  #乱码

#以什么方式编码的，就需要用什么方式解码

# 解码方法1
# s1 = str(b2,'utf8')
# print(s1)  #Hello老王  #str数据类型
#
# #解码方法2
# s2 = b2.decode('utf8')
# print(s2)

s3 = b3.decode('gbk')
print(s3) #Hello老王