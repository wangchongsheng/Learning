# __author__: wang_chongsheng
# date: 2017/9/28 0028

import re

# s = '(2+0.5*3.9)'
ret1 = re.search('\d+\.?\d* [*/] \d+\.?\d*', '(2+0.5*3.9)')
print(ret1.group())