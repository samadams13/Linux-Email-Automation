import smtplib, ssl, time, os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

'''
This file takes the SMTP Sender Email address, Receiver Email address as inputs and 
sends a mail with a specific message using GMail as the SMTP server.

This file is useful to send mails from the commandline or programmatically without opening a browser

'''
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "" # Enter sender's email
receiver_email = ""  # Enter receiver address
password = "" #Enter sender's pass
date = time.ctime()
message = MIMEMultipart()
text = MIMEText("""\
Subject: [Web Development Course Reminder]

This message is sent because you have took oath that you will study daily web development. So, start now.
Current Time/Date: {date}
--Abhishek Raj
--Naam to suna hi hoga.""")
message.attach(text) #attaches text to the email
img_data = open('', 'rb').read() #Enter image filename
image = MIMEImage(img_data, name=os.path.basename()) #Enter image filename
message.attach(image) #attaches image to the email

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
