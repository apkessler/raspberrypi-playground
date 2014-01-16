import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import getpass

def send_mail(send_from, password, send_to, subject, text, files=[], server="smtp.gmail.com",port=587):
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server,port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(send_from,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    
def promptAndSend(files=[]):
    this_user = raw_input('User?')
    this_pwd = getpass.getpass()

    send_mail(this_user,this_pwd,[this_user],'Hi!','Testing...',files)

