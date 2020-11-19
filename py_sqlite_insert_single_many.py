import sqlite3
connection = sqlite3.connect('data/test.db')
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS flashcards (`id` INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, front TEXT, back TEXT)")

# insert single record
# cursor.execute("INSERT INTO flashcards (category, front, back) VALUES ('spanish', 'sky', 'el cielo')")
singleFlashcard = ('spanish', 'pen', 'el bolígrafo')
cursor.execute("INSERT INTO flashcards (category, front, back) VALUES (?,?,?)", singleFlashcard)

# insert multiple records
flashcards = [
	('spanish', 'table', 'la mesa'),
	('spanish', 'floor', 'el piso'),
	('spanish', 'window', 'la ventana'),
]
cursor.executemany("INSERT INTO flashcards (category, front, back) VALUES (?,?,?)", flashcards)

records = cursor.execute('SELECT * FROM flashcards')
for record in records:
	print(record)
connection.commit()
connection.close()