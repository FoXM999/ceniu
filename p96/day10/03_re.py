# Author:zqbin
# @Time:2023/9/20 15:34
# @Author:14988
# @Site:
# @File:03_re.py
# @Software:PyCharm
import re

m = re.search(r'(\d+)\.(\d+)', 'a24.123 12.23')
print('m=', m)
print('group=', m.group())
print('groups=', m.groups())

# 从开头开始匹配到才算，相当于开头多了 ^ 符号
m = re.match(r'(\d+)\.(\d+)', 'a24.123 12.23')
print('m=', m)  # m = None
# print('group=',m.group())
# print('groups=',m.groups())

# 整个字符串匹配到才算
m = re.fullmatch(r'(\d+)\.(\d+)', '24.123 12.23')
print('m=', m)
# print('group=',m.group())
# print('groups=',m.groups())

m = re.split(r'\s+', 'my  name is Tom')
print('m=', m)
m = re.split(r'[a-z]+', '0a1d2G3', flags=re.IGNORECASE)
print('m=', m)

m = re.findall(r'\b\w+', 'My name is Tome My')
print('m=', m)

m = re.sub(r'<a>.+</a>',
           'https://www.baidu.com',
           '<p>hello</p><a>https://www.baidu.com</a>')
print('m=', m)

print('=' * 100)


def func(obj):
    print('obj=', obj)
    if obj.group(0) == '<p>':
        return '<span>'
    elif obj.group(0) == '</p>':
        return '</span>'
    else:
        return obj.group(0)


m = re.sub(r'<.*?>',
           func,
           '<p>hello</p><a>https://www.baidu.com</a>')
print('m=', m)

m = re.subn(r'<a>.+</a>',
            'https://www.baidu.com',
            '<p>hello</p><a>https://www.baidu.com</a>')
print('m=', m)

m = re.search(r'<a>.+</a>',
              '<p>hello</p><a>https://www.baidu.com</a>')
print('start=', m.start())
print('end=', m.end())
print('span=', m.span())

print('=' * 100)


m = re.findall(r'<.*>.*?</.*>',
           '<p>hello</p><a>https://www.baidu.com</a>')
print('m=', m)