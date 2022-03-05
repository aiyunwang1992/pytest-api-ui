#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleCases.py
@IDE ：PyCharm
用例方法
"""
from common.handleLog import log
from projects.soulmiaApi.common.handleTestStep import HandleTestStep


def handle_case(data, token=None):
    log.info(f"用例{data['title']}测试的步骤为{data['teststeps']}")
    hts = HandleTestStep(data['title'])
    # 实际结果
    actually_result = hts.handle_teststep(data['apipath'], data['teststeps'])
    return actually_result
