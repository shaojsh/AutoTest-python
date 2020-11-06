#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:44:26 2018
"""
import requests

'''
此12306自动订票爬虫，
仅限用于python学习与交流，请勿用于商业或非法活动！
知乎专栏：https://zhuanlan.zhihu.com/p/48077823

文档使用说明：
1.请替换成自己的"用户名"与"密码"；
2.请注意验证码图片下载地址，默认下载到py文件所在文件夹，名称为"vcode.png"；
3.如果验证码看不清楚，可输入"0"刷新验证码；
4.默认订购预订二等座，其他座位类型请自行修改代码

'''

username = "shaojunshuai"
password = "Shuai2019"
choose_no = ""  # 乘客序号，默认为空值
# choose_no="1"


from urllib import request, parse
from http.cookiejar import CookieJar
import re
import ssl
import datetime
import time
import json

# 为了防止ssl出现错误，可以加上下面一行代码
ssl._create_default_https_context = ssl._create_unverified_context


# 站名三字码提取 station_names={"上海"：“AOH”}
def StationName():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9069"
    html = request.urlopen(url).read().decode("utf-8", "ignore")
    pat = "var station_names ='(.*?)';"
    result = re.compile(pat, re.S).findall(html)[0]
    datas = result.split("|")
    station_names = {}
    for i in range(0, (len(datas) // 5)):
        station_names[datas[1 + 5 * i]] = datas[2 + 5 * i]
    return station_names


# query_leftTicket--余票查询(get)
def query_leftTicket():
    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=" + train_date + "&leftTicketDTO.from_station=" + from_station + "&leftTicketDTO.to_station=" + to_station + "&purpose_codes=" + purpose_codes
    # context = ssl._create_unverified_context()
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_uab_collina=160404173781648102218101; JSESSIONID=699CC77AF02EF4FD2C85BB1C1EABFAD5; RAIL_EXPIRATION=1604303483535; RAIL_DEVICEID=daRi71bA2TsRQB7EaxiLHCbHqNrsoicRikrJ1YxXetHphH-kS_9NNz6DachZMsVs_6GhIz6_Y5eELXrVLS6QBHhSekotZTo1j1MBKvVH6P-3cNd22QBxbOS8N7zYmsgGge0HdASJoIwna5awWdT6p7pDplmZnQS5; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=703595018.24610.0000; BIGipServerpool_passport=216269322.50215.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%2CBJP; _jc_save_fromDate=2020-11-01; _jc_save_toDate=2020-10-30; _jc_save_wfdc_flag=dc",
        "Host": "kyfw.12306.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    req = requests.get(url, headers=header, stream=True, verify=False)
    data = json.loads(req.text)
    return data['data']


# 用户登录
def Login12306():
    # 1.checkUser--检查用户登录状态
    print("正在检查用户登录状态...")
    checkUser_url = "https://kyfw.12306.cn/otn/login/checkUser"
    checkUser_data = parse.urlencode({"_json_att": ""}).encode("utf-8")
    checkUser_req = request.Request(checkUser_url, checkUser_data, headers)
    checkUser_response = request.urlopen(checkUser_req).read().decode("utf-8", "ignore")
    # print(checkUser_response)

    # 2.conf--检查配置信息
    print("正在检查配置状态... ")
    conf_url = "https://kyfw.12306.cn/otn/login/conf"
    conf_data = parse.urlencode({"_json_att": ""}).encode("utf-8")
    conf_req = request.Request(conf_url, conf_data, headers)
    conf_response = request.urlopen(conf_req).read().decode("utf-8", "ignore")
    # print(conf_response)

    # 3.captcha--获取验证码图片
    print("正在处理验证码... ")
    vcode_url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
    while True:
        request.urlretrieve(vcode_url, 'vcode.png')  # 验证码图片下载到本地
        inputs = input("请输入验证码，输入第几张图片即可： ")
        if (inputs != "0"):
            break
    positions = list(inputs)
    vcode_xy = ["41,42", "113,48", "182,40", "250,43", "42,126", "115,121", "183,118", "253,117"]
    # 用列表的下标来一一对应数字与坐标
    vcode_values = []
    for i in range(0, len(positions)):
        vcode_value = vcode_xy[int(positions[i]) - 1]
        vcode_values.append(vcode_value)

    thisvcode = ",".join(vcode_values)
    # print(thisvcode)

    # captcha--验证码验证
    capCheck_url = "https://kyfw.12306.cn/passport/captcha/captcha-check"
    capCheck_form = {
        "answer": thisvcode,
        "login_site": "E",
        "rand": "sjrand",
    }
    capCheck_data = parse.urlencode(capCheck_form).encode("utf-8")
    capCheck_req = request.Request(capCheck_url, capCheck_data, headers)
    capCheck_response = request.urlopen(capCheck_req).read().decode("utf-8", "ignore")
    # print(capCheck_response)

    # 4.1 login--用户名、密码验证
    print("正在验证用户名/密码... ")
    login_url = "https://kyfw.12306.cn/passport/web/login"
    login_form = {
        "_json_att": "",
        "appid": "otn",
        "answer": thisvcode,
        "password": password,
        "username": username,
    }
    login_data = parse.urlencode(login_form).encode("utf-8")
    login_req = request.Request(login_url, login_data, headers)
    login_response = request.urlopen(login_req).read().decode("utf-8", "ignore")
    # print(login_response)

    # 5.uamtk--登录uamtk，验证appid
    appid_url = "https://kyfw.12306.cn/passport/web/auth/uamtk"
    appid_data = parse.urlencode({"appid": "otn", "_json_att": "", }).encode("utf-8")
    appid_req = request.Request(appid_url, appid_data, headers)
    appid_response = request.urlopen(appid_req).read().decode("utf-8", "ignore")
    # print(appid_response)
    pat_tk = '"newapptk":"(.*?)"'
    tk = re.compile(pat_tk, re.S).findall(appid_response)
    while len(tk) == 0:
        print("******* 验证码校验失败！********")
        break

    else:
        tk = tk[0]
        pass

        # 6.登录uamauthclient --验证tk
        tk_url = "https://kyfw.12306.cn/otn/uamauthclient"
        tk_data = parse.urlencode({"tk": tk, "_json_att": "", }).encode("utf-8")
        tk_req = request.Request(tk_url, tk_data, headers)
        tk_response = request.urlopen(tk_req).read().decode("utf-8", "ignore")
        # print(tk_response)

        # 7.登录成功--爬取个人中心
        print("登录成功！")
        mycenter_url = "https://kyfw.12306.cn/otn/index/initMy12306"
        mycenter_req = request.Request(mycenter_url)
        mycenter_response = request.urlopen(mycenter_req).read().decode("utf-8", "ignore")
        print("正在爬取个人中心......")
        pat = '<a id="login_user".*?><span.*?>(.*?)</span>.*?</a>'
        urser = re.compile(pat, re.S).findall(mycenter_response)
        print("用户名已成功抓取，当前用户名是" + urser[0])
        print("------------------------")


# 初始化购票页面
def init_buy_page():
    url = "https://kyfw.12306.cn/otn/leftTicket/init"
    req = request.Request(url)
    html = request.urlopen(req).read().decode("utf-8", "ignore")


# 确认用户登录状态
def checkUser(headers):
    url = "https://kyfw.12306.cn/otn/login/checkUser"
    data = parse.urlencode({"_json_att": ""}).encode("utf-8")
    req = request.Request(url, data, headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    # print(result)


# 提交车票预定信息
def submitOrderRequest(headers, back_date, purpose_codes, from_name, to_name, secretStr, train_date):
    url = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
    data = {
        "back_train_date": back_date,
        "purpose_codes": purpose_codes,
        "query_from_station_name": from_name,
        "query_to_station_name": to_name,
        "secretStr": secretStr,
        "tour_flag": "dc",
        "train_date": train_date,
        "undefined": "", }
    req = request.Request(url, parse.urlencode(data).encode("utf-8"), headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    # print(result)


# 确认预订信息
def initDc(headers):
    url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"
    data = parse.urlencode({"_json_att": ""}).encode("utf-8")
    req = request.Request(url, data, headers)
    html = request.urlopen(req).read().decode("utf-8", "ignore")
    return html


# 获取乘客信息
def getPassenger(headers, token):
    url = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
    data = parse.urlencode({'REPEAT_SUBMIT_TOKEN': token, "_json_att": "", }).encode("utf-8")
    req = request.Request(url, data, headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    data = json.loads(result)["data"]
    return data


# 确认订单信息
def checkOrderInfo(headers, name, Id, mobile, token):
    url = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
    data = {"_json_att": "",
            "bed_level_order_num": "000000000000000000000000000000",
            "cancel_flag": "2",
            "oldPassengerStr": name + ",1," + Id + ",1_",
            "passengerTicketStr": "O,0,1," + name + ",1," + Id + "," + mobile + ",N",
            "randCode": "",
            "REPEAT_SUBMIT_TOKEN": token,
            "tour_flag": "dc",
            "whatsSelect": "1", }
    req = request.Request(url, parse.urlencode(data).encode("utf-8"), headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    # print(result)


# 提交预订请求
def getQueueCount(headers, train_no, fromStationTelecode, toStationTelecode, this_code, train_location, token):
    url = "https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"
    thisdatestr = train_date  # 需要的买票时间,先将字符串转为常规时间格式
    thisdate = datetime.datetime.strptime(thisdatestr, "%Y-%m-%d").date()
    gmt = "%a+%b+%d+%Y"  # 再转为对应的格林时间
    thisgmtdate = thisdate.strftime(gmt)
    leftstr2 = leftTicketStr.replace("%", "%25")
    data = "train_date=" + str(thisgmtdate) + "+00%3A00%3A00+GMT%2B0800+\
        (%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&train_no=" + train_no + "\
        &stationTrainCode=" + this_code + "&seatType=M&fromStationTelecode=" + fromStationTelecode + "\
        &toStationTelecode=" + toStationTelecode + "&leftTicket=" + leftstr2 + "&purpose_codes=00\
        &train_location=" + train_location + "&_json_att=&REPEAT_SUBMIT_TOKEN=" + str(token)
    req = request.Request(url, data.encode("utf-8"), headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    # print(result)


# 检查提交状态
def confirmSingleForQueue(headers, key_check_isChange, leftTicketStr, passenger_name, passenger_id, passenger_mobile,
                          token, train_location):
    url = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
    data = {
        "choose_seats": "1A",
        "dwAll": "N",
        "key_check_isChange": key_check_isChange,
        "leftTicketStr": leftTicketStr,
        "oldPassengerStr": passenger_name + ",1," + passenger_id + ",1_",
        "passengerTicketStr": "O,0,1," + passenger_name + ",1," + passenger_id + "," + passenger_mobile + ",N",
        "purpose_codes": "00",
        "randCode": "",
        "REPEAT_SUBMIT_TOKEN": token,
        "roomType": "00",
        "seatDetailType": "000",
        "train_location": train_location,
        "whatsSelect": "1",
        "_json_att": "", }
    req = request.Request(url, parse.urlencode(data).encode("utf-8"), headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")


# 排队等待
def queryOrderWaitTime(headers):
    url = "https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=" + str(
        int(time.time() * 1000)) + "&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=" + token
    req = request.Request(url)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    datas = json.loads(result)
    orderid = datas["data"]["orderId"]
    return orderid


# 请求预订结果
def resultOrderForDcQueue(headers, orderid, token):
    url = "https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
    data = {
        "_json_att": "",
        "orderSequence_no": orderid,
        "REPEAT_SUBMIT_TOKEN": token,
    }
    req = request.Request(url, parse.urlencode(data).encode("utf-8"), headers)
    result = request.urlopen(req).read().decode("utf-8", "ignore")
    print("请求结果完成！")


if __name__ == "__main__":

    # 余票查询
    station_names = StationName()
    # from_name = "上海"
    from_name = input("请输入起始站：")
    from_station = station_names[from_name]
    # to_name = "北京"
    to_name = input("请输入到达站：")
    to_station = station_names[to_name]
    # train_date = "2018-11-11"
    train_date = input("请输入乘车日期，如：2018-10-30  ")
    # isstudent = "0"
    isstudent = input("是学生吗？是：1，不是：0   ")
    if isstudent == "0":
        purpose_codes = "ADULT"
    else:
        purpose_codes = "0X00"

    leftTicket_data = query_leftTicket()
    Ticket_results = leftTicket_data['result']
    station_map = leftTicket_data['map']
    print("车次\t出发站名\t到达站名\t出发时间\t到达时间\t一等座\t二等座\t硬座\t无座\t硬卧\t软卧")
    for i in range(0, len(Ticket_results)):
        try:
            train = Ticket_results[i].split("|")
            train_code = train[3]  # [3]---->车次 : train_code
            from_station = train[6]  # [6]---->出发站：from_station
            from_station1 = station_map[from_station]
            to_station = train[7]  # [7]---->到达站：to_station
            to_station1 = station_map[to_station]
            stime = train[8]  # [8]---->出发时间：stime
            atime = train[9]  # [9]---->到达时间：atime
            sit_1 = train[31]  # [31]---->一等座：sit_1
            sit_2 = train[30]  # [30]---->二等座：sit_2
            sit_h = train[29]  # [29]---->硬座：sit_h
            sit_0 = train[26]  # [26]---->无座：sit_0
            bed_h = train[28]  # [28]---->硬卧：bed_h
            bed_s = train[23]  # [23]---->软卧：bed_s
            print(
                train_code + "\t" + from_station1 + "\t" + to_station1 + "\t" + stime + "\t" + atime + "\t" + sit_1 + "\t" + sit_2 + "\t" + sit_h + "\t" + sit_0 + "\t" + bed_h + "\t" + bed_s)
        except Exception as err:
            pass
    print("-" * 80)
    isdo = input('查票完成，请输入"1"继续...')
    # isdo=1
    if isdo == 1 or isdo == "1":
        pass
    else:
        raise Exception('输入不是"1",结束执行！')

    # 建立cookie处理
    print("Cookie处理中......")
    cookiejar = CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cookiejar))
    request.install_opener(opener)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'}

    print()
    print("进入用户登录环节：")
    print()
    Login12306()

    isdo = input('查票完成，请输入"1"继续...')
    # isdo=1
    if isdo == 1 or isdo == "1":
        pass
    else:
        raise Exception('输入不是"1",结束执行！')

    this_code = input("请输入要预定的车次：")
    # 自动抢票
    while True:
        try:
            # 初始化订票页面
            print("1.正在初始化订票页面...")
            init_buy_page()
            # 余票查询
            print("2.查询余票...")
            leftTicket_data = query_leftTicket()
            trains_info = leftTicket_data['result']
            station_map = leftTicket_data['map']
            # 存储车次与secretStr信息
            train_codes = []
            secretStrs = []
            sits = []
            for i in range(0, len(trains_info)):
                try:
                    this_train = trains_info[i].split("|")
                    train_code = this_train[3]  # [3]---code 车次
                    train_codes.append(train_code)
                    this_secretStr1 = this_train[0].replace('"', "")  # [0]---secretStr
                    this_secretStr = parse.unquote(this_secretStr1)
                    secretStrs.append(this_secretStr)
                    this_sit = this_train[30]  # [30]---sit_2二等座
                    sits.append(this_sit)
                except Exception as err:
                    pass
            # 用字典train_sit存储车次有没有票的信息
            train_sit = {}
            for i in range(0, len(train_codes)):
                train_sit[train_codes[i]] = sits[i]
            # 用字典train_data存储车次secretStr信息，以供后续订票操作
            # 存储的格式：train_data={"车次1"："secretStr1"，"车次2"："secretStr2"}
            train_data = {}
            for i in range(0, len(train_codes)):
                train_data[train_codes[i]] = secretStrs[i]

            # 用户确认
            print("3.正在确认用户登录状态...")
            checkUser(headers)
            # 自动得到当前时间并转为“年-月-日”格式,后面back_train_data用到
            back_date = datetime.datetime.now()
            back_date = back_date.strftime("%Y-%m-%d")
            # 提交车票预定信息
            print("4.正在提交预订信息...")
            submitOrderRequest(headers, back_date, purpose_codes, from_name, to_name, train_data[this_code], train_date)

            # 确认预订信息
            print("5.正在确认预订信息... ")
            initdc_html = initDc(headers)
            # 获取train_no,leftTicketStr,fromStationTelecode,toStationTelecode,train_location
            train_no_pat = "'train_no':'(.*?)'"
            leftTicketStr_pat = "'leftTicketStr':'(.*?)'"
            fromStationTelecode_pat = "'from_station_telecode':'(.*?)'"
            toStationTelecode_pat = "'to_station_telecode':'(.*?)'"
            train_location_pat = "'train_location':'(.*?)'"
            token_pat = "var globalRepeatSubmitToken = '(.*?)';"
            key_check_isChange_pat = "'key_check_isChange':'(.*?)'"
            train_no_all = re.compile(train_no_pat, re.S).findall(initdc_html)
            if (len(train_no_all) != 0):
                train_no = train_no_all[0]
            else:
                raise Exception("train_no获取失败")
            leftTicketStr_all = re.compile(leftTicketStr_pat, re.S).findall(initdc_html)
            if len(leftTicketStr_all) != 0:
                leftTicketStr = leftTicketStr_all[0]
            else:
                raise Exception("leftTicketStr获取失败")
            fromStationTelecode_all = re.compile(fromStationTelecode_pat, re.S).findall(initdc_html)
            if len(fromStationTelecode_all) != 0:
                fromStationTelecode = fromStationTelecode_all[0]
            else:
                raise Exception("from_station_telecode获取失败")
            toStationTelecode_all = re.compile(toStationTelecode_pat, re.S).findall(initdc_html)
            if len(toStationTelecode_all) != 0:
                toStationTelecode = toStationTelecode_all[0]
            else:
                raise Exception("to_station_telecode获取失败")
            train_location_all = re.compile(train_location_pat, re.S).findall(initdc_html)
            if len(train_location_all) != 0:
                train_location = train_location_all[0]
            else:
                raise Exception("train_location获取失败")
            token_all = re.compile(token_pat, re.S).findall(initdc_html)
            if len(token_all) != 0:
                token = token_all[0]
            else:
                raise Exception("token获取失败")
            key_check_isChange_all = re.compile(key_check_isChange_pat, re.S).findall(initdc_html)
            if len(key_check_isChange_all) != 0:
                key_check_isChange = key_check_isChange_all[0]
            else:
                raise Exception("key_check_isChange获取失败")
            print("确认完成！")

            # 获取乘客信息
            print("6.正在获取乘客信息... ")
            getPassenger_data = getPassenger(headers, token)
            Passenger_data = getPassenger_data['normal_passengers']
            passenger_names = []  # 姓名
            passenger_ids = []  # 证件号码
            passenger_mobiles = []  # 手机号码
            for i in range(0, len(Passenger_data)):
                passenger_names.append(Passenger_data[i]['passenger_name'])
                passenger_ids.append(Passenger_data[i]['passenger_id_no'])
                passenger_mobiles.append(Passenger_data[i]['mobile_no'])

            # 选择乘客
            if choose_no != "":
                pass
            else:
                for i in range(0, len(passenger_names)):
                    print("第" + str(i + 1) + "位用户， 姓名：" + str(passenger_names[i]))
                choose_no = input("请选择需要订票的乘客，并输入乘客序号:")
                # this_no为对应乘客的下标，比次序号少1，比如序号为1的乘客在列表中的下标为0
                this_no = int(choose_no) - 1
            # 如果无票，将继续监控
            if train_sit[this_code] == "无":
                print("当前无票，继续监控...")
                continue

            # 确认订单信息
            print("7.正在确认订单信息...")
            checkOrderInfo(headers, passenger_names[this_no], passenger_ids[this_no], passenger_mobiles[this_no], token)

            # 提交预订请求
            print("8.正在提交预订请求... ")
            getQueueCount(headers, train_no, fromStationTelecode, toStationTelecode, this_code, train_location, token)

            # 检查提交状态
            print("9.正在确认配置信息...")
            confirmSingleForQueue(headers, key_check_isChange, leftTicketStr, passenger_names[this_no],
                                  passenger_ids[this_no], passenger_mobiles[this_no], token, train_location)

            # 排队等待--直到获取orderid
            time1 = time.time()
            while True:
                time2 = time.time()
                if (time2 - time1) // 60 > 5:
                    print("获取orderid超时，正在进行新一次抢购")
                    break
                print("排队等待中... ")
                orderid = queryOrderWaitTime(headers)
                if orderid == None:
                    print("未获得orderid,正在进行新一次请求。")
                    continue

                else:
                    # orderid = orderid[0]
                    print(orderid)
                    break
            print("抢票成功!")

            # 请求预订结果
            print("11.正在请求预订结果... ")
            resultOrderForDcQueue(headers, orderid, token)

            try:
                # payOrder--支付接口页面
                pay_url = "https://kyfw.12306.cn/otn//payOrder/init?random=" + str(int(time.time() * 1000))
                pay_dict = {
                    "&REPEAT_SUBMIT_TOKEN": token,
                    "_json_att": "",
                }
                pay_data = parse.urlencode(pay_dict).encode("utf-8")
                pay_req = request.Request(pay_url, pay_data, headers)
                pay_response = request.urlopen(pay_req).read().decode("utf-8", "ignore")
                print("订单已经完成提交，")
                print("您可以登录后台进行支付了！")
                break
            except Exception as err:
                print(err)
        except Exception as err:
            print(err)
