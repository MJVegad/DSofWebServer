class Event:
	"""docstring for Event"""
	# arrival=0, departure=1, quantumExpired=2, scheduleNextRequest=3, requestTimeout=4
	def __init__(self, timestamp, eventType, requestId):
		self.timestamp = timestamp
		self.eventType = eventType
		self.requestId = requestId       