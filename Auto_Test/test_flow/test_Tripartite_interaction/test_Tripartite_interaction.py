import os
import sys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure
import pytest
from airtest.core.api import text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.dbLink import getPhoneMessage, flushDb, getVerification, getVerification_ui
from flow_path.path_Tripartite_interaction import path_Tripartite_interaction
from run_all_case import yamldict, logger, runMode, mobileDriver
from common.BaseFunction import waitUntilDisplay, waitUntilClick, waitUntilClick_xpath, scrollText, \
    waitUntilDisplay_xpath, is_not_visible, waiteForClick, dragUntilTextAppear
from test_flow.test_Authentication.test_backStage_examine import backStageLogin
from test_flow.test_Authentication.test_login import login
from selenium.webdriver.common.keys import Keys

url_forward = yamldict['test_path_list']['url_ui_forward']
url_back = yamldict['test_path_list']['url_ui_back']
RequestURL = yamldict['test_redisdb_list']['RequestURL']
act = yamldict['test_userlist']['company_user']

# 前端账户
company_user = yamldict['test_userlist']['company_user']
company_user_pass = yamldict['test_userlist']['company_user_pass']

# 银行账户
company_bank = yamldict['test_backStageUserList']['company_bank']
company_bank_pass = yamldict['test_backStageUserList']['company_bank_pass']

# 担保公司账户
company_Guarantee = yamldict['test_backStageUserList']['company_Guarantee']
company_Guarantee_pass = yamldict['test_backStageUserList']['company_Guarantee_pass']

# 产品名称
product_name = yamldict['test_backStageUserList']['product_name']


# 担保费审核
def costAudit(driver_risk):
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_homeBackStage_css.value).click()
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_feeCheckMan_css.value)
    sleep(1)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_feeCheckMan_css.value).click()
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_feeCheckOk_css.value)
    sleep(1)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_feeCheckOk_css.value).click()
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_feeConfirm_css.value)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_feeConfirm_css.value).click()
    waitUntilClick(driver_risk, path_Tripartite_interaction.input_feeGetConfirm_css.value)
    sleep(1)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.input_feeMarks_css.value).send_keys('担保费审核通过')
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.input_feeGetConfirm_css.value).click()
    sleep(2)
    driver_risk.quit()


# 银行放款审核
def loanReview(driver_bank):
    sleep(2)
    logger.info('银行放款审核首页')
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_homeBackStage_css.value).click()
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_loanReview_css.value)
    sleep(1)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_loanReview_css.value).click()

    logger.info('银行放款审核列表')
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_loanCheck_css.value)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_loanCheck_css.value).click()

    logger.info('银行放款审核页面')
    waitUntilDisplay_xpath(driver_bank, path_Tripartite_interaction.btn_loanOk_xpath.value)
    sleep(0.5)
    driver_bank.find_element_by_xpath(path_Tripartite_interaction.btn_calender_xpath.value).click()
    el = driver_bank.find_element_by_xpath(path_Tripartite_interaction.choose_calender_xpath.value)
    sleep(0.5)
    el.send_keys(Keys.ENTER)
    driver_bank.find_element_by_xpath(path_Tripartite_interaction.input_loanReason_xpath.value).send_keys("银行放款通过")
    sleep(0.5)
    driver_bank.find_element_by_xpath(path_Tripartite_interaction.btn_loanOk_xpath.value).click()
    waitUntilClick_xpath(driver_bank, path_Tripartite_interaction.btn_tagLoan_xpath.value)
    sleep(2)


# 前端还款
def toRepay(driver_forward):
    sleep(2)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_loanApply_css.value).click()
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_repayment_css.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_repayment_css.value).click()

    # 还款申请页面
    logger.info('还款申请页面')
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_submitRepay_cs.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_repayBankName_css.value).send_keys(
        "工商银行")
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_repayBankNum_css.value).send_keys(
        "123456789012")
    picture_dir1 = os.getcwd() + '\\test_data\\picture\\id_1.jpg'
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.upload_repayPic_css.value).send_keys(
        picture_dir1)
    sleep(1)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.checkBox_repayAgree_css.value).click()
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_submitRepay_cs.value).click()

    logger.info('还款申请提交完成页面')
    waitUntilDisplay(driver_forward, path_Tripartite_interaction.txt_RepayOk_cs.value)
    sleep(1)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_myMain_css.value).click()
    sleep(1)
    driver_forward.quit()


# 银行还款审核
def replayCheck_Bank(driver_bank):
    logger.info('银行还款审核首页')
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_homeBackStage_css.value).click()
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_replayCheck_css.value)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_replayCheck_css.value).click()

    logger.info('银行还款审核列表')
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_replayCheckList_css.value)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_replayCheckList_css.value).click()

    logger.info('银行还款审核')
    sleep(1)
    driver_bank.find_element_by_xpath(path_Tripartite_interaction.input_replayReason_xpath.value).send_keys("银行还款审核通过")
    sleep(1)
    driver_bank.find_element_by_xpath(path_Tripartite_interaction.btn_replayOk_xpath.value).click()
    sleep(1)
    driver_bank.quit()


@pytest.mark.run(order=-1)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10052/#/account/login 三方（企业，银行，前端）交互")
@allure.testcase("http://10.10.128.152:10052/#/account/login", "三方（企业，银行，前端）交互 👇")
def test_Tripartite_interaction():
    def_name = sys._getframe().f_code.co_name
    logger.info("开始执行脚本%s:\n", def_name)

    # 前端账户授信申请
    if runMode == 'UI':
        driver_forward = webdriver.Chrome()
        driver_forward.maximize_window()
        driver_forward.get(url_forward)
        logger.info('前端账户登录授信申请')
        login(driver_forward)
        sleep(2)
        creditExtension(driver_forward)
    else:
        waiteForClick(mobileDriver(text='首页'))
        waiteForClick(mobileDriver(text='立即申请'))
        el = mobileDriver(text='首页', name='android.view.View', type='android.view.View')
        dragUntilTextAppear(el, '产品服务', product_name)
        waiteForClick(mobileDriver(text=product_name))
        waiteForClick(mobileDriver(text='立即申请'))

        logger.info('授信采购信息画面')
        waiteForClick(mobileDriver(text='请输入银行账号'))
        text('123456789012')
        mobileDriver(text='分支行').click()
        waiteForClick(mobileDriver(text='请选择项目'))
        waiteForClick(mobileDriver(text='请输入项目名称').parent().parent().parent().child()[2])
        waiteForClick(mobileDriver(text='下一步'))

        logger.info('授信基本资料页面')
        waiteForClick(mobileDriver(text='下一步'))

        logger.info('授信页面')
        mobileDriver(text='企业经营场所照片').drag_to(mobileDriver(text='业务申请'), 0.5)
        mobileDriver(text='企业征信').drag_to(mobileDriver(text='业务申请'), 0.5)
        mobileDriver(text='财务证明资料').drag_to(mobileDriver(text='业务申请'), 0.5)
        waiteForClick(mobileDriver(text='我已阅读并同意提交资料', type='android.widget.CheckBox').child().child())
        waiteForClick(mobileDriver(text='提交授信'))
        # 活体认证欺诈性校验
        getVerification()
        mobileDriver(name='com.tencent.mm:id/dc')
        waiteForClick(mobileDriver(text='我的'))
        logger.info('授信完成页面')

    # 银行授信审核
    driver_bank = webdriver.Chrome()
    driver_bank.maximize_window()
    driver_bank.get(url_back)
    logger.info('银行授信审核')
    backStageLogin(driver_bank, company_bank, company_bank_pass, 0)
    CreditAudit_Bank(driver_bank)

    # 担保公司审核
    driver_risk = webdriver.Chrome()
    driver_risk.maximize_window()
    driver_risk.get(url_back)
    logger.info('担保公司审核')
    backStageLogin(driver_risk, company_Guarantee, company_Guarantee_pass, 0)
    CreditAudit_Risk(driver_risk)

    # 借款申请
    if runMode == 'UI':
        loanApply(driver_forward)
    else:
        # 移动端借款申请
        waiteForClick(mobileDriver(text='我的授信'))
        waiteForClick(mobileDriver(text='马上使用'))
        logger.info('添加银行卡账户画面')
        waiteForClick(mobileDriver(text='请输入银行账号'))
        text('1234567890123')
        mobileDriver(text='对公银行账号').click()
        waiteForClick(mobileDriver(text='获取验证码'))

        while 1:
            message = getPhoneMessage().get("loanMes")
            if message is None:
                sleep(0.5)
                continue
            else:
                break
        waiteForClick(mobileDriver(textMatches='重新获取.*').parent().child())
        text(message.strip().strip('"'))
        waiteForClick(mobileDriver(text='验证码'))
        waiteForClick(mobileDriver(text='确定'))

        logger.info('借款申请页面')

        waiteForClick(mobileDriver(text='请选择收款银行账号'))
        waiteForClick(mobileDriver(text='1234567890123'))

        waiteForClick(mobileDriver(text='请输入借款金额'))
        text('100000')
        mobileDriver(text='请输入借款期限').click()

        mobileDriver(text='请输入借款期限').click()
        text('8')
        waiteForClick(mobileDriver(text='借款金额'))

        waiteForClick(mobileDriver(text='请具体描述详细借款用途'))
        text('借钱还账')
        waiteForClick(mobileDriver(text='还款方式'))

        waiteForClick(mobileDriver(text='我已阅读并同意提交资料').child()[2])
        waiteForClick(mobileDriver(text='提交借款申请'))
        sleep(5)
        getVerification()
        waiteForClick(mobileDriver(name='com.tencent.mm:id/dc'))
        waiteForClick(mobileDriver(name='com.tencent.mm:id/dc'))
    loanCheck_bank(driver_bank)
    loanCheck_Risk(driver_risk)

    if runMode == 'UI':
        # 去缴费
        goToPay(driver_forward)
    else:
        waiteForClick(mobileDriver(text='我的'))
        waiteForClick(mobileDriver(text='我的借款'))
        waiteForClick(mobileDriver(text='去缴纳'))
        sleep(2)
        mobileDriver(text='缴费凭证').drag_to(mobileDriver(text='缴费申请'), 0.5)
        waiteForClick(mobileDriver(text='上传担保费缴费凭证'))
        mobileDriver("android.widget.LinearLayout").offspring("com.tencent.mm:id/dm6").child("com.tencent.mm:id/f4b")[
            1].child(
            "com.tencent.mm:id/dm8").click()
        waiteForClick(mobileDriver(text='完成'))
        waiteForClick(mobileDriver(text='提交申请'))
        waiteForClick(mobileDriver(name='com.tencent.mm:id/dc'))
        waiteForClick(mobileDriver(name='com.tencent.mm:id/dc'))

    # 担保费审核
    costAudit(driver_risk)

    # 银行放款审核
    loanReview(driver_bank)

    # 还款申请
    toRepay(driver_forward)
    # 银行还款审核
    replayCheck_Bank(driver_bank)


# 前端授信申请
def creditExtension(driver_forward):
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_home_css.value)
    sleep(3)

    logger.info('进入到前端首页')
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_home_css.value).click()

    logger.info('进入到前端进入产品选择首页')
    sleep(0.5)
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_apply_css.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_apply_css.value).click()
    sleep(1.5)
    logger.info('进入到前端进入产品详情页')
    path = "//*[text() = \'" + product_name + "\']/../../a/button"  # 查看详情按钮
    waitUntilClick_xpath(driver_forward, path)
    driver_forward.find_element_by_xpath(path).click()
    logger.info('进入到前端进入产品借款页')
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_rent_css.value)
    sleep(1.5)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_rent_css.value).click()
    # 授信采购信息页面
    logger.info('进入授信采购信息页面')
    sleep(1.5)
    waitUntilClick(driver_forward, path_Tripartite_interaction.input_bankNum_css.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_bankNum_css.value).send_keys(
        "1234567890123")

    while True:
        try:
            driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_province_css.value).click()
            sleep(1)
            driver_forward.find_elements_by_xpath("//*[text() = '山西省']")[0].click()
            break
        except:
            continue

    while True:
        try:
            driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_city_css.value).click()
            sleep(1)
            driver_forward.find_elements_by_xpath("//*[text() = '太原市']")[0].click()
            break
        except:
            continue

    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_branchBank_css.value).send_keys(
        "太原文博支行")
    el = driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_branchBank_css.value)
    el.click()
    sleep(1)
    el.send_keys(Keys.ENTER)
    sleep(0.5)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_next1_css.value).click()

    # 基本资料页面
    logger.info('进入授信基本资料页面')
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_next2_css.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_next2_css.value).click()

    # 授信资料完善页面
    logger.info('授信资料完善页面')
    waitUntilClick(driver_forward, path_Tripartite_interaction.checkBox_agree_css.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.checkBox_agree_css.value).click()
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_submit_css.value).click()

    # 授信完成页面
    logger.info('授信完成页面')

    while True:
        # 活体认证欺诈性校验
        try:
            sleep(5)
            getVerification()
            break
        except:
            continue
    # 活体认证
    WebDriverWait(driver_forward, 1200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, path_Tripartite_interaction.text_apply_css.value)))
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_myMain_css.value).click()
    logger.info("实名认证成功画面显示")


# 银行授信审核
def CreditAudit_Bank(driver_bank):
    logger.info('银行授信审核首页')
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_creditCheck_css.value)
    sleep(2)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_creditCheck_css.value).click()

    logger.info('银行待审批授信页面')
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_Check_css.value)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_Check_css.value).click()

    logger.info('审批授信评分卡页面')
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_toCheck_css.value)
    sleep(1)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_toCheck_css.value).click()
    waitUntilClick(driver_bank, path_Tripartite_interaction.input_checkOK_css.value)
    sleep(1)
    logger.info('审批授信审核页面')
    el1 = driver_bank.find_element_by_css_selector(path_Tripartite_interaction.input_checkMoney_css.value)
    el1.send_keys(Keys.CONTROL + 'a')
    el1.send_keys(Keys.DELETE)
    el1.send_keys('100000')

    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.input_checkMonth_css.value).send_keys("12")

    el3 = driver_bank.find_element_by_css_selector(path_Tripartite_interaction.input_checkRate_css.value)
    el3.send_keys(Keys.CONTROL + 'a')
    el3.send_keys(Keys.DELETE)
    el3.send_keys('10')

    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.input_remarks_css.value).send_keys('银行授信审批通过')

    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.input_checkOK_css.value).click()


# 担保公司授信审核
def CreditAudit_Risk(driver_risk):
    logger.info('担保公司授信审核首页')
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_creditCheck_css.value)
    sleep(2)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_creditCheck_css.value).click()

    logger.info('银行待审批授信页面')
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_Check_css.value)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_Check_css.value).click()

    logger.info('审批授信评分卡页面')
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_toCheck_css.value)
    sleep(1)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_toCheck_css.value).click()
    logger.info('审批授信审核页面')
    sleep(0.5)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.input_remarks_css.value).send_keys(
        '担保公司授信审批通过')

    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.input_checkOK_css.value).click()


# 前端借款申请
def loanApply(driver_forward):
    sleep(2)
    productChoose(driver_forward)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_productQuery_css.value).click()
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_productSubmit_css.value)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_productSubmit_css.value).click()

    logger.info('进入收款账户管理画面')

    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_next_css.value)
    sleep(1)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_bankNumMan_css.value).send_keys(
        '12222221222222')
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_bankPhone_css.value).send_keys(
        company_user)
    flushDb()
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_veryCod_css.value).click()
    while 1:
        message = getPhoneMessage().get("loanMes")
        if message is None:
            sleep(0.5)
            continue
        else:
            break
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_veryCod_css.value).send_keys(
        message.strip().strip('"'))

    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_next_css.value).click()

    logger.info('银行卡已经添加')

    logger.info('进入借款申请画面')
    sleep(2)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_act_css.value).click()
    sleep(0.5)
    driver_forward.find_element_by_xpath("//*[text() = '12222221222222']").click()
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_loanMoney_css.value).send_keys(
        '90000')
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_loanMonth_css.value).send_keys(
        '12')

    while True:
        try:
            driver_forward.find_element_by_css_selector(
                path_Tripartite_interaction.select_repaymentWay_css.value).click()
            sleep(1)
            driver_forward.find_element_by_xpath("//*[text() = '随借随还']").click()
            break
        except:
            continue
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.input_reason_css.value).send_keys(
        '政府项目借贷')

    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.checkBox_agreeLoan_css.value).click()
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_submitLoan_css.value).click()
    # 点击返回
    while True:
        # 活体认证欺诈性校验
        try:
            sleep(5)
            getVerification()
            break
        except:
            continue
    WebDriverWait(driver_forward, 1200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, path_Tripartite_interaction.text_back_css.value)))
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_myMain_css.value).click()


# 银行借款审核
def loanCheck_bank(driver_bank):
    logger.info('银行借款审核首页')
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_homeBackStage_css.value).click()
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_LoanCheck_css.value)
    sleep(2)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_LoanCheck_css.value).click()

    logger.info('银行借款审核列表首页')
    waitUntilClick(driver_bank, path_Tripartite_interaction.btn_CheckBank_css.value)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_CheckBank_css.value).click()

    logger.info('银行审核页面')
    sleep(1)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_CheckOkReason_css.value).send_keys(
        "银行借款审核通过")
    sleep(1)
    driver_bank.find_element_by_css_selector(path_Tripartite_interaction.btn_checkOkBank_css.value).click()
    sleep(1)


# 担保公司借款审核
def loanCheck_Risk(driver_risk):
    logger.info('担保公司借款审核首页')
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_homeBackStage_css.value).click()
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_LoanCheck_css.value)
    sleep(2)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_LoanCheck_css.value).click()

    logger.info('担保公司借款审核列表首页')
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_CheckBank_css.value)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_CheckBank_css.value).click()

    logger.info('担保公司审核页面')
    waitUntilClick(driver_risk, path_Tripartite_interaction.btn_checkOkBank_css.value)
    sleep(1)
    el1 = driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_checkOkRiskMoney_css.value)
    el1.send_keys(Keys.CONTROL + 'a')
    el1.send_keys(Keys.DELETE)
    el1.send_keys('1000')
    sleep(1)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_CheckOkReasonRisk_css.value).send_keys(
        "担保公司借款审核通过")
    sleep(0.5)
    driver_risk.find_element_by_css_selector(path_Tripartite_interaction.btn_checkOkBank_css.value).click()
    is_not_visible(driver_risk, path_Tripartite_interaction.btn_CheckOkReasonRisk_css.value)
    sleep(2)


# 去缴费
def goToPay(driver_forward):
    sleep(3)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_loanApply_css.value).click()
    waitUntilClick(driver_forward, path_Tripartite_interaction.select_productQuery_css.value)
    sleep(1)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_productQuery_css.value).click()
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_goToPay_css.value)
    sleep(0.5)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_goToPay_css.value).click()
    sleep(1)
    logger.info('担保费缴费画面')
    waitUntilClick(driver_forward, path_Tripartite_interaction.btn_applyPay_css.value)
    picture_dir1 = os.getcwd() + '\\test_data\\picture\\id_1.jpg'
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.upload_payPicture_css.value).send_keys(
        picture_dir1)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_applyPay_css.value).click()
    logger.info('担保费缴费完了画面')
    waitUntilDisplay(driver_forward, path_Tripartite_interaction.txt_applyPay_css.value)
    sleep(1)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_myMain_css.value).click()


# 产品下拉框选择
def productChoose(driver_forward):
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.btn_loanApply_css.value).click()
    logger.info('进入借款检索一览画面')
    while True:
        try:
            waitUntilClick(driver_forward, path_Tripartite_interaction.select_productName_css.value)
            sleep(2)
            el = driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_productName_css.value)
            el.click()
            break
        except:
            continue
    sleep(1)
    el2 = driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_productNameList_css.value)
    scrollText(driver_forward, el2, product_name)
    driver_forward.find_element_by_css_selector(path_Tripartite_interaction.select_productQuery_css.value).click()
