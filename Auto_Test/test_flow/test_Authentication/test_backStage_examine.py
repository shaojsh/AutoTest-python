import sys
from time import sleep

import allure
import pytest
from selenium import webdriver
from common.BaseFunction import waitUntilDisplay
from common.dbLink import updateNameCompany, getPhoneMessage
from flow_path.path_backStage_authentication import path_backStage_authentication
from flow_path.path_backstage_examine import path_backstage_examine
from run_all_case import yamldict, logger, runMode, driverPath, jenkins
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
    if jenkins:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 浏览器不提供可视化页面
        option.add_argument('no-sandbox')  # 以最高权限运行
        option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
        option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        option.add_argument('--window-size=1920,1080')  # 设置浏览器分辨率（窗口大小）
        driver = webdriver.Chrome(options=option)
    else:
        driver = webdriver.Chrome(executable_path=driverPath)
    driver.maximize_window()
    driver.get(url_back)

    act = yamldict['test_backStageUserList']['company_user']
    pwd = yamldict['test_backStageUserList']['company_user_pass']

    # 登陆页面
    backStageLogin(driver, act, pwd, 0)
    updateNameCompany()
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
    bussPath = path_backstage_examine.btn_bussListName_xpath.value + '[' + str(index + 1) + ']' + '/td[8]' + '/span/a'
    driver.find_elements_by_xpath(bussPath)[0].click()
    sleep(0.5)
    waitUntilDisplay(driver, path_backstage_examine.txt_userInfor_css.value)
    userInforTxt = driver.find_element_by_css_selector(path_backstage_examine.txt_userInfor_css.value).text
    test_Assert.assert_text_ui(userInforTxt, "用户基本信息")
    logger.info('成功进入企业信息审核画面')

    driver.find_element_by_css_selector(path_backstage_examine.input_examine_css.value).send_keys('企业审核通过')

    driver.find_element_by_css_selector(path_backstage_examine.btn_code_css.value).click()

    while 1:
        message = getPhoneMessage().get("Audit")
        if message is None:
            sleep(0.5)
            continue
        else:
            break
    driver.find_element_by_css_selector(path_backstage_examine.input_code_css.value).send_keys(message.strip().strip('"'))

    driver.find_element_by_css_selector(path_backstage_examine.btn_examinePass_css.value).click()
    sleep(1)
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
