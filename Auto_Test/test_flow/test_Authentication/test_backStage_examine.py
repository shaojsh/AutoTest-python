import sys
from time import sleep

import allure
import pytest
from selenium import webdriver
from common.BaseFunction import waitUntilDisplay
from flow_path.path_backStage_authentication import path_backStage_authentication
from flow_path.path_backstage_examine import path_backstage_examine
from run_all_uicase import yamldict, logger
from common import Assert

businessName = yamldict['test_backStageUserList']['company_name']
url_back = yamldict['test_path_list']['url_ui_back']


@pytest.mark.run(order=4)
@allure.severity("blocker")
@allure.description("http://10.10.128.152:10052/#/enterprise/list 企业审核")
@allure.testcase("http://10.10.128.152:10052/#/enterprise/list", "企业审核 👇")
def test_backstage_examine():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_back)

    act = yamldict['test_backStageUserList']['company_user']
    pwd = yamldict['test_backStageUserList']['company_user_pass']

    # 登陆页面
    backStageLogin(driver, act, pwd, 0)
    sleep(2)
    driver.find_element_by_xpath(path_backstage_examine.btn_bussMan_xpath.value).click()
    sleep(1)
    driver.find_element_by_css_selector(path_backstage_examine.btn_bussList_css.value).click()
    sleep(1)
    elList = driver.find_elements_by_xpath(path_backstage_examine.btn_bussListName_xpath.value)
    index = 0
    for i in range(len(elList)):
        path = path_backstage_examine.btn_bussListName_xpath.value + '[' + str(i + 1) + ']/' + 'td' + '[' + str(1) + ']'
        text = driver.find_element_by_xpath(path).text
        if text == businessName:
            index = i
            break
    bussPath = path_backstage_examine.btn_bussListName_xpath.value + '[' + str(index + 1) + ']' + '/td[7]' + '/span/a'
    driver.find_elements_by_xpath(bussPath)[0].click()
    sleep(0.5)
    waitUntilDisplay(driver, path_backstage_examine.txt_userInfor_css.value)
    userInforTxt = driver.find_element_by_css_selector(path_backstage_examine.txt_userInfor_css.value).text
    test_Assert.assert_text_ui(userInforTxt, "用户基本信息")
    logger.info('成功进入企业信息审核画面')

    driver.find_element_by_css_selector(path_backstage_examine.btn_examinePass_css.value).click()
    sleep(1)
    # examine_finalText = driver.find_element_by_xpath(bussPath).text
    # test_Assert.assert_text_ui(examine_finalText, "查看详情")
    logger.info("企业认证通过")
    driver.quit()


# 后台登录操作
def backStageLogin(driver, act, pwd, flag):
    driver.find_element_by_css_selector(path_backstage_examine.input_actLogin_css.value).send_keys(act)
    driver.find_element_by_css_selector(path_backstage_examine.input_actPwd_css.value).send_keys(pwd)
    driver.find_element_by_css_selector(path_backstage_examine.btn_login_css.value).click()
    if flag != 1:
        waitUntilDisplay(driver, path_backstage_examine.txt_backstage_css.value)
    else:
        waitUntilDisplay(driver, path_backStage_authentication.btn_codeAu_css.value)
    logger.info('成功登录后台系统')
