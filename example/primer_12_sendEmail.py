from email.mime.text import MIMEText
import smtplib
import urllib
import time
import datetime
from email.utils import parseaddr,formataddr
from threading import Timer


def send_email():
    from_address = ''  # 发件人的邮箱地址及密码
    password = ''
    to_address = '' #lixiaopengbean@163.com

    stmp_server = 'smtp.126.com' # 输入STMP服务器地址

    current_time = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    #print(current_time)

    msgCount = '<html>' \
               '<body>' \
               '<h5>晚上好，李晓鹏:</h5>' \
               '<h5>今天('+ current_time + ')过得怎么样?今天写日记了吗?每天都要坚持记日记哦！</h5>' \
               '<h6><a href="http://www.baidu.com">百度搜索</a></h6></body>' \
               '</html>'
    msg = MIMEText(msgCount,'html','utf-8')
    msg['Subject'] = '记日记提醒！'
    msg['Content-Type'] = 'Text/HTML'
    msg['From'] = formataddr(["小宠物", from_address])
    msg['To'] = to_address
    print(msgCount)
    try:
        print('建立连接中.....')
        server = smtplib.SMTP(stmp_server, 25)
        server.set_debuglevel(1)
        print('模拟登陆中.....')
        server.login(from_address, password)
        print('发送邮件中.....')
        server.sendmail(from_address, [to_address], msg.as_string())
        server.quit()
        print ('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败'+e)

def timer_run(schedu_time):
    flag = 0
    while True:
        # print(format(schedu_time))
        # print(format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        if format(schedu_time) == format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
            #print('进入方法啦')
            send_email()
            flag = 1
            time.sleep(2)
        else :
            if flag == 1:
                schedu_time = schedu_time + datetime.timedelta(hours=24)
                #print(schedu_time)
                flag = 0
schedu_time = datetime.datetime(int(time.strftime("%Y")),int(time.strftime("%m")),int(time.strftime("%d")),21,30,0)
print('程序运行中,请勿关闭......')
timer_run(schedu_time)
