# __author__: wang_chongsheng
# date: 2017/10/23 0023
import json
#
# f = open('JSON_text', 'r')
#
# data = f.read()
# data = json.loads(data)
#
# print(data['name'])



f = open('JSON_text', 'r')

# data = f.read()
# data = json.loads(data)
data = json.load(f)

print(data['name'])
