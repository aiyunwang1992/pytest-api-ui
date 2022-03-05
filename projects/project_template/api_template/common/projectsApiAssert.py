#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleAsserts.py
@IDE ：PyCharm
接口部分自定义断言处理
"""
from common.handleJsonPath import handle_jsonpath
from common.handleRelateData import HandleRelateData
from common.handleAssert import HandleAssert


class ProjectsApiAssert(HandleAssert):

    # 加购的断言
    def add_to_cart_assert(self, res):
        old_goods_number = getattr(HandleRelateData, 'old_goods_number')
        now_goods_number = handle_jsonpath(res, '$..goods_number')
        goods_number = getattr(HandleRelateData, 'goods_number')
        actual_goods_number = now_goods_number - old_goods_number
        return self.assert_method(goods_number, actual_goods_number)

    # 接口断言直接调用的方法
    def soulmia_api_assert(self, api_url, res, validate_content):
        assert_result = self.assert_exec(api_url, res, validate_content)
        return assert_result


if __name__ == '__main__':
    e = {'msg': {'status': 'success', 'statusCode': 100, 'result': {'total_number': '1'}, 'message': ''}}
    r = {'status': 'success', 'statusCode': 200, 'result': {'total_number': '1'}, 'message': ''}
    h = HandleAssert(e, r, 'abc')
    print(h.handle_assert())
