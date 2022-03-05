#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：project_path.py
@IDE ：PyCharm
项目路径维护
"""
import os

# 项目根路径
basepath = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# baseapi
baseapi_path = os.path.join(basepath, 'baseapi')
# conf
conf_path = os.path.join(basepath, 'conf')
# gloable_conf
gloable_conf_path = os.path.join(conf_path, 'gloable_conf')
# beta_conf
beta_conf_path = os.path.join(conf_path, 'beta_conf')
# template
template_path = os.path.join(basepath, 'template')
# reports
reports_path = os.path.join(basepath, 'reports')
# history_datas
history_path = os.path.join(reports_path, 'history')
# 测试报告
# reports_path = os.path.join(testreports_path, 'reports')
# 日志
logs_path = os.path.join(basepath, 'logs')
# 数据库信息
db_path = os.path.join(conf_path, 'db.conf')
# 项目地址
projects_path = os.path.join(basepath, 'projects')
