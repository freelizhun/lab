from cStringIO import StringIO
from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL
from smtplib import SMTP


from smtplib import SMTP_SSL


MAILBOX='jonahjun.wu'
PASSWD='2xuiuiji'
who ='%s@gmail.com'%MAILBOX
from_ = who
to_ = 'junmein@hotmail.com'
to=[to_]


headers=[
'From:%s' %from_,
'To: %s' % ','.join(to),
'Subject: test email server sending',
]
bodyC=' a href link: http:/asdfasdf/asdfasdfasfasfd/asfdasdfasdfasdf/'
body = [
    'Hello',
    'World',
     bodyC,
]

msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))
s = SMTP_SSL('smtp.gmail.com',465)
s.ehlo()
print 'login'
s.login(MAILBOX, PASSWD)
print 'send mail'
s.sendmail(from_, to, msg)
s.quit()
print 'mail sended'
