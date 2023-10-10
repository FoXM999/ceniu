# Author:zqbin
# @Time:2023/10/10 16:01
# @Author:14988
# @Site:
# @File:conftest.py
# @Software:PyCharm
import pytest

ddtDataList = [
    {"name": "注册时两次密码不一致", "data": {"name": "test_register_ddt_801", "password1": "123456", "password2": "123457", "msg": "Password Is Not Same One"}},
    {"name": "注册的用户已经存在", "data": {"name": "admin", "password1": "123456", "password2": "123456", "msg": "User Is Exists"}}
]


@pytest.fixture(params=[item["data"] for item in ddtDataList], ids=[item["name"] for item in ddtDataList])
def fixture_for_register_ddt(request):
    data = request.param
    yield data


def pytest_collection_modifyitems(items):

    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # item._nodeid = item.nodeid.split('::')[0] +'::'+ item.nodeid.split('::')[1].encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.split('::')[0] + '::' + item.name