# Author:zqbin
# @Time:2023/9/16 15:30
# @Author:14988
# @Site:
# @File:06_json.py
# @Software:PyCharm

import json
dict1 = {
    "name": "qinr",
    "age": 18,
    "height": 168.55,
    "test": True,
    "other": [False, None]
}
s1 = json.dumps(dict1)
print(s1, type(s1))

temp = json.loads((s1))
print(temp, type(temp))

# with open('./file/testjson.json','w') as f:
#     json.dump(dict1,f,ensure_ascii=False,indent=4)

with open('./file/testjson.json','r') as f:
    print(json.load(f))