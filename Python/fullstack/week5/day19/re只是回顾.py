# __author__: wang_chongsheng
# date: 2017/9/28 0028

import re
# ret = re.findall('www.(\w+).com','www.baidu.com')
# print(ret) #分组优先的原则，所有只取出分组里面的值

ret = re.findall('www.(?:\w+).com','www.baidu.com')
print(ret) #加?: 取消分组匹配