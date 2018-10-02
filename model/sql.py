"""
时间:2018年9月29日20:14:31
作者:小莫先生
功能:连接Mysql 查询账号的ID
"""
import pymysql

db_config = {
    'host': '192.168.200.100',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'charset': 'utf8',
    'db': 'zx'
}

def sql_con(account_name):
    conn_obj = pymysql.connect(**db_config)
    cur = conn_obj.cursor()
    sql_comm = "SELECT id FROM users WHERE name='2'"
    cur.execute(sql_comm)
    result = cur.fetchone()
    cur.close()
    conn_obj.close()
    return  result[0]


