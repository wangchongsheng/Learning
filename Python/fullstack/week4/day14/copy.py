# __author__: wang_chongsheng
# date: 2017/9/20 0020


# s = [1, 'Bob', 'Alice']
#
# s2 = s.copy()
# s2[0] = 3
# print(s)
# print(s2)
# 浅拷贝
# s = [[1,2], 'Bob', 'Alice']
# s3 = s.copy()
# print(s3)
# s[0][1] = 3
# print(s3)
# print(s)
import copy

#
# husband = ['Bob', 123, [15000, 9000]]
#
# wife = husband.copy()
# wife[0] = "Alice"
# wife[1] = 345
#
# # xiaosan = copy.copy() #shallow copy
# xiaosan = copy.deepcopy(husband)
# xiaosan[0] = "Lucy"
# xiaosan[1] = 666
#
# xiaosan[2][1] -= 1999
#
# husband[2][1] -= 3000
#
# print(wife)
# print(xiaosan)

a = ['a', 1, [100, 90]]

b = a.copy()
b[0] = 'b'
b[1] = 2

c = copy.deepcopy(a)
c[0] = 'c'
c[1] = 3

c[2][1] -= 20
b[2][1] -= 15

print(b)
print(c)
