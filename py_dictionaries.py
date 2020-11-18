computer = {
	"operatingSystem": "windows",
	"location": "sales",
	"type": "lenovo"
}
print(computer)
print(computer['location'])
computer['type'] = "dell"
print(computer.get("type"))

# loop
print("--KEYS AND VALUES:")
for key in computer:
	print(key + " = " + computer[key])

print("--VALUES")
for value in computer.values():
	print(value)

print("--KEYS AND VALUES")
for key,value in computer.items():
	print(key + " = " + value)

if "location" in computer:
	print("Yes, it has a location")

print(len(computer))

computer["diskSpaceGigabytes"] = 1000
print(computer)
backupComputer = computer.copy()
computer.popitem() # removes last inserted item
print(computer)
computer.pop("location")
print(computer)
del computer['type']
print(computer)
computer.clear()
print(computer)
del computer
print(backupComputer)
secondBackupComputer = dict(backupComputer)
print(secondBackupComputer)

# nested dictionaries
children = {
  "child1" : {
    "name" : "John",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2000
  },
  "child3" : {
    "name" : "Jack",
    "year" : 2011
  }
}
print(children)

secondComputer = dict(location = "sales", diskSpaceGigabytes = 500)
print(secondComputer)