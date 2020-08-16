'''
install pandas,smpt
go to securities in email and allow unknown apps to login
make a excel file as email.xlsx and store emails in it 



'''
import pandas as pd
import smtplib

SenderAddress = "Sender Email Address"
password = "Password of sender"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(SenderAddress,password)
msg = "Hellow this is bulk email from python2"
subject = "Python"
body = "Subject : {}\n\n{}".format(subject,msg)


for email in emails:
	server.sendmail(SenderAddress,email,body)
	print("Email send . . . . .")
server.quit() 
