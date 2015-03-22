import random;

class Client:
	"""Information related to each client"""
	
	def __init__(self, clientId, thinkTimeDistribution, constantDistributionValue=None, uniformRangeA=None, uniformRangeB=None, normalMu=None, normalSigma=None, expoLambda=None, clientStatus):
		if thinkTimeDistribution == 0: #constant 
			self.thinkTime = constantDistributionValue
		elif thinkTimeDistribution == 1: #uniform
			self.thinkTime = random.uniform(uniformRangeA,uniformRangeB)
		elif thinkTimeDistribution == 2: #normal
			self.thinkTime = random.normalvariate(normalMu,normalSigma)
		elif thinkTimeDistribution == 3: #exponential
			self.thinkTime = random.expovariate(expoLambda)	

		self.clientId = clientId
		self.clientStatus = clientStatus    #0 - thinking, 1 - waiting for response