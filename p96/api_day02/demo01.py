# Author:zqbin
# @Time:2023/9/27 10:30
# @Author:14988
# @Site:
# @File:demo01.py
# @Software:PyCharm
from configparser import RawConfigParser
config = RawConfigParser()
config.read('config.ini')
print(config.sections())
print(config, type(config))

print(config['server']['baseUrl'])
print(config['database']['port'], type(config['database']['port']))

print(config.get('database', 'port'), type(config.get('database', 'port')))
print(config.getint('database', 'port'), type(config.getint('database', 'port')))
