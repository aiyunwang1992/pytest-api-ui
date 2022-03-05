#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleDb.py
@IDE ：PyCharm
数据库操作
"""
import pymysql
import traceback
import contextlib
from common.handleYaml import read_yaml
from common.handleLog import log
from conf.projectPath import *


class HandleDb:

    def __init__(self):
        # 1、数据库连接配置
        self.config = read_yaml(os.path.join(conf_path, 'config.yaml'))['db_conf']

    @contextlib.contextmanager
    def handle_db(self):
        """
        使用上文管理器连接数据库
        """
        try:
            # 建立连接
            self.conn = pymysql.connect(**self.config, charset="utf8", cursorclass=pymysql.cursors.DictCursor)
            # 建立游标
            self.cur = self.conn.cursor()
            yield self.cur
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            traceback.print_exc()
            log.error(f'数据库操作失败，报错为：{traceback.format_exc()}')
            raise e
        finally:
            self.cur.close()
            self.conn.close()
        return

    # 获取查询结果的个数
    def get_count(self, sql, args=None):
        with self.handle_db() as db:
            result = db.execute(sql, args)
            return result

    # 获取查询的一条数据/1个数据
    def get_one(self, sql, args=None):
        with self.handle_db() as db:
            db.execute(sql, args)
            result = db.fetchone()
            log.info(f'查询结果为：{result}')
        return result

    # 获取查询到的所有数据
    def get_all(self, sql, args=None):
        with self.handle_db() as db:
            db.execute(sql, args)
            result = db.fetchall()
            log.info(f'查询结果为：{result}')
        return result

    # 修改数据 - 事务的回滚(rollback)和提交(commit) - 事务的4个特性
    def update(self, sql):
        with self.handle_db() as db:
            db.execute(sql)


if __name__ == '__main__':
    import json

    hd = HandleDb()
    b = '728005'
    order_info = "select is_dingyue_success from eload_users where firstname='728005'"
    res = hd.get_one(order_info)
    print(res)
