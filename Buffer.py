class Buffer:
	"""It realizes a FIFO queue of requests waiting (which doesn’t get any thread) to get executed"""
	requestsInBuffer = []

	def __init__(self, sizeOfBuffer):
		self.sizeOfBuffer = sizeOfBuffer

	def addToBuffer(self,request):
			self.requestsInBuffer.append(request)

	def removeFromBuffer(self):
			self.requestsInBuffer = self.requestsInBuffer[2:]  #FIFO queue
		
		