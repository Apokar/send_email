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
        # s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # qq邮箱发
        s = smtplib.SMTP_SSL("smtp.mxhichina.com", 465)
        s.login(sender_email, sender_passwd)
        for receiver in receiver_list:
            s.sendmail(sender_email, receiver, content.as_string())
            print '给 ' + receiver + ' 的邮件,发送成功!' + str(datetime.datetime.now())
        s.quit()
        print "Success!"
    except smtplib.SMTPException, e:
        print "Falied,%s" % e[0]
        print e[1].decode('gbk')


def make_content():
    # HTML 内容(文本+图片)
    contentRoot = MIMEMultipart('related')
    contentRoot['Subject'] = '批量邮件测试'
    contentRoot["From"] = sender_email

    # 文本 内容
    content_text = MIMEText(
        '<html>'
        '<head>'
        '<title>email</title>'
        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
        '</head>'
        '<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">'
        '<!-- Save for Web Slices (email.png) -->'
        '<table id="__01" width="750" height="1300" border="0" cellpadding="0" cellspacing="0">'
        '<tr>'
        '<td colspan="3">'
        '<img src="http://www.somaodata.com/upload/email/email_01.gif" width="750" height="1145" alt=""></td>'
        '</tr>'
        '<tr>'
        '<td rowspan="2">'
        '<img src="http://www.somaodata.com/upload/email/email_02.gif" width="53" height="155" alt=""></td>'
        '<td>'
        '<a href="http://www.somaodata.com/cooperation"'
        'onmouseover="window.status="跳转搜猫数据";  return true;"'
        'onmouseout="window.status='';  return true;">'
        '<img src="http://www.somaodata.com/upload/email/email_03.gif" width="640" height="59" border="0" alt=""></a></td>'
        '<td rowspan="2">'
        '<img src="http://www.somaodata.com/upload/email/email_04.gif" width="57" height="155" alt=""></td>'
        '</tr>'
        '<tr>'
        '<td>'
        '<img src="http://www.somaodata.com/upload/email/email_05.gif" width="640" height="96" alt=""></td>'
        '</tr>'
        '</table>'
        '<!-- End Save for Web Slices -->'
        '</body>'
        '</html>'

        '<p><b>葛鑫  销售总监</b></p>'
        '<p>微信：<b>15805165835</b></p>'
        '<p>QQ：<b>1905487560</b></p>'
        '<p>Mobile：<b>15805165835</b></p>'
        '<p>E - mail：<b>gexin@somaodata.cm</b></p>'
        '<p>Add：<b>南京市鼓楼区新模范马路66号物联网科技园12楼1201</b></p>'
        ,
        'html',
        'utf-8')
    contentRoot.attach(content_text)

    # 图片内容

    # fp = open('/Users/huaiz/PycharmProjects/send_email/test_img.jpeg', 'rb')
    # content_image = MIMEImage(fp.read())
    # fp.close()
    #
    # content_image.add_header('Content-ID', 'image_id')
    # contentRoot.attach(content_image)

    return contentRoot


if __name__ == '__main__':
    # 接受邮箱列表
    receiver_list = ['wuhuaizheng@somaodata.com','leiming@somaodata.com']

    # 发件人信息
    sender_email = 'gexin@somaodata.com'
    sender_password = 'somao@520'

    content = make_content()

    # 发送
    email_sender(receiver_list, sender_email, sender_password, content)
