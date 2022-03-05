#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： wangaiyun
@File ：handleRequests.py
@IDE ：PyCharm
处理请求方法
"""
import requests
import json
from common.handleEnv import EntryPoint


class HandleRequests:
    url=EntryPoint().URL
    def send_requests(self,method,url,data,token=None):
        """发送接口请求的方法"""
        header =self.__header(token=token)
        url=self.__deal_url(url)
        header['host']=self.__deal_host(url)
        # get请求
        if method.upper()=='GET':
            response=requests.request(method,url,params=data,headers=header)
        # post请求4
        else:
            header['Content-Type'] = 'application/json'
            response=requests.request(method,url,data=json.dumps(data),headers=header)
        return response
    def __header(self,token=None):
        """处理header中带token的情况"""
        header={}
        if token:
            header['Authorization'] = f'Bearer {token}'
        return header
    def __deal_url(self,url):
        """处理url的切换"""
        if not url.startswith('http://'):
            base_url=self.url
            url=base_url + url
        return url
    def __deal_host(self,url):
        """处理host的切换"""
        url=self.__deal_url(url)
        host=url.split('/')[2]
        return host
