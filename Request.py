class Request:
	"""docstring for ClassName"""
	# request state codes
	# thinking = 0 , executing = 1 , buffered = 2 , inCoreQueue = 3
	requestIdCounter = 0
	def __init__(self, arrivalTime, totalServiceTime, timeout):
		self.requestState = 0
		self.arrivalTime = arrivalTime
		self.requestId = requestIdCounter + 1
		self.threadId = -1		
		self.remServiceTime = totalServiceTime
		self.timeout = timeout
	def setRequestState(self, requestState):
		self.requestState = requestState