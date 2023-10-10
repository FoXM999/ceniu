# Author:zqbin
# @Time:2023/9/28 10:18
# @Author:14988
# @Site:
# @File:http_client.py
# @Software:PyCharm
"""
对requests模块的二次封装
使用session机制，
提供2个接口： request()   update()
"""
import requests
from lib.config import CONFIG
from lib.logger import Logger


class HTTPClient(object):
    logger = Logger()

    def __init__(self):
        self.s = requests.session()

    def __del__(self):
        self.s.close()

    def update(self, headers):
        self.s.headers.update(headers)

    def request(self, path, **kwargs):
        baseUrl = CONFIG["server"]["baseUrl"]
        url = baseUrl + path
        r = self.s.request(url=url, **kwargs)
        self.logger.debug("------ 发送HTTP请求")
        self.logger.debug(f"url: {r.request.url}")
        self.logger.debug(f"method: {r.request.method}")
        self.logger.debug(f"request_headers: {r.request.headers}")
        self.logger.debug(f"request_body: {r.request.body}")
        self.logger.debug(f"status_code: {r.status_code}")
        self.logger.debug(f"response_headers: {r.headers}")
        self.logger.debug(f"response_body: {r.text}")
        self.logger.debug("------------------")
        return r
