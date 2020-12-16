# cmd = schtasks /create /tn start /tr C:\Users\shaojunshuai\PycharmProjects\AutoTest-python\Auto_Test\start.py /sc daily /st 18:00
# 每天执行定时任务py   开机  控制面板  维护
# 1.wins+R
# 2. 执行命令 cmd
# 3. schtasks 删除任务：schtasks /Delete /TN start /F
import os

import hashlib

# 调用后会自动关机
import time

from common.Request import RequestsHandler
from common.Retrun_Response import dict_style


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
                                    params={"id": "28073838491000832", "auditOpinion": "YES", "auditRemark": "不同意",
                                            "lockId": "28073292667346944", }, headers=headers)
    print(r0.text)


# 调用后自动开机
# def start_up():
#     pass

if __name__ == "__main__":
    gettoken()
