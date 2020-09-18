#!/usr/bin/python
# -*- coding: UTF-8 _*_
import os
import sys

import pytest

from common.Request import RequestsHandler
from Conf.conf import *
import allure
from common import Assert
from common import Consts
from common.Retrun_Response import dict_style

from common.Yaml_Data import HandleYaml
from run_all_case import logger

API_dir_cnf = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'
handleyaml = HandleYaml(API_dir_cnf + '\\test_data\\test_yaml_data.yaml')
yamldict = handleyaml.get_data()


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试http://calapi.51jirili.com/config/common接口")
@allure.testcase("http://calapi.51jirili.com/config/common", "测试用例地址 👇")
def test_config_common():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)
    opera_url = server_ip('realse') + yamldict['test_operation_list']['url']
    opera_result = RequestsHandler().post_Req(url=opera_url, params='')
    sting_response = opera_result.content.decode()
    json_response = dict_style(sting_response)
    test_Assert.assert_code(json_response['code'], 10006)

    test_Assert.assert_body(json_response, 'msg', '签名校验失败')
    Consts.RESULT_LIST.append('pass')
