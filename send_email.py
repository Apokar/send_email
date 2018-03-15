# -*- coding: utf-8 -*-
# @Time         : 2018/3/15 10:30
# @Author       : Huaiz
# @Email        : Apokar@163.com
# @File         : send_email.py
# @Software     : PyCharm Community Edition
# @PROJECT_NAME : send_email

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def email_sender(receiver_list, sender_email, sender_passwd, content):
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(sender_email, sender_passwd)
        for receiver in receiver_list:
            s.sendmail(sender_email, receiver, content.as_string())
            print '给 ' + receiver + ' 的邮件,发送成功!' + str(datetime.datetime.now())
        s.quit()
        print "Success!"
    except smtplib.SMTPException, e:
        print "Falied,%s" % e


def make_content():
    # HTML 内容(文本+图片)
    contentRoot = MIMEMultipart('related')
    contentRoot['Subject'] = '批量邮件测试'
    contentRoot["From"] = sender_email

    # 文本 内容
    link = 'https://github.com/Apokar/'
    content_text = MIMEText(
        '<p><b>My<a href=' + link + '><i> Github </i></a>link</b></p> '
        '<p>And Batman.</p><p><img alt="" src="cid:image_id" /></p> '
        '<p><li>good!</p>',
        'html',
        'utf-8')
    contentRoot.attach(content_text)

    # 图片内容

    fp = open('/Users/huaiz/PycharmProjects/send_email/test_img.jpeg', 'rb')
    content_image = MIMEImage(fp.read())
    fp.close()

    content_image.add_header('Content-ID', 'image_id')
    contentRoot.attach(content_image)

    return contentRoot


if __name__ == '__main__':
    # 接受邮箱列表
    receiver_list = ['apokar@163.com', 'wuhuaizheng@somaodata.com']

    # 发件人信息
    sender_email = '729975476@qq.com'
    sender_password = 'lhimuhzrhkhcbehf'

    content = make_content()

    # 发送
    email_sender(receiver_list, sender_email, sender_password, content)
