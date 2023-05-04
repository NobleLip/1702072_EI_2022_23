import hashlib
from colorama import init,Fore, Style
import os

arr = os.listdir()


init(autoreset=True)

def hash(fname):
	HashTypes = [hashlib.md5(),hashlib.sha1(),hashlib.sha224(),hashlib.sha256(),hashlib.sha384(),hashlib.sha512(),hashlib.blake2b(),hashlib.blake2s()]
	HashNames = ["MD5","SHA1","SHA224","SHA256","SHA384","SHA512" ,"BLAKE2B","BLAKE2S"]
	print('\n['+Fore.YELLOW+'+'+Fore.WHITE+'] '+' Hashing File '+ Fore.YELLOW+fname)
	for i in range(len(HashTypes)):
		hashAll = HashTypes[i]
		with open(fname, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hashAll.update(chunk)
		hashDone = hashAll.hexdigest()
		print('	['+Fore.GREEN+'+'+Fore.WHITE+'] '+ HashNames[i] +':'+Fore.GREEN+Style.BRIGHT+ hashDone)
	return print('['+Fore.GREEN+'+'+Fore.WHITE+'] '+ ' File Done Hashing')


arr.remove("hashfile.py")
for i in arr:
	hash(i)