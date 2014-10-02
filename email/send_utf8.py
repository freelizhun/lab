#!/usr/bin/env python
# -*- coding: utf-8 -*-
from email.header    import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL

# provide credentials
login = 'wcmein@yahoo.com'
password = '2xuiuiji'

# create message
msg = MIMEText('哈哈哈', 'plain', 'utf-8')
msg['Subject'] = Header('大部份測試', 'utf-8')
msg['From'] = login
msg['To'] = 'junmein@hotmail.com'

# send it   
s = SMTP_SSL('smtp.mail.yahoo.com', timeout=10) #NOTE: no server cert. check
s.set_debuglevel(0)
try:
    s.login(login, password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
finally:
    s.quit()
