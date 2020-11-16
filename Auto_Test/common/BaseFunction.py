# 等待元素出现
import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from aip import AipOcr

# 等待直到元素出现
from run_all_case import mobileDriver
from faker.factory import Factory

APP_ID = '22989781'
API_KEY = 'Y4LjYlL4O6aqGe4gVw0ziE27'
SECRET_KEY = 'Mwwa3MRGcnkoXRv7ghex99cQXmmtxyBG'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def waitUntilDisplay(driver, ByCss):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ByCss)))


# 等待直到元素出现
def waitUntilDisplay_xpath(driver, ByCss):
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, ByCss)))


# 等待直到元素可点击
def waitUntilClick(driver, ByCss):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ByCss)))


# 等待直到元素可点击
def waitUntilClick_xpath(driver, xpatn):
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpatn)))


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


# 验证码识别（爬虫/UI自动化用 OCR识别）
def getVerCode(imagePath):
    # https://www.cnblogs.com/xiaowenshu/p/11792012.html
    with open(imagePath, 'rb') as fp:
        image = fp.read()
    # """ 调用通用文字识别（高精度版） """
    code = client.basicAccurate(image)
    return code.get('words_result')[0].get('words')


# 移动端 等待元素出现并点击
def waiteForClick(el):
    while True:
        try:
            sleep(0.5)
            el.wait_for_appearance(timeout=0.1)
            el.click()
            break
        except:
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


# 拖动到文本出现
def dragUntilTextAppear(el, text2, text3):
    while True:
        el.drag_to(mobileDriver(text=text2), 0.5)
        if mobileDriver(text=text3).exists():
            break
        else:
            continue


# 随机得到模拟数据
def getFakerClass():
    # https://www.jianshu.com/p/6bd6869631d9
    fakerInfor = Factory().create('zh_CN')
    return fakerInfor


if __name__ == '__main__':
    faker = getFakerClass()
    print(faker.ssn())
