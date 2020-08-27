import sys
from time import sleep

import allure
import pytest
from selenium import webdriver
from common.BaseFunction import actionChainsClick, waitUntilClick
from flow_path.path_backStage_authentication import path_backStage_authentication
from flow_path.path_backstage_examine import path_backstage_examine
from run_all_uicase import yamldict, logger
from common import Assert
from test_flow.test_Authentication.test_backStage_examine import backStageLogin

act = yamldict['test_backStageUserList']['company_user']
pwd = yamldict['test_backStageUserList']['company_user_pass']
enterprise_name = yamldict['test_backStageAuthentication']['enterprise_name']
enterprise_type = yamldict['test_backStageAuthentication']['enterprise_type']


@pytest.mark.run(order=-1)
@allure.severity("blocker")
@allure.description("http://10.10.128.152:10052/#/authority/mechanism 后台认证")
@allure.testcase("http://10.10.128.152:10052/#/authority/mechanism", "后台认证 👇")
def test_backStage_authentication():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.10.128.152:10052/#/account/login")

    # 登陆页面
    backStageLogin(driver, test_Assert)

    sleep(2)
    driver.find_element_by_xpath(path_backStage_authentication.btn_jurisdiction_xpath.value).click()
    sleep(1)
    el = driver.find_element_by_xpath(path_backStage_authentication.btn_mechanism_xpath.value)
    actionChainsClick(driver, el)

    waitUntilClick(driver, path_backStage_authentication.btn_addMechanism_css.value)
    driver.find_element_by_css_selector(path_backStage_authentication.btn_addMechanism_css.value).click()

    driver.find_element_by_css_selector(path_backStage_authentication.input_MechanismName_css.value).send_keys(
        enterprise_name)
    driver.find_element_by_css_selector(path_backStage_authentication.input_MechanismSimName_css.value).send_keys('诚泰')

    driver.find_element_by_css_selector(path_backStage_authentication.select_MechanismType_css.value).click()
    driver.find_elements_by_xpath("//*[text() = " + enterprise_type + "]")[0].click()
    driver.find_element_by_css_selector(path_backStage_authentication.select_MechanismStatue_css.value).click()
    driver.find_elements_by_xpath("//*[text() = '启用']")[0].click()

    driver.find_element_by_css_selector(path_backStage_authentication.btn_confirm_css.value).click()
