#__author__:"wang_chongsheng"
#date: 2017/9/13

name = input("Name: ")
age = input("Age: ")
job = input("Job: ")
salary = input("Salary: ")

msg = '''
---info of %s---
Name:%s
Age :%d
job :%s
Salary:%f 
-----End-----
''' % (name,name,age,job,salary)
print(msg)

# %s s = string 字符串
# %d d = digit  整数
# %f f = float  浮点型，小数