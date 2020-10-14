# 等待元素出现
from time import sleep
import threading
import time

from poco.exceptions import PocoTargetTimeout
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image
import pytesseract

# 等待直到元素出现
from run_all_case import mobileDriver


def waitUntilDisplay(driver, ByCss):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ByCss)))


# 等待直到元素出现
def waitUntilDisplay_xpath(driver, ByCss):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, ByCss)))


# 等待直到元素可点击
def waitUntilClick(driver, ByCss):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ByCss)))


# 一直等待某个元素消失，默认超时10秒
def is_not_visible(driver, locator, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return True
    except TimeoutException:
        return False


# 等待直到元素可点击
def waitUntilClick_xpath(driver, ByXpath):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ByXpath)))


# 元素需要移动到相应地点才能点击
def actionChainsClick(driver, element):
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()


# 滑轮滚动
def scrollText(driver, element, text):
    while 1:
        try:
            sleep(0.5)
            xpath = "//*[text() =\'" + text + "\']"
            driver.find_element_by_xpath(xpath).click()
            break
        except:
            driver.execute_script("arguments[0].scrollIntoView(false);", element)
            continue


# n秒内持续调用某方法（每秒调用一次 :回调函数）
# def fun_timer():
#     global timer
#     timer = threading.Timer(5.5, fun_timer)
#     timer.start()
#
#
# timer = threading.Timer(1, fun_timer)
# timer.start()
#
# time.sleep(15)  # 15秒后停止定时器
# timer.cancel()

# 验证码识别（爬虫/UI自动化用 OCR识别，需要自己下载语言包支持）
def getVerCode(imagePath):
    captcha = Image.open(imagePath)
    code = pytesseract.image_to_string(captcha)
    print(code)
    return code


# 移动端 等待元素出现并点击
def waiteForClick(el):
    while True:
        try:
            sleep(0.1)
            el.wait_for_appearance(timeout=0.1)
            el.click()
            break
        except:
            sleep(0.1)
            continue


# 移动端 等待直到元素消失
def waiteForNotExist(text):
    while True:
        el = mobileDriver(text=text)
        if el.attr('visible'):
            sleep(0.5)
            continue
        else:
            break
