
import urllib.request

import chardet
rawdata = urllib.request.urlopen('https://www.google.cn/').read()

print(chardet.detect(rawdata))