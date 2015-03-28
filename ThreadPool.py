class  ThreadPool:
	"""Pool of all the available threads
	   numberOfThreads : maximum number of threads in the pool
	   numberOfBusyThreads : number of threads currently allocated to any request
	   threadStatus : list of status of each thread, free or busy"""

	
	def __init__(self, numberOfThreads):
		self.numberOfThreads = numberOfThreads
		self.numberOfBusyThreads = 0
		self.threadStatus = []
		# Threadstatus is a dictionary where key will be thread id and value will be a list whose first element will be request id and 2nd elelemt will be core id
		for index in list(range(self.numberOfThreads)) :
			self.threadStatus.append(0)						# 0 - free thread

    #to allocate a thread to a request
	def allocateThread(self):
		threadId = self.getFreeThreadId()
		self.numberOfBusyThreads = self.numberOfBusyThreads + 1
		self.threadStatus[threadId] = 1
		#self.numberOfBusyThreads = self.numberOfBusyThreads + 1

    #to retain the thread from completed process
	def freeThread(self, threadId):
		self.threadStatus[threadId] = 0
		self.numberOfBusyThreads = self.numberOfBusyThreads - 1

    #to get free thread with lowest threadId
	def getFreeThreadId(self):
		# Returns a threadId of a free thread otherwise -1
		if self.numberOfBusyThreads < self.numberOfThreads:
			# find thread id whose thread status is idle
			for index in list(range(self.numberOfThreads)) :
				if self.threadStatus[index] == 0 :
					return index
		else:
			return -1