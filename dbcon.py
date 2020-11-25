import mysql.connector


mydb = mysql.connector.connect(host="localhost",user="pratik",passwd="1234",database="School")

mycursor = mydb.cursor()

mycursor.execute("select * from Student")
result = mycursor.fetchone()
for i in result:
	print(i)