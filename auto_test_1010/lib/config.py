# Author:zqbin
# @Time:2023/9/27 10:53
# @Author:14988
# @Site:
# @File:config.py
# @Software:PyCharm
"""
读取框架的配置文件到CONFIG全局变量当中
其它地方要用到配置文件只需要导入该全局变量即可
"""
import os
from configparser import RawConfigParser

CONFIG = RawConfigParser()

configPath = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    ), "config", "config.ini"
)

CONFIG.read(configPath)