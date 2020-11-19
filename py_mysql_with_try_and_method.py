from os import error
import mysql.connector as mysql

def connect(db_name):
	try:
		return mysql.connect(
			host="localhost",
			user="root",
			port="3306",
			password="rootroot",
			database=db_name)
	except error as e:
			print(e)

if __name__ == '__main__':
	db = connect("onespace")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM flashcards")
	records = cursor.fetchall()

	count = 1
	for record in records:
		if count == 5:
			break
		print(count, record[1:4])
		count = count + 1
	
	db.close()
