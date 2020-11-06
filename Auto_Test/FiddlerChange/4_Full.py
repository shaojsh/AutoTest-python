#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = 'http://10.10.128.152:10894/v1/enterprise/admin/getEnterpriseInfo'
headers = {'Host': '10.10.128.152:10894', 'Connection': 'keep-alive', 'Accept': 'application/json, text/plain, */*', 'Origin': 'http://10.10.128.152:10052', 'Sso-Token': 'c44b904e-ca11-4ae9-b7c1-05da416743ee', 'appId': 'chengtay-zcd', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36', 'Referer': 'http://10.10.128.152:10052/', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {}
data = {}

html = requests.get(url, headers=headers, verify=False, cookies=cookies)
print(len(html.text))
print(html.text)
