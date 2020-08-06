# 等待元素出现
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait


# 等待直到元素出现
def waitUntilDisplay(driver, ByCss):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ByCss)))


# 等待直到元素可点击
def waitUntilClick(driver, ByCss):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ByCss)))


# 等待直到元素可点击
def waitUntilClick_xpath(driver, ByXpath):
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, ByXpath)))
