__author__ = "xiaoyu hao"

import logging,time

from logging import handlers

logger = logging.getLogger(__name__)

log_file = "timelog.log"
#fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3)  # 按文件大小分割,保留3个
fh = handlers.TimedRotatingFileHandler(filename=log_file,when="S",interval=5,backupCount=3,encoding="utf-8")

formatter = logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(message)s')

fh.setFormatter(formatter)

logger.addHandler(fh)


logger.warning("test1")
time.sleep(3)
logger.warning("test12")
time.sleep(3)
logger.warning("test13")
logger.warning("test14")