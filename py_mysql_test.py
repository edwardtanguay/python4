import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	port="3306",
	password="rootroot",
	database="world"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM city")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)




	