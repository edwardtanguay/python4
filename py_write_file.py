import os
fp = open("data/testfile.txt", "w")
for x in range(1,100):
	fp.write("this is the first line\n")
fp.close()