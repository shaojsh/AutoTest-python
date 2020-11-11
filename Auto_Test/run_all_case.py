#!/usr/bin/python
# -*- coding: UTF-8 _*_
import start
import sys
import time
import os
import sys

import androidBaseFlow
from common.Logs import Log
import pytest
from common import Shell

from common.Yaml_Data import HandleYaml

root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'
runMode = 'UI'
evn = ''
# 环境run取得
config = HandleYaml(root_dir + '\\test_data\\config.yaml')
# runMode = config.get_data()['configEvn']['runMode']
# evn = config.get_data()['config']['evn']
runMode = 'UI'
evn = 'SIT'
if evn == 'SIT':
    handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol-SIT.yaml')
else:
    handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol-UAT.yaml')

# handleyaml = HandleYaml(os.getcwd() + '\\..\\test_data\\ConfigGol-SIT.yaml')  # 调试db用

yamldict = handleyaml.get_data()

mobileDriver = ''
if runMode != 'UI':
    mobileDriver = androidBaseFlow.poco
file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger
if __name__ == "__main__":
    try:
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime()) + "===================================")
        root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test' + yamldict['test_path_list']['url_ui']
        pytest.main([root_dir, "--alluredir",
                     "./report/reportallure/"])
        print("脚本执行完成")
    except Exception as e:
        # i = i + 1
        # im = ImageGrab.grab()  # 可以添加一个坐标元组进去
        # im.save(os.getcwd() + '\\test_data\\error_pic\\' + i + '.jpg')
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

    try:
        shell = Shell.Shell()
        cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/', './report//reporthtml/')
        print("开始执行报告生成")
        shell.invoke(cmd)
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        raise

    time.sleep(5)
    # mail()
