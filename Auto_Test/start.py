# cmd = schtasks /create /tn start /tr C:\Users\shaojunshuai\PycharmProjects\AutoTest-python\Auto_Test\start.py /sc daily /st 18:00
# 每天执行定时任务py   开机  控制面板  维护
# 1.wins+R
# 2. 执行命令 cmd
# 3. schtasks 删除任务：schtasks /Delete /TN start /F
import os
import hashlib
import glob
import fitz  # 导入本模块需安装pymupdf库
import os

# 调用后会自动关机
import re
import time
import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.BaseFunction import matchRe
from common.Request import RequestsHandler
from common.Retrun_Response import dict_style
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests

from common.dbLink import getVerification_ui


def shout_dowm():
    pass
    # os.system('shutdown -s -f -t 10')


# 银行token 30分钟有效期
def gettoken():
    appid = "zcd"
    timeNow = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    checkCode = "zcd" + timeNow + "87288aae-49e5-42e5-be97-609ae7fc35ba"
    md5Pas = hashlib.md5(checkCode.encode())
    url = "http://124.70.221.250:8080/gpl/webservice/security/getToken?appid=" + appid + "&timestamp=" + timeNow + "&checkcode=" + md5Pas.hexdigest()
    opera_result = RequestsHandler().post_Req(url=url, params='')
    sting_response = opera_result.content.decode()
    json_response = dict_style(sting_response)
    token = json_response.get("token")
    if token is None:
        print('ERROR,Token没拿到')
    headers = {'X-PM-API-TOKENID': token}
    url1 = 'http://124.70.221.250:8080/gpl/webservice/procurement/updatePurchaserOpinion'
    r0 = RequestsHandler().post_Req(url=url1,
                                    params={"id": "29444836203225088", "auditOpinion": "NO", "auditRemark": "不同意",
                                            "lockId": "28698031703252992", }, headers=headers)
    print(r0.text)


# 生成环境日志构建
def productError():
    option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    url = "http://10.10.128.153:5601/app/kibana#/discover?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h,to:now))&_a=(columns:!(appname,level,message),filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'4cedbc90-f8b1-11ea-8343-ed223af86c0a',key:level,negate:!f,params:(query:ERROR),type:phrase),query:(match_phrase:(level:ERROR)))),index:'4cedbc90-f8b1-11ea-8343-ed223af86c0a',interval:auto,query:(language:kuery,query:''),sort:!())"
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Refresh']")))
    el = driver.find_element_by_class_name('dscResultCount')
    error_tag = el.text
    time.sleep(2)
    html = driver.find_element_by_xpath("//*/tbody").get_attribute("outerHTML")
    driver.save_screenshot('prdLog.png')


# 调用后自动开机
def start_up():
    # 生产环境log日志查看 过去24小时
    productError()


# 爬取百度文库资源信息
def baiduWenku():
    option = webdriver.ChromeOptions()
    # option.add_argument('--headless')
    option.add_argument(
        'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    url = "https://wenku.baidu.com/view/e9dc4552a55177232f60ddccda38376bae1fe062.html?fr=search-score_2-psrec1&fixfr=wis0bMgD2qzRL%2B1FgwGT%2Bg%3D%3D"
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=option)
    driver.get(url)

    xpath2 = "//*[text() = '继续阅读']"
    xpath3 = "//*[text() = '确定']"

    driver.refresh()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath2)))
    time.sleep(2)
    driver.find_element_by_xpath(xpath2).click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath2)))
    driver.find_element_by_xpath(xpath3).click()
    html = driver.page_source

    start = '\"htmlUrls\":'
    end = ',\"free_page\"'

    urls = matchRe(html, start, end)

    # 下载链接
    i = 0

    path = os.getcwd() + '\\spider\\pdf\\'

    for url in str(urls)[1:-1].split(','):
        url = url.replace("\"", '')
        f = requests.get(url)
        with open(path + str(i) + ".jpg", "wb") as code:
            code.write(f.content)
        i = i + 1
        picPdf(path, path, r'\wenku.pdf')
    driver.quit()


def picPdf(img_path, pdf_path, pdf_name):
    doc = fitz.open()

    for img in sorted(glob.glob(img_path + "*.jpg")):
        imgdoc = fitz.open(img)
        pdfbytes = imgdoc.convertToPDF()
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)
    doc.save(pdf_path + pdf_name)
    doc.close()


if __name__ == "__main__":
    # gettoken()
    # 活体认证
    # while True:
    #     getVerification_ui("http://10.10.128.152:10000/v1/account/login", "17082238021")
    #     continue
    baiduWenku()
