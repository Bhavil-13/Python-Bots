import smtplib
from abc import msg

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('bhavilsharma001@gmail.com', '12P@0PP1330b')
server.sendmail('bhavilsharma001@gmail.com', 'bhavilsharma83@gmail.com', msg.message)