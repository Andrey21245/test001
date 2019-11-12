#print("START")
# i = 15
# n = 15
# while(i != 0):
# 	while(n != 8):
# 		print("_")
# 		n = n-1
# 	print("@")
# 	while(n != 0):
# 		print("_")
# 		n = n-1

from sys  import stdout
from time import sleep

prefix=""
suffix=""

for i in range(1,20):
	j=i
	k=20-i

	while j >0:
		prefix += "-"
		j -=1

	while k >0:
		suffix += "-"
		k -=1

	output=prefix+"X"+suffix	
	
	stdout.write("\r%s" % output)
	stdout.flush()
	sleep(0.1)
	c=''
	e=''
stdout.write("\n") # move the cursor to the next line