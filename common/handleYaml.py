#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleYaml.py
@IDE ：PyCharm
处理yaml数据
"""
from ruamel import yaml
from common.handleEnv import EntryPoint
from common.handleLog import log
from conf.projectPath import *


def read_yaml(file_path):
    """读取yaml的数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.load(file.read(), Loader=yaml.Loader)
            return data
    except Exception as e:
        log.error(f'读取报错,报错为{e}')
        raise e


def write_yaml(file_path, content):
    """将数据写入到yaml中"""
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            yaml.dump(content, file, allow_unicode=True, Dumper=yaml.RoundTripDumper)
    except Exception as e:
        log.error(f'读取报错,报错为{e}')
        raise e


def read_test_yaml(filename):
    """读取测试数据"""
    cases_path = os.path.join(testdatas_path, filename)
    cases_datas = read_yaml(cases_path)
    return cases_datas


def read_env_conf_yaml(filename):
    """根据环境变量读取不同的配置"""
    conf_path = EntryPoint().CONF_PATH
    conf_file_path = os.path.join(conf_path, filename)
    conf_datas = read_yaml(conf_file_path)
    return conf_datas
