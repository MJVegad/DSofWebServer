import Buffer, Core, ThreadPool

class System:
	"""All parameters related to the system to be simulated"""
	def __init__(self, sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime):
		self.buffer = Buffer(sizeOfBuffer)

		for y in list(range(numberOfCores)):
				self.cores[y] = Core(y, 0)

		self.threadPool = ThreadPool(numberOfThreads)
		self.timeQuantum = timeQuantum
		self.contextSwitchTime = contextSwitchTime


	


		