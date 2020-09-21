#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('.')
__author__ = '1084502012@qq.com'

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)

print(poco.adb_client.get_device_info()) # 获取设备信息