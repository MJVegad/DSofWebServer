import random

class Request:
	"""docstring for ClassName"""
	# request state codes
	# spawned = 0, executing = 1 , buffered = 2 , inCoreQueue = 3
	requestIdCounter = 0
	def __init__(self, clientId, arrivalTimeDistributionLambda, serviceTimeDistribution, constantDistributionValue=None, uniformRangeA=None, uniformRangeB=None, normalMu=None, normalSigma=None, expoLambda=None, timeout):
		self.clientId = clientId
		self.requestState = 0
		self.arrivalTime = random.expovariate(arrivalTimeDistributionLambda)
		self.requestId = requestIdCounter + 1
		self.threadId = -1
		if serviceTimeDistribution == 0: #constant 
			self.serviceTime = constantDistributionValue
		elif serviceTimeDistribution == 1: #uniform
			self.serviceTime = random.uniform(uniformRangeA,uniformRangeB)
		elif serviceTimeDistribution == 2: #normal
			self.serviceTime = random.normalvariate(normalMu,normalSigma)
		elif serviceTimeDistribution == 3: #exponential
			self.serviceTime = random.expovariate(expoLambda)	
		self.remainingServiceTime = serviceTime
		self.timeout = timeout
	def setRequestState(self, requestState):
		self.requestState = requestState