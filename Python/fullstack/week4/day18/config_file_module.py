# __author__: wang_chongsheng
# date: 2017/9/27 0027

import configparser

# # 创建一个对象
config = configparser.ConfigParser()
#
# # 创建配置文件键值对
# config["DEFAULT"] = {'basedir': '/data/mysql',
#                      'socket': '/tmp/mysqld.sock',
#                      'error_log': 'mysqld_error.log'
#                      }
# config['server'] = {'port': '3306'}
#
# config['client'] = {'user': 'root',
#                     'password': '123456'
#                     }
# #将建配置信息写入配置文件
# with open('config.ini', 'w') as configfile:
#     config.write(configfile)

# print(config.sections())

# 读取配置文件中的键，因为default是特殊的键所以不能读取
config.read('config.ini')
# print(config.sections())
# print(config.defaults()) #打印default的值

# print(config['server']['port']) #打印键值对中的值

# for key in config['client']:
#     print(key)

# 删除
# config.remove_section('server')
# config.write(open('1.cfg','w'))

#改
config.set('client', 'user', 'Alice')
config.write(open('2.cfg','w'))

# 删除或者修改的过程，将新生成的内容放在对象里面，然后再覆盖之前的内容；并不知真正的取修改文件内容。

#增删改查功能
