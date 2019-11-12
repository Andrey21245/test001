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

for N in "Andrey":
	prefix=""
	suffix=""
	for i in range(1,100):
		j=i
		k=99-i
		while j >0:
			prefix += "-"
			j -=1
		while k >0:
			suffix += "-"
			k -=1
		output="\r" + prefix+"X"+suffix	
		stdout.write(output)
		stdout.flush()
		#print(output)
		sleep(0.01)
		prefix=''
		suffix=''	
stdout.write("\n") # move the cursor to the next line