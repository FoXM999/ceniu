# Author:zqbin
# @Time:2023/10/10 15:22
# @Author:14988
# @Site:
# @File:conftest.py
# @Software:PyCharm
import pytest
from lib.http_client import HTTPClient
from lib.mysql_client import MySQLClient


@pytest.fixture
def fixture_for_login_01():
    mysqlClient = MySQLClient()
    httpClient = HTTPClient()
    # setup ===
    print("\nsetup")
    # 调用接口实现注册
    name = "test_10_10_001"
    password = "123456"
    path = "/register/"
    method = "post"
    data = {
        "name": name,
        "password1": password,
        "password2": password
    }
    r = httpClient.request(path=path, method=method, json=data)
    print(r.text)

    yield name, password

    # teardown
    print("\nteardown")
    sqlList = [
        f"DELETE FROM auth_user WHERE username = '{name}';",
        f"DELETE FROM user_profile WHERE name = '{name}';"
    ]
    mysqlClient.execute(sqlList)