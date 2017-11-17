# __author__: wang_chongsheng
# date: 2017/9/28 0028

import re, os, sys

# s = '1 -2 *((60-30 +(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14)) -(-4*3)/(16-3*2))'
#
# #将字符串中的空格替换掉
# ret_sub = re.sub(' ','',s)
#
# #先匹配最里面的括号
# ret = re.search('\([^()]+\)',ret_sub).group()
# print(eval(ret))

source = '1 -2 *((60-30 +(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14)) -(-4*3)/(16-3*2))'


# 检查表达式合法
def check(s):
    flag = True
    if re.findall('[a-zA-Z]', s):
        print('Invalid')
        flag = False
    return flag


# 格式化字符串
def format(s):
    s = s.replace(' ', '')
    s = s.replace('++', '+')
    s = s.replace('+-', '-')
    s = s.replace('-+', '-')
    s = s.replace('--', '+')
    s = s.replace('*+', '*')
    s = s.replace('/+', "/")
    return s


def cal_mul_div(s):
    ret1 = re.search('\d+\.?\d* [*/] \d+\.?\d*', s).group()
    x, y = re.split('[*/]', ret)  # '0.5' '3.9'

    if '*' in ret1:  # 判断乘除
        ret2 = float(x) * float(y)
        str(ret2)
    else:
        ret2 = float(x) / float(y)
        str(ret2)
    s.replace(ret1, ret2)

    return s


def cal_add_sub(s):
    ret1 = re.search('\d+\.?\d* [+-] \d+\.?\d*', s).group()
    x, y = re.split('[+-]', ret)  # '0.5' '3.9'

    if '+' in ret1:  # 判断加减
        ret2 = float(x) + float(y)
        str(ret2)
    else:
        ret2 = float(x) - float(y)
        str(ret2)
    s.replace(ret1, ret2)

    return s


# 检查函数
if check(source):
    strs = format(source)

    while re.search('\('):
        strs = re.search('\([^()]\)', strs)
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs)
    else:
        strs = cal_mul_div(strs)
        strs = cal_add_sub(strs)
