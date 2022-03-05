#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：test_api_register.py
@IDE ：PyCharm
"""
import pytest
import allure
from common.handleLog import log
from common.handleCases import handle_case
from common.handleYaml import read_yaml
from conf.projectPath import *
test_datas=read_yaml(os.path.join(projects_path,'soulmiaApi/testcasedatas/api_cart_add_to_cart.yaml'))
print(test_datas)
# 读取测试数据
@allure.feature('soulmiaApi测试报告')
@pytest.mark.flyback
@pytest.mark.usefixture('setUp_tearDown')
class TestCase:
    @allure.story('注册相关场景')
    @pytest.mark.parametrize('data',test_datas)
    def test_api_register(self,data,setUp_tearDown):
        with allure.step(data['title']):
            data['token']=setUp_tearDown
            actually_result =handle_case(data)
            try:
                assert actually_result==True
            except Exception as e:
                log.debug(f"用例{data['title']}未通过: 报错为{e}")
                raise e