import random

class Request:
	"""docstring for ClassName"""
	# request state codes
	# spawned = 0, executing = 1 , buffered = 2 , inCoreQueue = 3
	#global requestIdCounter
	requestIdCounter = 0
	def __init__(self, clientId, arrivalTimeDistributionLambda, serviceTimeDistribution, timeout, param1, param2 = None):
		self.clientId = clientId
		self.requestState = 0
		self.arrivalTimeDistributionLambda = arrivalTimeDistributionLambda
		self.serviceTimeDistribution = serviceTimeDistribution
		self.param1 = param1
		self.param2 = param2
		self.arrivalTime = self.getArrivalTime(arrivalTimeDistributionLambda)
		self.requestId = self.requestIdCounter + 1
		#self.requestIdCounter = self.requestIdCounter + 1;
		self.threadId = -1

		if param2 is None:
			self.serviceTime = self.getServiceTime(serviceTimeDistribution, param1)
		else:
			self.serviceTime = self.getServiceTime(serviceTimeDistribution, param1, param2)

		self.remainingServiceTime = self.serviceTime
		self.timeout = timeout

	def setRequestState(self, requestState):
		self.requestState = requestState



	def getArrivalTime(self, expoLambda):
		return random.expovariate(expoLambda)

	def getServiceTime(self, serviceTimeDistribution, param1, param2 = None):
		serviceTime=0
		if serviceTimeDistribution == 0: #constant 
			serviceTime = param1
		elif serviceTimeDistribution == 1: #uniform
			serviceTime = random.uniform(param1, param2)
		elif serviceTimeDistribution == 2: #normal
			serviceTime = random.normalvariate(param1, param2)
		elif serviceTimeDistribution == 3: #exponential
			serviceTime = random.expovariate(param1)	
		return serviceTime
