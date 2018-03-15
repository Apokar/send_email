#encoding=utf-8
import time
import datetime
import pyodbc
import smtplib
from email.mime.text import MIMEText
from email.header import Header
alertThresSeconds = 3600
alertInterval = 10800
algReceivers = ['leiming@somaodata.com','shenyukuan@somaodata.com']
etlReceivers = ['jiangzhibin@somaodata.com','shenyukuan@somaodata.com','wangbiao@somaodata.com']
mail_host="smtp.somaodata.com"  #设置服务器
mail_user="service@somaodata.com"    #用户名
mail_pass="Somao1129"   #口令 
sender = 'service@somaodata.com'

def sendMail(receivers,text):
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("service@somaodata.com", 'utf-8')
    message['To'] =  Header(",".join(receivers), 'utf-8')
     
    subject = 'Somaodata Prod Monitor Service'
    message['Subject'] = Header(subject, 'utf-8')
     
    while True:
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            print u"邮件发送成功 接收者：\n%s\nText:\n%s"% (",".join(receivers),text)
            break
        except smtplib.SMTPException:
            print u"Error: 无法发送邮件,20秒后重新发送"
            time.sleep(20)

if __name__ == '__main__': 
    #sendMail(algReceivers,"prod text sending... 201712151448")
    monitorDic = {}
    alertDic = {}
    alertHisDic = {}
    for receiver in (etlReceivers+algReceivers):
        alertDic[receiver] = ""
    while True:
        # update alertHisDic
        conn = pyodbc.connect('DRIVER={MySQL ODBC 5.1 Driver};Server=sh-cdb-o5mf4yqk.sql.tencentcdb.com;Port=63631;Database=somao;User=root; Password=Somao@520;Option=3)')
        cursor = conn.cursor()
        cursor.execute("select id from s_explore where status!='3' and createtime>='2017-12-01'")
        pairs = cursor.fetchall()
        cursor.close()
        conn.close()
        if len(pairs)==0:
            print "No missions processing... %s" % (str(datetime.datetime.now()))
        for pair in pairs:
            if pair[0] in alertHisDic.keys():
                if (datetime.datetime.now()-alertHisDic[pair[0]]).seconds<=alertInterval:
                    print "Alert just now... Skip... %s" % pair[0]
                    continue
                else:
                    del alertHisDic[pair[0]]
            if not monitorDic.has_key(pair[0]):
                monitorDic[pair[0]] = datetime.datetime.now()
            else:
                if (datetime.datetime.now()-monitorDic[pair[0]]).seconds>=alertThresSeconds:
                    alertHisDic[pair[0]] = datetime.datetime.now()
                    print "Alert locating... id:\n%s" % pair[0]
                    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.3,1433;DATABASE=ML;UID=sa;PWD=somao@520')
                    cursor = conn.cursor()
                    sqlstr = "select case when sum(1) is null then 0 else sum(1) end,sum(case when flag='0' then 1 else 0 end) from cfb.dbo.ml_cmpy_tmp where id='%s'" % pair[0]
                    cursor.execute(sqlstr)
                    res1 = cursor.fetchall()
                    sqlstr = "select case when sum(1) is null then 0 else sum(1) end,sum(case when flag='0' then 1 else 0 end) from cfb.dbo.ml_result where id='%s'" % pair[0]
                    cursor.execute(sqlstr)
                    res2 = cursor.fetchall()
                    if res1[0][0]==0:   # first syn not comlete
                        for etlReceiver in etlReceivers:
                            alertDic[etlReceiver] += "id:%s no data in cfb.dbo.ml_cmpy_tmp\n%s\n" % (pair[0],str(datetime.datetime.now()))
                    else:    #first syn comlete
                        if res2[0][0]==0: # alg didn't product any result
                            for algReceiver in algReceivers:
                                alertDic[algReceiver] += "id:%s no data in cfb.dbo.ml_result\n%s\n" % (pair[0],str(datetime.datetime.now()))
                        else: # alg product some result,but second syn not work
                            for etlReceiver in etlReceivers:
                                alertDic[etlReceiver] += "id:%s has data in cfb.dbo.ml_result but mission failed\n%s\n" % (pair[0],str(datetime.datetime.now()))
        for key in alertDic:
            if alertDic[key]!="":
                sendMail([key],alertDic[key])
                alertDic[key] = ""
        time.sleep(120)

     
