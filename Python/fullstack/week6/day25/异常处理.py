# @Time    : 2017/10/27 0027 09:58
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 异常处理.py
"""
while True:
    try:
        #代码块逻辑
        inp = input('请输入序号：')
        i= int(inp)
    except Exception as e:
    #Exception：能捕获所有Error
    #上述代码如果出错，自动执行当前块的内容
        i =1
    print(i)
"""

"""
#相当于做了if...else判断
try:
    int('waa')

# 如果捕获到相应类型错误，就不往下执行
except IndexError as e:
    print('IndexError',e)
except ValueError as e:
    print('ValueError',e)
except Exception as e:
    print('Exception',e)

else:
    print('else')

# 无论结果是什么，都会执行
finally:
    print('...')

"""

"""
try:
    raise Exception('BUGUOLE')
except Exception as e:
    print(e)
def db():
    return False
def index():
    try:
        r = input(">>")
        int(r)
        result = db()
        if not result:
            # r = open('log','a')
            # r.write('数据库错误')
            # 打开文件写日志
            raise Exception('数据库错误')

    except Exception as e:
        str_error = str(e)
        print(str_error)
        r = open('log','a')
        r.write(str_error)
        #打开文件写日志

index()
"""

"""
#自定义Error
class MyError(Exception):

    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

# obj = MyError('Error')
# print(obj)

try:
    raise MyError("oh...Error")
except MyError as e:
    print(e)  #e对象的__str__()方法，获取返回
"""


# assert条件，断言，强制用户服从，不服从就报错，并且可捕获，但是一般不捕获
print(23)
assert  1==2  #如果满足这个条件就输出23，不满足就输出456
print(456)