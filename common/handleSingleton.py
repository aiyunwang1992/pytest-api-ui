#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleSignleton.py
@IDE ：PyCharm
单例模式装饰器
"""
import wrapt

obj = {}


@wrapt.decorator
def singleton(wrapped, instance, args, kwargs):
    if not obj:
        obj['obj'] = wrapped(*args, **kwargs)
    return obj['obj']
