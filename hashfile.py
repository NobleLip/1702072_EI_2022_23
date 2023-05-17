import hashlib
from colorama import init,Fore, Style
import os
import rsa
import argparse

arr = os.listdir()


parser = argparse.ArgumentParser(description='Sign files')
parser.add_argument('--all', metavar='True/False', dest= 'all',
                    help='Sign all files in directory')
parser.add_argument('--file', metavar = "Name of File", dest= 'file',
                    help='File to Sign')

args = parser.parse_args()



init(autoreset=True)

def hash(fname):
	HashTypes = [hashlib.md5(),hashlib.sha1(),hashlib.sha224(),hashlib.sha256(),hashlib.sha384(),hashlib.sha512(),hashlib.blake2b(),hashlib.blake2s()]
	HashNames = ["MD5","SHA1","SHA224","SHA256","SHA384","SHA512" ,"BLAKE2B","BLAKE2S"]
	print('\n['+Fore.YELLOW+'+'+Fore.WHITE+'] '+'A Assinar o ficheiro : '+ Fore.YELLOW+fname+Fore.WHITE+'\n')
	KeyTXTFile = open("KeyChain.txt", "a")
	for i in range(len(HashTypes)):
		(pubkey, privkey) = rsa.newkeys(512)
		KeyTXTFile.write("\n------------"+fname+" -> "+HashNames[i]+"------------")
		KeyTXTFile.write("\n\n"+str(pubkey))
		KeyTXTFile.write("\n\n"+str(privkey)+"\n") 
		hashAll = HashTypes[i]
		f = open(fname[:-4]+HashNames[i]+"Assinado.txt", "wb")
		fi = open(fname, "rb")
		f.write(fi.read())
		fi.close()
		with open(fname, "rb") as fi:
			for chunk in iter(lambda: fi.read(4096), b""):
				hashAll.update(chunk)
			hashAll.update(str(privkey)[11:-1].encode())
			hashDone = hashAll.hexdigest()
			print('	['+Fore.GREEN+'+'+Fore.WHITE+'] '+ HashNames[i] +'('+fname+', Private Key) = H1 :'+Fore.GREEN+Style.BRIGHT+ hashDone)
			f.write("\nHash(Mensagem, ChavePrivada) = H1 = ".encode()+ hashDone.encode())
			hashPub = HashTypes[i]
			hashPub.update((str(hashDone)+str(str(pubkey)[10:-1])).encode())
			hashPubDone = hashPub.hexdigest()
			f.write("\nHash(H1, ChavePublica) = H2 = ".encode()+ hashPubDone.encode())
			f.write("\nChave Publica = ".encode()+ str(str(pubkey)[10:-1]).encode())
			print('	['+Fore.GREEN+'+'+Fore.WHITE+'] '+ HashNames[i] +'(H1, Public Key) = H2 :'+Fore.GREEN+Style.BRIGHT+ hashPubDone+"\n")
			fi.close()
		#Escreve o ficheiro Linha
		f.close()
		#Fechar
	return print('['+Fore.GREEN+'+'+Fore.WHITE+'] '+ ' File Done Hashing')

arr.remove("hashfile.py")
if (args.all == "True"):
	for i in arr:
		hash(i)
elif (args.file != None):
	hash(args.file)
else:
	parser.print_help()

