# __author__: wang_chongsheng
# date: 2017/10/23 0023
import sys,os
#查找绝对路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR) #添加路径
# print(os.path.abspath(__file__))
from mudule import main
# print(os.path.dirname(os.path.abspath(__file__)))
main.main()