# @Time    : 2017/11/10 0010 10:34
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : setting.py

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BIND_HOST = '127.0.0.1'
BIND_PORT = 9992

USER_HOME = os.path.join(BASE_DIR, 'home')

USER_ACCOUNT = {
    'alice': {
        'password': 'alice123',
        'quotation': 1000000,
        'expire': '2017-10-22'
    },
    'lucy': {
        'password': 'lucy123',
        'quotation': 1000000,
        'expire': '2017-10-22'
    },
}
