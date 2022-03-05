#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleSign.py
@IDE ：PyCharm
处理接口签名
"""
import hashlib
import urllib.parse

hlb = hashlib.md5()


class HandleSign:
    """
    针对中台的接口返回签名
    """

    def handle_sign(self, data):
        if isinstance(data, str):
            data_dict = {}
            for i in data.split('&'):
                if '=' in i:
                    data_dict[i.split('=')[0]] = i.split('=')[1]
                else:
                    data_dict[i] = ''
        else:
            data_dict = data
        dict1 = {item: data_dict[item] for item in sorted(data_dict)}
        url_encode = urllib.parse
        param = url_encode.urlencode(dict1) + 'J+/PqxKej/UGFldY+B9kCVeWF7Ls1eHHy7ufSLSECj4='
        hlb.update(param.encode())
        sign = hlb.hexdigest()
        return sign


if __name__ == '__main__':
    data = "keywords=813001@qq.com"
    data1 = "start_date=2021-06-22 00:00:00&end_date=2021-06-22 23:59:59&page=1&size=20&site_code=all"
    HandleSign().handle_sign(data)
