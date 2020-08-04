import os

import pymysql

from common.Yaml_Data import HandleYaml

root_dir = os.path.dirname(os.path.abspath('.'))
handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol.yaml')

yamldict = handleyaml.get_data()


def getSqldata(sqlStr):
    # 连接数据库
    connect = pymysql.connect(
        host=yamldict['test_db_list']['host'],
        user=yamldict['test_db_list']['user'],
        password=yamldict['test_db_list']['password'],
        port=yamldict['test_db_list']['port'],
        db=yamldict['test_db_list']['db']
    )
    # 创建一个游标对象:有两种创建方法
    cursor = connect.cursor()  # 或：cursor=pymysql.cursors.Cursor(connect)
    # 使用游标的execute()方法执行sql语句
    cursor.execute(sqlStr)
    # 使用fetchall()获取全部数据
    r1 = cursor.fetchall()
    print(r1)
    return r1
    # 关闭游标连接
    cursor.close()
    # 关闭数据库连接
    connect.close()


if __name__ == '__main__':
    sqlstr = yamldict['test_db_sqllist']['sql0000001']
    data = getSqldata(sqlstr)
    print(data[0][0])
