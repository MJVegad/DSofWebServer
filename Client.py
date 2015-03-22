import random;

class Client:
	"""Information related to each client"""
	
	def __init__(self, clientId, thinkTimeDistribution, param1, clientStatus, param2=None):
		if thinkTimeDistribution == 0: #constant
			self.thinkTime = constantDistributionValue
		elif thinkTimeDistribution == 1: #uniform
			self.thinkTime = random.uniform(param1, param2) #param1 to param2- range a to b
		elif thinkTimeDistribution == 2: #normal
			self.thinkTime = random.normalvariate(param1, param2) #param1 - Mu, param2 - Sigma
		elif thinkTimeDistribution == 3: #exponential
			self.thinkTime = random.expovariate(param1)   #param1 - lambda	

		self.clientId = clientId
		self.clientStatus = clientStatus    #0 - thinking, 1 - waiting for response