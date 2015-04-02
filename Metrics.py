class Metrics:
	"""docstring for Metrics"""

	def __init__(self):
		self.responseTime = 0
		self.noOfTimeoutRequests = 0
		self.noOfRequestsWithoutTimeout = 0

	def getAvgResponseTime(self, departureCount):
		return self.responseTime / departureCount

	def getBadput(self, simulationTime):
		return self.noOfTimeoutRequests / simulationTime

	def getGoodput(self, simulationTime):
		return self.noOfRequestsWithoutTimeout / simulationTime

	def getThroughput(self, simulationTime):
		return (self.noOfRequestsWithoutTimeout + self.noOfTimeoutRequests) / simulationTime