#!/usr/bin/python
# -*- coding: utf-8 -*-
# 接口测试用例模板
import pytest
import allure
from common.handleLog import log
from common.handleCases import handle_case
from common.handleYaml import read_yaml
from conf.projectPath import *
test_datas=read_yaml(os.path.join(projects_path,r"soulmiaApi/testcasedatas/api_register_process.yaml"))
@allure.feature("soulmial报告")
@pytest.mark.flyback
@pytest.mark.usefixture('setUp_tearDown')
class TestCase:
    def test_api_register_process(self,data,setUp_tearDown):
        with allure.step(data['title']):
            data['token'] = setUp_tearDown
            actually_result = handle_case(data)
            try:
                assert actually_result == True
            except Exception as e:
                log.debug(f"用例{data['title']}未通过: 报错为{e}")
                raise e