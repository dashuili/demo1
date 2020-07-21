from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import smtplib

host_server = 'smtp.gmail.com'
sender = '1479085261@qq.com'
receivers = 'zhannd0828@gmail.com'
#pwd = 'secgflyewguoijdi'
pwd = 'rzznqfhexpylbagb'
body = "hello"
subject = 'qqmail'

smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender,pwd)

msg = MIMEText(body,'plain', 'utf-8')
msg["Subject"] = Header(subject, 'utf-8')
msg["From"] = sender
msg["To"] = receivers
smtp.sendmail(sender, receivers, msg.as_string())
smtp.quit()
