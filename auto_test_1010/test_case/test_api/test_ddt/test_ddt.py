# Author:zqbin
# @Time:2023/10/10 16:38
# @Author:14988
# @Site:
# @File:test_ddt.py
# @Software:PyCharm
import allure
import yaml
import os
import pytest
import json
import jsonpath
from lib.logger import Logger
from lib.http_client import HTTPClient
from lib.mysql_client import MySQLClient

dataFilePath = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        )
    ), "data", "data.yaml"
)


def read_yaml_data():
    with open(dataFilePath, encoding="utf8") as f:
        result = yaml.load(f, yaml.SafeLoader)
        temp = [{"name": key, "data": value} for key, value in result.items()]
        return temp


@allure.epic("接口测试用例")
# @allure.feature([item["name"] for item in read_yaml_data()])
# @allure.story()
# @allure.title()
class TestApiDDT(object):
    logger = Logger()
    httpClient = HTTPClient()
    mysqlClient = MySQLClient()
    argsDict = {}

    @pytest.mark.parametrize("kwargs", [item["data"] for item in read_yaml_data()],
                             ids=[item["name"] for item in read_yaml_data()])
    def test_method(self, kwargs):
        print(kwargs)
        self.logger.info("\n" + f"  {kwargs['name']}  ".center(100, "="))

        # 1. 处理setup
        with allure.step("setup"):
            if kwargs.get("setup") is not None:
                self.logger.info("setUp")
                for item in kwargs.get("setup"):
                    if item["type"] == "api":
                        self.logger.info(f"通过调用接口: {item['name']}进行测试环境初始化")
                        self.httpClient.request(**item["data"])

        self.teardown = kwargs.get("teardown")
        try:
            # 2. 处理接口调用
            apis = kwargs.get("apis")
            if apis is not None:
                for i, api in enumerate(apis):
                    with allure.step(f"step{i + 1:02d}: 调用{api['name']}"):
                        # 将字典转换成json字符串
                        api = json.dumps(api)
                        # 使用argsDict来格式化字符串
                        self.logger.warning(f'api={api}')
                        api = api % self.argsDict
                        self.logger.warning(f'api2={api}')
                        # 将json字符串转换回字典
                        api = json.loads(api)
                        self.logger.info(f"调用接口: {api['name']}")
                        r = self.httpClient.request(**api["data"])
                        # 处理接口的断言
                        assertData = api.get("assert")
                        if assertData is not None:
                            for item in assertData:
                                if item["type"] == "status_code":
                                    expectValue = item["expect"]
                                    currentValue = r.status_code
                                    self.logger.info(
                                        f"对HTTP状态码进行断言, 预期结果: {expectValue}, 实际结果: {currentValue}")
                                    assert expectValue == currentValue, f"HTTP状态码断言失败, 预期结果: {expectValue}, 实际结果: {currentValue}"
                                elif item["type"] == "json_filed":
                                    expectValue = item["expect"]
                                    filed = item["filed"]
                                    currentValue = jsonpath.jsonpath(r.json(), f"$..{filed}")[item["index"]]
                                    self.logger.info(
                                        f"对JSON{filed}进行断言, 预期结果: {expectValue}, 实际结果: {currentValue}")
                                    assert expectValue == currentValue, f"JSON{filed}断言失败, 预期结果: {expectValue}, 实际结果: {currentValue}"
                                elif item["type"] == "db":
                                    expectValue = item["expect"]
                                    sql = item["sql"]
                                    currentValue = self.mysqlClient.select(sql)
                                    self.logger.info("对数据库进行断言")
                                    assert expectValue == currentValue, f"数据库断言失败，预期结果: {expectValue}, 实际结果: {currentValue}"
                        # 更新会话的请求头
                        if api.get("update_headers") is not None:
                            for item in api.get("update_headers"):
                                key = item["key"]
                                filed = item["filed"]
                                value = str(jsonpath.jsonpath(r.json(), f"$..{filed}")[item["index"]])
                                headers = {key: value}
                                self.logger.info(f"更新会话请求头: {headers}")
                                self.httpClient.update(headers)
                        # 保存接口关联需要用到的字段到字典当中
                        if api.get("save_args") is not None:
                            for item in api.get("save_args"):
                                key = item["key"]
                                filed = item["filed"]
                                value = jsonpath.jsonpath(r.json(), f"$..{filed}")[item["index"]]
                                self.argsDict[key] = value
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            raise Exception(e)
        finally:
            with allure.step("teardown"):
                if self.teardown is not None:
                    self.logger.info("tearDown")
                    for item in self.teardown:
                        if item["type"] == "db":
                            self.logger.info("通过执行SQL语句清理测试环境")
                            sqlList = item["sqlList"]
                            self.mysqlClient.execute(sqlList)
                self.logger.info("\n" + "=" * 100)
