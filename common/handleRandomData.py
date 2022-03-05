#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleRandomData.py
@IDE ：PyCharm
随机数据生成
"""
import random
import string
from faker import Faker


class HandleRandomData:
    faker = Faker('zh_CN')
    num = string.digits
    letters = string.ascii_letters

    # 随机返回整数
    def rand_int(self, m, n):
        num = random.randint(m, n)
        return num

    # 随机生成email
    def rand_email(self):
        email = self.faker.email()
        return email

    # 随机生成数字
    def rand_num(self, n):
        num = ''.join(random.choice(f"{self.num}") for i in range(n))
        return num

    # 随机生成N位数的数字,字母的字符串
    def rand_num_string(self, n):
        rand_letters = ''.join(random.choice(f"{self.num}" + f"{self.letters}") for i in range(n))
        return rand_letters

    # 随机生成N位数的字符串
    def rand_string(self, n):
        rand_letters = ''.join(random.choice(f"{self.letters}") for i in range(n))
        return rand_letters

    # 随机返回单个字符串
    def rand_choice(self, param):
        choice = random.choice(param)
        return choice


if __name__ == '__main__':
    h = HandleRandomData()
    r = h.rand_email()
    print(r)
