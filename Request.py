import random

class Request:
	"""contains all the parameters related to a request in the system
		clientId : client which generated the request
		requestState : spawned, executing, buffered, inCoreQueue
		arrivalTimeDistributionLambda : lambda for Exp distribution
		serviceTimeDistribution : constant, uniform, normal, exponential
		arrivalTime : arrivalTime of the request
		requestId
		requestIdCounter : to generate request Id for new requests
		threadId: thread allocated to request, if none then -1
		remainingServiceTime : remaining service time of the request
		timeout : timeout for client which generated the request"""

	requestIdCounter = 0

	def __init__(self, clientId, arrivalTimeDistributionLambda, serviceTimeDistribution, timeout, param1, param2 = None):
		self.clientId = clientId
		self.requestState = 0
		self.arrivalTimeDistributionLambda = arrivalTimeDistributionLambda
		self.serviceTimeDistribution = serviceTimeDistribution
		self.param1 = param1
		self.param2 = param2
		self.arrivalTime = self.getArrivalTime(arrivalTimeDistributionLambda)

		if(clientId == -1):
			self.requestId = -1
		else:
			self.requestId = Request.requestIdCounter
			Request.requestIdCounter = Request.requestIdCounter + 1;

		self.threadId = -1

		if param2 is None:
			self.serviceTime = self.getServiceTime(serviceTimeDistribution, param1)
		else:
			self.serviceTime = self.getServiceTime(serviceTimeDistribution, param1, param2)

		self.remainingServiceTime = self.serviceTime
		self.timeout = timeout

	@staticmethod
	def initRequestId():
		Request.requestIdCounter = 0

	#to set request state
	def setRequestState(self, requestState):
		self.requestState = requestState


	#to get exponential arrival time
	def getArrivalTime(self, expoLambda):
		return random.expovariate(expoLambda)

	#to get service time according to distribution and parameters passed by user
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
