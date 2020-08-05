import sys
from datetime import time

from time import sleep

import allure
import pytest
from selenium import webdriver

from common import Assert
from common.BaseFunction import waitUntilDisplay, waitUntilClick
from common.dbLink import deleteAct
from flow_path.path_login import loginOn
from run_all_uicase import yamldict, logger

act = yamldict['test_userlist']['company_user']
pwd = yamldict['test_userlist']['company_user_pass']


@pytest.mark.run(order=3)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/user/login 中小微企业登录流程")
@allure.testcase("#root > div > div.header___1E4MV > div > div.flex > div > a:nth-child(1)", "loginOn 👇")
def test_companyLoginOn():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.10.128.152:10053/user/login")

    # 登陆页面
    driver.find_element_by_css_selector(loginOn.input_actLogin_css.value).send_keys(act)
    driver.find_element_by_css_selector(loginOn.input_passLogin_css.value).send_keys(pwd)
    driver.find_element_by_css_selector(loginOn.input_very_codeLogin_css.value).send_keys(' ')
    driver.find_element_by_css_selector(loginOn.btn_login_css.value).click()

    # 首页
    waitUntilDisplay(driver, loginOn.link_home_css.value)
    homeText = driver.find_element_by_css_selector(loginOn.link_home_css.value)

    test_Assert.assert_text_ui(homeText.text, '首页')
    logger.info("中小微企业金融服务聚合平台登录成功！")


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/user/register 中小微企业注册流程")
@allure.testcase("http://10.10.128.152:10053/user/register", "注册 👇")
def test_companyRegister():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.10.128.152:10053/user/register")
    # db中清除已注册的账户
    deleteAct()
    logger.info("对已注册的账户进行删除操作")

    waitUntilClick(driver, loginOn.btn_agree_css.value)
    driver.find_element_by_css_selector(loginOn.btn_agree_css.value).click()
    driver.find_element_by_css_selector(loginOn.input_act_css.value).send_keys(act)
    driver.find_element_by_css_selector(loginOn.input_pwd_css.value).send_keys(pwd)
    driver.find_element_by_css_selector(loginOn.input_conPwd_css.value).send_keys(pwd)
    sleep(2)
    waitUntilClick(driver, loginOn.btn_phoneCode_css.value)
    driver.find_element_by_css_selector(loginOn.btn_phoneCode_css.value).click()
    # print('============================================================================')
    # print(time.localtime())
    sleep(20)
    # print(time.localtime())
    # print('============================================================================')
    driver.find_element_by_css_selector(loginOn.btn_agreeReg.value).click()

    title = driver.title
    test_Assert.assert_text_ui(title, '中小微企业金融服务聚合平台')
    logger.info("注册成功，返回到登陆页面")
    driver.quit()


@pytest.mark.run(order=2)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/user/forget 中小微企业密码修改流程")
@allure.testcase("http://10.10.128.152:10053/user/forget", "密码修改 👇")
def test_companyPassForget():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.10.128.152:10053/user/forget")

    driver.find_element_by_css_selector(loginOn.input_actForget_css.value).send_keys(act)
    driver.find_element_by_css_selector(loginOn.input_codeForget_css.value).send_keys(' ')
    waitUntilClick(driver, loginOn.btn_phoneCodeForget_css.value)
    driver.find_element_by_css_selector(loginOn.btn_phoneCodeForget_css.value).click()

    sleep(20)

    # 密码重置页面
    waitUntilClick(driver, loginOn.btn_next_css.value)
    driver.find_element_by_css_selector(loginOn.btn_next_css.value).click()
    waitUntilDisplay(driver, loginOn.txt_pwd_css.value)
    textAct = driver.find_element_by_css_selector(loginOn.txt_pwd_css.value).text
    sleep(2)
    test_Assert.assert_text_ui(textAct, '重置密码')
    logger.info("成功进入到密码重置页面", )
    driver.find_element_by_css_selector(loginOn.input_pwdForget_css.value).send_keys(pwd)
    driver.find_element_by_css_selector(loginOn.input_pwdConfirm_css.value).send_keys(pwd)
    waitUntilClick(driver, loginOn.btn_nextPwd_css.value)
    driver.find_element_by_css_selector(loginOn.btn_nextPwd_css.value).click()

    # 修改完成画面
    waitUntilDisplay(driver, loginOn.txt_changeOver_css.value)
    textPwdChangeOver = driver.find_element_by_css_selector(loginOn.txt_changeOver_css.value).text
    sleep(2)
    test_Assert.assert_text_ui(textPwdChangeOver, '完成修改')
    logger.info("成功进入到密码修改完成页面")
    driver.quit()
