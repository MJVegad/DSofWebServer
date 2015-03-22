class  ThreadPool:
	"""ThreadPool for  """
	# Index of thread will be from 1 to max number of threads
	def __init__(self, numberOfThreads):
		self.numberOfThreads = numberOfThreads
		numberOfBusyThreads = 0
		# Threadstatus is a dictionary where key will be thread id and value will be a list whose first element will be request id and 2nd elelemt will be core id
		threadStatus = {}
	def allocateThread(self, requestId, coreId, threadId):
		self.numberOfBusyThreads = self.numberOfBusyThreads + 1
		threadStatus[threadId] = [requestId, coreId]
	def freeThread(self, threadId):
		del self.threadStatus[threadId]

	def getFreeThreadId(self):
		# Returns a threadId of a free thread otherwise -1
		if numberOfBusyThreads < numberOfThreads:
			# find thread id with min index
			return min(self.threadStatus)
		else:
			return -1