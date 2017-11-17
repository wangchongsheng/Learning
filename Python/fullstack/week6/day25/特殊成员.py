# @Time    : 2017/10/26 0026 15:32
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 特殊成员.py
'''
class Foo:
    def __init__(self):
        print('init')
    def __call__(self, *args, **kwargs):
        print('call')
# obj = Foo()
# obj()
Foo()()
'''


'''
class Foo:
    def __init__(self):
        pass

    def __int__(self):
        return 111

    def __str__(self):
        return "Alice"

obj = Foo()

r = int(obj)
print(r)

s = str(obj)
print(s)
'''


'''
class Foo:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def __str__(self):
        return "%s--%s" %(self.name,self.age,)

# obj = Foo('Alice',18)
#
# print(obj)

# d = Foo.__dict__
# print(d)
'''

"""
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __getitem__(self, item):
        # return item+10
        #如果item是基本类型：int,str，索引取值
        #slice对象的话，做切片处理
        if item == slice:
            print("调用者进行内部切片处理")
        else:
            print("调用者希望内部做索引处理")
    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)
li = Foo('Alice',18)
# r = li[8] #自动执行li对象的类中的__getitem__方法，8当作参数传递给item
# print(r)
#
# re = li[100] = 'asdf'
#
# del li[999]

#除了getitem有返回值外，其他的都没有返回值

li[123]
li[1:4:2]
"""

'''
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __iter__(self):
        return iter([11,22,33])
li = Foo('Alice',18)
#如果类中有__iter__方法，那么类中的对象就是可迭代对象
# 对象.__iter__() 的返回值: 迭代器
# for 循环，迭代器，next
# for 循环，可迭代对象，对象.__iter__方法，并获取返回值
#1、获取li对象中的类Foo类中的__iter__方法，并获取其返回值
#2、循环上一步中返回的对象
for i in li:
    print(i)
'''

