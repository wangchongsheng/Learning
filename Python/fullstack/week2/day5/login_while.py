#__author__:"wang_chongsheng"
#__date__:"2017/9/14"

_user = "wcs"
_passwd = "123"

count = 0

while count < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == _user and password == _passwd:
        print("Welcome %s login"% _user)
        break
    else:
        print("Invalid username or password.")
    count += 1

    if count == 3:
        keep_going_choice = input("是否要继续登陆？[Y/n]")
        if keep_going_choice == "y":
            count = 0
else:
    print("输入错误次数过多，系统已退出.")