# __author__: wang_chongsheng
# date: 2017/10/25 0025

# 函数式编程
# def foo(name,age,sex,content):
#     print(name,age,sex,content)
#
# foo('Alice','18','famel','123')
# foo('Alice', '18', 'famel', '456')
# foo('Alice', '18', 'famel', '852')


# 面向对象

# class Bar:
#     def foo(self,name, age, sex, content):
#         print(name, age, sex, content)
#
# obj = Bar()
# obj.foo('Alice', '18', 'famel', '123')
# obj.foo('Alice', '18', 'famel', '456')
# obj.foo('Alice', '18', 'famel', '852')

#一个简单的class例子
# class Test:
#     def foo(self, arg):
#         print(self,self.name,self.age,self.content,arg)


# obj = Test()
# ret = obj.foo('Alice')
# print(ret)


# z = Test()
# z.name = 'Alice'
# z.age = '18'
# z.content= '123'
# z.foo('aaa')
#
# z1 = Test()
# z1.name = 'Lucy'
# z1.age = '24'
# z1.content= '456'
# z1.foo('ccc')
'''
# class 升级版
class Test:
    def add(self, arg):
        print(self,self.name,self.age,self.content,arg)
    def delete(self, arg):
        print(self,self.name,self.age,self.content,arg)
    def update(self, arg):
        print(self,self.name,self.age,self.content,arg)
    def get(self, arg):
        print(self,self.name,self.age,self.content,arg)
#class封装
obj = Test()
obj.name = 'Alice'
obj.age = '18'
obj.content = 'man'

obj.add('aaa')
obj.add('bbb')
obj.add('ccc')
'''


#class的构造方法
#
# class Test:
#     def __init__(self,n1,n2,n3,n4):
#         """
#         构造方法：构造方法的特性：类名()自动执行构造方法
#         """
#         self.name1=n1
#         self.name2=n2
#         self.name3=n3
#         self.name4=n4
#     def foo(self):
#         print(self.name1,self.name2,self.name3,self.name4)
#
# z = Test(1,2,3,4)
# print(z.name1)
# z.foo()
#init的特殊方法以及封装
# class Bar:
#     def __init__(self,n,a,s):
#         self.name=n
#         self.age=a
#         self.sex=s
#
#     def show(self,content):
#         print(self.name,self.age,self.sex,content)
#
#
# z = Bar('小明','18','男')
# z.show(111)
# z.show(222)
# z.show(333)

class DatabaseHelper:
    def __init__(self,ip,port,username,pwd):
        self.ip = ip
        self.port = port
        self.username = username
        self.pwd = pwd
    def add(self):
        print('')
s1 = DatabaseHelper('120.24.56.150','3306','admin','shengyan777.com')
