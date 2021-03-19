from email import message
import smtplib

username = "som.jaiswal.sj4@gmail.com"
password = "59865412357"

recieverEmail = "prakharshrivastav971@gmail.com"
subject = "Email Form Python"
message = "I am a python master"

server = smtplib.SMTP_SSL(host='smtp.gmail.com',port='465')
server.login(username,password)
server.sendmail(username,recieverEmail,message)
print("Email sent")
server.quit()

