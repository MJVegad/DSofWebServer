import Buffer, Core, ThreadPool

class System:
	"""All parameters related to the system to be simulated
	   buffer : object of type Buffer, for buffer of the system
	   cores : list of Core type objects
	   threadPool : object of type ThreadPool, pool of all the available threads
	   timeQuantum : timeQuantum of process on any core
	   contextSwitchTime : switching time between two processes on any core """

	def __init__(self, sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime):
		Buffer.Buffer.initBufferCount()
		self.buffer = Buffer.Buffer(sizeOfBuffer)	
		self.numberOfCores = numberOfCores
		self.cores = []

		for y in list(range(numberOfCores)):
				self.cores.append(Core.Core(y, 0))

		self.threadPool = ThreadPool.ThreadPool(numberOfThreads)
		self.timeQuantum = timeQuantum
		self.contextSwitchTime = contextSwitchTime