import sys

from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from androidBaseFlow import startWeinxin
from common import Assert
from common.BaseFunction import waitUntilDisplay, waitUntilClick, waiteForClick, waiteForNotExist
from common.dbLink import deleteAct, getPhoneMessage, flushDb, deleteInforMobile, getVerification
from flow_path.path_backStage_authentication import path_backStage_authentication
from flow_path.path_login import loginOn
from run_all_case import yamldict, logger, runMode, mobileDriver

act = yamldict['test_userlist']['company_user']
pwd = yamldict['test_userlist']['company_user_pass']
url_forward = yamldict['test_path_list']['url_ui_forward']
url_ui_register = yamldict['test_path_list']['url_ui_register']
url_ui_forget = yamldict['test_path_list']['url_ui_forget']
RequestURL = yamldict['test_redisdb_list']['RequestURL']


# 登录
def companyLoginOn():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_forward)

    # 登陆页面
    login(driver)

    # 首页
    waitUntilDisplay(driver, loginOn.link_home_css.value)
    homeText = driver.find_element_by_css_selector(loginOn.link_home_css.value)

    test_Assert.assert_text_ui(homeText.text, '首页')
    logger.info("中小微企业金融服务聚合平台登录成功！")
    driver.quit()


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/user/register 中小微企业注册流程")
@allure.testcase("http://10.10.128.152:10053/user/register", "注册 👇")
def test_companyRegister():
    if runMode == 'UI':
        def_name = sys._getframe().f_code.co_name
        test_Assert = Assert.Assertions(def_name)
        logger.info("开始执行脚本%s:\n", def_name)

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url_ui_register)
        # db中清除已注册的账户
        deleteInforMobile()
        logger.info("对已注册的账户进行删除操作")
        sleep(1)
        waitUntilClick(driver, loginOn.btn_agree_css.value)
        driver.find_element_by_css_selector(loginOn.btn_agree_css.value).click()

        waitUntilDisplay(driver, loginOn.input_act_css.value)
        driver.find_element_by_css_selector(loginOn.input_act_css.value).send_keys(act)
        driver.find_element_by_css_selector(loginOn.input_pwd_css.value).send_keys(pwd)
        driver.find_element_by_css_selector(loginOn.input_conPwd_css.value).send_keys(pwd)
        waitUntilClick(driver, loginOn.btn_phoneCode_css.value)
        sleep(2)
        flushDb()
        driver.find_element_by_css_selector(loginOn.btn_phoneCode_css.value).click()

        while 1:
            message = getPhoneMessage().get("regMes")
            if message is None:
                sleep(0.5)
                continue
            else:
                break

        driver.find_element_by_css_selector(loginOn.input_phoneCode_css.value).send_keys(message.strip().strip('"'))
        waitUntilClick(driver, loginOn.btn_agreeReg.value)
        driver.find_element_by_css_selector(loginOn.btn_agreeReg.value).click()

        title = driver.title
        test_Assert.assert_text_ui(title, '中小微企业金融服务聚合平台')
        logger.info("注册成功，返回到登陆页面")
        sleep(1)
        driver.quit()
    else:
        deleteInforMobile()  # 删除个人信息
        startWeinxin()
        while True:
            if mobileDriver(text='一键微信授权登录').exists():
                waiteForClick(mobileDriver(text='一键微信授权登录'))
                break
            else:
                continue
        waiteForClick(mobileDriver(text='允许'))
        waiteForClick(mobileDriver(text='授权手机号'))
        waiteForClick(mobileDriver(text='允许'))

        logger.info("PC 端进行密码修改")
        companyPassForgetForward(act)
        logger.info("小程序个人实名认证页面")

        # 上传身份证正反面
        waiteForClick(mobileDriver(text='请上传身份证头像面'))
        waiteForClick(mobileDriver(text='所有图片'))
        waiteForClick(mobileDriver(text='自动化测试专用相册'))
        mobileDriver("android.widget.LinearLayout").offspring("com.tencent.mm:id/dm6").child("com.tencent.mm:id/f4b")[
            3].child(
            "com.tencent.mm:id/dm0").click()
        waiteForClick(mobileDriver(text='完成'))
        sleep(2)
        waiteForClick(mobileDriver(text='请上传身份证国徽面'))
        waiteForClick(mobileDriver(text='所有图片'))
        waiteForClick(mobileDriver(text='自动化测试专用相册'))
        mobileDriver("android.widget.LinearLayout").offspring("com.tencent.mm:id/dm6").child("com.tencent.mm:id/f4b")[
            2].child(
            "com.tencent.mm:id/dm8").click()
        waiteForClick(mobileDriver(text='完成'))
        waiteForClick(mobileDriver(text='提交认证'))

        # 活体认证欺诈性校验
        getVerification(RequestURL, act)
        # 等待直到元素消失
        while True:
            if mobileDriver(text='认证中').exists():
                continue
            else:
                break
        waiteForClick(mobileDriver(name='com.tencent.mm:id/dc'))


# 后端账户修改密码
def companyPassForget(driver, Act, Type):
    waitUntilClick(driver, path_backStage_authentication.btn_forPass_css.value)
    sleep(1)
    driver.find_element_by_css_selector(path_backStage_authentication.btn_forPass_css.value).click()
    waitUntilClick(driver, loginOn.btn_next_css.value)
    sleep(0.5)
    driver.find_element_by_css_selector(loginOn.input_actForget_css.value).send_keys(Act)
    driver.find_element_by_css_selector(loginOn.input_codeForget_css.value).send_keys(' ')
    waitUntilClick(driver, loginOn.btn_phoneCodeForget_css.value)
    sleep(0.5)
    flushDb()
    driver.find_element_by_css_selector(loginOn.btn_phoneCodeForget_css.value).click()
    while 1:
        if Type == 1:
            message = getPhoneMessage().get("actBank")
        else:
            message = getPhoneMessage().get("actRisk")
        if message is None:
            sleep(1)
            continue
        else:
            break
    message = message.strip().strip('"')
    el = driver.find_element_by_css_selector(loginOn.input_phoneCodeForget_css.value)
    el.send_keys(Keys.LEFT)
    el.send_keys(message)
    el.send_keys(Keys.DELETE)
    # 密码重置页面
    waitUntilClick(driver, loginOn.btn_next_css.value)
    sleep(0.5)
    driver.find_element_by_css_selector(loginOn.btn_next_css.value).click()
    waitUntilDisplay(driver, loginOn.btn_nextPwd_css.value)
    logger.info("成功进入到密码重置页面")
    sleep(0.5)
    driver.find_element_by_css_selector(loginOn.input_pwdForget_css.value).send_keys('123456')
    driver.find_element_by_css_selector(loginOn.input_pwdConfirm_css.value).send_keys('123456')
    driver.find_element_by_css_selector(loginOn.btn_nextPwd_css.value).click()
    # 修改完成画面
    sleep(2)
    logger.info("成功进入到密码修改完成页面")


# 前端账户修改密码：
def companyPassForgetForward(act):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_forward)
    logger.info("登录页面")
    waitUntilClick(driver, loginOn.href_passForget_css.value)
    sleep(1)
    driver.find_element_by_css_selector(loginOn.href_passForget_css.value).click()
    waitUntilClick(driver, loginOn.btn_nextPwd1_css.value)
    logger.info("安全验证页面")
    driver.find_element_by_css_selector(loginOn.input_phoneNum_css.value).send_keys(act)
    driver.find_element_by_css_selector(loginOn.input_veryCode_css.value).send_keys(' ')
    driver.find_element_by_css_selector(loginOn.btn_phoneVeryCode_css.value).click()
    flushDb()
    while 1:
        message = getPhoneMessage().get("forgeMes")
        if message is None:
            sleep(1)
            continue
        else:
            break
    driver.find_element_by_css_selector(loginOn.input_phoneVeryCode_css.value).send_keys(message.strip().strip('"'))

    driver.find_element_by_css_selector(loginOn.btn_nextPwd1_css.value).click()
    waitUntilClick(driver, loginOn.btn_nextPwd2_css.value)
    logger.info("重置密码页面")
    driver.find_element_by_css_selector(loginOn.input_newPwd_css.value).send_keys(pwd)
    driver.find_element_by_css_selector(loginOn.input_newPwdCon_css.value).send_keys(pwd)

    driver.find_element_by_css_selector(loginOn.btn_nextPwd2_css.value).click()
    sleep(1)
    driver.quit()


def login(driver):
    # 登陆页面
    driver.find_element_by_css_selector(loginOn.input_actLogin_css.value).send_keys(act)
    driver.find_element_by_css_selector(loginOn.input_passLogin_css.value).send_keys(pwd)
    driver.find_element_by_css_selector(loginOn.input_very_codeLogin_css.value).send_keys(' ')
    driver.find_element_by_css_selector(loginOn.btn_login_css.value).click()


if __name__ == '__main__':
    companyPassForget()
