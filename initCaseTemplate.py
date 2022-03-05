#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleCaseTemplate.py
@IDE ：PyCharm
生成用例的模板
"""
import jinja2
from common.handleLog import log
from conf.projectPath import *


class HandleCaseTemplate:
    def __init__(self, project_name, report_name):
        self.report_name = report_name
        self.project_name = project_name
        self.testcases_path = os.path.join(projects_path, f"{project_name}/testcases")
        self.data_file_path = os.path.join(projects_path, f"{project_name}/testcasedatas")

    # 模板中的参数组成
    def template_variable(self):
        data_yaml_list = [i for i in os.listdir(os.path.join(self.data_file_path)) if i.endswith('.yaml')]
        cases_list = []
        for yaml_name in data_yaml_list:
            case_item = {}
            case_item['report_name'] = self.report_name
            case_item['data_file_path'] = f"{self.project_name}/testcasedatas/{yaml_name}"
            case_item['case_name'] = f"test_{yaml_name.split('.')[0]}"
            cases_list.append(case_item)
        return cases_list

    # 生成api的测试用例文件
    def api_create_cases(self):
        cases_list = self.template_variable()
        for case_item in cases_list:
            try:
                temp_loader = jinja2.FileSystemLoader(searchpath=template_path)
                temp_env = jinja2.Environment(loader=temp_loader)
                temp_var = {
                    'case_item': case_item
                }
                template = temp_env.get_template('api_testcases_template')
                casefilename = f"{case_item['case_name']}.py"
                casefile = os.path.join(self.testcases_path, casefilename)
                with open(casefile, 'w', encoding='utf-8') as f:
                    f.write(template.render(temp_var))
            except Exception as e:
                log.error(f"测试用例文件生成失败，报错为:{e}")
        log.info("测试用例文件生成完成")


if __name__ == '__main__':
    HandleCaseTemplate('soulmiaApi', 'soulmial报告').api_create_cases()
