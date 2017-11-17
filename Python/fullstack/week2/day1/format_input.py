#__Author__:wang_chongsheng
#__Date__: 2017-09-13

name = input("Name: ")
age = int(input("Age: "))
job = input("Job: ")
salary = input("Salary: ")
retired = 65

if salary.isdigit():
    salary = int(salary)
# else:
#     print("must input digit")
#     exit("must input digit")

msg = '''
-------info of %s--------
Name: %s
Age : %d
Job : %s
Salary: %f
You will be retired in %s years
---------End-------------
''' %(name,name,age,job,salary,retired  - age)
# %s s=string 字符串
# %d d=digit 证书
# %f f=float 小数f
print(msg)