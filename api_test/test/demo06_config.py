# Author:zqbin
# @Time:2023/10/1 13:51
# @Author:14988
# @Site:
# @File:demo06_config.py
# @Software:PyCharm
import os.path
import time
import unittest
from configparser import RawConfigParser
import logging

import pymysql
import requests
import yaml
from testcase.test_test import TestTest
from lib.HTMLTestRunner import HTMLTestRunner

# config = RawConfigParser()
# config.read('../config/config.ini')
# print(config.get('server', 'baseUrl'))
# print(config['database']['port'])
#
# logger = logging.getLogger('test')
# logger.setLevel(logging.INFO)
# sh = logging.StreamHandler()
# fm = logging.Formatter(
#     fmt='%(asctime)s-%(module)s-%(lineno)d-%(levelname)s:%(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# sh.setFormatter(fm)
# sh.setLevel(logging.INFO)
# fh = logging.FileHandler(
#     filename='./log.log',
#     encoding='utf8'
# )
# fh.setLevel(logging.WARNING)
# fh.setFormatter(fm)
# logger.addHandler(sh)
# logger.addHandler(fh)
#
# logger.info('info')
# logger.warning('warning')
# logger.error('error')

CONFIG = RawConfigParser()
config_dir = os.path.join(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ), 'config'
)
if not os.path.exists(config_dir):
    os.mkdir(config_dir)
fillfilename = os.path.join(config_dir, 'config.ini')
print(fillfilename)
CONFIG.read(fillfilename)


class Logger:
    __logger = None

    def __new__(cls, *args, **kwargs):
        if cls.__logger is None:
            logger = logging.getLogger('APITest')
            loggerLevel = CONFIG.get('logger', 'loggerLevel')
            loggerLevel = getattr(logging, loggerLevel.upper()) if loggerLevel is not None else logging.INFO
            logger.setLevel(loggerLevel)
            sh = logging.StreamHandler()
            shLevel = getattr(logging, CONFIG.get('logger', 'shLevel').upper(), None)
            sh.setLevel(shLevel if shLevel is not None else logging.WARNING)
            fmtconfig = CONFIG.get('logger', 'format')
            fmtconfig = fmtconfig if fmtconfig is not None else '%(asctime)s-%(module)s-%(lineno)d-%(levelname)s:%(message)s'
            timeFormat = CONFIG.get('logger', 'timeFormat')
            timeFormat = timeFormat if timeFormat is not None else '%Y-%m-%d %H:%M:%S'
            fm = logging.Formatter(
                fmt=fmtconfig,
                datefmt=timeFormat
            )
            sh.setFormatter(fm)
            logger.addHandler(sh)
            filename = time.strftime('%Y-%m-%d.log')
            fh = logging.FileHandler(
                filename=filename,
                encoding='utf8'
            )
            fhLevel = getattr(logging, CONFIG.get('logger', 'fhLevel').upper(), None)
            fh.setLevel(fhLevel if fhLevel is not None else logging.INFO)
            fh.setFormatter(fm)
            logger.addHandler(fh)
            cls.__logger = logger
            return cls.__logger


if __name__ == '__main__':
    # print(CONFIG.get('server', 'baseUrl'))
    # logger2 = Logger()
    # logger2.debug('debug')
    # logger2.info('info')
    # logger2.warning('warning')
    # logger2.error('error')

    # data = '''
    # info:
    #  name: zs
    #  age: 18
    # '''
    # d = yaml.safe_load(data)
    # print(d)
    # d['address'] = '广西'
    # res = yaml.safe_dump(d, allow_unicode=True)
    # print(res)
    # with open('./data.yaml', 'w', encoding='utf8') as f:
    #     yaml.safe_dump(d, f, allow_unicode=True)
    # with open('./data.yaml', 'r', encoding='utf8') as f:
    #     print(yaml.safe_load(f))

    # res = requests.request(url="http://httpbin.org/get", method='GET')
    # data = {
    #     'username': 'test',
    #     'password': '123456'
    # }
    # res = requests.request(url='http://httpbin.org/post', method='POST', json=data)
    # print(res.status_code)
    # print(res.headers)
    # print(res.text)
    # print(res.json())
    # print(res.request.url)
    # print(res.request.method)
    # print(res.request.headers)
    # print(res.request.body)

    # suite = unittest.TestSuite()
    # suite.addTest(TestTest('test_demo1'))
    # suite.addTest(TestTest('test_demo2'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # path = os.path.join(os.path.dirname(__file__), 'testcase')
    # print(path)
    # suite = unittest.defaultTestLoader.discover(path)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # path = os.path.join(os.path.dirname(__file__), 'testcase')
    # suite = unittest.defaultTestLoader.discover(path)
    # filename = time.strftime('report_%Y_%m_%d_%H_%M_%S.html')
    # with open(filename, 'wb') as f:
    #     runner = HTMLTestRunner(
    #         stream=f,
    #         verbosity=2,
    #         title=filename.split('.')[0],
    #         description='描述信息'
    #     )
    #     runner.run(suite)

    # database = {
    #     "host": 'localhost',
    #     "port": 33060,
    #     "db": 'student',
    #     "user": 'root',
    #     "password": '123456',
    # }
    #
    # conn = pymysql.connect(**database)
    # cursor = conn.cursor()
    # sql = 'update students set name="刘备" where studentNo="017"'
    # cursor.execute(sql)
    # conn.commit()
    # cursor.close()
    # conn.close()

    database = {
        "host": 'localhost',
        "port": 33060,
        "db": 'student',
        "user": 'root',
        "password": '123456',
    }

    with pymysql.connect(**database) as conn:
        with conn.cursor() as cur:
            sql = 'select * from students limit 10'
            ret = cur.execute(sql)
            print(ret)
            al = cur.fetchall()
            for item in al:
                print(item)
