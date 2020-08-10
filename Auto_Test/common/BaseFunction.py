# 等待元素出现
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait


# 等待直到元素出现
def waitUntilDisplay(driver, ByCss):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ByCss)))


# 等待直到元素出现
def waitUntilDisplay_xpath(driver, ByCss):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ByCss)))


# 等待直到元素可点击
def waitUntilClick(driver, ByCss):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ByCss)))


# 等待直到元素可点击
def waitUntilClick_xpath(driver, ByXpath):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ByXpath)))


# 元素需要移动到相应地点才能点击
def actionChainsClick(driver, element):
    webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
