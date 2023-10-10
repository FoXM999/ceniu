# Author:zqbin
# @Time:2023/10/10 16:02
# @Author:14988
# @Site:
# @File:extend_ec.py
# @Software:PyCharm
def text_is_not_null(locator):
    def method(d):
        return d.find_element(*locator).text

    return method
