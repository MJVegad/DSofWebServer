import random;

class Client:
	"""Information related to each client"""
	
	def __init__(self, clientId, thinkTimeDistribution, param1, clientStatus, param2=None):
		

		self.clientId = clientId
		self.thinkTimeDistribution = thinkTimeDistribution
		self.paramThinkTime1 = 0
		self.paramThinkTime2 = 0

		if param2 is None:
			self.thinkTime = self.getThinkTime(thinkTimeDistribution, param1)
			self.paramThinkTime1 = param1
		else:
			self.thinkTime = self.getThinkTime(thinkTimeDistribution, param1, param2)
			self.paramThinkTime1 = param1
			self.paramThinkTime2 = param2

		self.clientStatus = clientStatus    #0 - thinking, 1 - waiting for response


	def getThinkTime(self, thinkTimeDistribution, param1, param2 = None):
		if thinkTimeDistribution == 0: #constant
			thinkTime = param1
		elif thinkTimeDistribution == 1: #uniform
			thinkTime = random.uniform(param1, param2) #param1 to param2- range a to b
		elif thinkTimeDistribution == 2: #normal
			thinkTime = random.normalvariate(param1, param2) #param1 - Mu, param2 - Sigma
		elif thinkTimeDistribution == 3: #exponential
			thinkTime = random.expovariate(param1)   #param1 - lambda
		return thinkTime