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
		if threadId is None:
			return -1
		else:
			return (threadId % self.system.numberOfCores)

	def getRequestFromEvent(self, event):
		request = Request.Request(-1,-1,-1,-1,-1)
		for x in list(range(event.eventId)):
		 	if (self.requestList.requestList[x].requestId == event.eventId):
		 		request = self.requestList.requestList[x]
		 		break		     	
		return request
	

	def arrivalEventHandler(self, event):
		availableThreadId = self.system.threadPool.getFreeThreadId()
		request = self.getRequestFromEvent(event)

		if (availableThreadId == -1):
			request.setRequestState(2)  #2-buffered 
			self.system.buffer.addToBuffer(request)
		else:
			coreId = self.getCoreIdFromThreadId(availableThreadId)
			self.system.threadPool.allocateThread(event.eventId, coreId)


			if(self.system.cores[coreId].coreState == 0):     #0 - idle	
				self.system.cores[coreId].coreState = 1       #1 - busy	
				request.setRequestState(1)      #1 - executing 
				if((request.remainingServiceTime) < self.system.timeQuantum):
					newEvent = Event.Event(self.simulationTime + request.remainingServiceTime, 1, request.requestId)
					self.eventList.enqueueEvent(newEvent)
				else:
					newEvent = Event.Event(self.simulationTime + self.system.timeQuantum ,2, request.requestId)
					self.eventList.enqueueEvent(newEvent)
			else:
				request.setRequestState(3)         #3 - inCoreQueue              
				self.system.cores[coreId].enqueueRequest(request)	


	def quantamExpiredEventHandler(self, event):
		# 	get core id
		#   get request object
		#   add request object in core queue
		request = self.getRequestFromEvent(event)
		request.remainingServiceTime = request.remainingServiceTime - self.system.timeQuantum
		coreId = self.getCoreIdFromThreadId(request.threadId)
		self.system.cores[coreId].enqueueRequest(request)
		request.setRequestState(3)                  #3 - inCoreQueue
		nextEvent = Event.Event(self.simulationTime + self.system.contextSwitchTime, 3, coreId)
		self.eventList.enqueueEvent(nextEvent)

	def departureEventHandler(self, event):
		request = Request.Request(-1,-1,-1,-1,-1)
		for x in list(range(event.eventId)):
		 	if (self.requestList.requestList[x].requestId == event.eventId):
		 		request = self.requestList.requestList[x]
		 		self.requestList.requestList = self.requestList.requestList[:x-1] + self.requestList.requestList[x+1:]
		 		break	 

		self.system.threadPool.freeThread(request.threadId)
		client = self.clients[request.clientId]
		client.clientStatus = 0;   #0 - thinking
        
		if(client.paramThinkTime2 is None):
			client.thinkTime = client.getThinkTime(client.thinkTimeDistribution, client.paramThinkTime1)
		else:
			client.thinkTime = client.getThinkTime(client.thinkTimeDistribution, client.paramThinkTime1, client.paramThinkTime2)

		if(self.system.cores[self.getCoreIdFromThreadId(request.threadId)].queuedRequestsList is not []):
			scheduleNextEvent = Event.Event(self.simulationTime + self.system.contextSwitchTime, 3, self.getCoreIdFromThreadId(request.threadId))
			self.eventList.enqueueEvent(scheduleNextEvent)
		else:
			self.system.cores[self.getCoreIdFromThreadId(request.threadId)].coreState = 0        #0 - idle

		newRequest = Request.Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
		self.requestList.addToRequestList(newRequest)
		newEvent = Event.Event(self.simulationTime + client.thinkTime, 0, newRequest.requestId)
		self.eventList.enqueueEvent(newEvent)

		if(self.system.buffer.requestsInBuffer is not []):
			requestFromBuffer = self.system.buffer.removeFromBuffer()
			newEvent = Event.Event(self.simulationTime, 0, requestFromBuffer.requestId)
			self.eventList.enqueueEvent(newEvent)

	def scheduleNextRequestEventHandler(self, event):
		# get coreId on which next request is to be scheduled
		coreId = event.eventId
		dequedRequest = self.system.cores[coreId].dequeueRequest()
		dequedRequest.setRequestState(1)		#1 - executing
		if dequedRequest.remainingServiceTime < self.system.timeQuantum :
			departureEvent = Event.Event(self.simulationTime + dequedRequest.remainingServiceTime, 1, dequedRequest.requestId)
			self.eventList.enqueueEvent(departureEvent)
		else :
			quantamExpiredEvent = Event.Event(self.simulationTime + self.system.timeQuantum, 1, dequedRequest.requestId)
			self.eventList.enqueueEvent(quantamExpiredEvent)

	def timeoutEventHandler(self, event):
		request = self.getRequestFromEvent(event)
		newRequest = Request.Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
		self.requestList.addToRequestList(newRequest)
		newEvent = Event.Event(self.simulationTime, 0, newRequest.requestId)
		self.eventList.enqueueEvent(newEvent)