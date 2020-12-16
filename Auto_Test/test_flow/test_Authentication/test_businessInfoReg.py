import os
import sys
from time import sleep
import random
import allure
import pytest
from airtest.core.api import text
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.BaseFunction import waitUntilDisplay, waitUntilClick, waitUntilClick_xpath, waitUntilDisplay_xpath, \
    waiteForClick
from common.dbLink import getVerification, updateNameCompany, getVerification_ui
from flow_path.path_businessInfoReg import path_businessInfoReg
from run_all_case import yamldict, logger, runMode, mobileDriver, driverPath, jenkins
from common import Assert
from test_flow.test_Authentication.test_login import login
from selenium.webdriver.common.keys import Keys

act = yamldict['test_userlist']['company_user']
pwd = yamldict['test_userlist']['company_user_pass']
businessName = yamldict['test_backStageUserList']['company_name']
url_forward = yamldict['test_path_list']['url_ui_forward']
RequestURL = yamldict['test_redisdb_list']['RequestURL']
idNum = yamldict['test_personalInfoRegList']['id_card']


@pytest.mark.run(order=3)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/personal/baseinfo 企业认证")
@allure.testcase("http://10.10.128.152:10053/personal/baseinfo", "企业认证 👇")
def test_businessInforReg():
    if runMode == 'UI':
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
        driver.get(url_forward)

        # 登陆页面
        login(driver)
        waitUntilDisplay(driver, path_businessInfoReg.txt_aut_css.value)
        txt_auTitle = driver.find_element_by_css_selector(path_businessInfoReg.txt_aut_css.value).text
        test_Assert.assert_text_ui(txt_auTitle, '企业基本资料')
        logger.info("企业基本资料画面正常显示")

        # 企业证件
        el = driver.find_element_by_css_selector(path_businessInfoReg.input_companyName_css.value)
        el.send_keys('诚泰融资租赁（上海）有限公司')
        waitUntilDisplay_xpath(driver, path_businessInfoReg.display_name_xpath.value)
        el.send_keys(Keys.ENTER)
        sleep(1)

        driver.find_element_by_css_selector(path_businessInfoReg.input_legalIdCard_css.value).send_keys(
            idNum)

        driver.find_element_by_css_selector(path_businessInfoReg.input_legalPhone_css.value).send_keys(
            "17621198933")

        while True:
            try:
                driver.find_element_by_css_selector(path_businessInfoReg.sel_province_css.value).click()
                sleep(0.5)
                driver.find_element_by_xpath("//*[text() = '河北省']").click()
                break
            except:
                continue
        sleep(0.5)

        while True:
            try:
                driver.find_element_by_css_selector(path_businessInfoReg.sel_city_css.value).click()
                sleep(0.5)
                driver.find_element_by_xpath("//*[text() = '邯郸市']").click()
                break
            except:
                continue
        sleep(0.5)

        while True:
            try:
                driver.find_element_by_css_selector(path_businessInfoReg.sel_area_css.value).click()
                sleep(0.5)
                driver.find_element_by_xpath("//*[text() = '复兴区']").click()
                break
            except:
                continue
        sleep(1)
        driver.find_element_by_css_selector(path_businessInfoReg.input_contractAddress_css.value).send_keys(
            "金砖大厦10楼")

        driver.find_element_by_css_selector(path_businessInfoReg.input_legalPersonPostCode_css.value).send_keys(
            "200120")

        picture_dir = os.getcwd() + '\\test_data\\picture\\id_3.jpg'
        driver.find_element_by_css_selector(path_businessInfoReg.upload_legalPersonCertificate_css.value).send_keys(
            picture_dir)
        # 生成随机银行号码
        bankNO = random.randint(0, 99999999999999)
        driver.find_element_by_css_selector(path_businessInfoReg.upload_legalPersonBankNo_css.value).send_keys(
            str(bankNO))
        sleep(0.5)
        while True:
            try:
                driver.find_element_by_css_selector(path_businessInfoReg.sel_bankName_css.value).click()
                sleep(0.5)
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/div[1]/div/div/div[3]").click()
                break
            except:
                continue
        sleep(0.5)
        while True:
            try:
                # 法定代表人信息
                driver.find_element_by_css_selector(path_businessInfoReg.sel_country_css.value).click()
                sleep(1)
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[2]/div[1]/div/div/div[2]").click()
                break
            except:
                continue

        sleep(0.5)
        picture_dir2 = os.getcwd() + '\\test_data\\picture\\id_1.jpg'
        picture_dir3 = os.getcwd() + '\\test_data\\picture\\id_2.jpg'
        picture_dir4 = os.getcwd() + '\\test_data\\picture\\id_4.jpg'

        driver.find_element_by_css_selector(path_businessInfoReg.sel_idCard1_css.value).send_keys(
            picture_dir2)
        driver.find_element_by_css_selector(path_businessInfoReg.sel_idCard2_css.value).send_keys(
            picture_dir3)

        # 实际控制人信息
        sleep(1)
        driver.find_element_by_css_selector(path_businessInfoReg.radio_controlPerson_css.value).click()
        driver.find_element_by_css_selector(path_businessInfoReg.upload_controlPersonId1_css.value).send_keys(
            picture_dir2)
        driver.find_element_by_css_selector(path_businessInfoReg.upload_controlPersonId2_css.value).send_keys(
            picture_dir3)
        driver.find_element_by_css_selector(path_businessInfoReg.upload_controlPersonFamPic_css.value).send_keys(
            picture_dir4)
        sleep(1)
        driver.find_element_by_css_selector(path_businessInfoReg.radio_legalPerson_css.value).click()
        waitUntilClick(driver, path_businessInfoReg.bth_submit_css.value)
        driver.find_element_by_css_selector(path_businessInfoReg.bth_submit_css.value).click()

        waitUntilDisplay(driver, path_businessInfoReg.text_atCof_css.value)
        txt_startAuTitle = driver.find_element_by_css_selector(path_businessInfoReg.text_atCof_css.value).text
        test_Assert.assert_text_ui(txt_startAuTitle, '请确认协议内容')
        logger.info("协议确认画面正常显示")
        waitUntilClick_xpath(driver, '//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/div[1]/div/button')
        sleep(2)
        driver.find_element_by_xpath(path_businessInfoReg.checkBox_agree_xpath.value).click()
        waitUntilClick(driver, path_businessInfoReg.btn_Certification_css.value)
        driver.find_element_by_css_selector(path_businessInfoReg.btn_Certification_css.value).click()

        waitUntilDisplay(driver, path_businessInfoReg.text_atMid_css.value)
        txt_middleAuTitle = driver.find_element_by_css_selector(path_businessInfoReg.text_atMid_css.value).text
        test_Assert.assert_text_ui(txt_middleAuTitle, '认证中')
        logger.info("企业信息认证中画面正常显示")

        # 活体认证欺诈性校验
        getVerification_ui(RequestURL, act)

        WebDriverWait(driver, 1200).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, path_businessInfoReg.text_bank_css.value)))

        driver.find_element_by_css_selector(path_businessInfoReg.input_moneyNum_css.value).send_keys('0.5')
        driver.find_element_by_css_selector(path_businessInfoReg.btn_middleCnf_css.value).click()
        sleep(3)
        waitUntilDisplay(driver, path_businessInfoReg.txt_examine_css.value)
        txt_examineAuTitle = driver.find_element_by_css_selector(path_businessInfoReg.txt_examine_css.value).text
        test_Assert.assert_text_ui(txt_examineAuTitle, '审核中')
        logger.info("企业信息审核中画面正常显示")
        driver.find_element_by_css_selector(path_businessInfoReg.btn_primary_css.value).click()

        # 登陆页面
        waitUntilDisplay(driver, path_businessInfoReg.txt_aut_css.value)
        txt_auTitle = driver.find_element_by_css_selector(path_businessInfoReg.txt_aut_css.value).text
        test_Assert.assert_text_ui(txt_auTitle, '企业基本资料')
        logger.info("企业基本资料画面正常显示")
        driver.quit()
    else:
        logger.info('企业认证画面')
        waiteForClick(mobileDriver(text='我的'))
        waiteForClick(mobileDriver(text='企业认证'))
        sleep(1)
        waiteForClick(mobileDriver(text='*上传营业执照').parent().child()[2].child())
        waiteForClick(mobileDriver(text='所有图片'))
        waiteForClick(mobileDriver(text='自动化测试专用相册'))
        mobileDriver("android.widget.LinearLayout").offspring("com.tencent.mm:id/dm6").child("com.tencent.mm:id/f4b")[
            1].child(
            "com.tencent.mm:id/dm8").click()
        waiteForClick(mobileDriver(text='完成'))
        sleep(2)
        waiteForClick(mobileDriver(text='*邮政编码').parent().child()[2])
        text("123456")
        mobileDriver(text='*邮政编码').click()
        mobileDriver(text='法人代表证件').drag_to(mobileDriver(text='企业证件照'), 0.5)
        waiteForClick(mobileDriver(text='*我是').parent().child()[2].child().child())
        waiteForClick(mobileDriver(text='*法人代表归属地').parent().child()[2].child())
        waiteForClick(mobileDriver(text='中国境内'))
        sleep(2)
        waiteForClick(mobileDriver(text='*实控人身份').parent().child()[2].child().child())

        waiteForClick(mobileDriver(text='*实控人户口本主页').parent().child()[2].child())
        waiteForClick(mobileDriver(text='所有图片'))
        waiteForClick(mobileDriver(text='自动化测试专用相册'))
        mobileDriver("android.widget.LinearLayout").offspring("com.tencent.mm:id/dm6").child("com.tencent.mm:id/f4b")[
            0].child(
            "com.tencent.mm:id/dm8").click()
        waiteForClick(mobileDriver(text='完成'))
        sleep(2)
        waiteForClick(mobileDriver(text='*实控人婚姻状况').parent().child()[2].child().child()[1])
        waiteForClick(mobileDriver(text='*对公银行账号').parent().child()[2])
        bankNO = random.randint(0, 99999999999999)
        text(str(bankNO))
        mobileDriver(text='*对公银行账号').click()
        waiteForClick(mobileDriver(text='*对公开户银行').parent().child()[2].child().child())
        waiteForClick(mobileDriver(text='鞍山银行'))

        waiteForClick(mobileDriver(text='下一步'))
        logger.info('平台服务协议画面')
        waiteForClick(mobileDriver(text='我已阅读并同意'))
        waiteForClick(mobileDriver(text='请输入打款金额'))
        text('0.1')
        waiteForClick(mobileDriver(text='收到的金额'))
        waiteForClick(mobileDriver(text='确认提交'))
        sleep(3)
        waiteForClick(mobileDriver(name='com.tencent.mm:id/dc'))
        # 更改企业名称
        updateNameCompany()
