# -*- coding: utf-8 -*-
# @Time         : 2018/2/16 23:51
# @Author       : Huaiz
# @Email        : Apokar@163.com
# @File         : email_reminder.py
# @Software     : PyCharm Community Edition
# @PROJECT_NAME : steam_market_spider

import smtplib
from email.mime.text import MIMEText


def send_email(link, item_name):
    _user = "729975476@qq.com"
    _pwd = "lhimuhzrhkhcbehf"
    _to = "apokar@163.com"

    mail_msg = """
    <p> Batman , 你想买的"""+item_name+"""已找到符合价位的那一个,已经加入购物车,赶紧去看看...</p>
    <p><a href=""" + link + """>这是链接</a></p>"""

    msg = MIMEText(mail_msg, 'html', 'utf-8')

    msg["Subject"] = "igxe 扫到货了!"
    msg["From"] = _user
    msg["To"] = _to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print "Success!"
    except smtplib.SMTPException, e:
        print "Falied,%s" % e

