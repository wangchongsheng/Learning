# @Time    : 2017/10/27 0027 14:13
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 单例模式.py


class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age
#
# obj = Foo() #obj对象，obj为称为F类的实例，（实例化）


#单例，用于使用同一份实例（对象）
"""
class Foo:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age)

v =None

while True:
    if v:
        v.show()
    else:
        v = Foo('Alice',18)
        v.show()
"""

class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo()
            return cls.__v
#不要在使用 类()
obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj2)
obj3 = Foo.get_instance()
print(obj3)