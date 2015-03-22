import Buffer, Core, ThreadPool

class System:
	"""All parameters related to the system to be simulated"""
	def __init__(self, sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime):
		self.buffer = Buffer.Buffer(sizeOfBuffer)	
		self.cores = []

		for y in list(range(numberOfCores)):
				self.cores.append(Core.Core(y, 0))

		self.threadPool = ThreadPool.ThreadPool(numberOfThreads)
		self.timeQuantum = timeQuantum
		self.contextSwitchTime = contextSwitchTime