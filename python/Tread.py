import threading
import time
import random
import math

class Miner():
	def __init__ (self, cpu, gpu, cmpid):
		self.CPUPower = cpu
		self.GPUPower = gpu
		self.ComputerID = cmpid
		self.Bitcoins = 0
	
	def Minerar(self):
		LOGS = open("logsBTC.txt", "a")
		Time = 100-(int(self.CPUPower/2)+int(self.CPUPower/2))
		time.sleep(Time)
		Mined = math.log((self.CPUPower*self.GPUPower),2)
		self.Bitcoins += Mined
		LOGS.write('[MINED] Computer '+str(self.ComputerID)+'--> Mined : '+str(Mined) +' BTC\n')
		LOGS.close()

	def TreadMine(self):
		self.Tre = threading.Thread(target=self.Minerar)
		self.Tre.start()

	def JoinT(self):
		self.Tre.join()
		self.TreadMine()
	
	def GetBT(self):
		return self.Bitcoins

Computers = []

for i in range(10):
	Computers.append(Miner(random.randint(2,10),random.randint(2,10), i))


def TreadsControl():
	for i in Computers:
		i.TreadMine()
	while 1:
		Soma = 0
		for i in Computers:
			i.JoinT()
			Soma += i.GetBT()
		print(Soma," BTC's")
	
TreadControl = threading.Thread(target=TreadsControl)
TreadControl.start()

for i in threading.enumerate():
	print(i)
