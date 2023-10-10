# Author:zqbin
# @Time:2023/10/3 11:17
# @Author:14988
# @Site:
# @File:temp_client.py
# @Software:PyCharm
import yaml
import os


class TempClient:
    def save(self, key, value):
        path = os.path.join(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            ), 'data/temp.yaml'
        )
        with open(path, 'r', encoding='utf8') as f:
            temp = yaml.safe_load(f)
        with open(path, 'w', encoding='utf8') as f:
            temp[key] = value
            yaml.safe_dump(temp, f, allow_unicode=True)
