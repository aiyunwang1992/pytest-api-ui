#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleAsserts.py
@IDE ：PyCharm
自定义断言处理公共方法
"""
from common.handleLog import log
from common.handleJsonPath import handle_jsonpath


class HandleAssert:
    def __init__(self, title):
        self.title = title
        self.validate_list = ['msg', 'validate_func']

    # 断言方法执行
    def assert_exec(self, api_url, res, validate_content):
        assert_result = {}
        for key, value in validate_content.items():
            if key == 'msg':
                assert_result[key] = self.handle_assert(api_url, res, validate_content)
            # 执行yaml中的断言方法
            elif key == 'validate_func':
                for k, v in value.items():
                    try:
                        assert_result[k] = eval(v)
                    except Exception as e:
                        log.debug(f'用例{self.title}的{api_url}接口断言方法{v}失败,结果为:{e}')
                        return False
        if False in assert_result.values():
            return False
        return True

    # 比较方式
    def assert_method(self, actual_value, value, type=None):
        if type == 'bool':
            try:
                assert bool(actual_value) == True
                return True
            except  AssertionError:
                return False
        else:
            try:
                assert value == actual_value
                return True
            except  AssertionError:
                return False

    # msg的断言
    def handle_assert(self, api_url, res, validate_content):
        assert_result_dict = {}
        for key, value in validate_content['msg'].items():
            jsonpath_result = handle_jsonpath(res, key)
            if not bool(jsonpath_result):
                assert_result_dict[key] = False
                break
            actual_value = handle_jsonpath(res, key)
            if value == 'True':
                assert_result_dict[key] = self.assert_method(actual_value, value, type='bool')
            else:
                assert_result_dict[key] = self.assert_method(actual_value, value)
        # 返回断言结果
        if False in assert_result_dict.values():
            log.debug(f'用例{self.title}的{api_url}接口断言失败,结果为:{assert_result_dict}')
            return False
        return True


if __name__ == '__main__':
    print(2)
    e = {'msg': {'status': 'success', 'statusCode': 200, 'result': {'total_number': '1'}, 'message': ''}}
    r = {'status': 'success', 'statusCode': 200, 'result': {'total_number': '1'}, 'message': ''}
    h = HandleAssert('这个用例', r, e)
    print(h.handle_assert('bbcd'))
