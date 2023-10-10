# Author:zqbin
# @Time:2023/9/27 11:54
# @Author:14988
# @Site:
# @File:demo02_logging.py
# @Software:PyCharm
# 1. 导入模块
import logging

# 2. 创建日志记录器
# logger = logging.getLogger()  # <RootLogger root (WARNING)>
# print(logger)
logger = logging.getLogger("test") # 创建test日志记录器<Logger test (WARNING)>，多次调用返回的是同一个日志记录器

# 3. 设置日志记录器的默认级别
logger.setLevel(logging.DEBUG)
# 4. 创建日志处理器
sh = logging.StreamHandler()
# 5. 设置日志处理器的默认级别
sh.setLevel(logging.WARNING)
# 6. 创建日志格式器
fm = logging.Formatter(
    fmt="[%(asctime)s]-%(module)s-%(lineno)d-%(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
# 7. 将日志格式器和处理器绑定
sh.setFormatter(fm)
# 8. 将日志处理器添加到日志记录器的handers当中
logger.addHandler(sh)

# 增加一个日志处理器，文件处理器
fh = logging.FileHandler(
    filename="test.log",
    encoding="utf8"
)
fh.setLevel(logging.DEBUG)
fh.setFormatter(fm)
logger.addHandler(fh)


logger.debug("这是DEBUG级别的日志")
logger.info("这是INFO级别的日志")
logger.warning("这是WARNING级别的日志")
logger.error("这是ERROR级别的日志")
logger.critical("这是CRITICAL级别的日志")