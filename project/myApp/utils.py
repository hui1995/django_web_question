#!/usr/bin/env python


"""
  @Author:  hui
  @Description: 
  @WebSite : https://www.breathcoder.cn
  @File:  test
  @Version: 1.0.0
  @Date: 2020/5/14 11:12 PM
 """

# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail:
    def __init__(self):
        # 第三方 SMTP 服务

        self.mail_host = "smtp.qq.com"  # 设置服务器:这个是qq邮箱服务器，直接复制就可以
        self.mail_pass = "Testingbob"  # 刚才我们获取的授权码
        self.sender = 'testing.bobw@gmail.com'  # 你的邮箱地址
        self.receivers = ['396811467@qq.com']  # 收件人的邮箱地址，可设置为你的QQ邮箱或者其他邮箱，可多个

    def send(self,info):

        content = info
        message = MIMEText(content, 'plain', 'utf-8')

        message['From'] = Header("发件人名字，可自由填写", 'utf-8')
        message['To'] = Header("收件人名字，可自由填写", 'utf-8')

        subject = 'xxxxx'  # 发送的主题，可自由填写
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP(self.mail_host, 587)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            smtpObj.quit()
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print(e)

            print('邮件发送失败')


if __name__ == '__main__':
    mail = Mail()
    mail.send("测试")