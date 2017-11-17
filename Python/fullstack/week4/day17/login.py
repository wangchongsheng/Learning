# __author__: wang_chongsheng
# date: 2017/9/25 0025
user = 'Alice'
passwd = '123456'

login_satus = False


def login():
    username = input("Please enter username: ").strip()
    password = input("Please enter password: ").strip()
    if user == username and passwd == password:
        print('Welcome ...')
        # home()
    else:
        print('Username or Password is not match.')

    return login

@login()
def home():
    print("Welcome to home page.")


home()
