#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Auth ： suoer
@File ：handleProjectCreate.py
@IDE ：PyCharm
创建子项目的方法
api或者ui的项目
"""
from shutil import copytree
from common.handleLog import log
from conf.projectPath import *
class HandleProjectCreate:
    project_template_api_path=os.path.join(projects_path,r'project_template\api_template')
    project_template_ui_path = os.path.join(projects_path, r'project_template\ui_template')

    #创建子项目
    def project_create(self,project_name,type='api'):
        new_project_path = os.path.join(projects_path,project_name )
        try:
            if type=='api':
                copytree(self.project_template_api_path,new_project_path)
            elif type=='ui':
                copytree(self.project_template_ui_path, new_project_path)
        except Exception as e:
            log.error(f'创建项目子目录出错，报错为:{e}')
if __name__=='__main__':
    HandleProjectCreate().project_create('abc')
