# __author__: wang_chongsheng
# date: 2017/10/23 0023
import shelve
f = shelve.open('SHELVE_text')

f['info']={'name':'Alice','age':'18'}
f['shopping']={'name':'Alice','price':'100'}
data=f.get('info')
# data=f['info']
print(data)