#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = 'http://10.10.128.152:10000/v1/account/login'
headers = {'Host': '10.10.128.152:10000', 'Connection': 'keep-alive', 'Content-Length': '65',
           'Accept': 'application/json, text/plain, */*', 'Origin': 'http://10.10.128.152:10053', 'Sso-Token': '',
           'appId': 'chengtay-zcd',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
           'Content-Type': 'application/json;charset=UTF-8', 'Referer': 'http://10.10.128.152:10053/user/login',
           'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'JSESSIONID': 'C1C036B865404E8BB41B041909F2BE96', 'Sso-Token': '49da647a-368a-433a-bb2b-cdd76975334c'}
data = {"userName": "17621198933", "verifyCode": " ", "password": "MTIzNDU2"}

html = requests.post(url, headers=headers, verify=False, cookies=cookies, data=data)
print(len(html.text))
print(html.text)
