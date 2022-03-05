#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleLog.py
@IDE ：PyCharm
"""
import logging
from datetime import datetime
from common.handleSingleton import singleton
from conf.projectPath import *


@singleton
class Log(logging.Logger):
    def __init__(self):
        super().__init__('api_soulmia_app')  # 日志收集器的名字
        # self.setLevel('INFO')  # 日志收集器的级别

        # 3、设置日志输出格式 - Formatter类
        fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s [第%(lineno)d行] %(message)s"
        formatter = logging.Formatter(fmt)

        # 4、创建一个输出渠道 - 终端输出
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)  # 设置日志输出的格式为第3步设置的样子

        # 4、创建一个输出渠道 - 输出到文件
        now_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        log_name = "{}_{}.log".format('api_soulmia_app', now_time)
        log_path = os.path.join(logs_path, log_name)
        handle2 = logging.FileHandler(log_path, encoding="utf-8")
        handle2.setFormatter(formatter)

        # 5、把输出渠道，添加到日志收集器对象中。
        self.addHandler(handle1)
        self.addHandler(handle2)


log = Log()
if __name__ == '__main__':
    log1 = Log()
    log2 = Log()
    print(id(log1), id(log2))
