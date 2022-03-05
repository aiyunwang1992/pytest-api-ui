#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleFront.py
@IDE ：PyCharm
执行测试步骤处理方法
"""
from common.handleLog import log
from common.handleYaml import read_yaml
from common.handleRelateData import HandleRelateData
from common.handleRequests import HandleRequests
from common.handleJsonPath import handle_jsonpath
from projects.soulmiaApi.common.soulmiaApiAssert import SoulmiaApiAssert
from common.handleRandomData import HandleRandomData
from conf.projectPath import *


class HandleTestStep:
    def __init__(self, casetitle):
        self.casetitle = casetitle
        self.data_param = None
        self.req = HandleRequests()
        self.sat = SoulmiaApiAssert(casetitle)

    def eval_data(self, datas):
        for key, value in datas.items():
            if 'func' in value:
                datas[key] = eval(value.split(':')[1])
        return datas

    # 处理测试步骤
    def handle_teststep(self, api_path, test_step):
        api_path = os.path.join(projects_path, api_path)
        api_temp = read_yaml(api_path)
        assert_result = {}
        if isinstance(test_step, list):
            for item in test_step:
                api_dict = api_temp[item['api']]
                if item.get('params'):
                    params = self.eval_data(item['params'])
                else:
                    params = ''
                # 上传需要关联的参数
                if item.get('setparam'):
                    for i in item['setparam']:
                        setattr(HandleRelateData, i, item['params'][i])
                # 发起接口请求
                if api_dict.get('token'):
                    try:
                        res = self.req.send_requests(api_dict['method'], api_dict['url'], params,
                                                     token=item['token']).json()
                    except Exception as e:
                        log.error(f"用例{self.casetitle}的接口{api_dict['url']}调用失败")
                        raise e
                else:
                    try:
                        res = self.req.send_requests(api_dict['method'], api_dict['url'], params).json()
                    except Exception as e:
                        log.error(f"用例{self.casetitle}的接口{api_dict['url']}调用失败")
                        raise e
                assert_result[item['api']] = self.sat.soulmia_api_assert(item['api'], res, item['validate_content'])
                # 提取关联参数
                if item.get('extract'):
                    for key, value in item['extract'].items():
                        result = handle_jsonpath(res, key)
                        setattr(HandleRelateData, value, result)
        if False in assert_result.values():
            log.debug(f'用例{self.casetitle}的断言失败,结果为:{assert_result}')
            return False
        return True


if __name__ == '__main__':
    h = HandleTestStep('abc')
    h.handle_teststep('soulmiaApi/common/baseapi.yaml', 'abc')
