#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleWeixin.py
@IDE ：PyCharm
企业微信机器人消息发送
"""
import requests
from common.handleYaml import read_yaml
from conf.projectPath import *

url = read_yaml(os.path.join(conf_path, 'config.yaml'))['TestweixinReportUrl']


def weixin(content):
    url = read_yaml(os.path.join(conf_path, 'config.yaml'))['TestweixinReportUrl']
    send_msg = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }
    r = requests.post(url=url, json=send_msg)
    return r.text


if __name__ == '__main__':
    url = "url"
