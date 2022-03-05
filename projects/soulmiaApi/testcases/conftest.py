# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：conftest.py
@IDE ：PyCharm
"""
"""前置后置条件"""
import pytest
import time
from _pytest import terminal
from projects.soulmiaApi.common.handleToken import get_token
from common.handleYaml import read_test_yaml
from common.handleRelateData import HandleRelateData

from conf.projectPath import *
from common.handleLog import log


# # 解决输出的用例标题中文乱码
# def pytest_collection_modifyitems(items) -> None:
#     for item in items:
#         item.name = item.name.encode("GBK").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("GBK").decode("unicode_escape")
# 统计测试结果
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    test_results = {}

    test_results["total"] = terminalreporter._numcollected
    test_results["pass"] = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    test_results["failed"] = len(
        [i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    test_results["error"] = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    test_results["skipped"] = len(
        [i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    setattr(HandleRelateData, 'test_results', test_results)
    # SaveValue.test_results["成功率"] = '%.2f' % (
    #             len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100) + '%'
    #
    # # terminalreporter._sessionstarttime 会话开始时间
    # duration = '%.2f' % (time.time() - terminalreporter._sessionstarttime)
    # SaveValue.test_results["total times"] = f'{duration}s'


"""--------------------------------前后置数据处理--------------------------------------------------------"""


# 前置登录
@pytest.fixture(scope="session")
def pre_login():
    token = get_token()
    if not token:
        raise ValueError
    else:
        yield token


# 数据初始化：加购前后清空购物车
@pytest.fixture(scope='function')
def clear_cart(pre_login):
    token = pre_login
    pass


# 前置处理步骤执行


# 注册
@pytest.fixture(params=read_test_yaml('api_register_login_process.yaml'))
def register_datas(request):
    data = request.param
    yield data


# 登录
@pytest.fixture(params=read_test_yaml('api_login.yaml'))
def login_param(request):
    data = request.param
    yield data


# 加购
@pytest.fixture(params=read_test_yaml('api_cart_add_to_cart.yaml'))
def add_to_cart_param(request, pre_login, clear_cart):
    data = request.param
    token = pre_login
    data['token'] = token
    yield data
