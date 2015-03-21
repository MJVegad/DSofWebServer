class Client:
	"""Information related to each client"""
	numberOfClients = 0
	thinkTime = []
	clientStatus = []

	def __init__(self, numberOfClients, thinkTime, clientStatus):
		self.numberOfClients = numberOfClients
		self.thinkTime = thinkTime
		self.clientStatus = clientStatus
		