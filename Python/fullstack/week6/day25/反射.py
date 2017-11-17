# @Time    : 2017/10/27 0027 11:13
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 反射.py

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        return "s%--s%" %(self.name,self.age)
obj = Foo('Alice',18)

func = getattr(obj,'show')
print(func)
r = func()
print(r)

# b = "name"
# obj.__dict__[b]
# obj.__dict__['name']

# inp  = input('>>')
# #去什么东西里面获取什么值
# # v = getattr(obj,'name')
# v = getattr(obj,inp)
#
# print(v)


# 设置
# setattr(obj,'k1','v1')
# print(obj.k1)

# 删除东西
