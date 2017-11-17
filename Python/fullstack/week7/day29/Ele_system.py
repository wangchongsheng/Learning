# @Time    : 2017/11/8 0008 11:29
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : Ele_system.py
import pickle

class School:

    def __init__(self,name):
        self.name = name

    def save(self):
        pickle.dump()

s1 = School('上海')
s2 = School('北京')