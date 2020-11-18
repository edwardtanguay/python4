data = []
file = open("data/text.csv", "r")
for line in file:
	data.append(line.split(";"))
file.close()

print(data)
print("-" * 50)
print(data[2:3])
print("-" * 50)
print(data[2][1])