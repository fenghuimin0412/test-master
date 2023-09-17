import os
from time import sleep

import allure
import pytest
from secsmart_autotest.lib.util.yaml_util import YamlUtil
from interface.dba.dba_getid_interface import DbaGetIdInterface
from interface.dba.set_modify_status import SetModifyStatus
from util.get_path import DATA_DIR


@allure.epic("数据库防火墙")
@allure.feature("数据资源管理")
class TestDbaSetStatus1(object):
    """
    数据资源模块，关闭资源状态开关
    """
    testdata_file = os.path.join(DATA_DIR, "../testdata/test_01_1006_dba_set_status.yaml")
    test_data = YamlUtil(testdata_file).read_yaml()["case_10000"]

    @pytest.mark.smoke_dba
    @pytest.mark.parametrize("data", test_data)
    @allure.title("数据库资源状态“关闭”功能正常")
    # @allure.story("数据资源")
    def test_dba_set_stop(self, data):
        """
        数据资源状态打开测试
        :return:
        """
        with allure.step("#1.关闭数据资源状态"):
            dbaid = DbaGetIdInterface().dba_dbname_getid(data)
            res = SetModifyStatus().request(dbaid, 0)
        with allure.step("#2.获取接口的报文，查看是否成功"):
            assert res["message"] == "接口调用成功"
            SetModifyStatus().request(dbaid, 1)
        sleep(5)
