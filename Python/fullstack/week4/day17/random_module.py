# __author__: wang_chongsheng
# date: 2017/9/26 0026

# 随机数模块

import random


# print(random.random())
# print(random.randint(1,8)) #1--8的随机数(包括8)
# print(random.choice('hello')) #字符串随机
# print(random.choice(['123',4,[1,2]])) #列表随机
# print(random.sample(['123',4,[1,2]],2))  #随机选择列表中的2个值
# print(random.randrange(1,3))  # 数字随机，不包含最后一位

# 5位验证码
def v_code():
    code = ''
    for i in range(5):
        add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        # if i == random.randint(0, 3):
        #     add = random.randrange(10)
        # else:
        #     add = chr(random.randrange(65, 91))

        code += str(add)

    print(code)


v_code()

# print(chr(97)) ASCLL对应值
