#__author__:"wang_chongsheng"
#__date__: 2017/9/14

_user = "wcs"
_passwd = "123"

for i in range(3):

    username = input("Username: ")
    password = input("password: ")

    if _user == username and _passwd == password:
        print("Welcome %s login ..." % _user)
        break
    else:
        print("Invalid username or password.")
else:
    print("错误次数过多，系统退出！")