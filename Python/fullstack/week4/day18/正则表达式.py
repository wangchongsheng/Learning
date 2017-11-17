# __author__: wang_chongsheng
# date: 2017/9/27 0027

# string提供的方法是完全匹配
# 引用正则：模糊匹配

import re

# 元字符

# string全找到
# ret = re.findall('w\w{2}l','hello world')
# print(ret)

# . 通配符
# ret = re.findall('w..l','hello world') # . 只能代指任意一个字符
# print(ret)

# ret = re.findall('w..l','hello w\n ld')
# print(ret)

# flag 修改正则规则，一般不用

# ^ 只匹配以第一个h开头的字符

# ret = re.findall('^h...o','hdadahello')
# print(ret)

# $ 从结尾开始匹配
# ret = re.findall('a...e$','fadgalicesdawsse')
# print(ret)


# * 重复匹配[0,+∞]
# ret = re.findall('uv*', 'sacasqaliceauvuuuuu')
# print(ret)

# + 重复匹配[1,+∞] 至少有一个能匹配
# ret = re.findall('ab+','dsgsdasdf')
# print(ret)

# ? [0,1] 重复0次或者一次
# ret = re.findall('a?b','aaabdsgsabdb')
# print(ret)

# {}
# ret = re.findall('a{1,3}b','aaaab') {1，}等价于{1，+∞}
# print(ret)

# 结论： *等于{0，正无穷}    + 等价于{1，+∞}   ?等价于{0，1}

# 字符集
# ret = re.findall('[cn,com]', 'aascn')
# ret = re.findall('[a-z]', 'adx')
# print(ret)

# []字符集：取消元字符的特殊功能 (\ ^ - 例外字符)

# ret = re.findall('[d,*]', 'adx*,')
# print(ret)

# ret = re.findall('[1-9,a-z,A-Z]', '12tyAS')
# print(ret)

# # ^放在[]里面：取反
# 反斜杠后边跟元字符去除特殊功能,比如\.
# 反斜杠后边跟普通字符实现特殊功能,比如\d
#
# \d  匹配任何十进制数；它相当于类 [0-9]。
# \D 匹配任何非数字字符；它相当于类 [^0-9]。
# \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
# \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
# \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
# \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
# \b  匹配一个特殊字符边界，比如空格 ，&，＃等

# print(re.findall('\d{11}','sasd1112411412123123346363'))

# print(re.findall(r'\bI','hello Iam a LIST'))



# 匹配出第一个满足条件的结果
# print(re.search('ab','fsfeabfgab'))
# <_sre.SRE_Match object; span=(4, 6), match='ab'>

# ret = re.search('a\.','a.gj').group()
# print(ret)


# print(re.findall('\\c','adsD\c'))
#
# print(re.findall('\\\\c','adsD\c'))
# ret = re.findall(r'\\','abc\de')
# print(ret)

# m = re.search(r'\bblow','blow') #加r表示原生字符串，不需要转义
# print(m)

# () 做分组
# print(re.search('(as)+', 'sdjkfasas').group())  # asas
# print(re.search('(as)|3', '3as').group())  # asas

# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
#
# print(ret.group())
# print(ret.group('id'))
# print(ret.group('name'))


# match（）： 只在字符串开始匹配

# ret = re.match('asd','asdfffasd')
# print(ret)
# print(ret.group())

# split *****

# ret =re.split('k','dfghksd')
# print(ret)

# ret =re.split('[g,s]','dfghksd')
# print(ret)

# sub 替换
# ret = re.sub('a...e','s...b','edaliceoe')
# print(ret)

# compile 把正则表达式编译成一个正则表达式对象
# obj = re.compile('\.com')
# ret = obj.findall('edalice.comoe')
# print(ret)

ret=re.findall('a[bc]d','abcd')
print(ret)