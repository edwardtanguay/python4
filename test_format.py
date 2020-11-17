age = 34
next = 35
fruits = ['apple', 'orange']
message = "James is {} this year and next year will be {}."
print(message.format(age, next))
print(message.upper())
print(message.replace("i", "a"))
print(message.endswith("nnn"))

if 'applex' in fruits:
	print('yes')

print(len(fruits))