import os 

# fp = open(os.path.abspath("C:/edward/nwo/onespace/src/custom/data/itemsHowtos.json"), "rb")
# fp = open(os.path.abspath("C:/edward/nwo/onespace/src/custom/data/itemsQuotes.txt"), "r")
fp = open("py_read_file.py", "r")
# print(fp.read())
for line in fp:
	print(line.rstrip())
fp.close()

print(os.getcwd())