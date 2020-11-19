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

def add_flashcard(cursor, category, front, back):
	data = (category, front, back)
	cursor.execute("INSERT INTO flashcards (category, front, back) VALUES (%s, %s, %s)", data)

if __name__ == '__main__':
	db = connect("onespace")
	cursor = db.cursor()
	add_flashcard(cursor, "spanish", "house", "la casa")
	db.commit()
	db.close()
