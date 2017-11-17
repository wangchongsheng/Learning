# __author__: wang_chongsheng
# date: 2017/10/23 0023
import json
#---------------dumps
# dic = {'name': 'Alice', 'age': '18'}
#
# data = json.dumps(dic)
# f = open('JSON_text', 'w')
# f.write(data)
# f.close()



#-----------dump
dic = {'name': 'Alice', 'age': '18'}

data = json.dumps(dic)
f = open('JSON_text', 'w')

json.dump(dic,f)
# f.write(data)
f.close()


