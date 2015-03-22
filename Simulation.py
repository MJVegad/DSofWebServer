import math, System, Event, EventList, Request, RequestList, Client

class Simulation:
	"""To begin and keep track of simulation"""

	def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
		self.eventList = EventList.EventList()
		self.simulationTime = 0
		self.clients = []

		for y in list(range(numberOfClients)):
			self.clients.append(Client.Client(y, thinkTimeDistribution, paramThinkTime1, 0, paramThinkTime2))        #0 - thinking

		self.requestList = RequestList.RequestList()
		
		for index in list(range(numberOfClients)):
			if serviceTimeDistribution == 1 or serviceTimeDistribution == 2: # Uniform or Normal distribution
				request = Request.Request(index, arrivalTimeDistributionLambda, serviceTimeDistribution, timeout, paramServiceTime1, paramServiceTime2)
			else:
				request = Request.Request(index, arrivalTimeDistributionLambda, serviceTimeDistribution, timeout, paramServiceTime1)
			
			self.requestList.addToRequestList(request)
			newEvent = Event.Event(self.simulationTime + request.arrivalTime, 0, request.requestId)
			self.eventList.enqueueEvent(newEvent)

		self.system = System.System(sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime)

	def getCoreIdFromThreadId(self,threadId):
		return (threadId % self.system.numberOfCores)

	def getRequestFromEvent(self, event):
		for x in list(range(event.eventId)):
		 	if (self.requestList[x].requestId == event.eventId):
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
			self.system.threadPool.allocateThread(event.eventId, coreId, availableThreadId)


			if(self.system.cores[coreId].coreState == 0):     #0 - idle	
				self.system.cores[coreId].coreState = 1       #1 - busy	
				request.setRequestState(1)      #1 - executing 
				if((request.remainingServiceTime) < self.system.timeQuantum):
					newEvent = Event(self.simulationTime + request.remainingServiceTime, 1, request.requestId)
					self.eventList.enqueueEvent(newEvent)
				else:
					newEvent = Event(self.simulationTime + timeQuantum ,2, request.requestId)
					self.eventList.enqueueEvent(newEvent)
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

		self.system.threadPool.freeThread(request.threadId)
		client = clients[request.clientId]
		client.clientStatus = 0;   #0 - thinking
        
		if(client.param2 is None):
			client.thinkTime = getThinkTime(client.thinkTimeDistribution, client.param1)
		else:
			client.thinkTime = getThinkTime(client.thinkTimeDistribution, client.param1, client.param2)

		if(self.system.cores[self.getCoreIdFromThreadId(request.threadId)].queuedRequestsList is not []):
			scheduleNextEvent = Event(self.simulationTime + self.system.contextSwitchTime, 3, self.getCoreIdFromThreadId(request.threadId))
			self.eventList.enqueueEvent(scheduleNextEvent)
		else:
			self.system.cores[self.getCoreIdFromThreadId(request.threadId)].coreState = 0        #0 - idle

		newRequest = Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
		self.requestList.addToRequestList(newRequest)
		newEvent = Event(self.simulationTime + client.thinkTime, 0, newRequest.requestId)
		self.eventList.enqueueEvent(newEvent)

		if(self.system.buffer.requestsInBuffer is not []):
			requestFromBuffer = self.system.buffer.removeFromBuffer()
			newEvent = Event(self.simulationTime, 0, requestFromBuffer.requestId)
			self.eventList.enqueueEvent(newEvent)

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

	def timeoutEventHandler(self, event):
		request = self.getRequestFromEvent(event)
		newRequest = Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
		self.requestList.addToRequestList(newRequest)
		newEvent = Event(self.simulationTime, 0, newRequest.requestId)
		self.eventList.enqueueEvent(newEvent)