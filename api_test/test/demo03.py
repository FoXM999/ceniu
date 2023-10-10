# Author:zqbin
# @Time:2023/9/26 19:49
# @Author:14988
# @Site:
# @File:demo03.py
# @Software:PyCharm
import requests

baseUrl = "http://39.108.127.130:8008"
path = "/register/"
method = "post"
data = {
    "name": "test926_901",
    "password1": "123456",
    "password2": "123456"
}
r = requests.request(method=method, url=baseUrl + path, json=data)

