__author__ = "xiaoyu hao"

import logging

#输出到屏幕同时输出到文件
#logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别
# create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # WARNING以上的输入到控制台

# create file handler and set level to warning
fh = logging.FileHandler("access.log",encoding='utf-8')
fh.setLevel(logging.ERROR)   # ERROR以上级别的输出到文件

# create formatter
ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh_formatter = logging.Formatter('%(asctime)s %(filename)s %(lineno)d - %(levelname)s:%(message)s')

# add formatter to ch and fh
ch.setFormatter(ch_formatter)
fh.setFormatter(fh_formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

