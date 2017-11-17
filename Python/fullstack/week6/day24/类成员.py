# @Time    : 2017/10/26 0026 09:55
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 类成员.py
# 类成员之字段
# class Province:
#     #静态字段，属于类，保存在类中
#     country = '中国'
#
#     def __init__(self,name):
#         #普通字段，属于对象，保存在内存中
#         self.name = name
#
# #通过类访问
# print(Province.country)
#
# #通过字段访问
# sichuan = Province('四川')
# print(sichuan.name)



class Foo:
    def bar(self):
        print('bar')

    @staticmethod
    def sta():
        print('123')

    @staticmethod
    def stat(a1, a2):
        print(a1, a2)

    @classmethod
    def classmd(cls):
        # cls 是类名
        print(cls)
        print('classmd')
    #用于执行obj.per
    @property
    def perr(self):
        return 1

    #obj=123
    @perr.setter
    def perr(self,val):
        print(val)

    @perr.deleter
    def perr(self):
        print(666)
# 普通方法
# obj = Foo()
# obj.bar()

# 静态方法
# Foo.sta()
# Foo.stat(321,123)

# 类方法  ，用处不大
# Foo.classmd()

#类的属性
obj = Foo()
r = obj.perr
# print(r)

obj.perr = 123

del obj.perr
