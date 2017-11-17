#__Author__:wang_chongsheng
#__Date__: 2017-09-13

# for i in range(1,101):
#     if i % 2 == 1:
#         print("loop:",i)

# for i in range(1,101,2): #2 步长
#     print("loop",i)

# for i in range(100):
#     if i < 50 or i > 70:
#         print(i)
        # continue
    # print(i)

_user = "wcs"
_passwd = "123"

# passwd_authentication = False  #标志位
#
# for i in range(3):
#     username = input("Username: ")
#     password = input("Password:")
#
#     if username == _user and password ==_passwd:
#         print("Welcome %s login ..." % _user)
#         passwd_authentication = True #真，成立
#         break #跳出循环
#     else:
#         print("Invalid username or password !")
#         # if i == 2:
#         #     print ("输错次数太多，滚")
#
# if not passwd_authentication: #只有为True的情况下，条件成立
#     print("输错次数太多，滚!!!")

# for i in range(3):
#     username = input("Username: ")
#     password = input("Password:")
#
#     if username == _user and password ==_passwd:
#         print("Welcome %s login ..." % _user)
#         passwd_authentication = True #真，成立
#         break #跳出循环
#     else:
#         print("Invalid username or password !")
#         # if i == 2:
#         #     print ("输错次数太多，滚")
#
# #只要For循环正常执行完毕，中间没有打断，就会执行else语句。
# else:
#     print("输错次数太多，滚")

for i in range(3):
    username = input("Name: ")
    password = input("Passwd: ")
    if username == _user and password == _passwd:
        print("Welcome %s login" %_user)
        break
    else:
        print("Invalid username or password")

else:
    print("输入错误次数已超过3次，滚！！！")