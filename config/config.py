import logging
import os
import time

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())
log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report_{}.html'.format(now))  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

# 数据库配置
db_host = 'localhost'   # 自己的服务器地址
db_port = 3306
db_user = 'root'
db_passwd = '7758258'
db = 'test2'

# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '18621626990@163.com'
smtp_password = 'DETYHFRVXQNVPRHJ'

sender = smtp_user  # 发件人
receiver = '352282664@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

send_email_after_run = False #增加send_email()开关