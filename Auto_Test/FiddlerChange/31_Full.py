#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

url = 'https://kyfw.12306.cn/otn/modifyUser/initQueryUserInfoApi'
headers = {'Host': 'kyfw.12306.cn', 'Connection': 'keep-alive', 'Content-Length': '0', 'Accept': '*/*', 'Origin': 'https://kyfw.12306.cn', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36', 'Referer': 'https://kyfw.12306.cn/otn/view/information.html', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9'}
cookies = {'JSESSIONID': '767F89D17AF1D87E800C44D9312E8CDC', 'tk': '2s1-2r76CcJRCVcNhaVbULJxNkDlamgiDf8-gmi48bchus1s0', 'BIGipServerotn': '787481098.24610.0000', 'BIGipServerpool_passport': '48497162.50215.0000', 'RAIL_EXPIRATION': '1604958337156', 'RAIL_DEVICEID': 'r5pX2kZerwKDZbdnuhdCQRIQu7JQ7mtKojidPvwa01RugwKIpCIJo3_17Tjw8AnzIYXgiY2zX5xZxN8qWb1NrchUbGr-KXwJFuXzamGgJx0mDTZWuGdfTQLTYQUketNf06NNPSr1AViYAGZsMQUuGbbTSV09yXiP', 'route': '495c805987d0f5c8c84b14f60212447d', 'uKey': 'f0db43ea72244db3f2106202ba8704630455878363eba795e21c514481e35aff'}
data = {}

html = requests.post(url, headers=headers, verify=False, cookies=cookies, data=data)
print(len(html.text))
print(html.text)
