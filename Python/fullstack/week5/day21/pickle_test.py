# __author__: wang_chongsheng
# date: 2017/10/23 0023
import pickle


def foo():
    print('ok')


data = pickle.dumps(foo)
f = open('PICKLE_text', 'wb')
f.write(data)
f.close()