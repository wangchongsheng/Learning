# @Time    : 2017/10/26 0026 11:03
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : test1.py

class Pagenation:
    def __init__(self,current_page):
        try:
            p = int(current_page)
        except Exception as e:
            P = 1
        self.page = p

    @property
    def star(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val
li = []
for i in range(1000):
    li.append(i)

while True:
    p = input("请输入要查看的页码：")
    obj = Pagenation(p)
    print(li[obj.star:obj.end])