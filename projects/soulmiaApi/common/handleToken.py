#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： wangaiyun
@File ：handleToken.py
@IDE ：PyCharm
"""
from projects.soulmiaApi.common.generatorAccountDatas import AccountGenerationData


def get_token():
    result = AccountGenerationData().login()
    token = result.get('result').get('token')
    return token


if __name__ == '__main__':
    r = get_token()
    print(r)