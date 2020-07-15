import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import walk

EMAIL_ADDRESS="#@gmail.com"
PASSWORD="#"
SUBJECT = "Send attachment"
BODY = "This is a test email for send attachment"




# send message function 
def send_email(subject,msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS,PASSWORD)
        messages = "subject ".format(subject,msg)
        server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,messages)
        server.quit()
        print("email has been sent")
    except:
        print("email sent failed")

subject = "test"

msg = MIMEMultipart()
msg['Subject'] = SUBJECT
msg.attach(MIMEText(BODY,'plain'))
text = msg.as_string()

send_email(subject,msg)



# change the directory 
for dirpath,dirnames, filenames in walk('/Users/ammarfalmban/Desktop/send'):
    print(filenames)
    

