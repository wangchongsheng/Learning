#__Author__:wang_chongsheng
#__Date__: 2017-09-13

_user = "wcs"
_passwd = "123"

count = 0
while count < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == _user and password == _passwd:
        print("Welcome %s login" % _user)
        break
    else:
        print("Invalid username or password")
    count += 1
    if count == 3:
        keep_going_choice = input("还想玩吗？[Y/n]")
        if keep_going_choice == "y":
            count = 0
else:
    print("输入错误次数已超过3次，滚！！！")