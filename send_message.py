from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib

class Send_Message:
    fromaddress = 'sample@gmail.com'
    toaddress = 'sample@hotmail.co.jp'
    password = 'password'

#初期化
    def __init__(self, fromaddress, toaddress, password):
        self.fromaddress = fromaddress
        self.toaddress = toaddress
        self.password = password


    def send(self, content):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.fromaddress, self.password)

        msg = MIMEText(content)
        msg['Subject'] = 'subject'
        msg['From'] = self.fromaddress
        msg['To'] = self.toaddress
        msg['Date'] = formatdate()

        smtpobj.sendmail(self.fromaddress, self.toaddress, msg.as_string())
        smtpobj.close()