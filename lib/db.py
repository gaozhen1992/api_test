import pymysql
import sys
sys.path.append('..')  # 提升一级到项目更目录下
from config.config import *  # 从项目根目录下导入

#获取连接方法
def get_db_conn():
    conn = pymysql.connect(host=db_host,port=db_port,
                       user=db_user,passwd=db_passwd,
                       db=db,charset='utf8') # 如果查询中有中文，需指定测试集编码
    return conn

#封装数据库查询操作
def query_db(sql):
    conn = get_db_conn() #获取连接
    cur = conn.cursor() #建立游标
    logging.debug(sql) #输出执行的sql
    cur.execute(sql) #执行sql
    result = cur.fetchall() #获取所有查询结果
    logging.debug(result) #输出查询结果
    cur.close() #关闭游标
    conn.close() #关闭连接
    return result #返回结果


#封装更改数据库操作
def change_db(sql):
    conn = get_db_conn() #获取连接
    cur = conn.cursor() #建立游标
    logging.debug(sql) #输出执行的sql
    try:
        cur.execute(sql) #执行sql
        conn.commit() #提交更改
    except Exception as e:
        conn.rollback() #回滚
        logging.error(str(e)) #输出错误信息
    finally:
        cur.close() #关闭游标
        conn.close() #关闭连接


#封装数据库常用操作
def check_user(sname):
    #注意sql中''号嵌套的问题
    sql = "select * from student where sname = '{}' ".format(sname)
    result = query_db(sql)
    return True if result else False

def add_user(sid,sname,sage,ssex):
    sql = "insert into student (sid,sname,sage,ssex) values ('{}','{}','{}','{}')".format(sid,sname,sage,ssex)
    change_db(sql)

def del_user(sname):
    sql = "delete from student where sname = '{}'".format(sname)
    change_db(sql)















