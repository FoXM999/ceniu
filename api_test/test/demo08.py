# Author:zqbin
# @Time:2023/10/3 9:58
# @Author:14988
# @Site:
# @File:demo08.py
# @Software:PyCharm
import os
import yaml  # 需要pip install pyyaml


def env_var_constructor(loader, node):
    value = loader.construct_scalar(node)  # PyYAML loader的固定方法，用于根据当前节点构造一个变量值
    var_name = value.strip('${} ')  # 去除变量值（例如${USER}）前后的特殊字符及空格
    return os.getenv(var_name, value)  # 尝试在环境变量中获取变量名（如USER）对应的值，获取不到使用默认值value（即原来的${USER}）


yaml.SafeLoader.add_constructor('!env', env_var_constructor)  # 为SafeLoader添加新的tag和构造器

path = os.path.join(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    ), 'data/data2.yaml'
)

with open(path, 'r', encoding='utf8') as f:
    data2 = yaml.safe_load(f)
    print(data2)  # 打开文件并使用SafeLoader加载文件内容
with open(path, 'w', encoding='utf8') as f:
    data2['user'] = 'zs'
    yaml.safe_dump(data2, f, allow_unicode=True)
with open(path, 'r', encoding='utf8') as f:
    data2 = yaml.safe_load(f)
    print(data2)  # 打开文件并使用SafeLoader加载文件内容
