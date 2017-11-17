# __author__: wang_chongsheng
# date: 2017/9/15 0015
# dic = {'name': 'Alice', 'age': 22, 'hbboy':{'gril_name':'Lucy','age':30},}
# dic = {'age': 'Alice', 'age': 22, 'hbboy':{'gril_name':'Lucy','age':30},}
# print(dic['hbboy'])
# a=list()
# print(a)
# dic ={'name':'Alice'}
# dic1 = {}
# dic2 = dict((('name','Alice'),))
# print(dic2)
# dic3 = dict([[1,2],])
# dic ={'name':'Alice'}
# dic['age']=18
# print(dic)
#
# dic.setdefault('hobby','gril')
# print(dic)
#
# dic3 = {'hobby': 'gril', 'name': 'Alice', 'age': 18}
#查找
# print(dic3['name'])
# print(list(dic3.keys()))
# print(list(dic3.values()))
# print(list(dic3.items()))

#修改
# dic4 = {'hobby': 'gril', 'name': 'Alice', 'age': 18}
# dic5 = {'name':'Luci'}
# dic4.update(dic5)
# print(dic4)

# dic5 = {'name': 'Luci', 'hobby': 'gril', 'age': 18}
# dic5.clear()  #清空字典
# print(dic5)
# del dic5['name'] #删除字典中指定键值对
# print(dic5)
#
# print(dic5.pop('age')) #删除字典中指定键值对,并返回键值对的值
# ret = dic5.pop('age')
# print(ret)
# print(dic5)
#
# a = dic5.popitem() #随机删除某组键值对，并以元组方式返回值
# print(a, dic5)
#
# del dic5  #删除整个字典
# print(dic5)

# dic6 = dict.fromkeys(['host','host2','host3'],['test1,test2,test3'])
# dic6 = dict.fromkeys(['host','host2','host3'],'test')
# dic6 = dict.fromkeys(['host','host2','host3'],['test1,test2,test3'])
# print(dic6)

# dic6['host2']='abc'
# print(dic6)

# 字典嵌套
# menu_catalog = {
#     "a":{
#         'a1':['aa'],
#         'a2':['ab'],
#         'a3':['ac']
#     },
#     "b":{
#       'b1':['ba']
#     },
#     'c':{
#         'c1':['ca']
#     }
# }
#
# #根据查找相应位置进行修改
# menu_catalog['a']['a1'][0]='hahaha...'
# print(menu_catalog)

# 排序，默认以键排序,values以值排序
# dic={5:'333',2:'666',4:'555'}
# print(sorted(dic.items()))


# 字典遍历
# dic5={'name':'Alice','age':18}
#
# for i in dic5: #i是键
#     print(i,dic5[i])
#
# for i,v  in dic5.items(): #字典转换成items耗时比索引慢
#     print(i,v)


# String 操作方法
# 单引号和双引号在python中无区别
# a = "Let's go"
# print(a)

# 重复输出字符串
# print("ha"*20)

# 通过索引取字符串
# print('Hello,World.'[2:])

# 关键字 in,字符串判断
# print('ll' in 'hello')

# 格式化字符串
# print("This is %s"%'pencil')

# 字符串拼接
# a = '123'
# b = 'abc'
# d = '345'
# c = a + b #效率低
# print(c)
#
# c = ' '.join([a, b, d]) #效率高
# print(c)


#string 的内置方法
# str = 'hello world {name} is {age}'
# print(str.count('l'))       #统计元素个数
# print(str.capitalize())     #字符串首字母大写
# print(str.center(50,'+'))   #居中
# print(str.endswith('d'))    #判断以某个内容结尾
# print(str.startswith('h'))  #判断以某个内容开始
# print(str.expandtabs(tabsize=10))
# print(str.find('z'))        #查找到第一个元素，并将索引值返回
# print(str.format(name='Alice',age='18'))    #格式化输出的另外一种方式
# print(str.format_map({'name':'Alice','age':18}))
# print(str.index('z'))
# print('12abc'.isidentifier()) #是否是非法变量
# print('My Title'.upper()) #小写字母变大写
# print('My Title'.lower()) #大写字母变小写
# print('My Title'.swapcase()) #反转，大变小，小变大
# print('My Title'.ljust(50,'*')) #元素左对齐
# print('My Title'.rjust(50,'*')) #元素右对齐
# print('\tMy Title\n'.strip())   #去掉换行符
# print('\tMy Title\n'.lstrip())  #去掉左边换行符
# print('\tMy Title\n'.rstrip())  #去掉右边换行符
# print('ok')
# print('My title'.rfind('t'))
# print('My name is Alice'.split())
# a = ['My', 'name', 'is', 'Alice']
# print(' '.join(a))
# print('My name is Alice'.rsplit('i',1))
# print('hello world'.title())



#摘一些重要的字符串方法
# str = 'hello world {name} is {age}'
# print(str.count('l'))       #统计元素个数
#
# print(str.center(50,'+'))   #居中
#
# print(str.startswith('h'))  #判断以某个内容开始
#
# print(str.find('z'))        #查找到第一个元素，并将索引值返回
# print(str.format(name='Alice',age='18'))    #格式化输出的另外一种方式
#
# print('My Title'.upper()) #小写字母变大写
# print('My Title'.lower()) #大写字母变小写
#
# print('\tMy Title\n'.strip())   #去掉换行符
#
# print('My name is Alice'.split())
# a = ['My', 'name', 'is', 'Alice']
# print(' '.join(a))


