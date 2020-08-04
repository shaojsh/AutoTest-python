import os
import sys

import allure
import pytest
from selenium import webdriver

from common import Assert
from common.Logs import Log

WebDriver = webdriver.Chrome()

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/ loginOn")
@allure.testcase("http://10.10.128.152:10053/", "loginOn 👇")
def test_loginOn():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    WebDriver.maximize_window()
    WebDriver.get("http://10.10.128.152:10052/account/login?v=1596002392301")
    test_Assert.assert_text_ui('sucess', 'sucess')
