class Core:
	"""information related to each core(processor)"""

	def __init__(self, coreId, coreState):
		self.coreId = coreId
		self.coreState = coreState


	def enqueueRequest(self, request):
		self.queuedRequestsList.append(request)


	def dequeueRequest(self):
		self.queuedRequestsList = self.queuedRequestsList[2:]
















	

	
	
