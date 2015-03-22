import math, System, Event, EventList

class Simulation:
	"""To begin and keep track of simulation"""
	def __init__(self, sizeOfBuffer, numberOfClients, typeOfDistribution, param1, param2=None, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime, equestsList):
		self.eventList = EventList()
		self.simulationTime = 0
		
		self.system = System(sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime)
		self.requestList = requestslist

    def getCoreIdFromThreadId(self,threadId):
		return threadId%self.system.numberOfCores

	def getRequestFromEvent(self, event):
		for x in list(range(event.requestId)):
		 	if (self.requestList[x].requestId == event.requestId):
		 		request = self.requestList[x]
		 		break	     	
		return request


	def arrivalEventHandler(self, event):
		availableThreadId = self.system.threadPool.getFreeThreadId()
		request = getRequestFromEvent(event)

		if (availableThreadId == -1):
			request.setRequestState(2)  #2-buffered 
			self.system.buffer.addToBuffer(request)
		else:
			coreId = getCoreIdFromThreadId(availableThreadId)
			self.system.threadPool.allocateThread(event.id, coreId, availableThreadId)


			if(self.system.cores[coreId].coreState == 0):     #0 - idle	
		 		self.system.cores[coreId].coreState = 1       #1 - busy	
		 		request.setRequestState(1)      #1 - executing 
		 		if((request.remainingServiceTime) < self.system.timeQuantum):
		 			newEvent = Event(self.simulationTime + request.remainingServiceTime, 1, )
		 			EventList.enqueueEvent(newEvent)
		 		else:
		 			newEvent = Event(self.simulationTime + timeQuantum ,2, coreId)
		 			EventList.enqueueEvent(newEvent)
		 	else:
		 		request.setRequestState(3)         #3 - inCoreQueue              
		 		self.system.cores[coreId].enqueueRequest(request)	


	def quantamExpiredEH(self, event):
		remainingServiceTime = remainingServiceTime - self.system.timeQuantum
		# 	get core id
		#   get request object
		#   add request object in core queue
		request = getRequestFromEvent(self, event)
		coreId = getCoreIdFromThreadId(request.threadId)
		self.system.cores[coreId].enqueueRequest(request)
		request.setRequestState(3)                  #3 - inCoreQueue
		nextEvent = Event(self.simulationTime + contextSwitchTime, 3, coreId)
		self.eventList.enqueueEvent(nextEvent)

	def departureEventHandler(self, event):
		for x in list(range(event.requestId)):
		 	if (self.requestList[x].requestId == event.requestId):
		 		request = self.requestList[x]
		 		self.requestList = self.requestList[:x-1] + self.requestList[x+1:]
		 		break	 

	def scheduleNextRequestEH(self, event):
		# get coreId on which next request is to be scheduled
		coreId = event.eventId
		dequedRequest = self.system.cores[coreId].dequeRequest()
		dequedRequest.setRequestState(1)		#1 - executing
		if dequedRequest.remainingServiceTime < self.system.timeQuantum :
			departureEvent = Event(self.simulationTime + remainingServiceTime, 1, dequedRequest.requestId)
			self.eventList.enqueueEvent(departureEvent)
		else :
			quantamExpiredEvent = Event(self.simulationTime + timeQuantum, 1, dequedRequest.requestId)
			self.eventList.enqueueEvent(quantamExpiredEvent)