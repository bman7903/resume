import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from res import Resume

username = 'XXXXXXX'
password = 'XXXXXXX'
msg = MIMEMultipart('alternative')

msg['Subject'] = "Resume"
msg['From']    = "myemail@things-n-stuff.appspotmail.com" 
msg['To']      = "bman7903@gmail.com"

text = " "
part1 = MIMEText(text, 'plain')

html = str( Resume( 'one', 'two' ) )
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

s = smtplib.SMTP('smtp.mandrillapp.com', 587)

s.login(username, password)
s.sendmail(msg['From'], msg['To'], msg.as_string())

s.quit()
