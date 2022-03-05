#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleJsonPath.py
@IDE ：PyCharm
对jsonpath的封装
"""
import jsonpath
from common.handleLog import log


def handle_jsonpath(data, key):
    try:
        result = jsonpath.jsonpath(data, key)[0]
    except Exception as e:
        log.error(f'未提取到值,表达式为:{key},返回值为：{data}')
        log.error(f'报错为{e}')
        return False
    return result


if __name__ == '__main__':
    print(handle_jsonpath({'email': 1}, '$..email'))
