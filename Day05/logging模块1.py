__author__ = "xiaoyu hao"

import logging

#logging的日志可以分为 debug(), info(), warning(), error() and critical() 5个级别
#logging.basicConfig(filename='example.log',level=logging.INFO)  #日志级别是INFO，下面只输出info和warning的信息
logging.basicConfig(filename='example.log',level=logging.INFO,
                    format='%(asctime)s %(filename)s %(module)s %(lineno)d - %(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')