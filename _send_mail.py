import smtplib 
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
receiver="joseph0402050104@gmail.com"
sender="chiumoon313@gmail.com"
Title="Test Email"
body= "this is python class testing"

msg=MIMEMultipart()
msg['From']=sender
msg['To']=receiver
msg['Subject']=Header(Title,'utf-8').encode()


msg.attach(MIMEText(body))
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender,"zaihigctjdcuatni")
    server.sendmail(sender,receiver,msg.as_string())
print("success send mail")