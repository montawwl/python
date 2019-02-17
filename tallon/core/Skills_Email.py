# -*- coding: utf-8 -*-
# @Time    : 2019-02-14 22:08
# @Author  : YangBo
# @File    : Skills_Email.py

#发邮件
import smtplib
from email.mime.text import MIMEText

receiver = input("输入接收者邮箱\n")
subject = input("邮件标题\n")
content = input("邮件内容\n")
host = "smtp.qq.com"  # QQ邮箱服务器

user_name = '352420160'  # 登录账号
pwd = 'aoqebpcsukpfbhab'  # SMTP密码
sender = '352420160@qq.com'  # 发送者邮箱

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = sender
message['to'] = receiver
message['Subject'] = subject

try:
    smtp_obj = smtplib.SMTP(host, 25)
    smtp_obj.login(user_name, pwd)
    smtp_obj.sendmail(sender, receiver, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException as error:
    print(error)
    print('邮件发送失败')
