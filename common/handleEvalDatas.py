#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleEvalDatas.py
@IDE ：PyCharm
执行用例中写的方法
"""
from common.handleRandomData import HandleRandomData


class HandleEvalDatas:
    def __init__(self, datas):
        self.datas = datas

    def eval_datas(self):
        for key, value in self.datas.items():
            if 'func' in value:
                self.datas[key] = eval(value.split(':')[1])
        return self.datas


if __name__ == '__main__':
    p = {"email": "func:HandleRandomData().rand_email()", "password": "123456"}
    h = HandleEvalDatas(p)
    print(h.eval_datas())
