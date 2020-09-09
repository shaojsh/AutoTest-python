import base64

import pymysql
import redis

# db数据操作
from run_all_uicase import yamldict


def Sqldata(sqlStr, flag):
    db = yamldict['test_db_list']['db1']
    if flag == 2:
        db = yamldict['test_db_list']['db2']
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

# if __name__ == '__main__':
#     A = getPhoneMessage()
#     print(A)
