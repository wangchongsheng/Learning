# __author__: wang_chongsheng
# date: 2017/9/21 0021

# def info(name,age,sex):
#     print('Name: %s' %name)
#     print('Age: %s' %age)
#     print('Sex: %s' %sex)


# info('Alice',18)    #必须参数
# info(age=18,name='Alice')   #关键字参数

# 默认参数
# def info(name,age,sex='male'):
#     print('Name: %s' %name)
#     print('Age: %s' %age)
#     print('Sex: %s' %sex)
#
#
# info('Luci',18)
# info('Bob',22)
# info('Alice',18,'female')

# Low
# def add(x,y):
#     print(x+y)
#
#
# add(1,2)

# High 不定长参数
# def add(*args):
#     print(args)
#     sum = 0
#     for i in args:  # args=(1, 2, 3, 4, 5)
#         sum += i
#     print(sum)
#
#
# add(1, 2, 3, 4, 5) #无命名参数

# 不定长命名参数
# def info(name,age,sex,job):
# def info(*args, **kwargs):
#     # print(args)  # ('Alice', 18, 'female')
#     # print(kwargs)  # {'height': 188, 'hobby': 'girls', 'job': 'IT'}
#     for i in kwargs:
#         print('%s:%s' % (i, kwargs[i]))


# info('Alice', 18, 'female', job='IT', hobby='girls', height=188)
# info('hahha',22,name='Alice',age=18,job='IT', hobby='girls', height=188)
# 关于不定长参数位置：无命名参数（*args）放在左边，命名参数**kwargs参数放在右边

# def info(sex='male',*args, **kwargs):
#     print(args)
#     print(sex)
#     # print(args)  # ('Alice', 18, 'female')
#     # print(kwargs)  # {'height': 188, 'hobby': 'girls', 'job': 'IT'}
#     for i in kwargs:
#         print('%s:%s' % (i, kwargs[i]))


# info()
# info('sss', 2, 3, 4, 'female',name='hello')
# info('Alice', 18, 'female', job='IT', hobby='girls', height=188)

# def f(*args):
#     print(args)
#
# f([1,2,3,4])

# 传输字典
# def f2(**kwargs):
#     print(kwargs)
#
# # f2(info={'name':'Alice'})
# f2(**{'name':'Alice'})