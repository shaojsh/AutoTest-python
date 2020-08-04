#!/usr/bin/python
# -*- coding: UTF-8 _*_

import pytest
import json
import sys
import os
from common import Shell
from common.Request import RequestsHandler
from common.Logs import Log
from common.Yaml_Data import HandleYaml
from Conf.conf import *
import allure
from common import Assert
from common import Consts

from common.Retrun_Response import dict_style

handleyaml = HandleYaml()
yamldict = handleyaml.get_data()

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


@allure.description("测试http://calapi.51jirili.com/config/common接口")
@allure.testcase("http://calapi.51jirili.com/config/common", "测试用例地址 👇")
def test_config_common():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)
    opera_url = server_ip('realse') + yamldict['test_operation_list']['url']
    opera_result = RequestsHandler().get_Req(url=opera_url, params='')
    sting_response = opera_result.content.decode()
    json_response = dict_style(sting_response)
    test_Assert.assert_code(json_response['code'], 10006)

    test_Assert.assert_body(json_response, 'msg', '签名校验失败')
    Consts.RESULT_LIST.append('pass')
