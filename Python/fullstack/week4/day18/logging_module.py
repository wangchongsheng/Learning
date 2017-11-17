# __author__: wang_chongsheng
# date: 2017/9/26 0026
import logging

# 日志级别
# critical > error > warning > info > debug
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')  #系统默认级别是warning以上
# logging.error('error message')
# logging.critical('critical message')

#修改日志输出配置，默认日志输出方式为屏幕输出
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='test.log',
                    )# filemode='a' 默认是a
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='w')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

