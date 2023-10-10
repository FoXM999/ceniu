# Author:zqbin
# @Time:2023/9/26 18:21
# @Author:14988
# @Site:
# @File:demo01_yaml.py
# @Software:PyCharm
import yaml

# 读取yaml文件
with open('../config/config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data, type(data))
    print(data.get('database').get('host'))

# 写入yaml文件
with open('./config.yaml', 'w', encoding='utf-8') as f:
    data = {
        'username': 'root',
        'password': '123456'
    }
    yaml.dump(data, f)
