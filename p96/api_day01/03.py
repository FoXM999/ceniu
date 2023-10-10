# Author:zqbin
# @Time:2023/9/26 11:21
# @Author:14988
# @Site:
# @File:03.py
# @Software:PyCharm
import requests

baseUrl = "http://39.108.127.130:8008"

# 1. 注册
method = "post"
path = "/login/"
data = {
    "name": "zqb",
    "password": "123456"
}

r = requests.request(method=method, url=baseUrl+path, json=data)
print(r.text)
headers = {
    "token": r.json()["data"]["openid"],
    "operator": str(r.json()["data"]["user_id"])
}

# 2. 上传供应商文件
method = "post"
path = "/uploadfile/supplierfile/"
data = {
    "file": open("./file/supplier_cn.xlsx", "rb")
}
headers["language"] = "zh-hans"
r = requests.request(method=method, url=baseUrl+path, headers=headers, files=data)
print(r.text)