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
    poco("com.tencent.mm:id/czk").offspring("com.tencent.mm:id/czl").child("android.widget.LinearLayout").child(
        "android.widget.RelativeLayout")[0].child("com.tencent.mm:id/cn_").offspring("com.tencent.mm:id/cnh").click()  # 点击【微信】按钮
    poco("com.tencent.mm:id/f8y").click()
    poco(text="小程序").click()
    text("财金通")


def getDevices():
    order = 'adb devices'
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
    print(pi.stdout.read())


if __name__ == '__main__':
    startWeinxin()
