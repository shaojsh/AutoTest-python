#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('.')
__author__ = 'shaojunshuai'

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import subprocess

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
print(poco.adb_client.get_device_info())  # 获取设备信息


# 打开微信
def startWeinxin():
    # 打开微信
    start_app("com.tencent.mm")


def getDevices():
    order = 'adb devices'
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    print(pi.stdout.read())


if __name__ == '__main__':
    startWeinxin()
