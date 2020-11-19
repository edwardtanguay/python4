import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	port="3307",
	password="rootroot",
	database="onespace"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM persons")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)




	