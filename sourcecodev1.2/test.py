# import re#正则表达式模块
# import sys
# import os
# import time
# from case import *
# #检查case目录下放case的文件，返回的是最新存放用例的文件，因为后面是[-1],表示截取元组最后一个元素
# maincase=[i for i in dir() if 'ak' in i][-1]
# #将获取到的文件名首字母大写，其他字母变小写
# mainclass=maincase.capitalize()

# class Start:
#     def __init__(self):
#         #定义报告中统计的失败用例,通过用例,程序开始时间
#         self.pass_case=0#pass_case用来保存通过的用例数量
#         self.fail_case=0#fail_case用来保存未通过的用例数量
#         self.startime=time.time()
#         #starttime表示程序开始时间，time.time()方法用来计算两个时间点的间隔
#     def syscheck(self):
#         #实例化测试用例类
#         self.Test=eval('{}.{}()'.format(maincase,mainclass))
#         # #获取系统检查类用例
#         # checkcase=re.findall(r'check\d+',str(dir(self.Test)))#获取所有check名称
#         # #执行检查类用例
#         # for i in checkcase:
#         #     eval('self.Test.{}()'.format(i))
import time, datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#获取当前时间
now = time.strftime('%Y-%m-%d')
smtpserver = 'smtp.163.com'

user = 'tingtinggilr@163.com'
password = ''

sender = 'tingtinggilr@163.com'
receive = 'tingting.fan@bangcle.com'

subject = '测试' + now
content = '测试结果'

msg = MIMEText(content,'html','utf-8')
msg['Subject'] = Header(subject,'utf-8')
msg['From'] = sender
# msg['To'] = ','.join(receives)
msg['To'] = receive
smtp = smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print('Start send Email....')

smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print('发送结束')
