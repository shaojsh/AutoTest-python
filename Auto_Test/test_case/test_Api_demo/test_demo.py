#!/usr/bin/python
# -*- coding: UTF-8 _*_
import os

from common.Request import RequestsHandler
from common.Retrun_Response import dict_style
import hashlib
import time

allCnt = 0
sucessCnt = 0
f = open(r'C:\Users\shaojunshuai\Desktop\log.txt', 'a+')


def test_loopApiAccuracy():
    # 优化格式化化版本
    timeNow = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    appid = 'cjt'
    checkcode = 'cjt' + timeNow + 'e14b7c06-f127-4f7c-86f0-eec9bbcdc8d6'
    m = hashlib.md5()
    m.update(checkcode.encode('utf-8'))

    opera_url = "http://123.133.28.226:60011/gpl/webservice/security/getToken?appid=" + appid + "&timestamp=" + timeNow + "&checkcode=" + m.hexdigest()
    opera_result = RequestsHandler().post_Req(url=opera_url, params='')
    sting_response = opera_result.content.decode()
    json_response = dict_style(sting_response)
    token = json_response.get("token")
    f.write(str(json_response) + os.linesep)
    print(json_response)
    if token is None:
        print(json_response + '  失败  ')
    else:
        return 'sucess'


if __name__ == "__main__":

    while allCnt < 30:
        try:
            time.sleep(1)
            allCnt = allCnt + 1
            result = test_loopApiAccuracy()
            if result == 'sucess':
                sucessCnt = sucessCnt + 1
            per = (sucessCnt / allCnt)
        except Exception as e:
            f.write('Failed to establish a new connection: [WinError 10051] 向一个无法连接的网络尝试了一个套接字操作')
            continue
    result = '共执行' + str(allCnt) + '次' ',其中成功次数为' + str(sucessCnt), '成功率为' + str(per)
    f.write(str(result) + os.linesep)
