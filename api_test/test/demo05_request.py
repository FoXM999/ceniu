# Author:zqbin
# @Time:2023/9/29 12:03
# @Author:14988
# @Site:
# @File:demo05_request.py
# @Software:PyCharm
import requests
from lib.config import CONFIG

class RequestClient:
    def __init__(self):
        self.s = requests.session()

    def request(self, path, **kwargs):
        baseUrl = CONFIG.get('server', 'baseUrl')
        res = self.s.request(baseUrl + path, **kwargs)
        return res

    def updateSession(self, headers):
        self.s.headers.update(headers)

    def __del__(self):
        self.s.close()
