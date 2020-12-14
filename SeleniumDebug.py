# selenium 调试方法：https://www.cnblogs.com/easy-test/p/13275684.html
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common import BaseFunction
os.system('chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium\chrome_temp"')
from flow_path.path_persionInfoReg import path_personalInfoReg

sleep(1)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(chrome_options=chrome_options)


def debugSelenium():
    picture_dir = os.getcwd()
    pcture_dirOne = '\\test_data\\picture\\id_1.jpg'
    pcture_dirTwo = '\\test_data\\picture\\id_2.jpg'
    driver.find_element_by_css_selector(path_personalInfoReg.file_idPicture1_css.value).send_keys(
        picture_dir + pcture_dirOne)
    BaseFunction.waitUntilDisplay(driver, path_personalInfoReg.btn_uplaodPicture1_css.value)
    driver.find_element_by_css_selector(path_personalInfoReg.file_idPicture2_css.value).send_keys(
        picture_dir + pcture_dirTwo)
    BaseFunction.waitUntilDisplay(driver, path_personalInfoReg.btn_uplaodPicture2_css.value)


if __name__ == "__main__":
    debugSelenium()
