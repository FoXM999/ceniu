# Author:zqbin
# @Time:2023/9/27 11:57
# @Author:14988
# @Site:
# @File:demo03_logging.py
# @Software:PyCharm
import logging


logger = logging.getLogger()

logger.debug("这是DEBUG级别的日志")
logger.info("这是INFO级别的日志")
logger.warning("这是WARNING级别的日志")
logger.error("这是ERROR级别的日志")
logger.critical("这是CRITICAL级别的日志")