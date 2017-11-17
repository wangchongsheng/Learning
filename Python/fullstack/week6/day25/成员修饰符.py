# @Time    : 2017/10/26 0026 14:51
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 成员修饰符.py


'''
class Foo:
    def __init__(self):
        self.name = 'Alice'  #公有字段
        self.__age = '18'   #私有字段，只能在内部调用
    def show(self):
        print(self.name,self.__age)
obj = Foo()
obj.show()

'''

"""
class F:
    __v = '123'
    def __info(self):  #私有方法
        return 666
    def show(self):
        r =  self.__info()
        return r
    @staticmethod
    def stat():
        return F.__v
ret = F.stat()
print(ret)

obj = F()
re = obj.show()
print(re)
"""

#class 执行构造方法

class MyType(type):
    def __init__(self,*args,**kwargs):
        #self =Foo
        print(123)
    def __call__(self, *args, **kwargs):
        #self = Foo
        r = self.__new__()

class Foo(object,metaclass=MyType):

    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        return '对象'
    def func(self):
        print("Hello World")

obj =Foo()
