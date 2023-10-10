# Author:zqbin
# @Time:2023/9/27 14:08
# @Author:14988
# @Site:
# @File:logger.py
# @Software:PyCharm
import logging
import time
import os
from lib.config import CONFIG


class Logger:
    __logger = None

    def __new__(cls, *args, **kwargs):
        if cls.__logger is None:
            logger = logging.getLogger()
            loggerLevel = getattr(logging, CONFIG.get("logger", "loggerLevel").upper(), None)
            logger.setLevel(loggerLevel if loggerLevel is not None else logging.DEBUG)
            sh = logging.StreamHandler()
            fmt = logging.Formatter(
                fmt="[%(asctime)s]-%(module)s-%(lineno)d-%(levelname)s: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            sh.setFormatter(fmt)
            shLevel = getattr(logging, CONFIG.get("logger", "shLevel").upper(), None)
            sh.setLevel(shLevel if shLevel is not None else logging.DEBUG)

            logdir = os.path.join(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                ), 'log'
            )
            if not os.path.exists(logdir):
                os.mkdir(logdir)
            logname = time.strftime("%Y-%m-%d.log")
            logpath = os.path.join(logdir, logname)
            fh = logging.FileHandler(
                filename=logpath,
                encoding="UTF-8"
            )
            fh.setFormatter(fmt)
            fhLevel = getattr(logging, CONFIG.get("logger", "fhLevel").upper(), None)
            fh.setLevel(fhLevel if fhLevel is not None else logging.DEBUG)

            logger.addHandler(sh)
            logger.addHandler(fh)
            cls.__logger = logger
        return cls.__logger


if __name__ == '__main__':
    logger2 = Logger()
    logger2.debug('debug')
    logger2.info('info')
    logger2.warning('warning')
    logger2.error('error')
