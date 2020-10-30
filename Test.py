import time

import requests
from selenium.webdriver.chrome import webdriver

header = {
    "Host": "kyfw.12306.cn",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "JSESSIONID=A7F53A59305DEE3BBC192622F95F9E46; tk=wtYklorgEPqYikbS5LFU3LAO56F_z937_EG2sea6rrMozs1s0; RAIL_EXPIRATION=1604303483535; RAIL_DEVICEID=daRi71bA2TsRQB7EaxiLHCbHqNrsoicRikrJ1YxXetHphH-kS_9NNz6DachZMsVs_6GhIz6_Y5eELXrVLS6QBHhSekotZTo1j1MBKvVH6P-3cNd22QBxbOS8N7zYmsgGge0HdASJoIwna5awWdT6p7pDplmZnQS5; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=703595018.24610.0000; BIGipServerpool_passport=216269322.50215.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_toDate=2020-10-30; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2020-11-11; uKey=f0db43ea72244db3f2106202ba870463b76dde7b5f69e0ff7be7062903f60774"
}

# s = requests.session()
# s.keep_alive = False
# page = requests.get('https://kyfw.12306.cn/otn/view/index.html', headers=header, verify=False)
# print(page.text.encode('utf-8'))
driver_forward = webdriver.Chrome()
driver_forward.maximize_window()
driver_forward.get('https://kyfw.12306.cn/otn/view/index.html', header=header)
