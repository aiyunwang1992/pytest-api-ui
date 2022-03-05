#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleEnv.py
@IDE ：PyCharm
处理多环境兼容
"""
from enum import Enum
from conf.projectPath import *


class Environment(Enum):
    """设置环境"""
    TEST = 0
    BETA = 1


class EntryPoint:
    """设置环境变量"""
    __ENV_URL = {
        Environment.TEST: 'http://test',
        Environment.BETA: 'http://beta'
    }
    _ENV_CONF_PATH = {
        Environment.TEST: gloable_conf_path,
        Environment.BETA: beta_conf_path
    }

    @property
    def URL(self):
        return self.__ENV_URL[env]

    @property
    def CONF_PATH(self):
        return self._ENV_CONF_PATH[env]


class EnvValue:
    """设置切换环境的值"""
    env = 'TEST'

    def env_value(self):
        try:
            e_value = getattr(Environment, self.env)
            return e_value
        except Exception  as e:
            print('环境不存在')
            raise e


env = EnvValue().env_value()
if __name__ == '__main__':
    EnvValue.env = 'BETA'
    c = EntryPoint.URL
    print(c)
