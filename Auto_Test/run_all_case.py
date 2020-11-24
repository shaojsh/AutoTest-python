#!/usr/bin/python
# -*- coding: UTF-8 _*_
import time
import os
import sys
from selenium import webdriver
import androidBaseFlow
from common.Logs import Log
import pytest
from common import Shell

from common.Yaml_Data import HandleYaml

root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'
runMode = 'UI'
evn = ''
jenkins = False
try:
    jenkins = os.environ["jenkins"]
    print('jenkins Run.....')
except:
    print('本地环境测试')
# 环境run取得
driverPath = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test\\' + 'chromedriver.exe'
if not jenkins:  # 本地 获取参数
    config = HandleYaml(root_dir + '\\test_data\\config.yaml')
    runMode = config.get_data()['configEvn']['runMode']
    evn = config.get_data()['configEvn']['evn']
if jenkins:
    driverPath = '/usr/bin/chromedriver'  # 谷歌版本（linux）:78.0.3904.70
    runMode = os.environ["runMode"]
    evn = os.environ["evn"]
    RunPath = os.environ["RunPath"]

if evn == 'SIT':
    handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol-SIT.yaml')
    if jenkins:  # linux 路径表示
        handleyaml = HandleYaml('/var/lib/jenkins/workspace/AutoTest-python/Auto_Test/test_data/ConfigGol-SIT.yaml')
else:
    handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol-UAT.yaml')
    if jenkins:  # linux 路径表示
        handleyaml = HandleYaml('/var/lib/jenkins/workspace/AutoTest-python/Auto_Test/test_data/ConfigGol-UAT.yaml')

# handleyaml = HandleYaml(os.getcwd() + '\\..\\test_data\\ConfigGol-SIT.yaml')  # 调试db用

yamldict = handleyaml.get_data()

mobileDriver = ''
if runMode != 'UI':
    mobileDriver = androidBaseFlow.poco
file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger


def is_driver():
    if 'linux' in sys.platform:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 浏览器不提供可视化页面
        option.add_argument('no-sandbox')  # 以最高权限运行
        option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
        option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        # option.add_argument('--window-size=1920,1080') # 设置浏览器分辨率（窗口大小）
        driver = webdriver.Chrome(options=option, executable_path='/usr/bin/chromedriver')
        driver.get('https://www.baidu.com/')
        print('title：', driver.title)
        print('执行完毕：！！！')
    driver.quit()


if __name__ == "__main__":
    try:
        is_driver()
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime()) + "===================================")
        if not jenkins:
            root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test' + yamldict['test_path_list']['url_ui']
        else:
            root_dir = os.path.dirname(os.path.abspath('.')) + '/Auto_Test' + RunPath
        pytest.main([root_dir, "--alluredir",
                     "./report/reportallure/"])
        print("脚本执行完成")
    except Exception as e:
        # i = i + 1
        # im = ImageGrab.grab()  # 可以添加一个坐标元组进去
        # im.save(os.getcwd() + '\\test_data\\error_pic\\' + i + '.jpg')
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

    try:
        shell = Shell.Shell()
        cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/', './report//reporthtml/')
        print("开始执行报告生成")
        shell.invoke(cmd)
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        raise

    time.sleep(5)
    # mail()
