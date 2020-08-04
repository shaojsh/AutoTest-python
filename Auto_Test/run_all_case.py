#!/usr/bin/python
# -*- coding: UTF-8 _*_

import time
import os
import sys
from common.Logs import Log
import pytest
from common import Shell

from common.Yaml_Data import HandleYaml
from common.emails import mail

root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'
handleyaml = HandleYaml(root_dir+'\\test_data\\ConfigGol.yaml')
yamldict = handleyaml.get_data()

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


if __name__ == "__main__":
    file = os.path.basename(sys.argv[0])
    log = Log(file)
    logger = log.Logger

    try:
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime()) + "===================================")
        root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'+yamldict['test_path_list']['url_api']
        pytest.main([root_dir, "--alluredir",
                     "./report/reportallure/"])

        print("脚本执行完成")
    except Exception as e:
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
