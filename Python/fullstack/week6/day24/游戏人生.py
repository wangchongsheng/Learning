# @Time    : 2017/10/25 23:24
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : 游戏人生.py
class PrintData:
    def show(self):
        print('姓名：%s,性别：%s,年龄：%s,你当前战斗力为：%s' % (self.name, self.gender, self.age, self.fight))
class Person(PrintData):
    def __init__(self,n,a,g,f):
        self.name = n
        self.age = a
        self.gender = g
        self.fight = f
    def  GrassBattle(self):
        self.fight = int(self.fight) - 200
        super(Person,self).show()
    def SelfCultivation(self):
        self.fight = self.fight + 100
        super(Person, self).show()
    def MultiplayerGames(self):
        self.fight = int(self.fight) - 500
        super(Person, self).show()
obj = Person('仓井井','女',18,2000)
obj.GrassBattle()
obj.SelfCultivation()
obj.MultiplayerGames()
