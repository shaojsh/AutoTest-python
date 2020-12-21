# cmd = schtasks /create /tn start /tr C:\Users\shaojunshuai\PycharmProjects\AutoTest-python\Auto_Test\start.py /sc daily /st 18:00
# 每天执行定时任务py   开机  控制面板  维护
# 1.wins+R
# 2. 执行命令 cmd
# 3. schtasks 删除任务：schtasks /Delete /TN start /F
import os

import hashlib

# 调用后会自动关机
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.Request import RequestsHandler
from common.Retrun_Response import dict_style
from common.dbLink import getVerification_ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pickle as pkl


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
                                    params={"id": "28181123393445888", "auditOpinion": "YES", "auditRemark": "不同意",
                                            "lockId": "28181110586138624", }, headers=headers)
    print(r0.text)


# 生成环境日志构建
def productError():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    url = "http://10.10.128.153:5601/app/kibana#/discover?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-1h,to:now))&_a=(columns:!(appname,level,message),filters:!(('$state':(store:appState),meta:(alias:!n,disabled:!f,index:'4cedbc90-f8b1-11ea-8343-ed223af86c0a',key:level,negate:!f,params:(query:ERROR),type:phrase),query:(match_phrase:(level:ERROR)))),index:'4cedbc90-f8b1-11ea-8343-ed223af86c0a',interval:auto,query:(language:kuery,query:''),sort:!())"
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Refresh']")))
    el = driver.find_element_by_class_name('dscResultCount')
    error_tag = el.text
    print(error_tag)
    driver.save_screenshot('error.png')


# 调用后自动开机
# def start_up():
#     pass

if __name__ == "__main__":
    # 活体认证
    # getVerification_ui("http://10.10.128.152:10000/v1/account/login", "17621198964")
    productError()
