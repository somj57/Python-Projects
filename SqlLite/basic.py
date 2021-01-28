'''
("UPDATE store  SET Email=?,Phno=? WHERE Name=?"(email,phon,name))
Python3 comes with sql lite preinstalled
'''

import sqlite3
import time
def create_table():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store(Name Text ,Email Text,Phno Integer)")
	conn.commit()
	conn.close()

def insert_data(name,email,phno):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES (?,?,?)",(name,email,phno))
	conn.commit()
	conn.close()


def view(item):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store WHERE Name=?",(item,))
	rows = cur.fetchall()
	conn.close()
	return rows

def view1():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(item):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM store WHERE Name=?",(item,))
	conn.commit()
	conn.close()


print("Enter 1 to insert \nEnter 2 to show data \nEnter 3 to delete ")
bol = int(input("Enter Your choice : "))
if bol == 2:
	opt = int(input("Enter 1 to print all 2 to item : "))
	if opt ==2:
		item = input("Enter name : ")
		dat = view(item)
		for i in dat:
			print(i)
	elif opt ==1:
		dat = view1()
		for i in dat:
			print(i)
	else:
		print("Wrong input")
elif bol == 1:
	name=input("Enter Name : ")
	email = input("Enter email : ")
	phno = int(input("Enter phno : "))
	insert_data(name,email,phno)

elif bol ==3:
	dele = input("Enter Name : ")
	delete(dele) 
	print("Deleted")
else:
	print("Wrong")
