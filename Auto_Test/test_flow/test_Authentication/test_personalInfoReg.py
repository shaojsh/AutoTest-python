import os
import sys

from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.BaseFunction import waitUntilDisplay, waitUntilClick
from common.dbLink import deletePerInforAndComInfor, getPhoneMessage
from flow_path.path_login import loginOn
from flow_path.path_persionInfoReg import path_personalInfoReg
from run_all_uicase import yamldict, logger
from common import Assert, BaseFunction
from test_flow.test_Authentication.test_login import login

act = yamldict['test_userlist']['company_user']
pwd = yamldict['test_userlist']['company_user_pass']
url_forward = yamldict['test_path_list']['url_ui_forward']


@pytest.mark.run(order=2)
@allure.severity("blocker")
@allure.description("测试 http://10.10.128.152:10053/personal/set/certification 个人实名认证")
@allure.testcase("http://10.10.128.152:10053/personal/set/certification", "个人实名认证 👇")
def test_infoReg():
    def_name = sys._getframe().f_code.co_name
    test_Assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:\n", def_name)

    # 对个人信息企业信息进行删除操作
    deletePerInforAndComInfor()
    logger.info("对个人信息企业信息进行删除操作")

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url_forward)

    # 登陆页面
    login(driver)

    waitUntilDisplay(driver, loginOn.link_home_css.value)
    sleep(1)
    homeText = driver.find_element_by_css_selector(loginOn.link_home_css.value)

    test_Assert.assert_text_ui(homeText.text, '首页')
    logger.info("进入登陆页面")

    waitUntilDisplay(driver, path_personalInfoReg.txt_aut_css.value)
    titleText = driver.find_element_by_css_selector(path_personalInfoReg.txt_aut_css.value)
    test_Assert.assert_text_ui(titleText.text, '实名认证')
    logger.info("实名认证画面成功显示")

    name = yamldict['test_personalInfoRegList']['name']
    idNum = yamldict['test_personalInfoRegList']['id_card']

    driver.find_element_by_css_selector(path_personalInfoReg.input_name_css.value).send_keys(name)
    driver.find_element_by_css_selector(path_personalInfoReg.input_idNum_css.value).send_keys(idNum)
    BaseFunction.waitUntilClick(driver, path_personalInfoReg.btn_phoneNum_css.value)
    driver.find_element_by_css_selector(path_personalInfoReg.btn_phoneNum_css.value).click()

    while 1:
        message = getPhoneMessage().get("auMes")
        if message is None:
            sleep(0.5)
            continue
        else:
            break
    driver.find_element_by_css_selector(path_personalInfoReg.input_phoneNum_css.value).send_keys(
        message.strip().strip('"'))

    picture_dir = os.getcwd()
    pcture_dirOne = '\\test_data\\picture\\id_1.jpg'
    pcture_dirTwo = '\\test_data\\picture\\id_2.jpg'
    driver.find_element_by_css_selector(path_personalInfoReg.file_idPicture1_css.value).send_keys(
        picture_dir + pcture_dirOne)
    BaseFunction.waitUntilDisplay(driver, path_personalInfoReg.btn_uplaodPicture1_css.value)
    driver.find_element_by_css_selector(path_personalInfoReg.file_idPicture2_css.value).send_keys(
        picture_dir + pcture_dirTwo)
    BaseFunction.waitUntilDisplay(driver, path_personalInfoReg.btn_uplaodPicture2_css.value)
    waitUntilClick(driver, path_personalInfoReg.btn_aut_css.value)
    sleep(1)
    driver.find_element_by_css_selector(path_personalInfoReg.btn_aut_css.value).click()

    BaseFunction.waitUntilDisplay(driver, path_personalInfoReg.txt_auting_css.value)
    text_auting = driver.find_element_by_css_selector(path_personalInfoReg.txt_auting_css.value).text
    test_Assert.assert_text_ui(text_auting, '认证中')
    logger.info("实名认证中画面显示")

    text_name_css = driver.find_element_by_css_selector(path_personalInfoReg.txt_name_css.value).text
    txt_idNum_css = driver.find_element_by_css_selector(path_personalInfoReg.txt_idNum_css.value).text
    text_phoneNum_css = driver.find_element_by_css_selector(path_personalInfoReg.txt_phoneNum_css.value).text

    test_Assert.assert_text_ui(text_name_css, name)
    test_Assert.assert_text_ui(txt_idNum_css, idNum)
    test_Assert.assert_text_ui(text_phoneNum_css, act)

    WebDriverWait(driver, 1200).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, path_personalInfoReg.txt_actSucess_css.value)))
    text_actSucess = driver.find_element_by_css_selector(path_personalInfoReg.txt_actSucess_css.value).text
    test_Assert.assert_text_ui(text_actSucess, "认证成功")
    logger.info("实名认证成功画面显示")

    driver.find_element_by_css_selector(path_personalInfoReg.btn_actInfor_css.value).click()
    titleText = driver.find_element_by_css_selector(path_personalInfoReg.txt_aut_css.value)
    test_Assert.assert_text_ui(titleText.text, '实名认证')
    logger.info("点击查看认证信息按钮，跳转到实名认证画面")

    driver.quit()
