# __author__: wang_chongsheng
# date: 2017/10/24 0024
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from core import main:

if __name__ == '__main__':
    main.run()