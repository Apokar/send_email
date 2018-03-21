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
from email.utils import parseaddr, formataddr
from email.header import Header
from email.utils import formataddr


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
    contentRoot['Subject'] = Header('搜猫数据打造人工智能销售新模式', 'utf-8')
    h = Header(u'搜猫数据', 'utf-8')
    h.append('<bd@somaodata.com>', 'ascii')
    contentRoot['From'] = h
    # contentRoot['From'] = Header(u'搜猫数据', 'utf-8')
    # contentRoot['From'] = Header(sender_email, 'utf-8')

    # 文本 内容
    content_text = MIMEText(

        '<html>'
        '<head>'
        '<title>email</title>'
        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
        '<style type="text/css">'
        '.border {'
        'border-top: 1px solid #ebebeb;'
        'margin-left: 65px;'
        'width: 650px;'
        '}'
        '.dm {'
        'margin-top: 20px;'
        '}'
        '</style>'
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
        '<div class="border">'
        '<table class="dm">'
        '<tbody>'

        '<tr>'
        '<td><b style="font-family:楷体,Times New Roman;font-size:16px">葛鑫</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">销售总监</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:楷体,Times New Roman;font-size:16px">微信</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">15805165835</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">QQ</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">1905487560</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">Tel</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">15805165835</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">Email</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">gexin@somaodata.com</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">Addr</b></td>'
        '<td><p style="font-family:楷体,Times New Roman;font-size:16px">南京市鼓楼区新模范马路66号物联网科技园12楼1201</p></td>'
        '</tr>'

        '</tbody>'
        '</table>'
        '</div>'
        '<!-- End Save for Web Slices -->'
        '</body>'
        '</html>'

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
    receiver_list = [

        'wuhuaizheng@somaodata.com'
        , 'leiming@somaodata.com'
        , 'wenwen@somaodata.com'
        , 'shenyukuan@somaodata.com'
    ]

    # 发件人信息
    sender_email = 'bd@somaodata.com'
    sender_password = 'somao@520'

    content = make_content()

    # 发送
    email_sender(receiver_list, sender_email, sender_password, content)
