#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：main.py
@IDE ：PyCharm
"""
import pytest
import time
from common.handleRelateData import HandleRelateData
from common.handleWeixin import weixin
from conf.projectPath import *

now = time.strftime('%Y-%m-%d_%H-%M-%S')
html_report = '--html=' + '' + '/apireport' + now + '.html'
allure_path = reports_path + '/allure/' + now
allureFile_path = '--alluredir=' + allure_path
allure_report = reports_path + '/allure_report'
# pytest.main(['-m','flyback',htmlreport,testcases_path+'/test_register.py'])

pytest.main(['-v', '-s', '-m', 'flyback', '-n', '2', '--disable-warnings', html_report,
             allureFile_path, projects_path])
os.system("allure generate " + allure_path + " -o " + allure_report + ' --clean')
# 获取测试结果
test_result = getattr(HandleRelateData, 'test_results')
if test_result['failed'] != 0:
    file = 'requirements.txt'
    content = f"自动化测试结果：用例总数为{test_result['total']},通过用例数{test_result['pass']}，失败用例数{test_result['failed']},报错用例数{test_result['error']}"
    weixin(content)
