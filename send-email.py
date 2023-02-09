#!/usr/bin/python3
from email.message import EmailMessage
from password import password
import ssl
import smtplib

email_sender = "zhoujingfightinghahaha@gmail.com"
email_password = password

email_receiver = "254644528@qq.com"

subject = "This is test"
body = """
This is a hello from zhoujing
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender, email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())

