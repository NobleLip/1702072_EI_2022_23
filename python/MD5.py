import hashlib
from itertools import combinations_with_replacement
import time

Letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~0123456789'

str2hash = "337b12e511ed93f8bb08c3d606c3b21a"

Zeros = 1

StartingTime = float(time.time())

while True:
	for r in range(1, 50):
		for combo in combinations_with_replacement(Letters, r=r):
			result = hashlib.md5((str2hash.join(combo)).encode())
			final = str(result.hexdigest())
			if final[0:Zeros] == "0"*Zeros:
				print("MD5 : ", end ="")
				print(final + "  With : "+ ''.join(combo) + " Time To Find : "+ str(float(time.time())-StartingTime ) + " Seconds")
				StartingTime = float(time.time())
				Zeros = Zeros + 1
				break
			else:
				print("MD5 : "+final, end ="\r")
 
# printing the equivalent hexadecimal value.



