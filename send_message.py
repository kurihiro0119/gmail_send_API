from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib

fromaddress = 'sample@gmail.com'
toaddress = 'sample@hotmail.co.jp'
password = 'password'

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()

#メールアドレスとパスワードを変更してください。
smtpobj.login(fromaddress, password)

msg = MIMEText('body message')
msg['Subject'] = 'subject'
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Date'] = formatdate()
print(msg)

smtpobj.sendmail(fromaddress, toaddress, msg.as_string())
smtpobj.close()