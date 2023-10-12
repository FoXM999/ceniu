# Author:zqbin
# @Time:2023/10/10 16:38
# @Author:14988
# @Site:
# @File:test_ddt.py
# @Software:PyCharm
import yaml
import os
import pytest
from jsonpath import jsonpath
from lib.http_client import HTTPClient
from lib.logger import Logger
from lib.mysql_client import MySQLClient
import json

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


class TestApiDDT(object):
    http_client = HTTPClient()
    logger = Logger()
    mysql_client = MySQLClient()
    argsDict = {}

    def set_up(self) -> None:
        self.logger.info("setUp开始".center(50, '-'))

        if self.data.get('setup') is not None:
            setup = self.data.get('setup')
            for item in setup:
                typ = item.get('type')
                if typ == 'api':
                    dt = item.get('data')
                    self.http_client.request(**dt)

        self.logger.info("setUp结束".center(50, '-'))

    def tearDown(self) -> None:
        self.logger.info("tearDown开始".center(50, '-'))

        if self.data.get('teardown') is not None:
            teardown = self.data.get('teardown')
            for t in teardown:
                typ = t.get('type')
                if typ == 'db':
                    sqlList = t.get('sqlList')
                    self.mysql_client.execute(sqlList)

        self.logger.info("tearDown结束".center(50, '-'))
        self.logger.info('=' * 55)

    @pytest.mark.parametrize("kwargs", [item["data"] for item in read_yaml_data()],
                             ids=[item["name"] for item in read_yaml_data()])
    def test_method(self, kwargs):
        print(kwargs)
        self.logger.info(kwargs.get('name').center(50, '='))

        self.data = kwargs
        self.set_up()

        try:
            if kwargs.get('apis') is not None:
                apis = kwargs.get('apis')
                for item in apis:
                    # 将字典转换成json字符串
                    item = json.dumps(item)
                    # 使用argsDict来格式化字符串
                    self.logger.warning(f'item={item}')
                    item = item % self.argsDict
                    # 将json字符串转换回字典
                    item = json.loads(item)

                    data = item.get('data')
                    res = self.http_client.request(**data)

                    if item.get('assert') is not None:
                        assertDataList = item.get('assert')
                        for assertData in assertDataList:
                            typ = assertData.get('type')
                            self.logger.info(f'typ={typ}')
                            expect = assertData.get('expect')
                            currentValue = ''

                            if typ == 'status_code':
                                currentValue = res.status_code
                                self.logger.info(f'针对status_code的断言：实际结果={currentValue},预期结果={expect}')
                            elif typ == 'json_filed':
                                filed = assertData.get('filed')
                                index = assertData.get('index')
                                currentValue = jsonpath(res.json(), f'$..{filed}')[index]
                                self.logger.info(f'针对{filed}的断言：实际结果={currentValue},预期结果={expect}')
                            elif typ == 'db':
                                sql = assertData.get('sql')
                                currentValue = self.mysql_client.select(sql)
                                self.logger.info(f'针对{sql}的断言：实际结果={currentValue},预期结果={expect}')

                            assert expect, currentValue

                    if item.get('update_headers') is not None:
                        update_headers = item.get('update_headers')
                        for headerItem in update_headers:
                            key = headerItem.get('key')
                            filed = headerItem.get('filed')
                            index = headerItem.get('index')
                            value = str(jsonpath(res.json(), f'$..{filed}')[index])
                            headers = {key: value}
                            self.http_client.update(headers)
                            self.logger.info(f'更新请求头:{headers}')

                    # 保存接口关联需要用到的字段到字典当中
                    if item.get("save_args") is not None:
                        for i in item.get("save_args"):
                            key = i["key"]
                            filed = i["filed"]
                            value = jsonpath(res.json(), f"$..{filed}")[i["index"]]
                            self.argsDict[key] = value
        except AssertionError as e:
            raise AssertionError(e)
        except Exception as e:
            raise Exception(e)
        finally:
            self.tearDown()