'''
Note : Let less secure apps access your account
https://myaccount.google.com/lesssecureapps
'''

import requests
from pyquery import PyQuery as pq
import smtplib
from email.mime.text import MIMEText
import time

dataUrl = 'http://www.miramarcinemas.tw/Home/startordertime'  #美麗華開放預購票訂位網址
doc = pq(url=dataUrl)
fc = doc('.content .row>p').filter(lambda i: i > 1 ).text(squash_space=False)
##print(fc)   

gmail_user = 'makyean@gmail.com' ##sender
gmail_password = '' ##gmail password

msg = MIMEText(fc)
msg['Subject'] = 'New Movie List'
msg['From'] = gmail_user
msg['To'] = 'makyean@gmail.com' ##addressee

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()
print('NewMovie Email sent!')