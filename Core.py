class Core:
	"""information related to each core(processor)"""

	def __init__(self, coreId, coreState, queuedRequestsList):
		self.coreId = coreId
		self.coreState = coreState
		self.queuedRequestsList = queuedRequestsList


	def enqueueRequest(self, request):
		self.queuedRequestsList.append(request)


	def dequeueRequest(self):
		self.queuedRequestsList = self.queuedRequestsList[2:]
















	

	
	
