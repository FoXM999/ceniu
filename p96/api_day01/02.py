# Author:zqbin
# @Time:2023/9/26 10:42
# @Author:14988
# @Site:
# @File:02.py
# @Software:PyCharm
import json
import requests

# r = requests.request(method='get', url='http://httpbin.org/get?name=zqb&password=123456')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.json())

data = {
    "name":"zqb",
    "password":"123456"
}
# r = requests.request(method='get', url='http://httpbin.org/get', params=data)
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.json())

# r = requests.request(method='post', url='http://httpbin.org/post', data=data)
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.json())

# r = requests.request(method="post", url="http://httpbin.org/post", json=data)
# print(r.json())
# print(r.request.body)

# r = requests.request(method="post", url="http://httpbin.org/post", json=data)
# print(r.json())
# print(r.request.body)

# r = requests.request(method="post", url="http://httpbin.org/post", data=json.dumps(data))
# print(r.json())
# print(r.request.body)

headers = {
    "Content-Type": "application/json"
}
r = requests.request(method="post", url="http://httpbin.org/post", data=json.dumps(data), headers=headers)
print(r.json())
print(r.request.body)