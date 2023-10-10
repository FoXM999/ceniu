# Author:zqbin
# @Time:2023/9/26 10:11
# @Author:14988
# @Site:
# @File:01.py
# @Software:PyCharm
import json
import requests

# get方法
# r = requests.get('http://httpbin.org/get')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(json.loads(r.text))

# post方法
# r = requests.post('http://httpbin.org/post')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(json.loads(r.text))

# put     http://httpbin.org/put
# r = requests.put('http://httpbin.org/put')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(json.loads(r.text))

# patch   http://httpbin.org/patch
# r = requests.patch('http://httpbin.org/patch')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(json.loads(r.text))

# delete  http://httpbin.org/delete
# r = requests.delete('http://httpbin.org/delete')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(json.loads(r.text))

# request发送get请求
# r = requests.request(method='get', url='http://httpbin.org/get')
# print(r.status_code)
# print(r.headers)
# print(r.text)
# print(r.json())
#
# print(r.request.method)
# print(r.request.url)
# print(r.request.headers)
# print(r.request.body)

# request发送post请求
r = requests.request(method='post', url='http://httpbin.org/post')
print(r.status_code)
print(r.headers)
print(r.text)
print(r.json())

print(r.request.method)
print(r.request.url)
print(r.request.headers)
print(r.request.body)