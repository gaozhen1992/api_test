import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
import sys
sys.path.append('..')
from config.config import *


def send_email(report_file):
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = '18621626990@163.com'  # 发件人
    msg['To'] = '352282664@qq.com'  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开 从配置文件中读取
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="{}"'.format(report_file)  # filename为邮件中附件显示的名字  参数化一下report_file
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server,465)  # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user, smtp_password)  # 用户名和密码
        smtp.sendmail(sender, receiver, msg.as_string())
        #smtp.sendmail("352282664@qq.com", "2329178575@qq.com", msg.as_string())  # 发送给另一个邮箱
        logging.info("邮件发送完成！")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()
