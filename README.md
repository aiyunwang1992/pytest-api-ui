**接口&ui自动化框架**
这个框架接口和ui均可用，只需要根据项目来添加即可
--common：公共方法层
--conf：参数配置层
--logs：日志记录
--projects：项目层，可添加ui或者接口相关的项目
    --project_template：项目相关模板
--template：测试用例模板存放
--initCaseTemplate.py：生成测试用例
--projectCreate.py 生成项目文件
--run.py:用例执行调用脚本
操作方法：
1.先执行projectCreate.py创建项目
2.在项目中写用例和方法
3.initCaseTemplate.py生成测试用例,调整
4.执行run.py
