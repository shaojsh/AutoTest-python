import base64
from time import sleep

import pymysql
import redis
from common.Request import RequestsHandler
from common.Retrun_Response import dict_style
# db数据操作
from run_all_case import yamldict


def Sqldata(sqlStr, flag):
    db = yamldict['test_db_list']['db1']
    if flag == 2:
        db = yamldict['test_db_list']['db2']
    if flag == 3:
        db = yamldict['test_db_list']['db3']
    # 连接数据库
    connect = pymysql.connect(
        host=yamldict['test_db_list']['host'],
        user=yamldict['test_db_list']['user'],
        password=yamldict['test_db_list']['password'],
        port=yamldict['test_db_list']['port'],
        db=db
    )
    # 创建一个游标对象:有两种创建方法
    cursor = connect.cursor()  # 或：cursor=pymysql.cursors.Cursor(connect)
    # 使用游标的execute()方法执行sql语句
    cursor.execute(sqlStr)
    connect.commit()
    # 使用fetchall()获取全部数据
    r1 = cursor.fetchall()
    print(r1)

    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    connect.close()


def RedisSqldata():
    pool = redis.ConnectionPool(
        host=yamldict['test_redisdb_list']['host'],
        port=yamldict['test_redisdb_list']['port'],
        password=yamldict['test_redisdb_list']['password'],
        db=yamldict['test_redisdb_list']['db3']
    )
    r = redis.Redis(connection_pool=pool)  # 获取连接对象
    return r


# 对企业账户进行删除操作（注册用）
def deleteAct():
    act = yamldict['test_userlist']['company_user']
    sqlStr1 = yamldict['test_db_sqllist']['sql0000001']
    sqlStr2 = yamldict['test_db_sqllist']['sql0000002']
    sqlStr3 = yamldict['test_db_sqllist']['sql0000003']

    sqlStr2 = sqlStr2.format("'" + act + "'")
    sqlStr3 = sqlStr3.format("'" + act + "'")

    print(sqlStr1)
    print(sqlStr2.format("'" + act + "'"))
    print(sqlStr3.format("'" + act + "'"))

    Sqldata(sqlStr1, 1)
    Sqldata(sqlStr2, 1)
    Sqldata(sqlStr3, 1)


# 删除个人信息以及企业信息
def deletePerInforAndComInfor():
    act = yamldict['test_userlist']['company_user']
    sqlStr4 = yamldict['test_db_sqllist']['sql0000004']
    sqlStr5 = yamldict['test_db_sqllist']['sql0000005']
    # sqlStr6 = yamldict['test_db_sqllist']['sql0000006']

    sqlStr5 = sqlStr5.format("'" + act + "'")
    # sqlStr6 = sqlStr6.format("'" + act + "'")

    print(sqlStr4)
    print(sqlStr5.format("'" + act + "'"))
    # print(sqlStr6.format("'" + act + "'"))

    Sqldata(sqlStr4, 2)
    Sqldata(sqlStr5, 2)
    # Sqldata(sqlStr6, 2)


# 删除机构信息
def deleteOrgInfor():
    autoTest_RiskName = yamldict['test_backStageUserList']['autoTest_RiskName']
    autoTest_BankName = yamldict['test_backStageUserList']['autoTest_BankName']
    company_bank = yamldict['test_backStageUserList']['company_bank']
    company_Guarantee = yamldict['test_backStageUserList']['company_Guarantee']

    sqlStr4 = yamldict['test_db_sqllist']['sql0000004']
    sqlStr6 = yamldict['test_db_sqllist']['sql0000006']
    sqlStr7 = yamldict['test_db_sqllist']['sql0000007']
    sqlStr8 = yamldict['test_db_sqllist']['sql0000008']
    sqlStr9 = yamldict['test_db_sqllist']['sql0000009']
    sqlStr10 = yamldict['test_db_sqllist']['sql0000010']
    sqlStr11 = yamldict['test_db_sqllist']['sql0000011']
    sqlStr12 = yamldict['test_db_sqllist']['sql0000012']
    sqlStr13 = yamldict['test_db_sqllist']['sql0000013']

    phone1 = '\'' + company_bank + '\','
    phone2 = '\'' + company_Guarantee + '\''
    phone = '(' + phone1 + phone2 + ')'
    name1 = '\'' + autoTest_RiskName + '\','
    name2 = '\'' + autoTest_BankName + '\''
    name = '(' + name1 + name2 + ')'
    print(phone)
    sqlStr6 = sqlStr6.format(phone)
    sqlStr7 = sqlStr7.format("'" + autoTest_BankName + "'")
    sqlStr8 = sqlStr8.format("'" + autoTest_BankName + "'")
    sqlStr9 = sqlStr9.format(phone)
    sqlStr10 = sqlStr10.format(phone)
    sqlStr11 = sqlStr11.format(phone)
    sqlStr12 = sqlStr12.format(name)
    sqlStr13 = sqlStr13.format(name)
    print(
        sqlStr6 + '\n' + sqlStr7 + '\n' + sqlStr8 + '\n' + sqlStr9 + '\n' + sqlStr10 + '\n' + sqlStr11 + '\n' + sqlStr12 + '\n' + sqlStr13 + '\n')

    Sqldata(sqlStr4, 1)
    Sqldata(sqlStr6, 1)
    Sqldata(sqlStr7, 2)
    Sqldata(sqlStr8, 2)
    Sqldata(sqlStr9, 2)
    Sqldata(sqlStr10, 2)
    Sqldata(sqlStr11, 2)
    Sqldata(sqlStr12, 2)
    Sqldata(sqlStr13, 2)


# 得到手机短信信息
def getPhoneMessage():
    act = yamldict['test_userlist']['company_user']
    company_bank = yamldict['test_backStageUserList']['company_bank']
    company_Guarantee = yamldict['test_backStageUserList']['company_Guarantee']
    r = RedisSqldata()

    keys = r.keys()
    pipe = r.pipeline()
    pipe_size = 100000
    len = 0
    key_list = []
    print(r.pipeline())

    for key in keys:
        key_list.append(key)
        pipe.get(key)
        if len < pipe_size:
            len += 1
        else:
            for (k, v) in zip(key_list, pipe.execute()):
                len = 0
                key_list = []
    phoneMessage = {}
    for (k, v) in zip(key_list, pipe.execute()):
        k = bytes.decode(k)
        v = bytes.decode(v)
        print(v)
        if k == 'code:A0002:' + act:  # 注册
            phoneMessage['regMes'] = v
        if k == 'code:A0003:' + act:  # 密码修改
            phoneMessage['forgeMes'] = v
        if k == 'code:ZCDA0132:' + act:  # 个人认证
            phoneMessage['auMes'] = v
        if k == 'code:ZCDA0131:17621198456':  # 借款管理
            phoneMessage['loanMes'] = v
        if k == 'code:A0003:' + company_bank:  # 修改密码 银行
            phoneMessage['actBank'] = v
        if k == 'code:A0003:' + company_Guarantee:  # 修改密码 担保公司
            phoneMessage['actRisk'] = v
        if k == 'code:ZCDA0132:' + company_bank:  # 认证 银行
            phoneMessage['AuBank'] = v
        if k == 'code:ZCDA0132:' + company_Guarantee:  # 修改密码 担保公司
            phoneMessage['AuRisk'] = v
    return phoneMessage


# 活体二维码码欺诈验证
def getVerification(url, act):
    r0 = RequestsHandler().post_Req(url=url, json={"userName": str(act), "password": "MTIzNDU2"}, )
    sting_response = r0.content.decode()
    json_response = dict_style(sting_response)
    data = json_response.get('data')
    print('token为：' + data)

    r = RedisSqldata()
    keys = r.keys()
    pipe = r.pipeline()
    pipe_size = 100000
    len = 0
    key_list = []
    print(r.pipeline())

    for key in keys:
        key_list.append(key)
        pipe.get(key)
        if len < pipe_size:
            len += 1
        else:
            for (k, v) in zip(key_list, pipe.execute()):
                len = 0
                key_list = []

    for (k, v) in zip(key_list, pipe.execute()):
        k = bytes.decode(k)
        v = bytes.decode(v)
        if k == 'token:' + data:
            v = v.replace('null', '\"' + 'ok' + '\"')
            dic = eval(v)
            userId = dic.get('userId')
            print('userId为：' + userId)
            break

    while 1:
        value1 = r.get(str(userId))
        if value1 is None:
            continue
        else:
            break
    strValue1 = bytes.decode(value1).replace('"', "")

    url_fin = 'http://sit.free.vipnps.vip/v1/certification/%s/callback'
    url_fin = url_fin.replace('%s', strValue1)
    while 1:
        value1 = r.get(str(userId))
        if value1 is None:
            break
        else:
            continue
    r1 = RequestsHandler().post_Req(url=url_fin, data={
        "Message": "q4o3qIRdHmQMmiECxSDEO8cOFdCngJCxluyefZ55scmFEcBSdgPbDxosxvUiGQbyP3XfOZ8cojLuDrVqWn/pvR2vJCxIxmCRbhMwe7ThciXRQpXF0O4blrizzkqx/9IqbYXYsQ6J0RrPKVJHEDgm2e6V8w2AWzMU00HUyclPXJAZU04QuX2rKLMAps3cg9WwXUUC+L6TokaSNmV8dRBKOYWx8J3TszXW3oOzLTmJFY/pSBOp3ObeG1N1+CnQnyc9mOkedroE9ZDx+1P7zKJ4qsI1jyYRJ1+2OxLBshbIqY4=",
        "Dgtlenvlp": "MvXuUCz6PVUBb7xJhkJ6eU8QmPrgNL3lSgt5XQRiAsjdbeoQf3WapDlmHKIgr9Kj9wJFCw6ovl+5xd77xAtWynr8Xl+puaihAFhXN05DWEvBBv5Qjhm7gmzFdf1davKM/DMMWParIVusIDWJvKTyviSIuUsnIA50RFBuHcSC9KWXLioLEQht1L4BFR3F1M0/pFDnT2///VjM3PsvT/iFlDB82pXL4y+AA7EADE5aD5PrLG6ah57iNOrQUeJBmf8FCXXG8JoU/W/a3KqgOG0DwCi0fgSFWC7XuJXrTCJZBROi7LvLnWkvRaKk9LOHseUGAyuUJUENi5C3TbztDRfXSg=="}, )
    print(r1)


# 清除redis缓存
def flushDb():
    r = RedisSqldata()
    list_keys = r.keys("code*")
    for key in list_keys:
        r.delete(key)


if __name__ == '__main__':
    getPhoneMessage()
