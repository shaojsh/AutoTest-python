#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('.')
__author__ = 'shaojunshuai'

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

try:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
except:
    print('未驱动手机')


# 打开微信
def startWeinxin():
    # 打开微信
    start_app("com.tencent.mm")
    poco(text='发现').click()  # 发现按钮
    poco(text="小程序").click()
    poco(text="诚泰财金通").click()


if __name__ == '__main__':
    startWeinxin()
