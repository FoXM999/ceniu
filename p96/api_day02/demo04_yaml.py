# Author:zqbin
# @Time:2023/9/27 16:20
# @Author:14988
# @Site:
# @File:demo04_yaml.py
# @Software:PyCharm
import yaml


with open('./test.yaml', 'r+', encoding='utf-8') as f:
    y = yaml.safe_load(f)
    print(y, type(y))
    print(y.get('user').get('name'))

    f.seek(0)

    y['user']['name'] = 'ls'
    yaml.safe_dump(y, f, allow_unicode=True)