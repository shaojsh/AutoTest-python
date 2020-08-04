import os
import sys

import allure
import pytest
from selenium import webdriver

from common import Assert
from flow_path.demo_login import loginOn
from run_all_uicase import yamldict, logger

WebDriver = webdriver.Chrome()


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/user/login 中小微企业页面登录")
@allure.testcase("http://10.10.128.152:10053/user/login", "loginOn 👇")
def test_companyloginOn():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    WebDriver.maximize_window()
    WebDriver.get("http://10.10.128.152:10053/user/login")
    test_Assert.assert_text_ui('sucess', 'sucess')
    act = yamldict['test_userlist']['company_user']
    WebDriver.find_element_by_css_selector(loginOn.act_css.value).send_keys(act)
