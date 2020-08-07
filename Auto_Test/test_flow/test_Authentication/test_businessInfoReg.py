import os
import sys
from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.BaseFunction import waitUntilDisplay, waitUntilClick, waitUntilClick_xpath
from flow_path.path_businessInfoReg import path_businessInfoReg
from run_all_uicase import yamldict, logger
from common import Assert
from test_flow.test_Authentication.test_login import login

act = yamldict['test_userlist']['company_user']
pwd = yamldict['test_userlist']['company_user_pass']


@pytest.mark.run(order=3)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/personal/baseinfo 企业认证")
@allure.testcase("http://10.10.128.152:10053/personal/baseinfo", "企业认证 👇")
def test_businessInforReg():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://10.10.128.152:10053/user/login")

    # 登陆页面
    login(driver)
    waitUntilDisplay(driver, path_businessInfoReg.txt_aut_css.value)
    txt_auTitle = driver.find_element_by_css_selector(path_businessInfoReg.txt_aut_css.value).text
    test_Assert.assert_text_ui(txt_auTitle, '企业基本资料')
    logger.info("企业基本资料画面正常显示")

    # 企业证件
    driver.find_element_by_css_selector(path_businessInfoReg.input_companyName_css.value).send_keys("诚泰科技-test")
    driver.find_element_by_css_selector(path_businessInfoReg.input_companyCode_css.value).send_keys(
        "92520628MA6FK07055")
    driver.find_element_by_css_selector(path_businessInfoReg.input_legalPersonName_css.value).send_keys("黄小明")
    driver.find_element_by_css_selector(path_businessInfoReg.input_legalPersonCardNo_css.value).send_keys(
        "110101199003077096")
    driver.find_element_by_css_selector(path_businessInfoReg.input_legalPersonAddress_css.value).send_keys(
        "上海市浦东新区陆家嘴金砖大厦")
    driver.find_element_by_css_selector(path_businessInfoReg.input_legalPersonPostCode_css.value).send_keys("200120")
    driver.find_element_by_css_selector(path_businessInfoReg.input_legalPersonIndustry_css.value).send_keys("金融")

    picture_dir = os.getcwd() + '\\test_data\\picture\\id_3.jpg'
    driver.find_element_by_css_selector(path_businessInfoReg.upload_legalPersonCertificate_css.value).send_keys(
        picture_dir)

    driver.find_element_by_css_selector(path_businessInfoReg.upload_legalPersonBankNo_css.value).send_keys(
        "6217996620000156427")

    driver.find_element_by_css_selector(path_businessInfoReg.sel_bankName_css.value).click()
    driver.find_elements_by_xpath("//*[text() = '中国邮政储蓄银行']")[0].click()

    sleep(1)
    # 法定代表人信息
    driver.find_element_by_css_selector(path_businessInfoReg.sel_country_css.value).click()
    driver.find_elements_by_xpath("//*[text() = '中国境内']")[0].click()

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
    waitUntilClick_xpath(driver, path_businessInfoReg.checkBox_agree_xpath.value)
    driver.find_element_by_xpath(path_businessInfoReg.checkBox_agree_xpath.value).click()
    sleep(1)
    driver.find_element_by_css_selector(path_businessInfoReg.btn_Certification_css.value).click()

    waitUntilDisplay(driver, path_businessInfoReg.text_atMid_css.value)
    txt_middleAuTitle = driver.find_element_by_css_selector(path_businessInfoReg.text_atMid_css.value).text
    test_Assert.assert_text_ui(txt_middleAuTitle, '认证中')
    logger.info("企业信息认证中画面正常显示")

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, path_businessInfoReg.text_bank_css.value)))

    driver.find_element_by_css_selector(path_businessInfoReg.input_moneyNum_css.value).send_keys('0.5')
    driver.find_element_by_css_selector(path_businessInfoReg.btn_middleCnf_css.value).click()

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


