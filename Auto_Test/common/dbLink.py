import os

import pymysql

# db数据操作
from run_all_uicase import yamldict


def Sqldata(sqlStr, by, flag):
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

    Sqldata(sqlStr1, 'select', 1)
    Sqldata(sqlStr2, 'delete', 1)
    Sqldata(sqlStr3, 'delete', 1)
