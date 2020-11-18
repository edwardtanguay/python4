persons = {"Plato", "Cicero", "Aristotles"}
print(persons)
persons.add("Parmenides") # doesn't necessarily add it to the end (sets are unordered)
print(persons)
persons.update(["Socrates","Pythagoras"])
print(persons)
persons.remove("Plato") # if doesn't exist, throws error
persons.discard("Aristotles") # if doesn't exist, no error
print(persons)
# always a different order
for person in persons:
	print(person)

if ("Cicero" in persons):
	print("Yes, Cicero is in the set")


frenchPersons = {"Descartes", "Sartre"}
both = persons.union(frenchPersons)
print(both)

persons.clear()
print(len(persons))
del persons