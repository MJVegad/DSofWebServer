import Request

class Buffer:
	"""It realizes a FIFO queue of requests which are waiting (which doesn’t get any thread) to get executed.
	   requestsInBuffer : contains list of Request objects, one for each request in the system """

	requestsInBuffer = []

	def __init__(self, sizeOfBuffer):
		self.sizeOfBuffer = sizeOfBuffer

	def addToBuffer(self,request):
		self.requestsInBuffer.append(request)

	def removeFromBuffer(self):
		request = Request.Request(-1,-1,-1,-1,-1)

		if len(self.requestsInBuffer) != 0 :
			request = self.requestsInBuffer[0]
			if len(self.requestsInBuffer) == 1 :
				self.requestsInBuffer = []
			else :
				self.requestsInBuffer = self.requestsInBuffer[1:]
		return request