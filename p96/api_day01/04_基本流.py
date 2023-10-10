# Author:zqbin
# @Time:2023/9/26 11:56
# @Author:14988
# @Site:
# @File:04_基本流.py
# @Software:PyCharm
import requests

baseUrl = "http://39.108.127.130:8008"
s = requests.session()

# 1. 登录
method = "post"
path = "/login/"
data = {
    "name": "zqb",
    "password": "123456"
}
r = s.request(method="method",
              url=baseUrl + path,
              json=data)
print(r.text)

# 更新会话的请求头
headers = {
    "token": r.json()["data"]["openid"],
    "operator": str(r.json()["data"]["user_id"])
}
s.headers.update(headers)

# 2. 创建到货通知书
method = "post"
path = "/asn/list/"
data = {
    "creater": "zqb"
}
r = s.request(method=method,
              url=baseUrl + path,
              json=data)
print(r.text)
asn_code = r.json()["asn_code"]
asn_id = r.json()["id"]

# 3. 修改到货通知书
method = "post"
path = "/asn/detail/"
data = {
    "asn_code": asn_code,
    "supplier": "华为",
    "goods_code": ["A000041"],
    "goods_qty": [10],
    "creater": "zqb"
}
r = s.request(method=method,
              url=baseUrl + path,
              json=data)
print(r.text)

# 4. 确认到货
method = "post"
path = f"/asn/preload/{asn_id}/"
data = {}
r = s.request(method=method,
              url=baseUrl + path,
              json=data)
print(r.text)

# 5. 确认卸货
method = "post"
path = f"/asn/presort/{asn_id}/"
data = {}
r = s.request(method=method,
              url=baseUrl + path,
              json=data)
print(r.text)

# 6. 查询到货通知书详情
method = "get"
path = "/asn/detail/"
data = {
    "asn_code": asn_code
}
r = s.request(method=method,
              url=baseUrl + path,
              params=data)
print(r.text)

goodsInfo = r.json()["results"]

# 7. 分拣
goodsInfo[0]["goods_actual_qty"] = "10"
method = "post"
path = f"/asn/sorted/{asn_id}/"
data = {
    "asn_code": asn_code,
    "supplier": "华为",
    "goodsData": goodsInfo,
    "creater": "zqb"
}
r = s.request(method=method,
              url=baseUrl + path,
              json=data)
print(r.text)

# 7. 上架
goodsId = goodsInfo[0]["id"]
goodsInfo[0]["bin_name"] = "A010101"
goodsInfo[0]["qty"] = 10
method = "post"
path = f"/asn/movetobin/{goodsId}/"
r = s.request(method=method,
              url=baseUrl + path,
              json=goodsInfo[0])
print(r.text)

s.close()  # 关闭session会话对象
