#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('.')
__author__ = 'shaojunshuai'

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import subprocess

try:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    print(poco.adb_client.get_device_info())  # 获取设备信息
except:
    print('手机未驱动')

auto_setup(__file__)


# 打开微信
def startWeinxin():
    # 打开微信
    start_app("com.tencent.mm")
    poco(text='发现').click()  # 发现按钮
    poco(text="小程序").click()
    # poco(text="我的小程序").click()
    poco(text="诚泰财金通").click()


def getDevices():
    order = 'adb devices'
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    print(pi.stdout.read())


if __name__ == '__main__':
    startWeinxin()
