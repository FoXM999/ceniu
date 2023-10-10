# Author:zqbin
# @Time:2023/9/27 14:12
# @Author:14988
# @Site:
# @File:demo04.py
# @Software:PyCharm
from lib.logger import Logger
from lib.config import CONFIG
import requests

class HTTPClient:
    def __init__(self):
        self.s = requests.session()

    def __del__(self):
        self.s.close()

    def update(self, headers):
        self.s.headers.update(headers)

    def request(self, path, **kwargs):
        url = CONFIG.get('server', 'baseUrl') + path
        r = self.s.request(url, **kwargs)
        return r

