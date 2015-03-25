class Event:
	"""Creates event object which contains members (timestamp, eventType, eventId) where,
	   eventType can be arrival=0, departure=1, quantumExpired=2, scheduleNextRequest=3, clientTimeout=4
	   eventId can be requestId if eventType is 0,1,2,4 or coreId if eventType is 4"""

	def __init__(self, timestamp, eventType, eventId):
		self.timestamp = timestamp
		self.eventType = eventType
		self.eventId = eventId

