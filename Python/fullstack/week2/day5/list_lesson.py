# __author__: wang_chongsheng
# date: 2017/9/14

# names = 'Alice Lucy David'
# a = ['Alice', 'Lucy', 'David', 'Luci','Tom']

# 增删改查


# print(a[1:]) #取到最后
# print(a[1:-1]) #取到倒数第二个值
# print(a[1:-1:1]) #从左到右一个一个去取
# print(a[1::2]) #从左到右隔一个去取
# print(a[3::-2]) #从右到左

# b = a[-2::-1]
# print(b[3]) #

# append insert
# a.append('Obama') #默认插入到最后一个位置
# print(a)
# a.insert(1,'Obama') #可以将数据插入到任意位置
# print(a)

# Modify
# a[3] = 'Tomcat'
# a[1:3] = ['Tomcat','Csking']
# print(a)

# remove pop Delete
# a.remove('Luci') #只能删除列表中的一个值
# a.remove(a[1])
# b = a.pop(1) #pop 删除后会返回一个值,如果不指定值回默认删除最后一个
# del a[1:5:2] #可删除任何值
# print(a)
# print(b)

# #统计列表中某个元素出现的次数
# a = ['to', 'or', 'not', 'not', 'to']
# print(a.count('to'))

# extend
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

# index 索引
# a = ['Alice', 'Lucy', 'David', 'Tom', 'Luci', 'Tom']
#
# first_tom_index = a.index('Tom') #取第一个Tom的位置
# print("first_tom_index",a.index('Tom'))
# litte_list = a[first_tom_index+1:] #切片取小列表
#
# second_tom_index = litte_list.index('Tom') #取第二个列表的位置
# print("second_tom_index",second_tom_index)
# print("second_tom",first_tom_index+second_tom_index+1)#打印出第二个Tom的位置

# reverse
# a = ['Alice', 'Lucy', 'David', 'Tom', 'Luci', 'Tom']
# a.reverse() #倒序
# print(a)

# x = [4, 6, 2, 1, 7, 9]
# x.sort(reverse=(True))
# print(x)

a = ['Alice', 'Lucy', 'David', 'Tom', 'Luci', 'Tom']
# a.sort() #排序
# print(a)
if a.count("Tom") == 0:
    print("Tom not exist.")
else:
    print ("Tom exist.")