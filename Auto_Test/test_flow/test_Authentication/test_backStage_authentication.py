import os
import sys
from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from common.BaseFunction import actionChainsClick, waitUntilClick, scrollText, waitUntilClick_xpath
from common.dbLink import getPhoneMessage, deleteOrgInfor, getVerification, flushDb
from flow_path.path_Tripartite_interaction import path_Tripartite_interaction
from flow_path.path_backStage_authentication import path_backStage_authentication
from run_all_case import yamldict, logger
from test_flow.test_Authentication.test_backStage_examine import backStageLogin
from test_flow.test_Authentication.test_login import companyPassForget
from selenium.webdriver.support import expected_conditions as EC

act = yamldict['test_backStageUserList']['company_user']
pwd = yamldict['test_backStageUserList']['company_user_pass']
delete_flag = yamldict['test_path_list']['delete_flag']
# 银行
autoTest_BankName = yamldict['test_backStageUserList']['autoTest_BankName']
company_bank = yamldict['test_backStageUserList']['company_bank']
company_bank_pass = yamldict['test_backStageUserList']['company_bank_pass']
product_name = yamldict['test_backStageUserList']['product_name']
# 担保公司
autoTest_RiskName = yamldict['test_backStageUserList']['autoTest_RiskName']
company_Guarantee = yamldict['test_backStageUserList']['company_Guarantee']
company_Guarantee_pass = yamldict['test_backStageUserList']['company_Guarantee_pass']
url_back = yamldict['test_path_list']['url_ui_back']
RequestURL = yamldict['test_redisdb_list']['RequestURL']
# 产品属性
rend_rule = yamldict['test_backStageUserList']['rend_rule']
rend_day = yamldict['test_backStageUserList']['rend_day']


# 创建金融产品
def createProduct(driver):
    waitUntilClick(driver, path_Tripartite_interaction.btn_homeBackStage_css.value)
    sleep(2)
    driver.find_element_by_css_selector(path_Tripartite_interaction.btn_homeBackStage_css.value).click()
    logger.info('首页')
    sleep(1)
    driver.find_elements_by_xpath(path_backStage_authentication.btn_goodList_xpath.value)[0].click()
    sleep(1)
    logger.info('产品基本信息')
    driver.find_element_by_css_selector(path_backStage_authentication.btn_goodAdd_css.value).click()
    waitUntilClick(driver, path_backStage_authentication.choose_goodType_css.value)

    driver.find_element_by_css_selector(path_backStage_authentication.choose_goodType_css.value).click()
    el1 = driver.find_element_by_css_selector(path_backStage_authentication.choose_goodType_css.value)
    scrollText(driver, el1, '财金通')

    driver.find_element_by_css_selector(path_backStage_authentication.input_goodName_css.value).send_keys(product_name)

    driver.find_element_by_css_selector(path_backStage_authentication.cal_okTime.value).click()
    el2 = driver.find_element_by_css_selector(path_backStage_authentication.input_cal_css.value)
    el2.send_keys(Keys.ENTER)

    driver.find_element_by_css_selector(path_backStage_authentication.choose_goodStatus_css.value).click()
    el3 = driver.find_element_by_css_selector(path_backStage_authentication.choose_goodStatus_css.value)
    scrollText(driver, el3, '启用')

    el4 = driver.find_element_by_css_selector(path_backStage_authentication.input_loanMin_css.value)
    el4.send_keys(Keys.CONTROL + 'a')
    el4.send_keys(Keys.DELETE)
    el4.send_keys('1')

    el5 = driver.find_element_by_css_selector(path_backStage_authentication.input_loanMax_css.value)
    el5.send_keys(Keys.CONTROL + 'a')
    el5.send_keys(Keys.DELETE)
    el5.send_keys('1000000')

    driver.find_element_by_css_selector(path_backStage_authentication.choose_loanGetWay_css.value).click()
    el6 = driver.find_element_by_css_selector(path_backStage_authentication.choose_loanGetWay_css.value)
    scrollText(driver, el6, '先交费后放款')

    driver.find_element_by_css_selector(path_backStage_authentication.choose_rendItem_css.value).click()
    el7 = driver.find_element_by_css_selector(path_backStage_authentication.choose_rendItem_css.value)
    scrollText(driver, el7, '按日')

    if rend_rule == 1:
        rule = '算头算尾'
    elif rend_rule == 2:
        rule = '算头不算尾'
    elif rend_rule == 3:
        rule = '算尾不算头'
    if rend_day == 1:
        day = '360天'
    elif rend_day == 2:
        day = '365天'

    driver.find_element_by_css_selector(path_backStage_authentication.choose_rendDay_css.value).click()
    el8 = driver.find_element_by_css_selector(path_backStage_authentication.choose_rendDay_css.value)
    scrollText(driver, el8, day)

    driver.find_element_by_css_selector(path_backStage_authentication.choose_rendWay_css.value).click()
    el9 = driver.find_element_by_css_selector(path_backStage_authentication.choose_rendWay_css.value)
    scrollText(driver, el9, rule)

    el10 = driver.find_element_by_css_selector(path_backStage_authentication.input_productMon_css.value)
    el10.send_keys(Keys.CONTROL + 'a')
    el10.send_keys(Keys.DELETE)
    el10.send_keys('13')

    driver.find_element_by_css_selector(path_backStage_authentication.choose_giveMoneyWay_css.value).click()
    el11 = driver.find_element_by_css_selector(path_backStage_authentication.choose_giveMoneyWay_css.value)
    scrollText(driver, el11, '随借随还')

    el12 = driver.find_element_by_css_selector(path_backStage_authentication.input_presentYearMin_css.value)
    el12.send_keys(Keys.CONTROL + 'a')
    el12.send_keys(Keys.DELETE)
    el12.send_keys('1')

    el13 = driver.find_element_by_css_selector(path_backStage_authentication.input_presentYearMax_css.value)
    el13.send_keys(Keys.CONTROL + 'a')
    el13.send_keys(Keys.DELETE)
    el13.send_keys('15')

    picture_dir1 = os.getcwd() + '\\test_data\\picture\\id_1.jpg'
    picture_dir2 = os.getcwd() + '\\test_data\\picture\\id_2.jpg'
    driver.find_element_by_css_selector(path_backStage_authentication.upload_pic4_css.value).send_keys(
        picture_dir1)
    driver.find_element_by_css_selector(path_backStage_authentication.upload_pic5_css.value).send_keys(
        picture_dir2)

    driver.find_element_by_css_selector(path_backStage_authentication.choose_risk_css.value).click()
    el14 = driver.find_element_by_css_selector(path_backStage_authentication.choose_risk_css.value)
    scrollText(driver, el14, autoTest_RiskName)

    driver.find_element_by_css_selector(path_backStage_authentication.input_area_css.value).send_keys('该产品价格实惠公道')
    driver.find_element_by_css_selector(path_backStage_authentication.btn_next1_css.value).click()
    logger.info('产品特性')
    waitUntilClick(driver, path_backStage_authentication.btn_add_css.value)
    sleep(0.5)
    driver.find_element_by_css_selector(path_backStage_authentication.btn_add_css.value).click()
    sleep(0.5)
    driver.find_element_by_css_selector(path_backStage_authentication.input_characteristicName_css.value).send_keys(
        '利率低')
    driver.find_element_by_css_selector(path_backStage_authentication.input_characteristicDes_css.value).send_keys(
        '利率低,很nice的产品')

    driver.find_element_by_css_selector(path_backStage_authentication.btn_save_css.value).click()
    waitUntilClick_xpath(driver, path_backStage_authentication.btn_next2_xpath.value)
    sleep(0.5)
    driver.find_element_by_xpath(path_backStage_authentication.btn_next2_xpath.value).click()

    logger.info('计分卡')
    waitUntilClick_xpath(driver, path_backStage_authentication.btn_next3_xpath.value)
    sleep(0.5)
    driver.find_element_by_xpath(path_backStage_authentication.btn_next3_xpath.value).click()

    waitUntilClick(driver, path_backStage_authentication.check_content_css.value)
    sleep(0.5)
    logger.info('进件信息')
    driver.find_element_by_css_selector(path_backStage_authentication.check_content_css.value).click()
    driver.find_element_by_css_selector(path_backStage_authentication.btn_submit_css.value).click()
    sleep(1)


@pytest.mark.run(order=5)
@allure.severity("blocker")
@allure.description("http://10.10.128.152:10052/#/authority/mechanism 后台机构创建")
@allure.testcase("http://10.10.128.152:10052/#/authority/mechanism", "后台机构创建 👇")
def test_backStageActCreate():
    def_name = sys._getframe().f_code.co_name
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_back)

    # 登陆页面
    backStageLogin(driver, act, pwd, 0)
    if delete_flag == 0:
        deleteOrgInfor()
        logger.info('机构信息DB删除')
    sleep(2)
    driver.find_element_by_xpath(path_backStage_authentication.btn_jurisdiction_xpath.value).click()
    sleep(1)
    el = driver.find_element_by_xpath(path_backStage_authentication.btn_mechanism_xpath.value)
    actionChainsClick(driver, el)

    waitUntilClick(driver, path_backStage_authentication.btn_addMechanism_css.value)

    # 创建担保公司机构
    createInstitutions(driver, autoTest_RiskName, 0)
    # 创建银行机构
    createInstitutions(driver, autoTest_BankName, 1)
    # 创建担保公司账号
    createAct(driver, company_Guarantee, autoTest_RiskName, 0)
    # 创建银行账号
    createAct(driver, company_bank, autoTest_BankName, 1)
    driver.quit()


# 机构认证
def authentication(driver, Type):
    if Type == 1:
        backStageLogin(driver, company_bank, company_bank_pass, 1)
    else:
        backStageLogin(driver, company_Guarantee, company_Guarantee_pass, 1)
    sleep(3)
    flushDb()
    driver.find_element_by_css_selector(path_backStage_authentication.btn_codeAu_css.value).click()
    while 1:
        if Type == 1:
            message = getPhoneMessage().get("AuBank")
        else:
            message = getPhoneMessage().get("AuRisk")
        if message is None:
            sleep(1)
            continue
        else:
            break
    message = message.strip().strip('"')
    driver.find_element_by_css_selector(path_backStage_authentication.input_codeAu_css.value).send_keys(message)
    picture_dir1 = os.getcwd() + '\\test_data\\picture\\id_1.jpg'
    picture_dir2 = os.getcwd() + '\\test_data\\picture\\id_2.jpg'
    picture_dir3 = os.getcwd() + '\\test_data\\picture\\id_3.jpg'
    driver.find_element_by_css_selector(path_backStage_authentication.upload_pic1_css.value).send_keys(
        picture_dir1)
    driver.find_element_by_css_selector(path_backStage_authentication.upload_pic2_css.value).send_keys(
        picture_dir2)

    driver.find_element_by_css_selector(path_backStage_authentication.btn_submitAu_css.value).click()
    sleep(1)

    # 企业信息认证
    logger.info('企业信息认证')
    waitUntilClick(driver, path_backStage_authentication.btn_goToAu_css.value)
    sleep(1)
    driver.find_element_by_css_selector(path_backStage_authentication.input_soCode_css.value).send_keys(
        '515328000000000510')
    driver.find_element_by_css_selector(path_backStage_authentication.input_layName_css.value).send_keys('黄晓明')
    driver.find_element_by_css_selector(path_backStage_authentication.input_IdCardLay_css.value).send_keys(
        '110101199003077774')
    sleep(1)
    driver.find_element_by_css_selector(path_backStage_authentication.input_addressLay_css.value).send_keys('陆家嘴金砖大厦')
    driver.find_element_by_css_selector(path_backStage_authentication.input_postLay_css.value).send_keys('220000')

    driver.find_element_by_css_selector(path_backStage_authentication.upload_pic3_css.value).send_keys(
        picture_dir3)

    driver.find_element_by_css_selector(path_backStage_authentication.btn_goToAu_css.value).click()

    logger.info('协议内容确认页面')
    waitUntilClick(driver, path_backStage_authentication.checkBox_agree_css.value)
    sleep(1.5)
    driver.find_element_by_css_selector(path_backStage_authentication.checkBox_agree_css.value).click()
    sleep(0.5)
    driver.find_element_by_css_selector(path_backStage_authentication.btn_startAu_css.value).click()
    if Type == 0:
        # 活体认证欺诈性校验(担保公司)
        getVerification(RequestURL, company_Guarantee)
    else:
        # 活体认证欺诈性校验（银行）
        getVerification(RequestURL, company_bank)
    logger.info('二维码认证页面')
    WebDriverWait(driver, 1200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, path_backStage_authentication.text_au_css.value)))
    if Type == 0:
        driver.quit()


@pytest.mark.run(order=6)
@allure.severity("blocker")
@allure.description("http://10.10.128.152:10052/#/authority/mechanism 后台账户认证")
@allure.testcase("http://10.10.128.152:10052/#/authority/mechanism", "后台账户认证 👇")
def test_backStage_authentication():
    def_name = sys._getframe().f_code.co_name
    logger.info("开始执行脚本%s:\n", def_name)

    def_name = sys._getframe().f_code.co_name
    logger.info("开始执行脚本%s:\n", def_name)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_back)
    # 银行密码修改
    companyPassForget(driver, company_bank, 1)
    # 担保公司密码修改
    companyPassForget(driver, company_Guarantee, 0)
    # 银行认证
    authentication(driver, 0)

    driver_bank = webdriver.Chrome()
    driver_bank.maximize_window()
    driver_bank.get(url_back)
    authentication(driver_bank, 1)
    # 创建产品
    createProduct(driver_bank)
    # backStageLogin(driver, company_bank, company_bank_pass, 0)
    # createProduct(driver)
    driver_bank.quit()


# 创建机构
def createInstitutions(driver, name, enterpriseType):
    sleep(1)
    driver.find_element_by_css_selector(path_backStage_authentication.btn_addMechanism_css.value).click()
    driver.find_element_by_css_selector(path_backStage_authentication.input_MechanismName_css.value).send_keys(
        name)
    driver.find_element_by_css_selector(path_backStage_authentication.input_MechanismSimName_css.value).send_keys(name)

    driver.find_element_by_css_selector(path_backStage_authentication.select_MechanismType_css.value).click()
    sleep(1)
    if enterpriseType == 1:
        driver.find_element_by_xpath(path_backStage_authentication.select_BankType_xpath.value).click()
    else:
        driver.find_element_by_xpath(path_backStage_authentication.select_RiskType_xpath.value).click()
    sleep(0.5)
    driver.find_element_by_css_selector(path_backStage_authentication.select_MechanismStatue_css.value).click()
    sleep(1)
    driver.find_element_by_xpath(path_backStage_authentication.select_StatueType_xpath.value).click()
    sleep(0.5)
    if enterpriseType == 1:
        # 添加银行账户
        driver.find_element_by_css_selector(path_backStage_authentication.select_bankAct_css.value).click()
        sleep(1)
        driver.find_element_by_xpath(path_backStage_authentication.select_bankAct_xpath.value).click()
        sleep(0.5)
    driver.find_element_by_css_selector(path_backStage_authentication.btn_confirm_css.value).click()
    sleep(1)


# 创建账号
def createAct(driver, account, name, enterpriseType):
    xpath = "//*[@id='root']/section/section/main/div/div/div/div[2]/table/tbody//*[text() = \'" + name + "\']/..//*[text()= '创建账号']"
    driver.find_element_by_xpath(xpath).click()
    sleep(1)
    if enterpriseType == 1:
        logger.info("进入银行账户创建页面")
    else:
        logger.info("进入担保公司创建页面")
    driver.find_element_by_css_selector(path_backStage_authentication.input_ActName_css.value).send_keys(name)
    driver.find_element_by_css_selector(path_backStage_authentication.input_PhoneNum_css.value).send_keys(account)
    driver.find_element_by_css_selector(path_backStage_authentication.input_Email_css.value).send_keys(
        "110101199003078371")
    # IdCard = random.randint(0, 99999999999999)
    # driver.find_element_by_css_selector(path_backStage_authentication.input_Id_Card_css.value).send_keys(
    #     '110101199003078371')
    driver.find_element_by_css_selector(path_backStage_authentication.btn_ActConfirm_css.value).click()
    sleep(2)
