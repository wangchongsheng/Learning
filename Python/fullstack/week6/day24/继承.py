# __author__: wang_chongsheng
# date: 2017/10/25 0025

#子承父类
"""
class F: #父类，基类

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')

class S(F): #子类，派生类
    def s1(self):
        print('S.s1')

obj=S()
obj.s1()
obj.f2()
"""
#子类只继承父类的某些特性
class F: #父类，基类

    def f1(self):
        print('F.f1')

    def f2(self):
        print('F.f2')

class S(F): #子类，派生类
    def s1(self):
        print('S.s1')
    def f2(self):
        # super(S,self).f2()#执行父类或者基类中的f2方法 （推荐使用）
        F.f2(self)          #执行父类或者基类中的f2方法
        print('S.f2')
"""
obj=S()
obj.s1()
obj.f2()
"""
"""
obj = S()
obj.s1() #s1中的self是形参，此时代指 obj
obj.f2() #self用于指调用方法的调用者
"""
"""
#同时执行子类和父类的f2
obj = S()
obj.f2()
"""

"""
#多继承
class F0:
    def b(self):
        print('F0.b')
class F1(F0):
    def a(self):
        print('F1.a')
class F2:
    def a(self):
        print('F2.a')

class S1(F1,F2): #从左到右，按顺序继承
    pass

obj = S1()
obj.b()
"""

#多继承的执行关系

class BaseRequest():
    def __init__(self):
        print('BaseRequest.init')
class RequestHandler(BaseRequest):
    def __init__(self):
        print('RequestHandler.init')  #2
    def server_forver(self):
        #self是obj。。。一定要记住self是谁的obj
        print('RequestHandler.server_forver')  #3
        self.process_request()
    def process_request(self):
        print('RequestHandler.process_request')
class Minx:
    def process_request(self):
        print('minx.process_request')       #5
class Son(Minx,RequestHandler):   #4
    pass

obj = Son() #1
obj.server_forver()  #6



# import socketserver
#
# obj = socketserver.TCPServer(1,2) #创建对象，init
# obj.serve_forever()