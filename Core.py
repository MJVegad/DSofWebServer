import queue

class Core:
	"""information related to each core(processor)"""

	def __init__(self, coreId, coreState):
		self.coreId = coreId
		self.coreState = coreState
		self.queuedRequestsList = queue.Queue()

	def enqueueRequest(self, request):
		self.queuedRequestsList.put(request)

	def dequeueRequest(self):
		return self.queuedRequestsList.get()
