# __author__: wang_chongsheng
# date: 2017/10/23 0023
import pickle

f = open('PICKLE_text', 'rb')

data = f.read()
data = pickle.loads(data)

data()