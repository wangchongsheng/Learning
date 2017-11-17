# __author__: wang_chongsheng
# date: 2017/9/26 0026
import logging

# 创建一个logger对象
logger = logging.getLogger()

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()

# 创建一个标准流对象
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

#获取标准流对象
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 添加logger对象
logger.addHandler(fh)
logger.addHandler(ch)

# 更改logger日志级别
logger.setLevel(logging.INFO)

# 默认级别warning
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
