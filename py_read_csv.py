data = []
try:
	file = open("data/text2.csv", "r")
	for line in file:
		data.append(line.split(";"))
	file.close()
except FileNotFoundError as e:
	print("This file was not found: ", e)
else:
	print(data)
	print("-" * 50)
	print(data[2:3])
	print("-" * 50)
	print(data[2][1])