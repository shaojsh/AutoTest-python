# 财经通后台管理系统登录
from selenium import webdriver
import os

chrome_driver = os.getcwd() + '\..\chromedriver.exe'
WebDriver = webdriver.Chrome(executable_path=chrome_driver)
WebDriver.maximize_window()
WebDriver.get("http://10.10.128.152:10052/account/login?v=1596002392301")
